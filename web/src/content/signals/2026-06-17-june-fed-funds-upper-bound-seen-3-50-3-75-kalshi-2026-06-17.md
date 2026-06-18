---
signal_id: "CMSIG2026061701"
signal_slug: "june-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-06-17"
headline: "June Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Fed funds upper bound consensus locks at 3.50-3.75 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-17T19:50:23.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Fed funds upper bound after June 2026 FOMC"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.36
  volume_24h_usd: 3.96
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-16T18:05:00Z"
bullets:
  - "Kalshi prices the Fed funds upper bound in the 3.50-3.75% range: 95% above 3.50% but only 36% above 3.75%, implying a sharp ceiling there."
  - "Warsh held rates at the June FOMC meeting, consistent with the 95% pricing at or above 3.50%; the hawkish dot plot aligns with the market's ceiling near 3.75%."
  - "The sharp drop from 95% to 36% between the 3.50% and 3.75% strikes signals the market prices exactly one hike as the modal outcome, not two."
  - "A companion Kalshi ladder (CM-EVT-PHWX2H6DM5) shows only 13% above 3.75%, a cross-ladder check confirming both distributions converge on the same implied terminal ceiling."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Chair Kevin Warsh held rates steady at his first FOMC meeting but the dot plot shifted significantly hawkish, with nine policymakers backing further hikes in 2026."
    publisher: "Micah Zimmerman"
    published_at: "2026-06-17T19:50:23.000Z"
    source_url: "https://bitcoinmagazine.com/news/fed-signals-rate-hikes-as-kevin-warsh"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Micah Zimmerman"
        source_url: "https://bitcoinmagazine.com/news/fed-signals-rate-hikes-as-kevin-warsh"
        retrieved_at: "2026-06-18T11:48:44+00:00"
  - type: "pm_response"
    notes: "Two independent Kalshi ladders (CM-EVT-4ZQLQPNH91 and CM-EVT-PHWX2H6DM5) produce consistent distributions, both pinning the upper bound consensus at 3.50-3.75% with a hard ceiling above 3.75%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Micah Zimmerman: Fed Signals Possible Rate Hikes As Kevin Warsh Opens ‘New Chapter’ At"
    url: "https://bitcoinmagazine.com/news/fed-signals-rate-hikes-as-kevin-warsh"
    published_at: "2026-06-17T19:50:23.000Z"
    retrieved_at: "2026-06-18T11:48:44+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
