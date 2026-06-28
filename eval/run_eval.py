#!/usr/bin/env python3
"""
ClearMarket MCP eval harness.

Runs realistic tasks through an agentic loop against the LIVE ClearMarket MCP
(api.clearmarket.fyi/mcp), then judges each result. The point (per Anthropic's
"Writing effective tools for agents"): MEASURE whether the tool descriptions +
server instructions let an agent succeed — so description changes are validated,
not asserted.

What it measures per task:
  - pass/fail (LLM judge against a success_criterion)
  - which tools the agent called vs. the expected tools (selection accuracy)
  - turns, token usage, tool errors
  - EVAL_FEEDBACK: the agent's own note on what was confusing/missing
    (this is the optimization signal for rewriting descriptions)

Usage:
  export ANTHROPIC_API_KEY=sk-ant-...
  pip install anthropic requests
  python3 eval/run_eval.py                 # run all tasks
  python3 eval/run_eval.py --dry-run       # verify MCP connectivity + print tasks, NO LLM calls (free)
  python3 eval/run_eval.py --task trust-basic
  python3 eval/run_eval.py --limit 3 --model claude-sonnet-4-6

Results are written to eval/results/run-<UTC>.json and printed as a scorecard.
Re-run after editing the server `instructions` / tool descriptions and diff the
scores. To close the loop: paste the results JSON into Claude Code and ask it to
propose description edits that fix the failures and the EVAL_FEEDBACK.
"""
import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone

MCP_URL = os.environ.get("CM_MCP_URL", "https://api.clearmarket.fyi/mcp")
DEFAULT_MODEL = os.environ.get("CM_EVAL_MODEL", "claude-sonnet-4-6")
HERE = os.path.dirname(os.path.abspath(__file__))
TASKS_PATH = os.path.join(HERE, "tasks.jsonl")
RESULTS_DIR = os.path.join(HERE, "results")

SYSTEM_SUFFIX = (
    "\n\nYou are being evaluated on whether ClearMarket's tools let you solve the task. "
    "Use the tools to ground every factual claim — do not answer prediction-market "
    "questions from memory. When you have enough, give a concise final answer. "
    "Then, on a final line, append `EVAL_FEEDBACK:` followed by one sentence on anything "
    "about the tools, their descriptions, or the server instructions that was confusing, "
    "missing, or made you call the wrong tool (write `EVAL_FEEDBACK: none` if nothing)."
)

# ---- live MCP client (JSON-RPC 2.0 over HTTP) ---------------------------
_rpc_id = 0
def _rpc(method, params):
    global _rpc_id
    _rpc_id += 1
    body = json.dumps({"jsonrpc": "2.0", "id": _rpc_id, "method": method, "params": params}).encode()
    req = urllib.request.Request(MCP_URL, data=body, headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        # Cloudflare 403s the default "Python-urllib" UA; send a descriptive one.
        "User-Agent": "Mozilla/5.0 (compatible; clearmarket-eval/1.0)",
    })
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.loads(r.read())

def mcp_init():
    """Returns (instructions, tools[]) from the live server."""
    init = _rpc("initialize", {})["result"]
    tools = _rpc("tools/list", {})["result"]["tools"]
    return init.get("instructions", ""), tools

def mcp_call(name, arguments):
    """Call a tool; return (data, error_str|None)."""
    try:
        res = _rpc("tools/call", {"name": name, "arguments": arguments or {}})
    except urllib.error.URLError as e:
        return None, f"transport error: {e}"
    if "error" in res:
        return None, f"rpc error: {res['error']}"
    result = res.get("result", {})
    if "structuredContent" in result:
        return result["structuredContent"], None
    content = result.get("content", [])
    if content and content[0].get("type") == "text":
        try:
            return json.loads(content[0]["text"]), None
        except Exception:
            return content[0]["text"], None
    return result, None

# ---- Anthropic agentic loop --------------------------------------------
def to_anthropic_tools(mcp_tools):
    return [{"name": t["name"], "description": t["description"], "input_schema": t["inputSchema"]} for t in mcp_tools]

def run_task(client, model, instructions, anth_tools, task, max_turns):
    messages = [{"role": "user", "content": task["prompt"]}]
    tools_called, errors = [], []
    in_tok = out_tok = 0
    final_text = ""
    for _ in range(max_turns):
        resp = client.messages.create(
            model=model, max_tokens=1500,
            system=(instructions + SYSTEM_SUFFIX),
            tools=anth_tools, messages=messages,
        )
        in_tok += resp.usage.input_tokens
        out_tok += resp.usage.output_tokens
        # collect any text + tool calls in this turn
        text_parts = [b.text for b in resp.content if b.type == "text"]
        if text_parts:
            final_text = "\n".join(text_parts)
        tool_uses = [b for b in resp.content if b.type == "tool_use"]
        if resp.stop_reason != "tool_use" or not tool_uses:
            break
        messages.append({"role": "assistant", "content": resp.content})
        results = []
        for tu in tool_uses:
            tools_called.append({"name": tu.name, "input": tu.input})
            data, err = mcp_call(tu.name, tu.input)
            if err:
                errors.append(f"{tu.name}: {err}")
            # was 8000 — that truncated multi-market get_event (up to ~36k chars / 18 markets)
            # into invalid JSON mid-field, forcing the agent to guess (judged as "fabrication").
            payload = json.dumps(data)[:50000] if not err else f"ERROR: {err}"
            results.append({"type": "tool_result", "tool_use_id": tu.id, "content": payload})
        messages.append({"role": "user", "content": results})
    feedback = ""
    if "EVAL_FEEDBACK:" in final_text:
        final_text, feedback = final_text.rsplit("EVAL_FEEDBACK:", 1)
        feedback = feedback.strip()
    return {
        "final": final_text.strip(), "feedback": feedback,
        "tools_called": tools_called, "tool_names": [t["name"] for t in tools_called],
        "errors": errors, "in_tok": in_tok, "out_tok": out_tok,
    }

