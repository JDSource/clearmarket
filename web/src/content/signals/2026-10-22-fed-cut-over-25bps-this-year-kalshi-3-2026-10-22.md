---
signal_id: "CMSIG2026102203"
signal_slug: "fed-cut-over-25bps-this-year-kalshi-3-2026-10-22"
headline: "Fed cut over 25bps this year: Kalshi 3%"
semantic_title: "Fed rate cut above 25 basis points stays a long shot"
telemetry: "Kalshi 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-22T00:00:00.000Z"
event_id: "CM-EVT-RWRZ1R3SD6"
event_slug: "kxlargecut-26"
event_question: "Will the Federal Reserve do a rate cut greater than 25 basis points this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLARGECUT-26"
  question_raw: "Will the Fed cut rates more than 25 bps in 2026?"
  current_price: 0.029
  volume_24h_usd: 11.36
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only 3% odds on any Fed rate cut exceeding 25 basis points in 2026."
  - "Reaccelerating CPI nowcast to 3.75% is consistent with Kalshi's near-zero probability on an oversized cut this year."
  - "Fed Governor Chicago Fed President Austan Goolsbee's warning about persistent price pressures (Story 6) reinforces the same directional read."
  - "Resolves via Federal Reserve official policy announcement; any emergency easing move would need to exceed 25 basis points to trigger a yes resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Cleveland Fed nowcast puts October CPI at 3.75% year-over-year, well above August's 3.4% print, shrinking the real rate buffer to roughly 30 basis points."
    publisher: "the-weekly-investor.com"
    published_at: "2026-10-22T00:00:00.000Z"
    source_url: "https://www.the-weekly-investor.com/articles/feds-real-rate-buffer-is-30-bps-and-shrinking-1792667103826"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "the-weekly-investor.com"
        source_url: "https://www.the-weekly-investor.com/articles/feds-real-rate-buffer-is-30-bps-and-shrinking-1792667103826"
        retrieved_at: "2026-10-23T07:48:07+00:00"
  - type: "pm_response"
    notes: "Kalshi at 3% shows the market fully dismisses dovish pivot scenarios for 2026, aligning with both the nowcast and Fed communications."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "the-weekly-investor.com: Fed's Real Rate Buffer Is 30 bps, and Shrinking"
    url: "https://www.the-weekly-investor.com/articles/feds-real-rate-buffer-is-30-bps-and-shrinking-1792667103826"
    published_at: "2026-10-22T00:00:00.000Z"
    retrieved_at: "2026-10-23T07:48:07+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
