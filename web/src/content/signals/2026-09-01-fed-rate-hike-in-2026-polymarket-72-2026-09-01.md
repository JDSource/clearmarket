---
signal_id: "CMSIG2026090102"
signal_slug: "fed-rate-hike-in-2026-polymarket-72-2026-09-01"
headline: "Fed rate hike in 2026: Polymarket 72%"
semantic_title: "Markets back a 2026 Fed hike at roughly 3-in-4 odds"
telemetry: "Polymarket 72%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-01T00:00:00.000Z"
event_id: "CM-EVT-87QV1G78C4"
event_slug: "fed-rate-hike-in-2026"
event_question: "Will the Federal Reserve raise its benchmark interest rate in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x80b3af88cb991980e8da1ce86b9794a0957f96ec98c29319dd7ba65e9744d82b"
  question_raw: "Fed rate hike in 2026?"
  current_price: 0.72
  volume_24h_usd: 99212.58526300002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-09T00:00:00Z"
bullets:
  - "The Polymarket contract on a 2026 Fed rate hike sits at 72%, a clear majority but well short of certainty."
  - "Slowing factory orders cut against the hike case on growth grounds, yet the Prices Index holding at 71.1 keeps inflation pressure alive and supports the 72% read."
  - "Fed Governor Michael Barr's conditional hike endorsement and Warsh's Jackson Hole signal together align with the market's majority-but-not-certain pricing."
  - "Resolution via UMA oracle on whether the Fed actually raises its benchmark rate at any 2026 meeting; the September meeting in roughly two weeks is the nearest trigger."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US manufacturing activity slowed in August while input prices remained elevated, adding to the stagflationary backdrop pressuring the Fed."
    publisher: "Thomson Reuters"
    published_at: "2026-09-01T00:00:00.000Z"
    source_url: "https://979weve.com/2026/09/01/us-manufacturing-activity-slows-in-august-input-prices-still-elevated/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Thomson Reuters"
        source_url: "https://979weve.com/2026/09/01/us-manufacturing-activity-slows-in-august-input-prices-still-elevated/"
        retrieved_at: "2026-09-02T12:29:02+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; the 72% probability is consistent with both the hawkish Fed commentary and the mixed manufacturing data in play this week."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Thomson Reuters: US factory activity slows in August; input prices remain elevated | 97"
    url: "https://979weve.com/2026/09/01/us-manufacturing-activity-slows-in-august-input-prices-still-elevated/"
    published_at: "2026-09-01T00:00:00.000Z"
    retrieved_at: "2026-09-02T12:29:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
