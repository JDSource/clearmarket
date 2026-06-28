# ClearMarket MCP eval

A small, evaluation-driven harness for the ClearMarket MCP, built on Anthropic's
["Writing effective tools for AI agents"](https://www.anthropic.com/engineering/writing-tools-for-agents).
Its job: **measure** whether the tool descriptions + server `instructions` let a real
agent succeed — so any change to them is validated, not asserted.

## Why this exists

You cannot tell from reading whether an instruction string is "clear to an agent."
Anthropic's own result is that Claude-optimized tool descriptions beat expert-hand-written
ones *on held-out tasks*. The only honest test is to run realistic tasks through an
agentic loop and look at where the agent gets confused. This is `loop-driven-development`
applied to the MCP itself: the eval is the verifier, the descriptions are the artifact
you optimize.

## What it measures

Per task (`tasks.jsonl`):
- **pass/fail** — an LLM judge against a written success criterion
- **tool selection** — did the agent call the expected tool(s)? (`hit` / `MISS`)
- **turns, tokens, tool errors**
- **`EVAL_FEEDBACK`** — the agent's own one-line note on what was confusing or missing.
  This is the signal you feed back into the descriptions.

## Run it

```bash
# free: verify live-MCP connectivity + see the tasks, no LLM calls
python3 eval/run_eval.py --dry-run

# full run (makes real Anthropic API calls — costs a few cents)
export ANTHROPIC_API_KEY=sk-ant-...
pip install anthropic            # requests not needed (stdlib urllib)
python3 eval/run_eval.py

# subsets
python3 eval/run_eval.py --task trust-basic
python3 eval/run_eval.py --limit 3 --model claude-sonnet-4-6
```

Results land in `eval/results/run-<UTC>.json` plus a printed scorecard.

## The optimization loop

1. Run the eval → note failures, `MISS` tool-selections, and the feedback digest.
2. Paste `eval/results/run-*.json` into Claude Code: *"propose edits to the server
   `instructions` and the tool descriptions in `api/src/mcp.ts` that fix these
   failures and this feedback — change copy only, not behavior."*
3. Deploy the worker, re-run the eval, diff the scores.
4. Keep what moves PASS / tool-hit up; discard what doesn't.

Hard rule: a description change only counts if the eval score improves. No vibes.

## Notes

- **Prompts use OUTSIDER language on purpose.** "Resolution Clarity Grade" / "RCG" is our
  invented vernacular — no real user or agent knows it. So task prompts ask in plain terms
  ("can I trust how this settles?", "least likely to end in a dispute"), never our jargon.
  The internal `success_criteria` (the judge's rubric) still references the grade, since
  that's what we check. This makes each task a real test of whether the tool *descriptions*
  bridge plain intent → our grade. If the agent only finds the grade when the user literally
  says "RCG," the descriptions are failing — which is exactly what we want to detect.
- The resolution-risk cluster (`placeholder-ambiguity`, `dispute-grounded`,
  `pre-trade-red-flags`, `why-risky-factors`, `cross-venue-divergence`,
  `resolution-risk-agent`) is the emphasis — it probes the core wedge from several angles,
  including a real blow-up case (the Strategy/MicroStrategy Bitcoin-sale market that disputed).
- Tasks hit the **live** MCP (`api.clearmarket.fyi/mcp`, open, no key) and current data,
  so phrasing is topic-based (e.g. "the Fed") to survive data drift, not hardcoded slugs
  (except `routing-direct-slug`, which tests exact-slug routing).
- Several tasks (`trust-basic`, `resolution-risk-agent`) deliberately frame from a
  *venue* reference the agent has no CM id for — they surface the venue-URL/ticker
  lookup gap. Expect those to need extra hops until that lookup ships.
- `how-common-no-source` is partly answerable from the server `instructions` alone — it's a
  direct test of whether the instruction string conveys the core thesis.
- Override the target with `CM_MCP_URL` (e.g. a staging worker) to eval a change before
  it hits production.
