---
signal_id: "CMSIG2026112606"
signal_slug: "ukraine-russia-peace-deal-before-2027-polymarket-9-2026-11-26"
headline: "Ukraine-Russia peace deal before 2027: Polymarket 9%"
semantic_title: "Ukraine-Russia peace deal before 2027 stays a long shot"
telemetry: "Polymarket 9%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-26T00:00:00.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.09
  volume_24h_usd: 15682.744935
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 9% chance Ukraine signs a peace deal with Russia before 2027, via UMA oracle."
  - "DRC-Rwanda mediation success has no direct read-across to the Ukraine conflict, but the US mediation role is a shared thread."
  - "Companion Polymarket contract CM-EVT-XP7FFT2MC9 on Ukraine ceding territory to Russia by 2026 sits at 3%, the market sees neither deal nor cession as likely this year."
  - "Resolution requires a formal signed peace agreement between Ukraine and Russia before January 1, 2027, per UMA oracle criteria."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The DRC and Rwanda reached a draft US and Qatari-mediated peace deal, underscoring active US mediation diplomacy, while the Ukraine-Russia conflict remains unresolved."
    publisher: "link.cfr.org"
    published_at: "2026-11-26T00:00:00.000Z"
    source_url: "https://link.cfr.org/public/40372845"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "link.cfr.org"
        source_url: "https://link.cfr.org/public/40372845"
        retrieved_at: "2026-11-27T07:47:43+00:00"
  - type: "pm_response"
    notes: "Polymarket holds the peace-deal contract at 9%, well below any coin-flip threshold despite elevated diplomatic activity."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "link.cfr.org: Across the Globe"
    url: "https://link.cfr.org/public/40372845"
    published_at: "2026-11-26T00:00:00.000Z"
    retrieved_at: "2026-11-27T07:47:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
