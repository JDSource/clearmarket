---
signal_id: "CMSIG2026110804"
signal_slug: "ukraine-russia-peace-deal-by-2027-polymarket-7-2026-11-08"
headline: "Ukraine-Russia peace deal by 2027: Polymarket 7%"
semantic_title: "Ukraine peace deal before 2027 remains a long shot"
telemetry: "Polymarket 7%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-08T00:00:00.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.07
  volume_24h_usd: 1881.014948
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts only 7% on Ukraine signing a peace deal with Russia before 2027."
  - "The U.S.-Ukraine resource deal is framed as hardening Ukraine's negotiating position, which is consistent with markets staying skeptical of near-term peace."
  - "A tighter companion contract, Polymarket at 4% for a Russia-Ukraine peace agreement by 2026, implies even shorter-horizon doubt is priced even lower."
  - "Polymarket also shows only 5% on Ukraine agreeing to cede territory to Russia by 2026, suggesting markets see neither peace nor concession as likely this year."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The U.S. and Ukraine agreed to jointly develop Ukrainian natural resources, with the Trump administration framing the deal as a signal to Russia."
    publisher: "link.cfr.org"
    published_at: "2026-11-08T00:00:00.000Z"
    source_url: "https://link.cfr.org/public/39669809"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "link.cfr.org"
        source_url: "https://link.cfr.org/public/39669809"
        retrieved_at: "2026-11-08T14:44:20+00:00"
  - type: "pm_response"
    notes: "Polymarket resolves via uma_oracle; three correlated contracts (peace deal, territory cession, 2026 peace agreement) all cluster in the 4-7% range, forming a consistent low-probability term structure."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "link.cfr.org: Across the Globe"
    url: "https://link.cfr.org/public/39669809"
    published_at: "2026-11-08T00:00:00.000Z"
    retrieved_at: "2026-11-08T14:44:20+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
