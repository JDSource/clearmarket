---
signal_id: "CMSIG2026073001"
signal_slug: "june-2026-fed-funds-upper-bound-seen-at-3-75-4-0-kalshi-2026-07-30"
headline: "June 2026 Fed funds upper bound seen at 3.75-4.0%: Kalshi"
semantic_title: "Fed funds seen holding at 3.75-4.0% after Q2 GDP miss"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-30T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Fed funds upper bound following June 2026 FOMC meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.02
  volume_24h_usd: 7.27
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder pins the Fed funds upper bound at 3.75-4.0%: 60% above 3.75% but only 2% above 4.0%, with volume up 1,551x day over day."
  - "GDP headline of 1.5% suggests a dovish lean, but the buried 3.9% domestic demand figure aligns with the market holding near the 3.75-4.0% zone rather than pricing deep cuts."
  - "Trading volume surge of over 1,550x signals this contract is drawing intense fresh attention after the GDP release and its hawkish subtext."
  - "The 30-year mortgage rate ladder prices an implied peak of 6.9-7.0% for 2026, consistent with a Fed that stays elevated well into the second half."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Q2 GDP grew at only 1.5% but a hidden 3.9% domestic demand surge is described as handing Fed hawks new ammunition for the September rate decision."
    publisher: "Jerry Owens  
 
 
 Published: Jul 30 2026, 9:53 AM EDT"
    published_at: "2026-07-30T00:00:00.000Z"
    source_url: "https://www.techtimes.com/articles/322203/20260730/us-gdp-q2-2026-disappoints-15-hidden-39-demand-surge-hands-hawks-new-ammunition.htm"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jerry Owens  
 
 
 Published: Jul 30 2026, 9:53 AM EDT"
        source_url: "https://www.techtimes.com/articles/322203/20260730/us-gdp-q2-2026-disappoints-15-hidden-39-demand-surge-hands-hawks-new-ammunition.htm"
        retrieved_at: "2026-08-02T09:52:49+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder shows a sharply defined range with near-zero probability above 4.0%, reflecting a market that sees the Fed on hold but not hiking further despite the demand data."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jerry Owens  
 
 
 Published: Jul 30 2026, 9:53 AM EDT: US GDP Q2 2026 Disappoints at 1.5%: Hidden 3.9% Demand Surge Hands Haw"
    url: "https://www.techtimes.com/articles/322203/20260730/us-gdp-q2-2026-disappoints-15-hidden-39-demand-surge-hands-hawks-new-ammunition.htm"
    published_at: "2026-07-30T00:00:00.000Z"
    retrieved_at: "2026-08-02T09:52:49+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
