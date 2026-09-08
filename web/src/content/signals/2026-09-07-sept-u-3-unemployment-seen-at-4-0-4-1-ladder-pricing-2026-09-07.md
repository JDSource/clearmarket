---
signal_id: "CMSIG2026090702"
signal_slug: "sept-u-3-unemployment-seen-at-4-0-4-1-ladder-pricing-2026-09-07"
headline: "Sept U-3 unemployment seen at 4.0-4.1%: ladder pricing"
semantic_title: "September unemployment rate holds near 4.1 percent in pricing"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-07T00:00:00.000Z"
event_id: "CM-EVT-720DZC17Y9"
event_slug: "kxu3-26sep"
event_question: "September 2026 U-3 unemployment rate"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26SEP-T4.1"
  question_raw: "Will the unemployment rate (U-3) be above 4.1% in September?"
  current_price: 0.45
  volume_24h_usd: 21.08
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "Prediction market ladder puts September unemployment in the 4.0-4.1% range: 84% above 4.0%, only 45% above 4.1%."
  - "August unemployment held at 4.1%, and the ladder is consistent with no meaningful deterioration expected in September."
  - "The 4.5% and higher strikes price at 6-8%, suggesting the market sees little risk of a sharp labor market deterioration."
  - "The separate peak unemployment ladder (CM-EVT-RBY62SKLC0) puts only 16% odds on unemployment ever exceeding 4.5% before 2027, aligning with the benign September read."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "August 2026 jobs report showed 162,000 nonfarm payrolls added with unemployment holding at 4.1%."
    publisher: "Economics Insider"
    published_at: "2026-09-07T00:00:00.000Z"
    source_url: "https://economicsinsider.com/us-jobs-report-august-2026/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Economics Insider"
        source_url: "https://economicsinsider.com/us-jobs-report-august-2026/"
        retrieved_at: "2026-09-08T12:33:52+00:00"
  - type: "pm_response"
    notes: "Prediction market ladder pricing closely tracks the August BLS print, treating 4.1% as the new equilibrium anchor."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Economics Insider: US Jobs Report August 2026: 162,000 Jobs Added as Unemployment Holds a"
    url: "https://economicsinsider.com/us-jobs-report-august-2026/"
    published_at: "2026-09-07T00:00:00.000Z"
    retrieved_at: "2026-09-08T12:33:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
