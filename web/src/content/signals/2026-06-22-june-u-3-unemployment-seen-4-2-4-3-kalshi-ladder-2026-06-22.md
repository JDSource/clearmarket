---
signal_id: "CMSIG2026062207"
signal_slug: "june-u-3-unemployment-seen-4-2-4-3-kalshi-ladder-2026-06-22"
headline: "June U-3 unemployment seen 4.2-4.3%: Kalshi ladder"
semantic_title: "June unemployment rate pricing centers on 4.2 to 4.3 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-22T09:31:22.641Z"
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
  - "Kalshi's ladder places June 2026 unemployment in the 4.2-4.3% range: 63% above 4.2% but only 31% above 4.3%, with the modal read near 4.2%."
  - "The low-hire, low-fire dynamic described by the St. Louis Fed is consistent with a steady, elevated unemployment rate rather than a sharp rise or fall."
  - "The above-4.5% strike at just 2% shows the market is not pricing a labor market deterioration, even as the jobs landscape remains tight for new entrants."
  - "Resolves via Bureau of Labor Statistics Employment Situation report; the U-3 headline rate is the settlement figure."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "St. Louis Fed research highlights a low-hire, low-fire labor market where young adult workers face fewer opportunities as firms prioritize efficiency over expansion."
    publisher: "stlouisfed.org"
    published_at: "2026-06-22T09:31:22.641Z"
    source_url: "https://www.stlouisfed.org/on-the-economy/2026/jun/its-still-business-cycle-young-adult-workers-low-hire-low-fire-labor-market"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "stlouisfed.org"
        source_url: "https://www.stlouisfed.org/on-the-economy/2026/jun/its-still-business-cycle-young-adult-workers-low-hire-low-fire-labor-market"
        retrieved_at: "2026-06-22T13:32:28+00:00"
  - type: "pm_response"
    notes: "Kalshi's distribution on June unemployment is consistent with a stable but not worsening jobs market, aligning with the low-hire, low-fire academic framing without signaling crisis."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "stlouisfed.org: Young Adult Workers in a 'Low-Hire, Low-Fire' Labor Market"
    url: "https://www.stlouisfed.org/on-the-economy/2026/jun/its-still-business-cycle-young-adult-workers-low-hire-low-fire-labor-market"
    published_at: "2026-06-22T09:31:22.641Z"
    retrieved_at: "2026-06-22T13:32:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
