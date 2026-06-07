---
signal_id: "CMSIG2026060604"
signal_slug: "any-hormuz-ship-transit-by-june-30-polymarket-58-2026-06-06"
headline: "Any Hormuz ship transit by June 30: Polymarket 58%"
semantic_title: "Hormuz ship transit by June 30 wavers near even odds"
telemetry: "Polymarket 58%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-06T07:51:28.000Z"
event_id: "CM-EVT-VB1YHPRLZ3"
event_slug: "will-ships-transit-the-strait-of-hormuz-on-any-day-by-june-30"
event_question: "Will any ships transit the Strait of Hormuz by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x2358809f9f612f8fb4f224b342ba2841ca644a6e3c46adb4c3bcee910cc31632"
  question_raw: "Will 20 ships transit the Strait of Hormuz on any day by June 30, 2026?"
  current_price: 0.58
  volume_24h_usd: 4003.476819
  arbitration_model: "uma_oracle"
  resolution_source: "portwatch.imf.org"
  resolves_at: "2026-06-30T16:00:00Z"
bullets:
  - "Polymarket prices a 58% chance that at least one ship transits the Strait of Hormuz by June 30."
  - "Active Iranian missile and drone launches toward the Strait are consistent with a market still below 60% on even minimal commercial transit resuming."
  - "The companion near-term Hormuz normalization contract sits at only 20% for full traffic return by end of June, reflecting deep skepticism on full reopening."
  - "Resolves via portwatch.imf.org shipping traffic data; even a single confirmed transit triggers yes."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran fired ballistic missiles and drones toward the Strait of Hormuz after U.S. forces struck Iranian coastal radar sites, further straining a fragile ceasefire."
    publisher: "Al Jazeera Staff"
    published_at: "2026-06-06T07:51:28.000Z"
    source_url: "https://1-e8259.azureedge.net/news/2026/6/6/us-intercepts-iranian-attacks-as-israel-continues-to-bomb-lebanon"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Al Jazeera Staff"
        source_url: "https://1-e8259.azureedge.net/news/2026/6/6/us-intercepts-iranian-attacks-as-israel-continues-to-bomb-lebanon"
        retrieved_at: "2026-06-07T10:26:16+00:00"
  - type: "pm_response"
    notes: "Polymarket at 58% on any transit reflects cautious optimism amid live exchanges of fire, a far cry from normalcy pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Al Jazeera Staff: Iran fires missiles at Gulf after US targets Iranian radar sites | US-"
    url: "https://1-e8259.azureedge.net/news/2026/6/6/us-intercepts-iranian-attacks-as-israel-continues-to-bomb-lebanon"
    published_at: "2026-06-06T07:51:28.000Z"
    retrieved_at: "2026-06-07T10:26:16+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
