---
signal_id: "CMSIG2026092305"
signal_slug: "strait-of-hormuz-normal-by-dec-31-polymarket-23-2026-09-23"
headline: "Strait of Hormuz normal by Dec 31: Polymarket 23%"
semantic_title: "Hormuz traffic returning to normal by year-end stays near 25%"
telemetry: "Polymarket 23%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-23T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.23
  volume_24h_usd: 316895.1091900001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 23% odds that Strait of Hormuz traffic returns to normal by December 31, keeping a reopening scenario a clear minority view."
  - "Iran's 'very productive' three-hour UN talks are modestly encouraging, but the market's 23% reflects the conditionality: Iran's seven preconditions remain on the table and unresolved."
  - "The gap between Iran's stated seven-day reopening timeline (if conditions met) and the market's 23% year-end probability signals markets are heavily discounting a swift deal."
  - "A companion Polymarket contract puts the chance Israel reopens its embassy in Iran by 2026 at just 1%, showing markets see normalization far beyond Hormuz reopening as essentially ruled out."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran denied dropping its seven preconditions at UN talks described as 'very productive,' while signaling Hormuz could reopen within seven days if conditions are met."
    publisher: "Patrick Wintour"
    published_at: "2026-09-23T00:00:00.000Z"
    source_url: "https://www.theguardian.com/world/2026/sep/23/iran-denies-dropping-preconditions-very-productive-three-hour-un-talks-new-york"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Patrick Wintour"
        source_url: "https://www.theguardian.com/world/2026/sep/23/iran-denies-dropping-preconditions-very-productive-three-hour-un-talks-new-york"
        retrieved_at: "2026-09-23T13:17:11+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 23%, resolved via UMA oracle; the 'very productive' diplomatic framing from both sides has not moved the market to price a near-term reopening."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Patrick Wintour: Iran denies dropping preconditions amid ‘very productive’ three-hour U"
    url: "https://www.theguardian.com/world/2026/sep/23/iran-denies-dropping-preconditions-very-productive-three-hour-un-talks-new-york"
    published_at: "2026-09-23T00:00:00.000Z"
    retrieved_at: "2026-09-23T13:17:11+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
