---
signal_id: "CMSIG2026080904"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-48-2026-08-09"
headline: "Hormuz traffic normal by Dec 31: Polymarket 48%"
semantic_title: "Strait of Hormuz reopening by year-end sits near 50%"
telemetry: "Polymarket 48%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-09T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.48
  volume_24h_usd: 223078.49461400005
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract prices a 48% chance Strait of Hormuz traffic returns to normal by December 31, effectively a coin flip."
  - "Iran hardening demands and Israel rejecting a Gaza deal are consistent with the market's near-even split; no resolution is clearly favored."
  - "An Iran-Oman lane deal in progress offers a partial resolution path, but the Polymarket price shows the market is not treating it as a near-certain unlock."
  - "Resolves via Polymarket's UMA oracle; the question likely turns on whether traffic volume benchmarks return to pre-crisis norms, not merely a formal agreement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Israel rejected Trump's Gaza plan and Iran hardened its conditions for reopening the Strait of Hormuz, while Tehran moved toward a partial lane deal with Oman."
    publisher: "The Associated Press"
    published_at: "2026-08-09T00:00:00.000Z"
    source_url: "https://www.foxcarolina.com/2026/08/09/israel-rejects-trumps-gaza-plan-more-details-emerge-strait-hormuz/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "The Associated Press"
        source_url: "https://www.foxcarolina.com/2026/08/09/israel-rejects-trumps-gaza-plan-more-details-emerge-strait-hormuz/"
        retrieved_at: "2026-08-12T09:07:43+00:00"
  - type: "pm_response"
    notes: "Polymarket is the sole priced venue; the 48% reading reflects genuine two-sided uncertainty as diplomatic signals remain mixed."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "The Associated Press: Israel rejects Trump’s Gaza plan, more details emerge on the Strait of"
    url: "https://www.foxcarolina.com/2026/08/09/israel-rejects-trumps-gaza-plan-more-details-emerge-strait-hormuz/"
    published_at: "2026-08-09T00:00:00.000Z"
    retrieved_at: "2026-08-12T09:07:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
