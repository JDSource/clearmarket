---
signal_id: "CMSIG2026112304"
signal_slug: "ukraine-russia-peace-deal-by-2027-polymarket-4-2026-11-23"
headline: "Ukraine-Russia peace deal by 2027: Polymarket 4%"
semantic_title: "Ukraine peace deal before 2027 stays a long shot on Polymarket"
telemetry: "Polymarket 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-23T07:26:44.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.045
  volume_24h_usd: 552.728037
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only a 4% chance Ukraine signs a peace deal with Russia before 2027, resolved via UMA oracle."
  - "Despite Trump and Putin's trilateral summit and public peace signals, the market is not moving toward a deal scenario."
  - "Active strikes on Ukraine and no Zelenskyy-Putin direct talks keep the market deeply skeptical of imminent resolution."
  - "The Polymarket contract on Trump, Putin, and Zelenskyy being seen together before 2027 sits at just 5%, consistent with the low peace-deal odds."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The war in Ukraine shows no sign of slowing, with continued bombing and sanctions even as Trump and Putin met at a historic summit and signaled interest in ending the conflict."
    publisher: "Leo Cendrowicz"
    published_at: "2026-11-23T07:26:44.000Z"
    source_url: "https://www.euronews.com/2026/11/23/sanctions-summits-and-strikes-the-war-in-ukraine-shows-no-sign-of-slowing"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Leo Cendrowicz"
        source_url: "https://www.euronews.com/2026/11/23/sanctions-summits-and-strikes-the-war-in-ukraine-shows-no-sign-of-slowing"
        retrieved_at: "2026-11-23T07:47:39+00:00"
  - type: "pm_response"
    notes: "Polymarket's 4% on a 2026 peace deal resolves via UMA oracle; summit optics are not shifting the market's deeply bearish assessment of near-term peace."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Leo Cendrowicz: Sanctions, summits and strikes: The war in Ukraine shows no sign of sl"
    url: "https://www.euronews.com/2026/11/23/sanctions-summits-and-strikes-the-war-in-ukraine-shows-no-sign-of-slowing"
    published_at: "2026-11-23T07:26:44.000Z"
    retrieved_at: "2026-11-23T07:47:39+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
