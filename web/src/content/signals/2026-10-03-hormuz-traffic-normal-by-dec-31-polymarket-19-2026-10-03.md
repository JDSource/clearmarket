---
signal_id: "CMSIG2026100308"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-19-2026-10-03"
headline: "Hormuz traffic normal by Dec 31: Polymarket 19%"
semantic_title: "Strait of Hormuz traffic back to normal by year-end stays a long shot"
telemetry: "Polymarket 19%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-03T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.19
  volume_24h_usd: 80819.146695
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 19% on Strait of Hormuz traffic returning to normal by December 31, 2026, reflecting persistent skepticism about near-term resolution."
  - "Houthi strikes on Saudi Aramco facilities and confirmed US strikes on Iranian targets both point to continued escalation, broadly consistent with the low normalization probability."
  - "US heavy strikes on Iran reported in Story 28 represent a further escalation step; markets are not pricing a rapid de-escalation pathway from the current military posture."
  - "Resolution via UMA oracle requires a return to normal transit volumes, a measurable operational standard, not just a ceasefire declaration."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran-backed Houthis struck a Saudi Aramco oil facility as Yemen hostilities escalated, adding further regional pressure on Gulf energy infrastructure."
    publisher: "abc.net.au"
    published_at: "2026-10-03T00:00:00.000Z"
    source_url: "https://www.abc.net.au/news/2026-10-04/houthi-saudi-yemen-iraq-middle-east-hostilities/107226524"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "abc.net.au"
        source_url: "https://www.abc.net.au/news/2026-10-04/houthi-saudi-yemen-iraq-middle-east-hostilities/107226524"
        retrieved_at: "2026-10-04T07:47:36+00:00"
  - type: "pm_response"
    notes: "Polymarket at 19% on Hormuz normalization is the only priced contract in this cluster; multiple related questions including Iranian fee-charging and US announcements of blockade end carry no live price, leaving Hormuz normalization as the primary available read."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "abc.net.au: Iran-backed Houthis target Saudi oil facility as hostilities escalate"
    url: "https://www.abc.net.au/news/2026-10-04/houthi-saudi-yemen-iraq-middle-east-hostilities/107226524"
    published_at: "2026-10-03T00:00:00.000Z"
    retrieved_at: "2026-10-04T07:47:36+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
