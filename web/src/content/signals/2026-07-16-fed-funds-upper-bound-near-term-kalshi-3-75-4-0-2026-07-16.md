---
signal_id: "CMSIG2026071604"
signal_slug: "fed-funds-upper-bound-near-term-kalshi-3-75-4-0-2026-07-16"
headline: "Fed funds upper bound near-term: Kalshi 3.75-4.0%"
semantic_title: "Near-term Fed funds path anchors at 3.75-4.0 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-16T13:25:24.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Near-term Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.29
  volume_24h_usd: 0.87
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the near-term Fed funds upper bound in the 3.75-4.0% range, with 57% above 3.75% but only 29% above 4.0%."
  - "A strong jobless claims print reinforces labor market resilience, consistent with the market holding the funds rate above current levels near-term."
  - "Longer-horizon ladders for the same rate level show sharply lower probabilities, with one ladder pricing only 4% above 3.75% at a later date, pointing to expected easing over time."
  - "Resolves via Federal Reserve official policy decision; the specific settlement date on this contract determines which FOMC meeting applies."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US initial jobless claims fell 8,000 to a seasonally adjusted 208,000, defying expectations of labor market softening."
    publisher: "finance.biggo.com"
    published_at: "2026-07-16T13:25:24.000Z"
    source_url: "https://finance.biggo.com/news/c4acb560-4102-48b5-8ffb-4ed7250847a7"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "finance.biggo.com"
        source_url: "https://finance.biggo.com/news/c4acb560-4102-48b5-8ffb-4ed7250847a7"
        retrieved_at: "2026-07-17T09:53:11+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder contract; implied range derived from the strike probability distribution provided, not a single binary price."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "finance.biggo.com: US Jobless Claims Drop to 208,000, Defying Expectations of Labor Marke"
    url: "https://finance.biggo.com/news/c4acb560-4102-48b5-8ffb-4ed7250847a7"
    published_at: "2026-07-16T13:25:24.000Z"
    retrieved_at: "2026-07-17T09:53:11+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
