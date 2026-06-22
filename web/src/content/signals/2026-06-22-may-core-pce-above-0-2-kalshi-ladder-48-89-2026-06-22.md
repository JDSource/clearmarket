---
signal_id: "CMSIG2026062206"
signal_slug: "may-core-pce-above-0-2-kalshi-ladder-48-89-2026-06-22"
headline: "May core PCE above 0.2%: Kalshi ladder 48-89%"
semantic_title: "Core PCE above zero in May nears full pricing consensus"
telemetry: "Kalshi ladder"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-06-22T00:00:00.000Z"
event_id: "CM-EVT-PG9RLBJ7F1"
event_slug: "kxpcecore-26may"
event_question: "May 2026 core PCE monthly change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPCECORE-26MAY-T0.3"
  question_raw: "Will the rate of core PCE inflation be above 0.3% in May 2026?"
  current_price: 0.48
  volume_24h_usd: 46.28
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Economic Analysis"
  resolves_at: "2026-06-25T14:00:00Z"
bullets:
  - "The Kalshi ladder prices May core PCE above 0.2% at 89% and above 0.3% at only 48%, placing the market-implied print squarely in the 0.2-0.3% range."
  - "A print at or above 0.3% would validate the Fed's hawkish shift; the market gives that outcome roughly even odds, not a consensus."
  - "The above-0.4% strike at just 13% shows the market is not pricing a hot surprise; a 0.2% or 0.3% read would be broadly expected and may not move policy expectations."
  - "Resolves via Bureau of Labor Statistics PCE release; the contract settles on the first published figure, not subsequent revisions."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The upcoming May PCE report is the week's key data point as markets ask whether it will validate the Fed's hawkish shift and BofA's no-cut-until-2028 forecast."
    publisher: "investing.com"
    published_at: "2026-06-22T00:00:00.000Z"
    source_url: "https://www.investing.com/analysis/economic-week-ahead-will-pce-inflation-validate-the-feds-hawkish-shift-200682501"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "investing.com"
        source_url: "https://www.investing.com/analysis/economic-week-ahead-will-pce-inflation-validate-the-feds-hawkish-shift-200682501"
        retrieved_at: "2026-06-22T13:32:28+00:00"
  - type: "pm_response"
    notes: "Kalshi's distribution on May core PCE implies a tame but positive monthly read is the central case, leaving the hawkish validation thesis dependent on whether the print rounds to 0.3% or above."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "investing.com: Economic Week Ahead: Will PCE Inflation Validate the Fed&rsquo;s Hawki"
    url: "https://www.investing.com/analysis/economic-week-ahead-will-pce-inflation-validate-the-feds-hawkish-shift-200682501"
    published_at: "2026-06-22T00:00:00.000Z"
    retrieved_at: "2026-06-22T13:32:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
