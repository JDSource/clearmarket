---
signal_id: "CMSIG2026062906"
signal_slug: "hormuz-traffic-normal-by-jun-30-polymarket-0-2026-06-29"
headline: "Hormuz traffic normal by Jun 30: Polymarket 0%"
semantic_title: "Hormuz traffic normal by June 30 sits at zero pricing"
telemetry: "Polymarket 0%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-29T20:14:00.000Z"
event_id: "CM-EVT-YPW93GCTK6"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-end-of-june"
event_question: "Will traffic through the Strait of Hormuz return to normal by the end of June?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x348cd9adf4f6855f58bd9c6dbf9ff251c4142ef77233a5dc95c65b4b61cd2187"
  question_raw: "Strait of Hormuz traffic returns to normal by end of June?"
  current_price: 0.005
  volume_24h_usd: 574061.824316
  arbitration_model: "uma_oracle"
  resolution_source: "portwatch.imf.org"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prediction market prices 0% odds that Strait of Hormuz traffic returns to normal by end of June 30."
  - "Weekend strikes and continued US-Iran disagreement over talks make a same-day Hormuz normalization effectively impossible, consistent with the 0% pricing."
  - "The Iranian regime survival contract (CM-EVT-XYC4HDKBW3) at 100% on Polymarket confirms markets see the strikes as contained, not existential, for the current Iranian government."
  - "Resolves via portwatch.imf.org traffic data by June 30; the unresolved diplomatic standoff reported across multiple wires makes this a near-certain zero at settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US and Iran pulled back from escalating weekend strikes near the Strait of Hormuz but remain at odds over the terms and format of any further negotiations."
    publisher: "The Christian Science Monitor"
    published_at: "2026-06-29T20:14:00.000Z"
    source_url: "https://www.csmonitor.com/World/Middle-East/2026/0629/trump-iran-war-ceasefire-violations-hormuz-control"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "The Christian Science Monitor"
        source_url: "https://www.csmonitor.com/World/Middle-East/2026/0629/trump-iran-war-ceasefire-violations-hormuz-control"
        retrieved_at: "2026-06-30T10:54:27+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via portwatch.imf.org; with no diplomatic breakthrough confirmed as of June 30, the 0% pricing aligns fully with current reported conditions."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "The Christian Science Monitor: Hormuz flare-up signals lasting fragility of US-Iran ceasefire - CSMon"
    url: "https://www.csmonitor.com/World/Middle-East/2026/0629/trump-iran-war-ceasefire-violations-hormuz-control"
    published_at: "2026-06-29T20:14:00.000Z"
    retrieved_at: "2026-06-30T10:54:27+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
