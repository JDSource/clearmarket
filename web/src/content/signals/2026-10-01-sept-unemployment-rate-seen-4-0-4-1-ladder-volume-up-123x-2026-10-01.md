---
signal_id: "CMSIG2026100103"
signal_slug: "sept-unemployment-rate-seen-4-0-4-1-ladder-volume-up-123x-2026-10-01"
headline: "Sept unemployment rate seen 4.0-4.1%: ladder, volume up 123x"
semantic_title: "September unemployment rate prices in around 4.0-4.1 percent"
telemetry: "Kalshi ladder"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-10-01T00:00:00.000Z"
event_id: "CM-EVT-720DZC17Y9"
event_slug: "kxu3-26sep"
event_question: "September 2026 unemployment rate (U-3)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26SEP-T4.1"
  question_raw: "Will the unemployment rate (U-3) be above 4.1% in September?"
  current_price: 0.38
  volume_24h_usd: 724.32
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "Prediction market ladder pins September U-3 in the 4.0-4.1% band: 69% above 4.0%, falling to 38% above 4.1% and only 8% above 4.2%."
  - "Trading volume on this contract surged 123.7 times day-over-day, signaling sharp fresh attention ahead of Friday's BLS release."
  - "Near-historic-low jobless claims are consistent with a rate in this range; the market is not pricing a meaningful deterioration."
  - "The 99% probability above 3.7% and 94% above 3.9% confirm a sub-4% print is seen as unlikely, framing Friday's report as a 4.0% vs 4.1% debate."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Ahead of Friday's jobs report, jobless claims drifted near 57-year lows, signaling a still-firm labor market."
    publisher: "CNN Newssource"
    published_at: "2026-10-01T00:00:00.000Z"
    source_url: "https://krdo.com/money/cnn-business-consumer/2026/10/01/americans-are-still-spending-fridays-jobs-report-will-show-if-that-can-last/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "CNN Newssource"
        source_url: "https://krdo.com/money/cnn-business-consumer/2026/10/01/americans-are-still-spending-fridays-jobs-report-will-show-if-that-can-last/"
        retrieved_at: "2026-10-01T15:03:15+00:00"
  - type: "pm_response"
    notes: "Ladder resolves via BLS Employment Situation report; the 123x volume spike is the clearest signal this contract is drawing concentrated pre-event positioning."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "CNN Newssource: Americans are still spending. Friday’s jobs report will show if that c"
    url: "https://krdo.com/money/cnn-business-consumer/2026/10/01/americans-are-still-spending-fridays-jobs-report-will-show-if-that-can-last/"
    published_at: "2026-10-01T00:00:00.000Z"
    retrieved_at: "2026-10-01T15:03:15+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
