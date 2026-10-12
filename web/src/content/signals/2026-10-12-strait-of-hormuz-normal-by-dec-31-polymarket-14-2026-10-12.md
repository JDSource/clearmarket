---
signal_id: "CMSIG2026101202"
signal_slug: "strait-of-hormuz-normal-by-dec-31-polymarket-14-2026-10-12"
headline: "Strait of Hormuz normal by Dec 31: Polymarket 14%"
semantic_title: "Hormuz traffic back to normal by year-end stays a long shot"
telemetry: "Polymarket 14%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-12T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.14
  volume_24h_usd: 76336.364558
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts only 14% odds on Strait of Hormuz traffic returning to normal by December 31, 2026."
  - "Reported US-Iran talks on a phased reopening deal are consistent with a slight opening for resolution, but the market firmly prices the deal as unlikely to close by year-end."
  - "Oil prices fell Monday partly on Trump's energy ceasefire claim, but the low Hormuz normalization probability suggests markets are not yet pricing a durable supply route restoration."
  - "Resolution via UMA oracle requires confirmed return of normal transit levels, not merely a political announcement, raising the bar beyond diplomacy alone."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Washington and Tehran have held talks on a phased deal to reopen the Strait of Hormuz and end a US blockade, according to Reuters sources."
    publisher: "Samuel Brown"
    published_at: "2026-10-12T00:00:00.000Z"
    source_url: "https://new-york.news/2026/10/12/us-and-iran-discuss-phased-deal-to-reopen-hormuz-and-end-us-blockade-sources-say-reuters/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Samuel Brown"
        source_url: "https://new-york.news/2026/10/12/us-and-iran-discuss-phased-deal-to-reopen-hormuz-and-end-us-blockade-sources-say-reuters/"
        retrieved_at: "2026-10-12T17:17:25+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; at 14%, the market prices the phased deal as a possibility but not a near-term probability."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Samuel Brown: US and Iran discuss phased deal to reopen Hormuz and end US blockade,"
    url: "https://new-york.news/2026/10/12/us-and-iran-discuss-phased-deal-to-reopen-hormuz-and-end-us-blockade-sources-say-reuters/"
    published_at: "2026-10-12T00:00:00.000Z"
    retrieved_at: "2026-10-12T17:17:25+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
