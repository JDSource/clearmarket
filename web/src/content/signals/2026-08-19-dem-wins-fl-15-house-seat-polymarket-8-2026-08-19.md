---
signal_id: "CMSIG2026081906"
signal_slug: "dem-wins-fl-15-house-seat-polymarket-8-2026-08-19"
headline: "Dem wins FL-15 House seat: Polymarket 8%"
semantic_title: "Democrats keep long odds on Florida 15th despite progressive wins"
telemetry: "Polymarket 8%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-19T00:00:00.000Z"
event_id: "CM-EVT-7YL4ZGZQN4"
event_slug: "fl-15-house-election-winner"
event_question: "Will the Republican or Democratic candidate win Florida's 15th Congressional District House election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5b7ff1a78f92f7476a6d929214f37d5162e4f7e48dc7ff7a70b213e5c44eee65"
  question_raw: "Will the Democratic Party win the FL-15 House seat?"
  current_price: 0.081
  volume_24h_usd: 20.0
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices only 8% on the Democratic candidate winning Florida's 15th Congressional District general election, resolving via UMA oracle."
  - "Progressive primary wins are generating attention, but the market prices Florida's 15th as a near-certain Republican hold in November."
  - "A companion FL-28 Polymarket contract also sits at 8%, suggesting the market treats multiple Florida districts as similarly out of reach for Democrats regardless of primary outcomes."
  - "Kalshi's FL-27 contract at 82% for the Republican candidate reinforces the pattern: Florida House seats are broadly priced as Republican locks even as primaries shift left."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Progressive Democratic candidates have scored a series of upset primary victories including in Florida, raising questions about the movement's general-election viability."
    publisher: "cbsnews.com"
    published_at: "2026-08-19T00:00:00.000Z"
    source_url: "https://www.cbsnews.com/news/democratic-primaries-progressive-wins-midterm-elections/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cbsnews.com"
        source_url: "https://www.cbsnews.com/news/democratic-primaries-progressive-wins-midterm-elections/"
        retrieved_at: "2026-08-22T08:23:10+00:00"
  - type: "pm_response"
    notes: "Three Florida House Polymarket contracts cluster at 8%, suggesting the market is consistently dismissing progressive primary momentum as a general-election factor in Florida."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cbsnews.com: How progressive wins in Democratic primaries are shaping the midterm l"
    url: "https://www.cbsnews.com/news/democratic-primaries-progressive-wins-midterm-elections/"
    published_at: "2026-08-19T00:00:00.000Z"
    retrieved_at: "2026-08-22T08:23:10+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
