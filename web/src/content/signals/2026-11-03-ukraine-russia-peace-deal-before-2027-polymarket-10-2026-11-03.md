---
signal_id: "CMSIG2026110308"
signal_slug: "ukraine-russia-peace-deal-before-2027-polymarket-10-2026-11-03"
headline: "Ukraine-Russia peace deal before 2027: Polymarket 10%"
semantic_title: "Ukraine peace deal before 2027 stays a long shot"
telemetry: "Polymarket 10%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-03T00:00:00.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.1
  volume_24h_usd: 12239.821441
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a Ukraine-Russia peace deal signed before 2027 at 10%."
  - "Zelensky's seven-to-ten day security guarantee push is a constructive signal, but Russian Foreign Minister Sergey Lavrov's skepticism keeps the market at long-shot odds."
  - "The Ukraine territory cession contract on Polymarket sits at 6%, suggesting the market sees an even narrower path to a deal that involves concessions."
  - "The two contracts together imply the market prices almost no viable deal architecture before year-end, regardless of the accelerating mediation activity."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The DRC and Rwanda reached a draft US-Qatari mediated peace deal, while Ukraine seeks consensus on security guarantees within seven to ten days."
    publisher: "link.cfr.org"
    published_at: "2026-11-03T00:00:00.000Z"
    source_url: "https://link.cfr.org/public/40372845"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "link.cfr.org"
        source_url: "https://link.cfr.org/public/40372845"
        retrieved_at: "2026-11-03T15:45:44+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle based on a signed, publicly confirmed peace agreement between Ukraine and Russia."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "link.cfr.org: Across the Globe"
    url: "https://link.cfr.org/public/40372845"
    published_at: "2026-11-03T00:00:00.000Z"
    retrieved_at: "2026-11-03T15:45:44+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
