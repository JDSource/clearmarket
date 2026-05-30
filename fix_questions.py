"""
Question sanitizer (data-layer cleanup). The enrichment step asked an LLM to rewrite each event's
question; for ~630 malformed/templated source questions it emitted garbage instead — LLM
meta-commentary ("I need clarification...", "Note: this question cannot be...") or leftover
[X]/[DATE]/[specific...] template placeholders. That garbage is visible on the events index,
event pages, REST API, and MCP.

Fix: for every event whose enriched question matches the garbage pattern, fall back to the raw
venue question (question_raw of the primary/first market), which is clean and accurate. Verified:
all garbage-question events have a usable raw. Emits api/questions-migration.sql for D1.

Run BEFORE patch_ladders.py (ladder events then get their metric labels, overriding any raw here).
Usage: python3 fix_questions.py  ->  rewrites the bundle + writes api/questions-migration.sql
"""
import json, re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent
BUNDLE = ROOT / "web/data/universe-enriched-linked.json"

# LLM meta-commentary OR any leftover [bracket placeholder] = not a real question.
BAD = re.compile(
    r"\b(I appreciate|I'm unable|I am unable|I need clarification|I cannot|I can't|doesn't appear|"
    r"Could you please|I'd be happy|I don't have|please provide|let me know|appears incomplete|"
    r"not a recognizable|I'm not able|I notice|Note:)\b|\[[^\]]+\]",
    re.I,
)


def esc(s):
    return str(s).replace("'", "''")


def main():
    b = json.loads(BUNDLE.read_text())
    mbye = defaultdict(list)
    for m in b["markets"]:
        mbye[m.get("event_id")].append(m)

    fixed = []
    for e in b["events"]:
        q = e.get("question", "") or ""
        if not BAD.search(q):
            continue
        ms = mbye.get(e["event_id"], [])
        # prefer the primary market's raw question, else the first market's
        raw = ""
        prim = next((m for m in ms if m.get("market_id") == e.get("primary_market_id")), None)
        for m in ([prim] if prim else []) + ms:
            cand = (m.get("question_raw") or "").strip()
            if cand and not BAD.search(cand):
                raw = cand
                break
        if raw:
            e["question"] = raw
            fixed.append(e)

    BUNDLE.write_text(json.dumps(b, default=str))

    lines = [
        f"UPDATE events SET question='{esc(e['question'])}' WHERE event_id='{esc(e['event_id'])}';"
        for e in fixed
    ]
    out = ROOT / "api/questions-migration.sql"
    out.write_text("\n".join(lines) + ("\n" if lines else ""))
    print(f"sanitized {len(fixed)} garbage event questions (fell back to raw venue question)")
    print(f"wrote {out}: {len(lines)} UPDATEs")


if __name__ == "__main__":
    main()
