---
signal_id: "CMSIG2026111203"
signal_slug: "fed-cut-greater-than-25bp-in-2026-kalshi-2-2026-11-12"
headline: "Fed cut greater than 25bp in 2026: Kalshi 2%"
semantic_title: "Odds on a large Fed cut this year hold near floor at 2 percent"
telemetry: "Kalshi 2%"
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
  current_price: 0.019
  volume_24h_usd: 7.5
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi contract on a Fed rate cut greater than 25 basis points in 2026 is priced at 2%, consistent with an entrenched hiking stance."
  - "Fed Vice Chair Philip Jefferson's data-dependent commentary and Chicago Fed President Austan Goolsbee's 'borderline disturbing' inflation read align with the near-zero cut probability."
  - "The Kalshi 1% contract on any cut before 2027 (CM-EVT-X2TT2M9D02) and this 2% contract form a coherent, mutually consistent picture: markets see the hiking cycle as firmly intact."
  - "Resolves via Federal Reserve decision; a greater-than-25bp cut in a year of active hikes would be historically anomalous."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "BOK Financial notes mixed inflation signals, with cooler-than-expected CPI and PPI but persistent underlying price pressures keeping the Fed on a tightening path."
    publisher: "bokfinancial.com"
    published_at: "2026-11-12T15:58:26.000Z"
    source_url: "https://www.bokfinancial.com/insights/articles/by-the-numbers_081426"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "bokfinancial.com"
        source_url: "https://www.bokfinancial.com/insights/articles/by-the-numbers_081426"
        retrieved_at: "2026-11-14T07:47:51+00:00"
  - type: "pm_response"
    notes: "Kalshi at 2% leaves a small residual for a tail scenario; no volume spike data available for this contract."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "bokfinancial.com: By the Numbers: Fed receiving conflicting inflation and job market sig"
    url: "https://www.bokfinancial.com/insights/articles/by-the-numbers_081426"
    published_at: "2026-11-12T15:58:26.000Z"
    retrieved_at: "2026-11-14T07:47:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
