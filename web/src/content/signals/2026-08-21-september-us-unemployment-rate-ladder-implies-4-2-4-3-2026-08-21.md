---
signal_id: "CMSIG2026082104"
signal_slug: "september-us-unemployment-rate-ladder-implies-4-2-4-3-2026-08-21"
headline: "September US unemployment rate: ladder implies 4.2-4.3%"
semantic_title: "September unemployment seen drifting to 4.2-4.3%"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-21T00:00:00.000Z"
event_id: "CM-EVT-720DZC17Y9"
event_slug: "kxu3-26sep"
event_question: "September 2026 US unemployment rate (U-3)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26SEP-T4.3"
  question_raw: "Will the unemployment rate (U-3) be above 4.3% in September?"
  current_price: 0.37
  volume_24h_usd: 1.48
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "Ladder pricing implies September U-3 in the 4.2-4.3% range: 54% above 4.2%, 37% above 4.3%, dropping sharply to 12% above 4.4%."
  - "The CBS analysis highlights broader labor underutilization, but prediction markets are priced off the official BLS U-3 measure, not alternative metrics."
  - "The 65% probability above 4.1% signals modest upward drift from July's reading is the consensus, not a sharp deterioration."
  - "Resolution tied to BLS official U-3; alternative unemployment definitions cited in the CBS report do not affect contract settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A CBS News analysis argues nearly 25% of US workers are functionally unemployed, well beyond the official 4.1% July U-3 rate."
    publisher: "cbsnews.com"
    published_at: "2026-08-21T00:00:00.000Z"
    source_url: "https://www.cbsnews.com/news/functional-unemployment-us-labor-market-analysis/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cbsnews.com"
        source_url: "https://www.cbsnews.com/news/functional-unemployment-us-labor-market-analysis/"
        retrieved_at: "2026-08-23T08:24:02+00:00"
  - type: "pm_response"
    notes: "Ladder distribution shows a tight consensus cluster at 4.2-4.3%, with thin tails above 4.5% aligning with sparse layoff data."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cbsnews.com: Nearly 25% of U.S. workers are \"functionally unemployed,\" economic ana"
    url: "https://www.cbsnews.com/news/functional-unemployment-us-labor-market-analysis/"
    published_at: "2026-08-21T00:00:00.000Z"
    retrieved_at: "2026-08-23T08:24:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