def judge(client, model, task, answer, tools_called):
    prompt = (
        f"Task given to an agent:\n{task['prompt']}\n\n"
        f"Success criterion:\n{task['success_criteria']}\n\n"
        f"Tools the agent actually called (its ground truth): {tools_called}\n\n"
        f"Agent's final answer:\n{answer}\n\n"
        "Grade ONLY against the success criterion. The agent's tool calls above ARE the ground "
        "truth — do NOT fail merely because a peripheral specific (e.g., an exact price or id) "
        "can't be independently re-verified here. Fail only if the CORE claim the criterion "
        "requires is missing, wrong, or clearly not grounded in the agent's tool use. "
        'Reply ONLY with JSON: {"pass": true|false, "reason": "<one sentence>"}'
    )
    resp = client.messages.create(model=model, max_tokens=300,
                                  messages=[{"role": "user", "content": prompt}])
    txt = "".join(b.text for b in resp.content if b.type == "text").strip()
    txt = txt[txt.find("{"): txt.rfind("}") + 1]
    try:
        return json.loads(txt)
    except Exception:
        return {"pass": False, "reason": "judge parse error: " + txt[:120]}

# ---- main ---------------------------------------------------------------
def load_tasks():
    out = []
    with open(TASKS_PATH) as f:
        for line in f:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", help="run a single task by id")
    ap.add_argument("--limit", type=int, help="run only the first N tasks")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--max-turns", type=int, default=8)
    ap.add_argument("--dry-run", action="store_true", help="verify MCP + print tasks, no LLM calls")
    args = ap.parse_args()

    tasks = load_tasks()
    if args.task:
        tasks = [t for t in tasks if t["id"] == args.task]
    if args.limit:
        tasks = tasks[: args.limit]
    if not tasks:
        sys.exit("no tasks matched")

    print(f"Connecting to live MCP: {MCP_URL}")
    instructions, mcp_tools = mcp_init()
    print(f"  serverInfo ok · {len(mcp_tools)} tools · instructions {len(instructions)} chars")
    print(f"  tools: {', '.join(t['name'] for t in mcp_tools)}\n")

    if args.dry_run:
        print("DRY RUN — tasks that would execute:\n")
        for t in tasks:
            print(f"  [{t['id']}] expect={t['expected_tools']}")
            print(f"      {t['prompt']}")
        # prove a real tool call works end-to-end
        data, err = mcp_call("list_events", {"q": "fed", "limit": 1})
        print("\n  live tool-call check (list_events q=fed):",
              "OK" if not err else f"FAIL {err}",
              f"· total={data.get('total') if isinstance(data, dict) else '?'}")
        return

    try:
        import anthropic
    except ImportError:
        sys.exit("pip install anthropic")
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("set ANTHROPIC_API_KEY")
    client = anthropic.Anthropic()
    anth_tools = to_anthropic_tools(mcp_tools)

    rows, results = [], []
    for t in tasks:
        t0 = time.time()
        run = run_task(client, args.model, instructions, anth_tools, t, args.max_turns)
        verdict = judge(client, args.model, t, run["final"], run["tool_names"])
        expected = set(t["expected_tools"])
        called = set(run["tool_names"])
        tool_match = "n/a" if not expected else ("hit" if expected & called else "MISS")
        row = {
            "id": t["id"], "pass": verdict["pass"], "tool_match": tool_match,
            "called": run["tool_names"], "expected": t["expected_tools"],
            "turns": len(run["tools_called"]), "tok": run["in_tok"] + run["out_tok"],
            "errors": run["errors"], "reason": verdict["reason"],
            "feedback": run["feedback"], "secs": round(time.time() - t0, 1),
        }
        rows.append(row)
        results.append({**row, "answer": run["final"]})
        mark = "PASS" if verdict["pass"] else "FAIL"
        print(f"[{mark}] {t['id']:<22} tools={tool_match:<4} called={run['tool_names']}")
        print(f"        judge: {verdict['reason']}")
        if run["feedback"] and run["feedback"].lower() != "none":
            print(f"        feedback: {run['feedback']}")
        if run["errors"]:
            print(f"        ERRORS: {run['errors']}")

    # scorecard
    npass = sum(1 for r in rows if r["pass"])
    nhit = sum(1 for r in rows if r["tool_match"] == "hit")
    ngraded = sum(1 for r in rows if r["tool_match"] != "n/a")
    tot_tok = sum(r["tok"] for r in rows)
    print("\n" + "=" * 64)
    print(f"PASS {npass}/{len(rows)}   ·   tool-selection {nhit}/{ngraded}   ·   tokens {tot_tok:,}")
    print("=" * 64)

    os.makedirs(RESULTS_DIR, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    outp = os.path.join(RESULTS_DIR, f"run-{stamp}.json")
    with open(outp, "w") as f:
        json.dump({"model": args.model, "mcp_url": MCP_URL, "instructions": instructions,
                   "summary": {"pass": npass, "n": len(rows), "tool_hit": nhit,
                               "tool_graded": ngraded, "tokens": tot_tok},
                   "results": results}, f, indent=2)
    print(f"\nwrote {outp}")
    fb = [f"- [{r['id']}] {r['feedback']}" for r in rows if r["feedback"] and r["feedback"].lower() != "none"]
    if fb:
        print("\nAgent feedback (description-optimization signal):")
        print("\n".join(fb))

if __name__ == "__main__":
    main()
