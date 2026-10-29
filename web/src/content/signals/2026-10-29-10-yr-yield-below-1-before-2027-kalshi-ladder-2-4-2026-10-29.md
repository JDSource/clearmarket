---
signal_id: "CMSIG2026102903"
signal_slug: "10-yr-yield-below-1-before-2027-kalshi-ladder-2-4-2026-10-29"
headline: "10-yr yield below 1% before 2027: Kalshi ladder 2-4%"
semantic_title: "Ten-year Treasury dipping below 1 percent stays a near-impossible bet"
telemetry: "Polymarket ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-29T00:00:00.000Z"
event_id: "CM-EVT-BD6QB5GC44"
event_slug: "how-low-will-10-year-treasury-yield-get-before-2027"
event_question: "10-year Treasury yield floor before 2027"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0828a02d7e64a7f79fde3e895356b6b102629344f801d930cb748a1e3a566c15"
  question_raw: "Will the 10-year Treasury yield dip below 1.0% before 2027?"
  current_price: 0.017
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Kalshi ladder assigns only 2-4% probability across all strikes from 1.0% to 3.9%, implying the market sees essentially zero chance the 10-year yield collapses to those levels before 2027."
  - "With the 10-year yield printing above 5% on the back of 3.4% GDP growth and accelerating PCE inflation, the ladder distribution is fully consistent with current macro conditions."
  - "The Fed's two hawkish dissenters and sticky inflation data further reduce any path to the dramatic yield collapse these ladder strikes would require."
  - "The Kalshi contract on a Fed rate cut greater than 25 bps this year (3%) corroborates: no easing catalyst exists that would drive yields anywhere near the ladder's strike range."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The 10-year Treasury yield hovered above 5% following the Fed's rate hold and stronger-than-expected Q3 GDP and inflation data."
    publisher: "Michelle Fox, Sean Conlon, Chloe Taylor"
    published_at: "2026-10-29T00:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/10/29/treasury-yields-federal-reserve-rates.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Michelle Fox, Sean Conlon, Chloe Taylor"
        source_url: "https://www.cnbc.com/2026/10/29/treasury-yields-federal-reserve-rates.html"
        retrieved_at: "2026-10-29T14:55:20+00:00"
  - type: "pm_response"
    notes: "Kalshi's ladder on yield floors resolves via market-observed Treasury yield data; all strikes price as near-certain non-events given current yield levels."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Michelle Fox, Sean Conlon, Chloe Taylor: 10-year Treasury yield hovers above 5% after strong GDP report, rising"
    url: "https://www.cnbc.com/2026/10/29/treasury-yields-federal-reserve-rates.html"
    published_at: "2026-10-29T00:00:00.000Z"
    retrieved_at: "2026-10-29T14:55:20+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
