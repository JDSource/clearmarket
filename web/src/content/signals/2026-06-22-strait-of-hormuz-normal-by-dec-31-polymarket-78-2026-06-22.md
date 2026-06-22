---
signal_id: "CMSIG2026062202"
signal_slug: "strait-of-hormuz-normal-by-dec-31-polymarket-78-2026-06-22"
headline: "Strait of Hormuz normal by Dec 31: Polymarket 78%"
semantic_title: "Hormuz full reopening by year-end commands strong consensus"
telemetry: "Polymarket 78%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-22T07:21:10.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will traffic through the Strait of Hormuz return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.78
  volume_24h_usd: 289674.7514719999
  arbitration_model: "uma_oracle"
  resolution_source: "portwatch.imf.org"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Strait of Hormuz traffic returning to normal by December 31 at 78%, reflecting confidence over the longer horizon."
  - "Talk progress supports the year-end contract; Trump's threat to take over the Strait adds escalation risk but markets are not pricing a breakdown."
  - "Near-term contracts tell a different story: June 30 reopening sits at only 18% and the July 31 contract at 47%, revealing a steep term structure."
  - "The December 31 contract resolves via portwatch.imf.org traffic data; a full return to normal shipping volumes is the settlement bar, not a political agreement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US-Iran Switzerland talks concluded with encouraging progress and technical sessions to continue, while Trump separately threatened to take over the Strait if it remains closed."
    publisher: "aljazeera.com"
    published_at: "2026-06-22T07:21:10.000Z"
    source_url: "https://www.aljazeera.com/news/2026/6/22/iran-war-day-115-lebanon-truce-appears-to-hold-as-switzerland-talks-end"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "aljazeera.com"
        source_url: "https://www.aljazeera.com/news/2026/6/22/iran-war-day-115-lebanon-truce-appears-to-hold-as-switzerland-talks-end"
        retrieved_at: "2026-06-22T13:32:28+00:00"
  - type: "pm_response"
    notes: "Polymarket's three-horizon ladder (18% June, 47% July, 78% December) captures the market's view that a deal is likely but weeks or months away, not imminent."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "aljazeera.com: Iran war day 115: Lebanon truce appears to hold as Switzerland talks e"
    url: "https://www.aljazeera.com/news/2026/6/22/iran-war-day-115-lebanon-truce-appears-to-hold-as-switzerland-talks-end"
    published_at: "2026-06-22T07:21:10.000Z"
    retrieved_at: "2026-06-22T13:32:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
