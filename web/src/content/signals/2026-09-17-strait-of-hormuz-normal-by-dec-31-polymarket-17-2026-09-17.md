---
signal_id: "CMSIG2026091708"
signal_slug: "strait-of-hormuz-normal-by-dec-31-polymarket-17-2026-09-17"
headline: "Strait of Hormuz normal by Dec 31: Polymarket 17%"
semantic_title: "Strait of Hormuz traffic returning to normal by year-end holds near 17 percent"
telemetry: "Polymarket 17%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-17T02:12:52.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.17
  volume_24h_usd: 24484.385409
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Strait of Hormuz traffic returning to normal by December 31 prices at 17%."
  - "Escalating Houthi-Saudi fighting and Iranian threats to oil supplies are consistent with the market's low probability of a near-term normalization."
  - "A companion Polymarket contract on an Israel-Turkey military clash before 2027 prices at 14%, reflecting broader regional instability being priced across contracts."
  - "The Polymarket contract resolves via UMA oracle; normalization would require verified resumption of unimpeded commercial transit through the strait."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Middle East conflict escalated as Iran and Houthis threatened oil supplies amid ongoing Saudi-Houthi fighting."
    publisher: "Balaram Menon,Christian Borbon,Jay Hilotin"
    published_at: "2026-09-17T02:12:52.000Z"
    source_url: "https://gulfnews.com/world/mena/middle-east-conflict-escalates-as-iran-houthis-threaten-oil-supplies-1.500677547"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Balaram Menon,Christian Borbon,Jay Hilotin"
        source_url: "https://gulfnews.com/world/mena/middle-east-conflict-escalates-as-iran-houthis-threaten-oil-supplies-1.500677547"
        retrieved_at: "2026-09-17T13:04:18+00:00"
  - type: "pm_response"
    notes: "Polymarket at 17% resolves via UMA oracle; the escalating conflict narrative aligns with the market's skeptical pricing on Hormuz normalization."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Balaram Menon,Christian Borbon,Jay Hilotin: Middle East conflict escalates as Iran, Houthis threaten oil supplies"
    url: "https://gulfnews.com/world/mena/middle-east-conflict-escalates-as-iran-houthis-threaten-oil-supplies-1.500677547"
    published_at: "2026-09-17T02:12:52.000Z"
    retrieved_at: "2026-09-17T13:04:18+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
