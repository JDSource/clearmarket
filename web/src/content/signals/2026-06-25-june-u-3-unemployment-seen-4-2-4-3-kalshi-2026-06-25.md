---
signal_id: "CMSIG2026062502"
signal_slug: "june-u-3-unemployment-seen-4-2-4-3-kalshi-2026-06-25"
headline: "June U-3 unemployment seen 4.2-4.3%: Kalshi"
semantic_title: "June unemployment rate consensus anchors near 4.2 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-25T12:57:12.000Z"
event_id: "CM-EVT-FJGT56DTV2"
event_slug: "kxu3-26jun"
event_question: "June 2026 U-3 unemployment rate"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26JUN-T4.3"
  question_raw: "Will the unemployment rate (U-3) be above 4.3% in June?"
  current_price: 0.31
  volume_24h_usd: 0.96
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-07-02T14:00:00Z"
bullets:
  - "Kalshi ladder implies June 2026 unemployment in the 4.2-4.3% range: 63% above 4.2%, 31% above 4.3%, and only 2% above 4.5%."
  - "Low weekly claims of 215,000 are consistent with the market's base case of contained unemployment, not a breakout toward 4.5% or higher."
  - "The steep drop from 87% at 4.1% to 31% at 4.3% shows the market treats 4.3% as a credible ceiling given current labor data."
  - "Resolves via Bureau of Labor Statistics June employment situation report; the 4.4% and above strikes pricing at 11% and 2% reflect limited tail risk."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US jobless claims fell to 215,000 last week, signaling layoffs remain low despite economic headwinds."
    publisher: "wtop.com"
    published_at: "2026-06-25T12:57:12.000Z"
    source_url: "https://wtop.com/business-finance/2026/06/us-jobless-aid-filings-fall-to-215000-last-week-as-layoffs-remain-low-despite-economic-headwinds-2/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "wtop.com"
        source_url: "https://wtop.com/business-finance/2026/06/us-jobless-aid-filings-fall-to-215000-last-week-as-layoffs-remain-low-despite-economic-headwinds-2/"
        retrieved_at: "2026-06-26T10:48:01+00:00"
  - type: "pm_response"
    notes: "Kalshi's unemployment ladder is consistent with the low-claims signal; no strikes above 4.5% carry meaningful probability."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "wtop.com: US jobless aid filings fall to 215,000 last week as layoffs remain low"
    url: "https://wtop.com/business-finance/2026/06/us-jobless-aid-filings-fall-to-215000-last-week-as-layoffs-remain-low-despite-economic-headwinds-2/"
    published_at: "2026-06-25T12:57:12.000Z"
    retrieved_at: "2026-06-26T10:48:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
