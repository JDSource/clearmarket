---
signal_id: "CMSIG2026062503"
signal_slug: "cpi-above-3-7-for-year-ending-july-kalshi-67-2026-06-25"
headline: "CPI above 3.7% for year ending July: Kalshi 67%"
semantic_title: "CPI above 3.7 percent by July hardens as consensus range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-25T15:53:20.000Z"
event_id: "CM-EVT-FC6YNQPJV4"
event_slug: "kxcpiyoy-26jun"
event_question: "CPI year-over-year rate for month ending July 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUN-T3.8"
  question_raw: "Will the rate of CPI inflation be above 3.8% for the year ending in June 2026?"
  current_price: 0.28
  volume_24h_usd: 1131.86
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-07-14T14:00:00Z"
bullets:
  - "Kalshi ladder implies CPI in the 3.7-3.8% range for the year ending July: 67% above 3.7%, dropping to 28% above 3.8%."
  - "The 4.1% PCE print, the catalyst behind the crypto liquidation wave, is a different index but a directionally consistent read for CPI trajectory."
  - "The sharp cliff from 67% to 28% between the 3.7% and 3.8% strikes marks the market's key inflection level; above 3.8% is priced as a tail."
  - "Resolves via Bureau of Labor Statistics CPI release for the relevant month."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The May PCE print at 4.1% triggered a $1.48 billion crypto liquidation wave and renewed rate-hike fears across risk assets."
    publisher: "Lawrence Mondal"
    published_at: "2026-06-25T15:53:20.000Z"
    source_url: "https://crypto.news/bitcoin-triggers-1-48b-liquidation-wave-after-pce-inflation-fuels-rate-fears/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Lawrence Mondal"
        source_url: "https://crypto.news/bitcoin-triggers-1-48b-liquidation-wave-after-pce-inflation-fuels-rate-fears/"
        retrieved_at: "2026-06-27T01:35:43+00:00"
  - type: "pm_response"
    notes: "Kalshi distribution concentrates probability in a narrow 3.7-3.8% band, signaling consensus rather than uncertainty about the CPI range."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Lawrence Mondal: Bitcoin triggers $1.48B liquidation wave after PCE inflation fuels rat"
    url: "https://crypto.news/bitcoin-triggers-1-48b-liquidation-wave-after-pce-inflation-fuels-rate-fears/"
    published_at: "2026-06-25T15:53:20.000Z"
    retrieved_at: "2026-06-27T01:35:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
