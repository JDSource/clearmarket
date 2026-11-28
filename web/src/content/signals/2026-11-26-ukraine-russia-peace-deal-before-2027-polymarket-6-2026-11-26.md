---
signal_id: "CMSIG2026112606"
signal_slug: "ukraine-russia-peace-deal-before-2027-polymarket-6-2026-11-26"
headline: "Ukraine-Russia peace deal before 2027: Polymarket 6%"
semantic_title: "Ukraine peace deal before 2027 stays near long-shot odds"
telemetry: "Polymarket 6%"
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
  current_price: 0.064
  volume_24h_usd: 1558.8238729999998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 6% chance Ukraine signs a peace deal with Russia before 2027, resolving via UMA oracle; trading volume surged 73x day-over-day on this contract."
  - "The volume spike signals this claim is drawing fresh attention, likely driven by the DRC-Rwanda deal news raising hopes for broader US mediation success."
  - "Despite the volume surge, the price remains at 6%, the market is not moving toward a YES; heightened attention has not translated into conviction."
  - "Russia's largest air attack of the war (Story 29) and Ukraine territory-cession odds at 3% (Story 27) confirm markets see no near-term deal framework."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The DRC and Rwanda reached a draft peace deal through US and Qatari mediation, but separate reporting shows Russia launched its largest air attack of the war this weekend."
    publisher: "link.cfr.org"
    published_at: "2026-11-26T00:00:00.000Z"
    source_url: "https://link.cfr.org/public/40372845"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "link.cfr.org"
        source_url: "https://link.cfr.org/public/40372845"
        retrieved_at: "2026-11-28T07:47:57+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; the 73x volume surge with no meaningful price move is a strong signal the market is absorbing bullish deal news and rejecting it."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "link.cfr.org: Across the Globe"
    url: "https://link.cfr.org/public/40372845"
    published_at: "2026-11-26T00:00:00.000Z"
    retrieved_at: "2026-11-28T07:47:57+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
