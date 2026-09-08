---
signal_id: "CMSIG2026090808"
signal_slug: "strait-of-hormuz-back-to-normal-by-dec-31-polymarket-24-2026-09-08"
headline: "Strait of Hormuz back to normal by Dec 31: Polymarket 24%"
semantic_title: "Hormuz traffic returning to normal by year-end stays near 25%"
telemetry: "Polymarket 24%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-08T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.24
  volume_24h_usd: 39644.571876
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Strait of Hormuz traffic returning to normal by December 31 sits at 24%."
  - "Iran's announcement of a new Gulf exclusion zone and missile threats are directly at odds with a near-term normalization, and the 24% pricing reflects that tension."
  - "A new exclusion zone, if implemented, would further constrain shipping lanes already disrupted by the six-month conflict, reinforcing the market's skeptical stance."
  - "Resolution via UMA oracle; the 76% probability that traffic does NOT normalize by year-end is the dominant market view given Iran's escalatory posture."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran announced plans for a new Persian Gulf exclusion zone and threatened the US with new missiles and economic warfare amid ongoing tensions."
    publisher: "straitstimes.com"
    published_at: "2026-09-08T00:00:00.000Z"
    source_url: "https://www.straitstimes.com/world/middle-east/iran-says-it-plans-new-gulf-exclusion-zone-threatens-us-with-new-missiles"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "straitstimes.com"
        source_url: "https://www.straitstimes.com/world/middle-east/iran-says-it-plans-new-gulf-exclusion-zone-threatens-us-with-new-missiles"
        retrieved_at: "2026-09-08T12:33:52+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; Iran's exclusion zone announcement and the 24% probability together represent a clear market rejection of near-term de-escalation."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "straitstimes.com: Iran says it plans new Gulf ‘exclusion zone’, threatens US with new mi"
    url: "https://www.straitstimes.com/world/middle-east/iran-says-it-plans-new-gulf-exclusion-zone-threatens-us-with-new-missiles"
    published_at: "2026-09-08T00:00:00.000Z"
    retrieved_at: "2026-09-08T12:33:52+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
