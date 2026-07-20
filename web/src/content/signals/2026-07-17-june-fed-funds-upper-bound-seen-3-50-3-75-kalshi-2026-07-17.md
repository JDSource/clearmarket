---
signal_id: "CMSIG2026071701"
signal_slug: "june-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-07-17"
headline: "June Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Fed funds upper bound anchors in 3.50-3.75 percent range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-17T00:00:00.000Z"
event_id: "CM-EVT-PHWX2H6DM5"
event_slug: "kxfed-26jul"
event_question: "June 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUL-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Jul 29, 2026 meeting?"
  current_price: 0.07
  volume_24h_usd: 530.94
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-08-05T18:05:00Z"
bullets:
  - "Kalshi ladder pins the June 2026 Fed funds upper bound in the 3.50-3.75% range: 98% above 3.50% but only 7% above 3.75%."
  - "June headline CPI at 3.5% is consistent with the market pricing a hold; the distribution shows virtually no chance of a cut pulling the upper bound below 3.50%."
  - "Fed Chair Kevin Warsh's explicit inflation-watch posture aligns with the ladder's sharp drop above 3.75%, signaling the market sees no near-term hike either."
  - "Resolution via the named June 2026 FOMC meeting outcome; any emergency inter-meeting action would also settle the contract."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "June CPI cooled to 3.5% year-over-year on cheaper gas, but core prices barely moved and Fed Chair Kevin Warsh warned against declaring victory."
    publisher: "James Veale  
 
 
 Published: Jul 17 2026, 11:37 AM EDT"
    published_at: "2026-07-17T00:00:00.000Z"
    source_url: "https://www.moneytimes.com/articles/60652/20260717/june-inflation-cooled-35-cheaper-gas-fed-says-relief-may-not-last.htm"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "James Veale  
 
 
 Published: Jul 17 2026, 11:37 AM EDT"
        source_url: "https://www.moneytimes.com/articles/60652/20260717/june-inflation-cooled-35-cheaper-gas-fed-says-relief-may-not-last.htm"
        retrieved_at: "2026-07-20T10:47:34+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder covers the full upper-bound strike range; distribution consistent with a hold and no imminent hike."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "James Veale  
 
 
 Published: Jul 17 2026, 11:37 AM EDT: June Inflation Cooled to 3.5% on Cheaper Gas, but the Fed Says the Rel"
    url: "https://www.moneytimes.com/articles/60652/20260717/june-inflation-cooled-35-cheaper-gas-fed-says-relief-may-not-last.htm"
    published_at: "2026-07-17T00:00:00.000Z"
    retrieved_at: "2026-07-20T10:47:34+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
