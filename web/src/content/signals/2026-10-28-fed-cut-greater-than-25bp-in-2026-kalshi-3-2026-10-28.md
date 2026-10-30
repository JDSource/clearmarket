---
signal_id: "CMSIG2026102805"
signal_slug: "fed-cut-greater-than-25bp-in-2026-kalshi-3-2026-10-28"
headline: "Fed cut greater than 25bp in 2026: Kalshi 3%"
semantic_title: "Fed rate cut above 25 basis points this year stays near zero odds"
telemetry: "Kalshi 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-10-28T04:01:06.000Z"
event_id: "CM-EVT-RWRZ1R3SD6"
event_slug: "kxlargecut-26"
event_question: "Will the Federal Reserve do a rate cut greater than 25 basis points this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLARGECUT-26"
  question_raw: "Will the Fed cut rates more than 25 bps in 2026?"
  current_price: 0.029
  volume_24h_usd: 3.45
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices a Fed rate cut greater than 25 basis points in 2026 at just 3%, a near-zero probability reflecting the hold decision."
  - "The Fed held rates steady citing elevated inflation; the Kalshi contract is consistent with this posture, as a large cut this year is now almost entirely ruled out by the market."
  - "NPR reporting notes investors widely expect a rate hike at December's meeting, which would make any cut in 2026 mathematically impossible, consistent with the 3% pricing."
  - "Kalshi resolves via Federal Reserve official policy announcement; the December meeting is the only remaining opportunity for 2026 resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Federal Reserve held its benchmark rate unchanged at approximately 3.9% at its October meeting despite elevated inflation, with investors now widely expecting a rate hike at the December meeting."
    publisher: "Christopher Rugaber"
    published_at: "2026-10-28T04:01:06.000Z"
    source_url: "https://apnews.com/article/inflation-warsh-interest-rates-federal-reserve-c06793b0c50641444701d5d098ccc2c8"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Christopher Rugaber"
        source_url: "https://apnews.com/article/inflation-warsh-interest-rates-federal-reserve-c06793b0c50641444701d5d098ccc2c8"
        retrieved_at: "2026-10-30T14:47:28+00:00"
  - type: "pm_response"
    notes: "Kalshi's 3% price on a greater-than-25bp cut this year is fully consistent with hold decisions and hike expectations; the contract is effectively priced out."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Christopher Rugaber: Fed keeps key rate unchanged at about 3.9% despite elevated inflation"
    url: "https://apnews.com/article/inflation-warsh-interest-rates-federal-reserve-c06793b0c50641444701d5d098ccc2c8"
    published_at: "2026-10-28T04:01:06.000Z"
    retrieved_at: "2026-10-30T14:47:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
