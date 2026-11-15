---
signal_id: "CMSIG2026111203"
signal_slug: "fed-cut-greater-than-25bps-in-2026-kalshi-1-2026-11-12"
headline: "Fed cut greater than 25bps in 2026: Kalshi 1%"
semantic_title: "Odds on a Fed cut above 25 basis points this year near zero"
telemetry: "Kalshi 1%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-12T15:58:26.000Z"
event_id: "CM-EVT-RWRZ1R3SD6"
event_slug: "kxlargecut-26"
event_question: "Will the Federal Reserve do a rate cut greater than 25 basis points this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLARGECUT-26"
  question_raw: "Will the Fed cut rates more than 25 bps in 2026?"
  current_price: 0.012
  volume_24h_usd: 3.52
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi contract on a Fed cut greater than 25 basis points in 2026 prices at just 1%."
  - "Even with cooler-than-expected CPI and PPI data, the market leaves essentially no room for an outsized cut, consistent with officials backing further hikes this cycle."
  - "The near-zero probability on a large cut corroborates the Kalshi ladder (CM-EVT-MR57HVWJT3) implying the upper bound stays at or above 4.0%."
  - "Resolves via the Federal Reserve's own rate decision; a cut of any size, let alone above 25 basis points, would require a dramatic reversal in Fed guidance."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "BOK Financial notes mixed signals as CPI and PPI came in cooler than expected but progress toward the Fed's 2% target remains slow amid higher energy prices."
    publisher: "bokfinancial.com"
    published_at: "2026-11-12T15:58:26.000Z"
    source_url: "https://www.bokfinancial.com/insights/articles/by-the-numbers_081426"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "bokfinancial.com"
        source_url: "https://www.bokfinancial.com/insights/articles/by-the-numbers_081426"
        retrieved_at: "2026-11-15T07:48:03+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 1%; resolves via Federal Reserve decision; no intraday move claimed."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "bokfinancial.com: By the Numbers: Fed receiving conflicting inflation and job market sig"
    url: "https://www.bokfinancial.com/insights/articles/by-the-numbers_081426"
    published_at: "2026-11-12T15:58:26.000Z"
    retrieved_at: "2026-11-15T07:48:03+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
