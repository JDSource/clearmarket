---
signal_id: "CMSIG2026070505"
signal_slug: "june-2026-cpi-year-over-year-above-3-7-ladder-69-2026-07-05"
headline: "June 2026 CPI year-over-year above 3.7%: ladder 69%"
semantic_title: "Annual CPI above 3.7 percent nears a pricing cliff"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-05T20:25:30.000Z"
event_id: "CM-EVT-FC6YNQPJV4"
event_slug: "kxcpiyoy-26jun"
event_question: "CPI year-over-year rate for June 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUN-T3.8"
  question_raw: "Will the rate of CPI inflation be above 3.8% for the year ending in June 2026?"
  current_price: 0.23
  volume_24h_usd: 1083.31
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-07-14T14:00:00Z"
bullets:
  - "Ladder prices 69% chance CPI year-over-year exceeds 3.7% for June 2026, falling sharply to 23% above 3.8%."
  - "Weak payrolls reduce demand-pull inflation pressure; the ladder's drop between 3.7% and 3.8% reflects that uncertainty."
  - "Above 3.5% is priced at 98%, so above-target inflation is near-certain; the debate is whether it reaches 3.8% or stalls."
  - "Resolves via the Bureau of Labor Statistics CPI release for June 2026; the year-over-year figure uses the prior-year base from June 2025."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "June payrolls plunged to 57,000, rapidly cooling Fed rate hike expectations and refocusing the market on the inflation outlook."
    publisher: "finance.biggo.com"
    published_at: "2026-07-05T20:25:30.000Z"
    source_url: "https://finance.biggo.com/news/e2b2479d-ad74-47db-bf75-11a5ce24b089"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "finance.biggo.com"
        source_url: "https://finance.biggo.com/news/e2b2479d-ad74-47db-bf75-11a5ce24b089"
        retrieved_at: "2026-07-06T12:00:14+00:00"
  - type: "pm_response"
    notes: "The ladder shows a consensus near 3.7% annual CPI with a sharp probability cliff at 3.8%, signaling high conviction on the band but not the tail."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "finance.biggo.com: U.S. June Nonfarm Payrolls Plunge to 57,000, Rapidly Cooling Fed Rate"
    url: "https://finance.biggo.com/news/e2b2479d-ad74-47db-bf75-11a5ce24b089"
    published_at: "2026-07-05T20:25:30.000Z"
    retrieved_at: "2026-07-06T12:00:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
