---
signal_id: "CMSIG2026072901"
signal_slug: "july-fed-funds-upper-bound-seen-3-75-kalshi-ladder-2026-07-29"
headline: "July Fed funds upper bound seen 3.75%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen near 3.75% after July hold"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-29T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Federal funds upper bound after July 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.03
  volume_24h_usd: 73.63
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder pins the post-July Fed funds upper bound near 3.75%, with 57% above 3.75% but only 3% above 4.0%."
  - "The Fed held at 3.5-3.75% as reported, which is broadly consistent with the ladder's sharp drop-off above 4.0%."
  - "Three dissents for a hike signal internal pressure, yet the ladder puts just 3% odds on 4.0% or higher, market is not pricing escalation."
  - "The 57% split at the 3.75% strike reflects genuine uncertainty about whether the upper bound sits at exactly 3.75% vs. 3.5%, not about a hike."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Federal Reserve held its benchmark rate unchanged at 3.5-3.75% for the fifth consecutive meeting, with three dissents in favor of a hike."
    publisher: "euronews.com"
    published_at: "2026-07-29T00:00:00.000Z"
    source_url: "https://www.euronews.com/business/2026/07/29/us-federal-reserve-holds-interest-rates-steady-as-three-policymakers-back-hike"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "euronews.com"
        source_url: "https://www.euronews.com/business/2026/07/29/us-federal-reserve-holds-interest-rates-steady-as-three-policymakers-back-hike"
        retrieved_at: "2026-07-31T10:34:33+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder distribution is consistent with the announced hold; the tiny probability above 4.0% suggests traders are not treating the three dissents as actionable."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "euronews.com: US Federal Reserve holds interest rates steady as three policymakers b"
    url: "https://www.euronews.com/business/2026/07/29/us-federal-reserve-holds-interest-rates-steady-as-three-policymakers-back-hike"
    published_at: "2026-07-29T00:00:00.000Z"
    retrieved_at: "2026-07-31T10:34:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
