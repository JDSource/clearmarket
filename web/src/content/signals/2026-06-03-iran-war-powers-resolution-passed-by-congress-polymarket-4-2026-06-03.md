---
signal_id: "CMSIG2026060302"
signal_slug: "iran-war-powers-resolution-passed-by-congress-polymarket-4-2026-06-03"
headline: "Iran war powers resolution passed by Congress: Polymarket 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-06-03T17:49:52.000Z"
event_id: "CM-EVT-KF5S4BY541"
event_slug: "congress-passes-iran-war-powers-resolution-by-june-30"
event_question: "Will Congress pass an Iran war powers resolution by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xcb3c2e94aefd13bb09a72fdf74d44fa7b2ebe437b863e0621831c020bfd4ed4d"
  question_raw: "Congress passes Iran war powers resolution by June 30?"
  current_price: 0.039
  volume_24h_usd: 1234.659639
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket contract prices only 4% on Congress passing an Iran war-powers resolution by June 30."
  - "House passage happened, but the contract likely requires Senate passage too, explaining the sharp gap between the news and the price."
  - "Senate passage remains the key hurdle; without it, the resolution is symbolic and the contract likely resolves No."
  - "Resolves via uma_oracle; resolution almost certainly requires both chambers to pass a binding measure by June 30."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US House passed a war-powers resolution directing Trump to end hostilities with Iran."
    publisher: "nhpr.org"
    published_at: "2026-06-03T17:49:52.000Z"
    source_url: "https://www.nhpr.org/2026-06-03/house-passes-war-powers-resolution-directing-trump-to-end-hostilities-with-iran"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "nhpr.org"
        source_url: "https://www.nhpr.org/2026-06-03/house-passes-war-powers-resolution-directing-trump-to-end-hostilities-with-iran"
        retrieved_at: "2026-06-04T03:24:20+00:00"
  - type: "pm_response"
    notes: "Polymarket at 4% reflects Senate blocking risk, not House action alone."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "nhpr.org: House passes war powers resolution directing Trump to end hostilities"
    url: "https://www.nhpr.org/2026-06-03/house-passes-war-powers-resolution-directing-trump-to-end-hostilities-with-iran"
    published_at: "2026-06-03T17:49:52.000Z"
    retrieved_at: "2026-06-04T03:24:20+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
