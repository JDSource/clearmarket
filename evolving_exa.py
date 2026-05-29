"""
Evolving / geopolitics catalysts via Exa + Claude, with deep-link + authoritative-source enforcement.

Per Jeremy: Exa search, PRESERVE deep links, prefer authoritative(ish) sources. The date is bound
to an Exa tool-result URL that (a) is a deep link (real path depth, not a root/section page) AND
(b) sits on an authoritative-ish domain (.gov / official body / reputable outlet). Events with no
clean authoritative deep link stay `none` — precision over recall on provenance.

Capped at EXA_CAP Exa calls/run. HOLDS the D1 push (LLM-extracted dates → human spot-check).
Reads/writes web/data/universe-enriched-linked.json.
"""
import json, os, re, requests, sys
from urllib.parse import urlparse
from pathlib import Path
from dotenv import load_dotenv
from enhance import llm_call, LLM_MODEL_HAIKU

ROOT = Path(__file__).parent
load_dotenv(ROOT / ".env")
EXA_KEY = os.getenv("EXA_API_KEY")
TODAY = "2026-05-28"
EXA_CAP = int(sys.argv[1]) if len(sys.argv) > 1 else 30

AUTH = (".gov", ".mil", "un.org", "europa.eu", "reuters.com", "apnews.com", "bloomberg.com",
        "ft.com", "wsj.com", "nytimes.com", "bbc.com", "bbc.co.uk", "politico.com", "politico.eu",
        "congress.gov", "parliament.uk", "whitehouse.gov", "aljazeera.com", "theguardian.com",
        "cnbc.com", "axios.com", "scotusblog.com")

def is_auth(url):
    h = (urlparse(url).hostname or "").lower()
    return any(h.endswith(d) or d in h for d in AUTH)

def is_deep(url):
    segs = [s for s in urlparse(url).path.split("/") if s]
    return len(segs) >= 2  # real article/page path, not a root or single-section landing page

def classify_evolving(ev):
    if ev.get("category") not in ("geopolitics", "politics"):
        return False
    if ev.get("catalyst_dates"):
        return False
    t = ((ev.get("question") or "") + " " + " ".join(ev.get("tags") or [])).lower()
    return bool(re.search(r"\b(ceasefire|war|invade|sanction|treaty|summit|election|vote|referendum|"
                          r"court|ruling|scotus|impeach|resign|out as|leave office|nato|nominee|"
                          r"confirm|sign into law|\bbill\b|legislation|hearing|trial|verdict)\b", t))

def exa(query):
    r = requests.post("https://api.exa.ai/search",
                      headers={"x-api-key": EXA_KEY, "Content-Type": "application/json"},
                      json={"query": query, "numResults": 6, "contents": {"text": {"maxCharacters": 600}}},
                      timeout=30)
    return r.json().get("results", []) if r.ok else []

SYS = ("Extract the NEXT scheduled date for the event described in the question, from the source text. "
       'Output ONLY JSON {"date":"YYYY-MM-DD"|null}. The date MUST be >= ' + TODAY + " and explicitly "
       "stated in the text. If not clearly stated, return null. NEVER invent a date.")

def lookup(question):
    for res in exa(f"{question[:90]} scheduled date 2026"):
        url = res.get("url", "")
        if not (is_auth(url) and is_deep(url)):
            continue
        try:
            raw = llm_call(f"QUESTION: {question!r}\nSOURCE ({url}):\n{(res.get('text') or '')[:600]}\n\nReturn JSON.",
                           system=SYS, max_tokens=80, model=LLM_MODEL_HAIKU)
            j = json.loads(re.search(r"\{.*\}", raw, re.S).group(0))
            if j.get("date") and j["date"] >= TODAY:
                return {"date": j["date"], "source_url": url}
        except Exception:
            pass
    return None

def main():
    path = ROOT / "web/data/universe-enriched-linked.json"
    bundle = json.loads(path.read_text())
    cands = [e for e in bundle["events"] if classify_evolving(e)]
    print(f"evolving candidates (geopolitics/politics, currently none): {len(cands)} | Exa cap this run: {EXA_CAP}")

    review = []
    rejected_nonauth = 0
    calls = 0
    for e in cands:
        if calls >= EXA_CAP:
            break
        calls += 1
        res = lookup(e.get("question", ""))
        if res:
            e["catalyst_dates"] = [{"date": res["date"], "type": "evolving", "label": "scheduled event", "source_url": res["source_url"]}]
            review.append((res["date"], e.get("question", "")[:50], res["source_url"]))
        else:
            rejected_nonauth += 1

    print(f"Exa calls: {calls} | populated w/ authoritative deep link: {len(review)} | no clean source (stay none): {rejected_nonauth}\n")
    for d, q, u in review[:25]:
        print(f"  {d}  {q!r}\n      {u}")
    path.write_text(json.dumps(bundle, default=str))
    print(f"\npopulated {len(review)} evolving events — HELD from D1 (spot-check the sources before pushing).")

if __name__ == "__main__":
    main()
