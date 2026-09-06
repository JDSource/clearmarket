---
signal_id: "CMSIG2026090607"
signal_slug: "ukraine-russia-peace-deal-before-2027-polymarket-15-2026-09-06"
headline: "Ukraine-Russia peace deal before 2027: Polymarket 15%"
semantic_title: "Ukraine peace deal before 2027 stays a long shot at 15%"
telemetry: "Polymarket 15%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-06T00:00:00.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.15
  volume_24h_usd: 7402.656255
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 15% on Ukraine signing a peace deal with Russia before 2027, resolving via UMA oracle."
  - "Kremlin describing talks as useful but producing no breakthrough is consistent with the market's heavy skepticism toward a near-term deal."
  - "Companion Polymarket contract on Ukraine ceding territory by 2026 (CM-EVT-XP7FFT2MC9) sits at 12%, suggesting markets see territorial concessions and a signed deal as roughly equally unlikely."
  - "Russia-Ukraine ceasefire by end of 2026 (CM-EVT-2089XJ01Y3) is priced at 13%, consistent with 15% on a full deal, implying markets see little gap between a ceasefire and a final settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US envoys Steve Witkoff and Jared Kushner discussed substantive plans for next steps to end the Ukraine war with Vladimir Putin in Moscow, then headed to Kyiv, with Kremlin calling talks useful but no breakthrough reported."
    publisher: "france24.com"
    published_at: "2026-09-06T00:00:00.000Z"
    source_url: "https://www.france24.com/en/live-news/20260906-us-envoys-discuss-with-putin-substantive-plans-for-steps-to-end-ukraine-war"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "france24.com"
        source_url: "https://www.france24.com/en/live-news/20260906-us-envoys-discuss-with-putin-substantive-plans-for-steps-to-end-ukraine-war"
        retrieved_at: "2026-09-06T11:54:11+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle on a signed Ukraine-Russia peace agreement before January 1, 2027; shuttle diplomacy is ongoing but talks showed no breakthrough."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "france24.com: US envoys discuss with Putin 'substantive' plans for steps to end Ukra"
    url: "https://www.france24.com/en/live-news/20260906-us-envoys-discuss-with-putin-substantive-plans-for-steps-to-end-ukraine-war"
    published_at: "2026-09-06T00:00:00.000Z"
    retrieved_at: "2026-09-06T11:54:11+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
