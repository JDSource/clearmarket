---
signal_id: "CMSIG2026082805"
signal_slug: "ukraine-russia-peace-deal-before-2027-polymarket-14-2026-08-28"
headline: "Ukraine-Russia peace deal before 2027: Polymarket 14%"
semantic_title: "Ukraine peace deal before 2027 stays a long shot at 14 percent"
telemetry: "Polymarket 14%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-28T00:00:00.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.14
  volume_24h_usd: 4605.24
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a Ukraine-Russia peace deal before 2027 at 14%, a clear long-shot assessment."
  - "The Kremlin's 'no new ideas' declaration and reported offensive planning are consistent with the low 14% pricing, not a near-term resolution scenario."
  - "The Polymarket contract on Ukraine agreeing to cede territory by 2026 sits at just 6%, suggesting markets see neither peace nor territorial concession as likely."
  - "Resolves via Polymarket's UMA oracle; any formal peace deal announcement would be the settlement trigger."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The Kremlin declared Ukraine peace talks are on hold with no new ideas, as Russia simultaneously plans possible offensive scenarios toward Kyiv and Chernihiv."
    publisher: "Yeni Şafak Gazetecilik A.Ş."
    published_at: "2026-08-28T00:00:00.000Z"
    source_url: "https://en.yenisafak.com/world/kremlin-ukraine-peace-talks-on-hold-with-no-new-ideas-3722493"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Yeni Şafak Gazetecilik A.Ş."
        source_url: "https://en.yenisafak.com/world/kremlin-ukraine-peace-talks-on-hold-with-no-new-ideas-3722493"
        retrieved_at: "2026-08-29T13:34:02+00:00"
  - type: "pm_response"
    notes: "Polymarket at 14% on a pre-2027 peace deal, with the companion territorial-cession contract at 6%, reflecting deep market skepticism about near-term resolution."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Yeni Şafak Gazetecilik A.Ş.: Kremlin: Ukraine peace talks on hold with no new ideas"
    url: "https://en.yenisafak.com/world/kremlin-ukraine-peace-talks-on-hold-with-no-new-ideas-3722493"
    published_at: "2026-08-28T00:00:00.000Z"
    retrieved_at: "2026-08-29T13:34:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
