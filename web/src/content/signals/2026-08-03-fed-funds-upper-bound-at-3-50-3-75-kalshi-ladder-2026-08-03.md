---
signal_id: "CMSIG2026080302"
signal_slug: "fed-funds-upper-bound-at-3-50-3-75-kalshi-ladder-2026-08-03"
headline: "Fed funds upper bound at 3.50-3.75%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen settling at 3.50-3.75%"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-03T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Federal funds upper bound (next decision)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.47
  volume_24h_usd: 9238.91
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder pins the federal funds upper bound in the 3.50-3.75% range: 99% above 3.50%, but only 47% above 3.75%, and just 2% above 4.00%."
  - "Manufacturing survey inflation fears align with the market pricing in at least one more hike to 3.75%, but the distribution shows limited conviction beyond that level."
  - "The sharp drop-off above 3.75% suggests the market is not pricing an aggressive tightening cycle despite hawkish commentary from Fed officials."
  - "Kansas City Fed President Jeff Schmid's remarks (Stories 4 and 7) calling current policy non-restrictive are consistent with the ladder's modal range but the market is not fully pricing his implied path higher."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "ISM Manufacturing survey showed robust factory conditions and elevated price pressures, with managers comparing pricing volatility to the Covid era."
    publisher: "Jeff Cox"
    published_at: "2026-08-03T00:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/08/03/manufacturing-survey-shows-inflation-worries-adding-to-pressure-on-fed.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jeff Cox"
        source_url: "https://www.cnbc.com/2026/08/03/manufacturing-survey-shows-inflation-worries-adding-to-pressure-on-fed.html"
        retrieved_at: "2026-08-06T10:35:15+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via Federal Reserve decision; the distribution is tightly concentrated at the 3.50-3.75% band with very thin tails above 4.00%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jeff Cox: Manufacturing survey shows inflation worries adding to pressure on Fed"
    url: "https://www.cnbc.com/2026/08/03/manufacturing-survey-shows-inflation-worries-adding-to-pressure-on-fed.html"
    published_at: "2026-08-03T00:00:00.000Z"
    retrieved_at: "2026-08-06T10:35:15+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
