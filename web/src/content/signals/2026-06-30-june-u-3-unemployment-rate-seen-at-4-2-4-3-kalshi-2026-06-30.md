---
signal_id: "CMSIG2026063001"
signal_slug: "june-u-3-unemployment-rate-seen-at-4-2-4-3-kalshi-2026-06-30"
headline: "June U-3 unemployment rate seen at 4.2-4.3%: Kalshi"
semantic_title: "June unemployment rate consensus anchors near 4.2 to 4.3 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-30T18:18:22.000Z"
event_id: "CM-EVT-FJGT56DTV2"
event_slug: "kxu3-26jun"
event_question: "June 2026 U-3 unemployment rate"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26JUN-T4.3"
  question_raw: "Will the unemployment rate (U-3) be above 4.3% in June?"
  current_price: 0.37
  volume_24h_usd: 2552.5
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-07-02T14:00:00Z"
bullets:
  - "Kalshi ladder prices 99% above 3.9%, 69% above 4.2%, only 37% above 4.3%, implying consensus squarely in the 4.2-4.3% range."
  - "Volume surged 115x day-over-day on this contract, signaling a sharp burst of fresh attention as the JOLTS and ADP prints landed."
  - "ADP private payrolls came in at 98,000, missing expectations, consistent with the market tilting toward the higher end of the 4.2-4.3% band."
  - "Resolves via FRED data from the Bureau of Labor Statistics Employment Situation release; the official June U-3 figure settles the contract."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US job openings rose to a two-year high in June while hiring remained sluggish, painting a split labor-market picture ahead of Friday's nonfarm payrolls release."
    publisher: "Reuters"
    published_at: "2026-06-30T18:18:22.000Z"
    source_url: "https://gvwire.com/2026/06/30/us-job-openings-rise-to-two-year-high-but-hiring-still-struggling/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Reuters"
        source_url: "https://gvwire.com/2026/06/30/us-job-openings-rise-to-two-year-high-but-hiring-still-struggling/"
        retrieved_at: "2026-07-02T10:34:14+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder on June 2026 U-3 unemployment rate drew exceptional volume, making this the sharpest labor-market signal in today's prediction-market prints."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Reuters: US Job Openings Rise to Two-Year High, but Hiring Still Struggling - G"
    url: "https://gvwire.com/2026/06/30/us-job-openings-rise-to-two-year-high-but-hiring-still-struggling/"
    published_at: "2026-06-30T18:18:22.000Z"
    retrieved_at: "2026-07-02T10:34:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
