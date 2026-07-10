---
signal_id: "CMSIG2026070906"
signal_slug: "ukraine-russia-peace-deal-before-2027-polymarket-21-2026-07-09"
headline: "Ukraine-Russia peace deal before 2027: Polymarket 21%"
semantic_title: "Ukraine-Russia peace deal by 2027 priced as long shot"
telemetry: "Polymarket 21%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-09T09:58:00.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.21
  volume_24h_usd: 980.785769
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract prices 21% on Ukraine signing a peace deal with Russia before 2027, resolving via UMA oracle."
  - "Reuters sourcing on likely Russian escalation is broadly consistent with the market's 79% implied probability that no deal materializes before year-end."
  - "Two correlated Polymarket contracts price even lower: Ukraine agreeing to cede the rest of Donbas at 5%, and a peace referendum passing at 10%, suggesting markets see territorial concessions as the binding constraint."
  - "Resolution via UMA oracle requires a verifiable signed peace agreement; ongoing Ukrainian drone strikes on Russian oil infrastructure further reduce near-term deal probability."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Sources tell Reuters that President Vladimir Putin is likely to escalate the war in Ukraine despite Trump administration peace efforts."
    publisher: "thestar.com.my"
    published_at: "2026-07-09T09:58:00.000Z"
    source_url: "https://www.thestar.com.my/news/world/2026/07/09/exclusive-putin-likely-to-escalate-ukraine-war-despite-trump-peace-push-sources-say"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "thestar.com.my"
        source_url: "https://www.thestar.com.my/news/world/2026/07/09/exclusive-putin-likely-to-escalate-ukraine-war-despite-trump-peace-push-sources-say"
        retrieved_at: "2026-07-10T10:49:37+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; the 21% price sits in rough alignment with the escalation reporting, with companion contracts on territorial concessions pricing far lower."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "thestar.com.my: Exclusive-Putin likely to escalate Ukraine war, despite Trump peace pu"
    url: "https://www.thestar.com.my/news/world/2026/07/09/exclusive-putin-likely-to-escalate-ukraine-war-despite-trump-peace-push-sources-say"
    published_at: "2026-07-09T09:58:00.000Z"
    retrieved_at: "2026-07-10T10:49:37+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
