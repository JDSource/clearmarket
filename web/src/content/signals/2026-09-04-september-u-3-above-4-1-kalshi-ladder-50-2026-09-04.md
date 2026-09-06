---
signal_id: "CMSIG2026090401"
signal_slug: "september-u-3-above-4-1-kalshi-ladder-50-2026-09-04"
headline: "September U-3 above 4.1%: Kalshi ladder 50%"
semantic_title: "September unemployment above 4.1% stays near 50-50"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-04T00:00:00.000Z"
event_id: "CM-EVT-720DZC17Y9"
event_slug: "kxu3-26sep"
event_question: "September 2026 unemployment rate (U-3)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26SEP-T4.2"
  question_raw: "Will the unemployment rate (U-3) be above 4.2% in September?"
  current_price: 0.16
  volume_24h_usd: 127.89
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "Kalshi ladder puts only 50% odds on September U-3 staying above 4.1%, with 83% above 4.0% and just 16% above 4.2%."
  - "August payrolls beat at 162,000 vs. 56,000 expected; market is consistent with a steady rate, not a drop toward 4.0% or a rise."
  - "Tail pricing is very tight: only 8% on above 4.3%, suggesting the market sees little risk of unemployment moving decisively in either direction."
  - "Companion ladder on peak unemployment (CM-EVT-RBY62SKLC0) prices 84% odds the rate stays below 4.5% before 2027, consistent with a contained labor market."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US nonfarm payrolls surged 162,000 in August, nearly triple the 56,000 consensus forecast, while the unemployment rate held steady at 4.1%."
    publisher: "Lucia Mutikani"
    published_at: "2026-09-04T00:00:00.000Z"
    source_url: "https://www.reuters.com/business/us-nonfarm-payrolls-surge-august-unemployment-rate-steady-41-2026-09-04/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Lucia Mutikani"
        source_url: "https://www.reuters.com/business/us-nonfarm-payrolls-surge-august-unemployment-rate-steady-41-2026-09-04/"
        retrieved_at: "2026-09-06T11:54:11+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves on BLS September 2026 unemployment release; implied range clusters tightly around 4.1%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Lucia Mutikani: US nonfarm payrolls surge in August; unemployment rate steady at 4.1%"
    url: "https://www.reuters.com/business/us-nonfarm-payrolls-surge-august-unemployment-rate-steady-41-2026-09-04/"
    published_at: "2026-09-04T00:00:00.000Z"
    retrieved_at: "2026-09-06T11:54:11+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
