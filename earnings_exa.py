"""
Earnings catalyst dates via Exa + Claude (API Ninjas free tier is historical-only).

For each event the classifier tagged corporate_earnings, do one Exa search for the company's
next earnings/report date and have Claude extract {date, source_url} from the retrieved text.
Populates catalyst_dates in the bundle but does NOT push to D1 — dates are LLM-extracted, so
hold for human spot-check (citation/integrity discipline). Within the Exa 75/day cap (~11 calls).

Reads/writes web/data/universe-enriched-linked.json. Prints a review table.
"""
import json, os, re, requests
from pathlib import Path
from dotenv import load_dotenv
from enhance import llm_call, LLM_MODEL_HAIKU

ROOT = Path(__file__).parent
load_dotenv(ROOT / ".env")
EXA_KEY = os.getenv("EXA_API_KEY")
TODAY = "2026-05-28"

def classify_earnings(ev):
    t = ((ev.get("question") or "") + " " + " ".join(ev.get("tags") or [])).lower()
    # same trigger as fetch_catalysts, minus the macro types (those are handled there)
    if re.search(r"\b(cpi|consumer price|inflation|jobs report|nonfarm|unemployment|gdp|gross domestic|ppi|producer price|fomc|fed rate|federal reserve|rate cut|rate hike|interest rate)\b", t):
        return False
    return bool(re.search(r"\b(earnings|revenue|eps|deliver|production|trip volume|skier visits|funded accounts|customers)\b", t))

def exa_search(query):
    r = requests.post("https://api.exa.ai/search",
                      headers={"x-api-key": EXA_KEY, "Content-Type": "application/json"},
                      json={"query": query, "numResults": 3, "contents": {"text": {"maxCharacters": 800}}},
                      timeout=30)
    if not r.ok:
        return []
    return [{"url": x.get("url"), "text": (x.get("text") or "")[:800]} for x in r.json().get("results", [])]

SYS = ("Extract a company's NEXT scheduled earnings/report date from search results. Output ONLY JSON: "
       '{"company": str|null, "next_earnings_date": "YYYY-MM-DD"|null, "source_url": str|null}. '
       "The date MUST be >= " + TODAY + " (a future scheduled report). If the results only show past "
       "earnings or you cannot find a future date, return null for next_earnings_date. NEVER invent a date.")

def lookup(question):
    company_hint = question[:80]
    results = exa_search(f"{company_hint} next earnings report date 2026")
    if not results:
        return None
    block = "\n".join(f"- {r['url']}\n  {r['text']}" for r in results)
    prompt = f"QUESTION: {question!r}\n\nSEARCH RESULTS:\n{block}\n\nReturn the JSON."
    try:
        raw = llm_call(prompt, system=SYS, max_tokens=200, model=LLM_MODEL_HAIKU)
        j = json.loads(re.search(r"\{.*\}", raw, re.S).group(0))
        if j.get("next_earnings_date") and j["next_earnings_date"] >= TODAY:
            return j
    except Exception:
        pass
    return None

def main():
    path = ROOT / "web/data/universe-enriched-linked.json"
    bundle = json.loads(path.read_text())
    targets = [e for e in bundle["events"] if classify_earnings(e)]
    print(f"earnings-classified events: {len(targets)}\n")

    review = []
    for e in targets:
        res = lookup(e.get("question", ""))
        if res:
            cd = {"date": res["next_earnings_date"], "type": "corporate_earnings",
                  "label": f"{res.get('company') or 'Company'} earnings", "source_url": res.get("source_url")}
            e["catalyst_dates"] = [cd]
            review.append((e["event_id"], e.get("question", "")[:48], cd["date"], res.get("company"), cd["source_url"]))
        else:
            review.append((e["event_id"], e.get("question", "")[:48], "—(no future date found)", None, None))

    print("=== REVIEW (NOT pushed to D1 — spot-check before going live) ===")
    for eid, q, d, co, url in review:
        print(f"  {d:24} {q!r}  [{co}]")
        if url: print(f"        src: {url}")
    populated = sum(1 for r in review if r[2].startswith("2"))
    print(f"\npopulated {populated}/{len(targets)} earnings events in the bundle (D1 push HELD for your review).")
    path.write_text(json.dumps(bundle, default=str))

if __name__ == "__main__":
    main()
