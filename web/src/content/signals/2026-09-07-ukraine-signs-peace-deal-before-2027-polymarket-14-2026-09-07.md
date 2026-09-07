---
signal_id: "CMSIG2026090706"
signal_slug: "ukraine-signs-peace-deal-before-2027-polymarket-14-2026-09-07"
headline: "Ukraine signs peace deal before 2027: Polymarket 14%"
semantic_title: "Ukraine peace deal before 2027 stays a long shot"
telemetry: "Polymarket 14%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-07T00:00:00.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.14
  volume_24h_usd: 2000.602003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Ukraine signing a peace deal with Russia before 2027 at just 14%, a long shot despite renewed US diplomacy."
  - "The Witkoff-Kushner Kyiv visit and diplomatic momentum described in news coverage is not moving the market's skeptical read, a clear fade of the peace-push narrative."
  - "A companion contract (CM-EVT-66S3LD3901) puts just 9% on Russia and Ukraine reaching a peace agreement by 2026, suggesting even less confidence in a near-term timeline."
  - "Zelenskyy's statement that war looks set to continue through winter (Story 28) is directionally consistent with the 14% pricing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US envoys Steve Witkoff and Jared Kushner brought new proposals to Kyiv after meeting Putin, but former ambassadors see no evidence of a Russian position shift."
    publisher: "france24.com"
    published_at: "2026-09-07T00:00:00.000Z"
    source_url: "https://www.france24.com/en/europe/20260907-us-envoys-more-effective-ukraine-peace-proposals-kyiv"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "france24.com"
        source_url: "https://www.france24.com/en/europe/20260907-us-envoys-more-effective-ukraine-peace-proposals-kyiv"
        retrieved_at: "2026-09-07T13:54:18+00:00"
  - type: "pm_response"
    notes: "Polymarket resolves via UMA oracle; the 14% deal vs. 10% territorial concession vs. 9% peace agreement spread reveals the market sees multiple distinct pathways each as unlikely."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "france24.com: US envoys bring ‘more effective’ Ukraine peace proposals to Kyiv, offi"
    url: "https://www.france24.com/en/europe/20260907-us-envoys-more-effective-ukraine-peace-proposals-kyiv"
    published_at: "2026-09-07T00:00:00.000Z"
    retrieved_at: "2026-09-07T13:54:18+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
