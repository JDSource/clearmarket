---
signal_id: "CMSIG2026072902"
signal_slug: "fed-july-hold-with-dissent-kalshi-60-2026-07-29"
headline: "Fed July hold with dissent: Kalshi 60%"
semantic_title: "Fed July dissent odds hold near 50% on hawk pressure"
telemetry: "Kalshi 60%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-29T00:00:00.000Z"
event_id: "CM-EVT-P6QJP9BW02"
event_slug: "kxfedcombo-26jul"
event_question: "Will the Federal Reserve in July 2026 cut rates and have at least one dissent?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDCOMBO-26JUL-0-T0"
  question_raw: "Will Federal Funds Rate Decision be No change AND Dissents be >0 for Jul 2026?"
  current_price: 0.6
  volume_24h_usd: 24412.57
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-07-29T17:55:00Z"
bullets:
  - "Kalshi prices a 60% probability the Fed holds rates in July 2026 with at least one hawkish dissent."
  - "News reporting that patience is running thin among Fed officials is broadly consistent with the above-even Kalshi dissent odds."
  - "A hold-with-dissent outcome would signal mounting internal pressure without committing to a hike, bridging the gap to the 76% full-year hike probability on Polymarket."
  - "Kalshi resolves this via Bureau of Labor Statistics data; note the resolution source appears atypical for a Fed vote outcome and may reflect a linked inflation trigger."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Multiple outlets report the Fed is expected to hold rates in July but that inflation hawks may push some policymakers to dissent in favor of a hike."
    publisher: "today.rtl.lu"
    published_at: "2026-07-29T00:00:00.000Z"
    source_url: "https://today.rtl.lu/news/world/us-fed-expected-to-hold-rates-steady-as-inflation-hawks-circle-197431541"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "today.rtl.lu"
        source_url: "https://today.rtl.lu/news/world/us-fed-expected-to-hold-rates-steady-as-inflation-hawks-circle-197431541"
        retrieved_at: "2026-07-29T10:35:12+00:00"
  - type: "pm_response"
    notes: "Kalshi at 60% is the only priced contract with a live number covering the July hold-plus-dissent scenario."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "today.rtl.lu: 'Patience running thin': US Fed expected to hold rates steady as infla"
    url: "https://today.rtl.lu/news/world/us-fed-expected-to-hold-rates-steady-as-inflation-hawks-circle-197431541"
    published_at: "2026-07-29T00:00:00.000Z"
    retrieved_at: "2026-07-29T10:35:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
