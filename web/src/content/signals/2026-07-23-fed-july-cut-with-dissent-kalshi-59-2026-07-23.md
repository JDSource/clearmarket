---
signal_id: "CMSIG2026072302"
signal_slug: "fed-july-cut-with-dissent-kalshi-59-2026-07-23"
headline: "Fed July cut with dissent: Kalshi 59%"
semantic_title: "Odds of a Fed July cut with dissent hold near 60%"
telemetry: "Kalshi 59%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-23T00:00:00.000Z"
event_id: "CM-EVT-P6QJP9BW02"
event_slug: "kxfedcombo-26jul"
event_question: "Will the Federal Reserve in July 2026 cut rates and have at least one dissent?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDCOMBO-26JUL-0-T0"
  question_raw: "Will Federal Funds Rate Decision be No change AND Dissents be >0 for Jul 2026?"
  current_price: 0.59
  volume_24h_usd: 184.78
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-07-29T17:55:00Z"
bullets:
  - "Kalshi prices a 59% chance the Fed cuts rates at the July 2026 meeting AND sees at least one dissent."
  - "Natixis forecasts a hold all year, yet Kalshi's majority probability favors a July cut with dissent, the market leans against the Natixis call."
  - "The ladder market (CM-EVT-PHWX2H6DM5) puts 99% on the upper bound staying above 3.50%, consistent with no dramatic easing, but not ruling out a single 25bp cut to 3.50%."
  - "Polymarket (CM-EVT-C0ZG1HDJQ1) prices 76% on the Fed making any rate decision between April and July, a softer bar that the 59% Kalshi dissent contract narrows further."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Natixis previews the July FOMC meeting, forecasting the Fed will hold rates steady through all of 2026 amid mixed economic data."
    publisher: "indexbox.io"
    published_at: "2026-07-23T00:00:00.000Z"
    source_url: "https://www.indexbox.io/blog/natixis-fed-to-hold-rates-steady-through-2026-amid-mixed-data/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "indexbox.io"
        source_url: "https://www.indexbox.io/blog/natixis-fed-to-hold-rates-steady-through-2026-amid-mixed-data/"
        retrieved_at: "2026-07-24T10:13:15+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via Bureau of Labor Statistics, an unusual resolution source for a Fed decision; traders should note potential settlement ambiguity."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "indexbox.io: Natixis FOMC Preview: Fed Expected to Maintain Policy Rate at July 202"
    url: "https://www.indexbox.io/blog/natixis-fed-to-hold-rates-steady-through-2026-amid-mixed-data/"
    published_at: "2026-07-23T00:00:00.000Z"
    retrieved_at: "2026-07-24T10:13:15+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
