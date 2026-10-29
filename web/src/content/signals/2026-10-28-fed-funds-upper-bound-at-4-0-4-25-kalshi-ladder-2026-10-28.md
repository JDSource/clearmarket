---
signal_id: "CMSIG2026102801"
signal_slug: "fed-funds-upper-bound-at-4-0-4-25-kalshi-ladder-2026-10-28"
headline: "Fed funds upper bound at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen staying near 4 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-28T04:01:06.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "October 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.03
  volume_24h_usd: 760.09
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the October 2026 Fed funds upper bound in the 4.0-4.25% range: 82% above 4.0%, collapsing to 3% above 4.25%."
  - "The hold is fully consistent with the market distribution; trading volume on this contract surged 4,352% day over day, confirming fresh attention on the print."
  - "The sharp drop from 82% to 3% between the 4.0% and 4.25% strikes shows the market treats 4.0% as the current ceiling, not a floor for further hikes at this meeting."
  - "NPR and AP report investors widely expect a December hike; a December-dated Kalshi or Polymarket contract would reveal whether that expectation is priced in over the next horizon."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Federal Reserve held its key rate unchanged at approximately 3.9% at its October 2026 meeting despite elevated inflation, with Chair Kevin Warsh signaling a possible December hike."
    publisher: "Christopher Rugaber"
    published_at: "2026-10-28T04:01:06.000Z"
    source_url: "https://apnews.com/article/inflation-warsh-interest-rates-federal-reserve-c06793b0c50641444701d5d098ccc2c8"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Christopher Rugaber"
        source_url: "https://apnews.com/article/inflation-warsh-interest-rates-federal-reserve-c06793b0c50641444701d5d098ccc2c8"
        retrieved_at: "2026-10-29T07:47:47+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder contract; 44.5x volume spike signals this was the dominant prediction-market focus on Fed decision day."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Christopher Rugaber: Fed keeps key rate unchanged at about 3.9% despite elevated inflation"
    url: "https://apnews.com/article/inflation-warsh-interest-rates-federal-reserve-c06793b0c50641444701d5d098ccc2c8"
    published_at: "2026-10-28T04:01:06.000Z"
    retrieved_at: "2026-10-29T07:47:47+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
