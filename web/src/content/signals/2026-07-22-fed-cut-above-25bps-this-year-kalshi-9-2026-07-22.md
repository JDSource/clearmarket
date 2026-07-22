---
signal_id: "CMSIG2026072206"
signal_slug: "fed-cut-above-25bps-this-year-kalshi-9-2026-07-22"
headline: "Fed cut above 25bps this year: Kalshi 9%"
semantic_title: "Odds on a large Fed cut this year stay deep in long-shot territory"
telemetry: "Kalshi 9%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-22T00:00:00.000Z"
event_id: "CM-EVT-RWRZ1R3SD6"
event_slug: "kxlargecut-26"
event_question: "Will the Federal Reserve do a rate cut greater than 25 basis points this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLARGECUT-26"
  question_raw: "Will the Fed cut rates more than 25 bps in 2026?"
  current_price: 0.09
  volume_24h_usd: 11.83
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi contract prices only 9% on the Federal Reserve cutting rates by more than 25 basis points this year."
  - "Despite job-loss headlines fueling cut speculation, the market gives barely one-in-ten odds on a larger-than-standard move."
  - "The rate-ladder consensus placing the Fed funds upper bound at 3.50-3.75% is consistent with at most one standard cut, not an aggressive easing cycle."
  - "Resolves via Federal Reserve official rate decisions; a single 25bps cut would not trigger this contract."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fresh US labor market data showing 92,000 job losses fueled speculation that the Federal Reserve could move toward rate cuts."
    publisher: "bitrss.com"
    published_at: "2026-07-22T00:00:00.000Z"
    source_url: "https://bitrss.com/u-s-economy-loses-92-000-jobs-fueling-speculation-of-fed-rate-cuts-190760"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "bitrss.com"
        source_url: "https://bitrss.com/u-s-economy-loses-92-000-jobs-fueling-speculation-of-fed-rate-cuts-190760"
        retrieved_at: "2026-07-22T10:22:09+00:00"
  - type: "pm_response"
    notes: "Kalshi at 9% shows the market treating large-cut speculation as noise against a backdrop of still-elevated inflation and a new Fed chair era."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "bitrss.com: U.S. Economy Loses 92,000 Jobs, Fueling Speculation of Fed Rate Cuts -"
    url: "https://bitrss.com/u-s-economy-loses-92-000-jobs-fueling-speculation-of-fed-rate-cuts-190760"
    published_at: "2026-07-22T00:00:00.000Z"
    retrieved_at: "2026-07-22T10:22:09+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
