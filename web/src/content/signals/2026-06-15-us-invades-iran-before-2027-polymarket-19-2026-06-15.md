---
signal_id: "CMSIG2026061503"
signal_slug: "us-invades-iran-before-2027-polymarket-19-2026-06-15"
headline: "US invades Iran before 2027: Polymarket 19%"
semantic_title: "US invasion of Iran before 2027 absorbs ceasefire news at 19 percent"
telemetry: "Polymarket 19%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-15T02:47:07.000Z"
event_id: "CM-EVT-WD982793G1"
event_slug: "will-the-us-invade-iran-before-2027"
event_question: "Will the United States invade Iran before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5db999fad322cea2914535aae5517060c3f80ad6d8c0231cde2124a434d16846"
  question_raw: "Will the U.S. invade Iran before 2027?"
  current_price: 0.19
  volume_24h_usd: 618551.2674090003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a US invasion of Iran before 2027 at 19%, holding well above zero despite a announced permanent ceasefire."
  - "The peace deal announcement is directionally consistent with reduced invasion risk, yet nearly one-in-five odds remain, reflecting market skepticism about deal durability."
  - "The Pahlavi recognition contract on Kalshi sits at only 8%, suggesting markets also see regime change as an unlikely outcome of current diplomacy."
  - "Resolution is via UMA oracle; what constitutes an invasion under contract terms versus ongoing or resumed strikes would be the key settlement edge."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "A US-Iran peace deal was announced with permanent end to military action and Hormuz reopening June 19."
    publisher: "AFP"
    published_at: "2026-06-15T02:47:07.000Z"
    source_url: "https://www.newindianexpress.com/amp/story/world/2026/Jun/15/us-iran-peace-deal-announced-with-permanent-end-to-military-action-hormuz-strait-to-open-june-19"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "AFP"
        source_url: "https://www.newindianexpress.com/amp/story/world/2026/Jun/15/us-iran-peace-deal-announced-with-permanent-end-to-military-action-hormuz-strait-to-open-june-19"
        retrieved_at: "2026-06-15T13:51:44+00:00"
  - type: "pm_response"
    notes: "Polymarket at 19% on invasion shows the market is not fully pricing the ceasefire as durable, retaining meaningful tail risk through 2026."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "AFP: US-Iran peace deal announced with ‘permanent’ end to military action;"
    url: "https://www.newindianexpress.com/amp/story/world/2026/Jun/15/us-iran-peace-deal-announced-with-permanent-end-to-military-action-hormuz-strait-to-open-june-19"
    published_at: "2026-06-15T02:47:07.000Z"
    retrieved_at: "2026-06-15T13:51:44+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
