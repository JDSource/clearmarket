---
signal_id: "CMSIG2026072402"
signal_slug: "fed-july-cut-with-dissent-kalshi-63-2026-07-24"
headline: "Fed July cut with dissent: Kalshi 63%"
semantic_title: "Fed July cut with dissent stays a long shot"
telemetry: "Kalshi 63%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-24T00:00:00.000Z"
event_id: "CM-EVT-P6QJP9BW02"
event_slug: "kxfedcombo-26jul"
event_question: "Will the Federal Reserve in July 2026 cut rates and have at least one dissent?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDCOMBO-26JUL-0-T0"
  question_raw: "Will Federal Funds Rate Decision be No change AND Dissents be >0 for Jul 2026?"
  current_price: 0.63
  volume_24h_usd: 663.59
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-07-29T17:55:00Z"
bullets:
  - "The Kalshi prediction market puts 63% odds on the Fed cutting rates in July 2026 with at least one dissent."
  - "A services-driven growth print at 2.3% alongside factory contraction is a mixed signal, the market is not pricing a clean consensus cut."
  - "The 63% reading suggests markets see a cut as more likely than not, but the dissent component implies internal Fed division is expected."
  - "Cross-check: the Polymarket contract on the Fed making any rate decision between April and July sits at 79%, broadly consistent with an expected but contested July cut."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US private-sector growth hit its fastest Q3 pace in months at a 2.3% annualized rate, even as manufacturing entered contraction."
    publisher: "Roger Satterfield  
 
 
 Published: Jul 24 2026, 10:34 AM EDT"
    published_at: "2026-07-24T00:00:00.000Z"
    source_url: "https://www.techtimes.com/articles/321476/20260724/services-surge-pushes-us-growth-23-pace-factories-enter-contraction.htm"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Roger Satterfield  
 
 
 Published: Jul 24 2026, 10:34 AM EDT"
        source_url: "https://www.techtimes.com/articles/321476/20260724/services-surge-pushes-us-growth-23-pace-factories-enter-contraction.htm"
        retrieved_at: "2026-07-26T09:55:47+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via Bureau of Labor Statistics; note the resolution source is unusual for a Fed decision, confirm settlement mechanic."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Roger Satterfield  
 
 
 Published: Jul 24 2026, 10:34 AM EDT: Services Surge Pushes US Growth to 2.3% Pace as Factories Enter Contra"
    url: "https://www.techtimes.com/articles/321476/20260724/services-surge-pushes-us-growth-23-pace-factories-enter-contraction.htm"
    published_at: "2026-07-24T00:00:00.000Z"
    retrieved_at: "2026-07-26T09:55:47+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
