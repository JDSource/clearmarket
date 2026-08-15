---
signal_id: "CMSIG2026081506"
signal_slug: "ukraine-russia-peace-deal-before-2027-polymarket-18-2026-08-15"
headline: "Ukraine-Russia peace deal before 2027: Polymarket 18%"
semantic_title: "Ukraine-Russia peace deal before 2027 stays a long shot"
telemetry: "Polymarket 18%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-15T07:00:00.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.18
  volume_24h_usd: 405.731736
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on a Ukraine-Russia peace deal before 2027 sits at 18%, a long-shot reading consistent with the Kremlin's maximalist posture."
  - "ISW's assessment that Russia is rejecting all compromise aligns with low market odds; the contract is not in tension with the news."
  - "Companion Polymarket contract CM-EVT-XP7FFT2MC9 puts only 8% on Ukraine agreeing to cede territory by 2026, suggesting the market sees capitulation as even less likely than a full deal."
  - "Resolves via UMA oracle on Polymarket; settlement would require credible reporting of a signed peace agreement before January 1, 2027."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The Kremlin rejected all peace efforts short of Ukraine accepting maximalist territorial demands, according to the Institute for the Study of War."
    publisher: "english.nv.ua"
    published_at: "2026-08-15T07:00:00.000Z"
    source_url: "https://english.nv.ua/russian-war/kremlin-rejects-peace-efforts-unless-ukraine-accepts-maximalist-demands-isw-50632807.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "english.nv.ua"
        source_url: "https://english.nv.ua/russian-war/kremlin-rejects-peace-efforts-unless-ukraine-accepts-maximalist-demands-isw-50632807.html"
        retrieved_at: "2026-08-15T08:21:50+00:00"
  - type: "pm_response"
    notes: "Polymarket pricing at 18% reflects a durable low-probability consensus on near-term resolution, consistent with the ISW report of entrenched Russian maximalism."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "english.nv.ua: Kremlin rejects peace efforts unless Ukraine accepts maximalist demand"
    url: "https://english.nv.ua/russian-war/kremlin-rejects-peace-efforts-unless-ukraine-accepts-maximalist-demands-isw-50632807.html"
    published_at: "2026-08-15T07:00:00.000Z"
    retrieved_at: "2026-08-15T08:21:50+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
