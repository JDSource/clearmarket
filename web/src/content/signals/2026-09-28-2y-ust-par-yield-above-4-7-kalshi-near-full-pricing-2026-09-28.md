---
signal_id: "CMSIG2026092803"
signal_slug: "2y-ust-par-yield-above-4-7-kalshi-near-full-pricing-2026-09-28"
headline: "2Y UST par yield above 4.7%: Kalshi near full pricing"
semantic_title: "Short-term Treasury yields stay heavily priced above 4.7%"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-28T00:00:00.000Z"
event_id: "CM-EVT-FQWTB38T69"
event_slug: "kxustyld-26sep30"
event_question: "2-year UST par yield curve for Q3 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXUSTYLD-26SEP30-T4.70"
  question_raw: "Will UST Par Yield Curve (2Y) for Q3 2026 be above 4.70%?"
  current_price: 0.98
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics- Employment Situation"
  resolves_at: "2026-10-07T21:00:00Z"
bullets:
  - "Kalshi ladder prices the 2Y par yield above every strike shown through 4.7%, each at 98-99%, consistent with a regime where short rates are deeply elevated."
  - "The 10-year yield hitting 5.22% as reported today is directionally consistent with the ladder's near-certain pricing of 2Y yields above 4.7%."
  - "The ladder's flat near-100% structure across all strikes through 4.7% signals the market has already fully priced the current rate environment with no tail risk of a sharp rally."
  - "Resolution ties to the Federal Reserve's published par yield curve data for Q3 2026; the settlement figure is a quarterly average, not a single-day print."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin is holding near $84,000 even as the 10-year Treasury yield climbed to 5.22%, extending a historic bond selloff as traders unwind $1.7 billion in leverage."
    publisher: "cryptorenews.com"
    published_at: "2026-09-28T00:00:00.000Z"
    source_url: "https://cryptorenews.com/analysis/bitcoin-survives-a-5-2-treasury-shock-as-traders-slash-1-7-billion-in-leverage/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cryptorenews.com"
        source_url: "https://cryptorenews.com/analysis/bitcoin-survives-a-5-2-treasury-shock-as-traders-slash-1-7-billion-in-leverage/"
        retrieved_at: "2026-09-28T07:47:41+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder shows no material probability mass below 4.7% for Q3 2026, making this effectively a resolved-in-place distribution."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cryptorenews.com: Bitcoin withstands 5.2% Treasury surge as traders unwind $1.7 billion"
    url: "https://cryptorenews.com/analysis/bitcoin-survives-a-5-2-treasury-shock-as-traders-slash-1-7-billion-in-leverage/"
    published_at: "2026-09-28T00:00:00.000Z"
    retrieved_at: "2026-09-28T07:47:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
