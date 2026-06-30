---
signal_id: "CMSIG2026063003"
signal_slug: "june-unemployment-above-4-2-kalshi-72-above-4-3-36-2026-06-30"
headline: "June unemployment above 4.2%: Kalshi 72%, above 4.3% 36%"
semantic_title: "June unemployment at 4.2-4.3 percent absorbs report print"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-06-30T07:35:25.000Z"
event_id: "CM-EVT-FJGT56DTV2"
event_slug: "kxu3-26jun"
event_question: "June 2026 unemployment rate (U-3)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26JUN-T4.3"
  question_raw: "Will the unemployment rate (U-3) be above 4.3% in June?"
  current_price: 0.36
  volume_24h_usd: 512.29
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-07-02T14:00:00Z"
bullets:
  - "Kalshi ladder priced 72% above 4.2% and 36% above 4.3% pre-print, with a 4.3% actual result landing squarely in the high-probability band."
  - "The reported 4.3% unemployment rate is consistent with market pricing that already assigned meaningful odds to the 4.2-4.3% range."
  - "The companion June NFP ladder (CM-EVT-NHWMG744L8) implies a payroll gain in the 100K-125K range, consistent with a modest labor market that supports a 4.3% unemployment rate."
  - "Resolves via Bureau of Labor Statistics Employment Situation release; large prior payroll revisions cited in the story are a known revision risk that does not affect the U-3 resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A news report citing US Bureau of Labor Statistics data shows the unemployment rate fell to 4.3% in the June jobs report despite significant downward revisions to prior payroll counts."
    publisher: "ins31.com"
    published_at: "2026-06-30T07:35:25.000Z"
    source_url: "https://ins31.com/article/us-jobs-report-unemployment-rate-falls-to-4-3-despite-payroll-revisions"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ins31.com"
        source_url: "https://ins31.com/article/us-jobs-report-unemployment-rate-falls-to-4-3-despite-payroll-revisions"
        retrieved_at: "2026-06-30T10:54:27+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via BLS Employment Situation; the 4.3% print lands near the modal implied range, suggesting the market was well-positioned ahead of the release."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ins31.com: US Jobs Report: Unemployment Rate Falls to 4.3% Despite Payroll Revisi"
    url: "https://ins31.com/article/us-jobs-report-unemployment-rate-falls-to-4-3-despite-payroll-revisions"
    published_at: "2026-06-30T07:35:25.000Z"
    retrieved_at: "2026-06-30T10:54:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
