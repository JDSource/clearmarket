---
signal_id: "CMSIG2026101806"
signal_slug: "ukraine-russia-peace-deal-before-2027-polymarket-8-2026-10-18"
headline: "Ukraine-Russia peace deal before 2027: Polymarket 8%"
semantic_title: "Ukraine peace deal before 2027 stays a long shot at 8 percent"
telemetry: "Polymarket 8%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-18T00:00:00.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.08
  volume_24h_usd: 560.99
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 8% probability on Ukraine signing a peace deal with Russia before 2027, with trading volume up 4,388% day over day, signaling the claim is drawing sharp fresh attention."
  - "Despite Trump's public pressure on Zelenskyy and the collapsed energy ceasefire, the prediction market holds near the long-shot range, not pricing a near-term breakthrough."
  - "Companion Polymarket contracts reinforce the skepticism: 6% on Ukraine ceding territory, 6% on Ukraine limiting its armed forces, and 5% on Nord Stream restarting before 2027."
  - "Resolves via Polymarket UMA oracle; a signed framework agreement, even without full implementation, would likely trigger resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump publicly accused Zelenskyy of not wanting to end the war, deepening the US-Ukraine rift as the energy ceasefire collapsed."
    publisher: "Guardian staff"
    published_at: "2026-10-18T00:00:00.000Z"
    source_url: "https://www.theguardian.com/world/2026/oct/19/ukraine-war-briefing-trump-accuses-zelenskyy-of-not-wanting-to-end-war-as-feud-rumbles-on"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Guardian staff"
        source_url: "https://www.theguardian.com/world/2026/oct/19/ukraine-war-briefing-trump-accuses-zelenskyy-of-not-wanting-to-end-war-as-feud-rumbles-on"
        retrieved_at: "2026-10-19T07:47:26+00:00"
  - type: "pm_response"
    notes: "Polymarket's 8% on a peace deal before 2027, alongside the volume spike, shows the market is actively re-evaluating the claim without pricing an imminent resolution."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Guardian staff: Ukraine war briefing: Trump accuses Zelenskyy of not wanting to end wa"
    url: "https://www.theguardian.com/world/2026/oct/19/ukraine-war-briefing-trump-accuses-zelenskyy-of-not-wanting-to-end-war-as-feud-rumbles-on"
    published_at: "2026-10-18T00:00:00.000Z"
    retrieved_at: "2026-10-19T07:47:26+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
