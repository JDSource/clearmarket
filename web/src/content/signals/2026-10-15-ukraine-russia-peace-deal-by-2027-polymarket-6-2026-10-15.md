---
signal_id: "CMSIG2026101506"
signal_slug: "ukraine-russia-peace-deal-by-2027-polymarket-6-2026-10-15"
headline: "Ukraine-Russia peace deal by 2027: Polymarket 6%"
semantic_title: "Ukraine peace deal before 2027 remains a long shot"
telemetry: "Polymarket 6%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-15T00:00:00.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.06
  volume_24h_usd: 4110.878694000001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract puts only 6% on Ukraine signing a peace deal with Russia before 2027."
  - "Guardian reporting of a deepening U.S.-Russia tilt and Moscow's resistance to security guarantees is fully consistent with a near-zero market probability on a near-term deal."
  - "A companion Polymarket contract on a ceasefire in 2026 (CM-EVT-2089XJ01Y3) also sits at 9%, and the Ukraine territory cession contract (CM-EVT-XP7FFT2MC9) is at 6%, the entire peace-process suite is priced as a long shot."
  - "Resolves via UMA oracle; the cluster of sub-10% readings across all three Polymarket contracts represents the most consistent geopolitical consensus in this batch."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "A Guardian briefing reports that erratic U.S. diplomacy under Trump is keeping a Ukraine peace settlement far away, with concerns of a pro-Russia White House tilt."
    publisher: "Michael Segalov"
    published_at: "2026-10-15T00:00:00.000Z"
    source_url: "https://www.theguardian.com/world/2026/oct/15/thursday-briefing-thanks-to-an-erratic-trump-peace-in-ukraine-is-still-far-away"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Michael Segalov"
        source_url: "https://www.theguardian.com/world/2026/oct/15/thursday-briefing-thanks-to-an-erratic-trump-peace-in-ukraine-is-still-far-away"
        retrieved_at: "2026-10-16T12:59:00+00:00"
  - type: "pm_response"
    notes: "Polymarket contract via UMA oracle; consistent with companion contracts on ceasefire and territory cession, all priced at single digits."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Michael Segalov: Thursday briefing: Thanks to an erratic Trump, peace in Ukraine is sti"
    url: "https://www.theguardian.com/world/2026/oct/15/thursday-briefing-thanks-to-an-erratic-trump-peace-in-ukraine-is-still-far-away"
    published_at: "2026-10-15T00:00:00.000Z"
    retrieved_at: "2026-10-16T12:59:00+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
