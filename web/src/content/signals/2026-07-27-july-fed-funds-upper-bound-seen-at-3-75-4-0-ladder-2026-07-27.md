---
signal_id: "CMSIG2026072701"
signal_slug: "july-fed-funds-upper-bound-seen-at-3-75-4-0-ladder-2026-07-27"
headline: "July Fed funds upper bound seen at 3.75-4.0%: ladder"
semantic_title: "Markets put long odds on a July Fed hike"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-27T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "July 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.36
  volume_24h_usd: 1.8
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Ladder prices the July 2026 Fed funds upper bound in the 3.75-4.0% range: 65% above 3.75% but only 36% above 4.0%."
  - "News reports one-in-three hike odds from futures; the ladder is consistent, centering on a hold at 3.75% with a live tail toward 4.0%."
  - "Oil retreating from $100 toward $97 is cited as the key catalyst cooling hike bets; the ladder tail above 4.0% reflects residual risk."
  - "Companion Kalshi contract CM-EVT-P6QJP9BW02 prices only 59% on the Fed cutting rates with a dissent in July, a separate angle on meeting dynamics."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Oil prices pulling back toward $97 from above $100 cooled but did not eliminate July rate-hike expectations, with futures traders pricing roughly one-in-three odds of a hike."
    publisher: "Collin Mercer  
 
 
 Published: Jul 27 2026, 9:50 AM EDT"
    published_at: "2026-07-27T00:00:00.000Z"
    source_url: "https://www.techtimes.com/articles/321675/20260727/federal-reserve-july-meeting-oil-pullback-cuts-hike-odds-one-three-september-surges.htm"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Collin Mercer  
 
 
 Published: Jul 27 2026, 9:50 AM EDT"
        source_url: "https://www.techtimes.com/articles/321675/20260727/federal-reserve-july-meeting-oil-pullback-cuts-hike-odds-one-three-september-surges.htm"
        retrieved_at: "2026-07-28T10:30:26+00:00"
  - type: "pm_response"
    notes: "Ladder distribution spans multiple resolution strikes; the sharp drop from 65% at 3.75% to 36% at 4.0% marks the consensus hold zone."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Collin Mercer  
 
 
 Published: Jul 27 2026, 9:50 AM EDT: Federal Reserve July Meeting: Oil Pullback Cuts Hike Odds to One-in-Th"
    url: "https://www.techtimes.com/articles/321675/20260727/federal-reserve-july-meeting-oil-pullback-cuts-hike-odds-one-three-september-surges.htm"
    published_at: "2026-07-27T00:00:00.000Z"
    retrieved_at: "2026-07-28T10:30:26+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
