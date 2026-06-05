---
signal_id: "CMSIG2026060407"
signal_slug: "bitcoin-above-64k-on-june-6-kalshi-51-2026-06-04"
headline: "Bitcoin above $64K on June 6: Kalshi 51%"
semantic_title: "Bitcoin above $64K on June 6 wavers at coin-flip territory"
telemetry: "Polymarket ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-04T01:30:53.000Z"
event_id: "CM-EVT-JCHVD3PD84"
event_slug: "bitcoin-above-on-june-6-2026"
event_question: "Bitcoin price on June 6, 2026"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xf3cffa523f32396cc47e21a1d31d3f54f199d6fc0a2536d2fdd6953126dd1447"
  question_raw: "Will the price of Bitcoin be above $68,000 on June 6?"
  current_price: 0.311
  volume_24h_usd: 13358.764983000003
  arbitration_model: "uma_oracle"
  resolution_source: "binance.com"
  resolves_at: "2026-06-06T16:00:00Z"
bullets:
  - "Kalshi's June 6 Bitcoin ladder implies a 51% chance BTC closes above $64,000, with only 31% above $66,000."
  - "The spot selloff to below $63,000 is consistent with the Kalshi distribution, which assigns near-even odds to a $64,000 recovery by Saturday."
  - "A companion Kalshi ladder for June 7 (CM-EVT-KDMRKTYKR2) shows 78% above $64,000 and 48% above $66,000, suggesting the market expects some stabilization over the weekend."
  - "Resolves via the named resolution source; the settlement price is the official Bitcoin rate on June 6, 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Bitcoin's price slid below $63,000 for the first time since February, driven by a selloff that also saw heavy liquidations across crypto longs."
    publisher: "coindesk.com"
    published_at: "2026-06-04T01:30:53.000Z"
    source_url: "https://www.coindesk.com/markets/2026/06/04/bitcoin-selloff-continues-as-prices-slide-below-usd63-000-for-the-first-time-since-february"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "coindesk.com"
        source_url: "https://www.coindesk.com/markets/2026/06/04/bitcoin-selloff-continues-as-prices-slide-below-usd63-000-for-the-first-time-since-february"
        retrieved_at: "2026-06-05T12:03:19+00:00"
  - type: "pm_response"
    notes: "Kalshi's near-even $64K odds on June 6 reflect the spot selloff, with the June 7 ladder at 78% above $64K implying traders expect a modest recovery into the weekend."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "coindesk.com: Bitcoin selloff continues as prices slide below $63,000 for the first"
    url: "https://www.coindesk.com/markets/2026/06/04/bitcoin-selloff-continues-as-prices-slide-below-usd63-000-for-the-first-time-since-february"
    published_at: "2026-06-04T01:30:53.000Z"
    retrieved_at: "2026-06-05T12:03:19+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
