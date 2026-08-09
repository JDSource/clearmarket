---
signal_id: "CMSIG2026080701"
signal_slug: "fed-funds-upper-bound-seen-3-50-3-75-kalshi-99-35-2026-08-07"
headline: "Fed funds upper bound seen 3.50-3.75%: Kalshi 99%/35%"
semantic_title: "Fed funds upper bound stays priced at 3.50-3.75 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-07T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Federal funds upper bound after September 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.35
  volume_24h_usd: 135.74
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder prices the September 2026 Fed funds upper bound firmly in the 3.50-3.75% range: 99% above 3.50%, only 35% above 3.75%."
  - "July payrolls shed 23,000 jobs versus a forecast of plus 95,000, the Kalshi distribution is consistent with a hold at the next meeting."
  - "Kalshi ladder implies nearly zero probability of a hike to 4.00% or above, with all strikes from 4.00% to 5.25% at 1%."
  - "CME FedWatch puts September hold odds at 60%; Kalshi's implied distribution aligns closely, confirming cross-venue consensus on no September hike."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A weaker-than-expected July jobs report caused traders to sharply reduce odds of a September Fed rate hike."
    publisher: "Davis Giangiulio"
    published_at: "2026-08-07T00:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/08/07/odds-the-fed-hikes-in-september-tumble-following-big-july-jobs-miss.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Davis Giangiulio"
        source_url: "https://www.cnbc.com/2026/08/07/odds-the-fed-hikes-in-september-tumble-following-big-july-jobs-miss.html"
        retrieved_at: "2026-08-09T08:36:33+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via the Federal Reserve's post-September meeting announcement; current distribution rules out any hike scenario."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Davis Giangiulio: Odds the Fed hikes in September tumble following big July jobs miss"
    url: "https://www.cnbc.com/2026/08/07/odds-the-fed-hikes-in-september-tumble-following-big-july-jobs-miss.html"
    published_at: "2026-08-07T00:00:00.000Z"
    retrieved_at: "2026-08-09T08:36:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
