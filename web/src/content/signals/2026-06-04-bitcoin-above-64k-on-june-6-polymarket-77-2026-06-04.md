---
signal_id: "CMSIG2026060407"
signal_slug: "bitcoin-above-64k-on-june-6-polymarket-77-2026-06-04"
headline: "Bitcoin above $64k on June 6: Polymarket 77%"
semantic_title: "Bitcoin above $68K on June 6 priced a long shot"
telemetry: "Polymarket 31%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-04T07:42:47.000Z"
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
  - "Polymarket prices 77% on Bitcoin closing above $64,000 on June 6, per the LADDER distribution."
  - "The ETF outflow news and sub-$62k intraday lows reported June 3-4 are in tension with a 77% probability of recovery to above $64k within days."
  - "A companion LADDER for June 7 shows an almost identical 78% above $64k, suggesting the market sees the dip as likely transient."
  - "Resolves via Polymarket's uma_oracle using Bitcoin price data on the specified date."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Crypto ETFs posted $449.6 million in combined Bitcoin and Ether net outflows on June 3 as the Bitcoin selloff extended below $62,000."
    publisher: "financefeeds.com"
    published_at: "2026-06-04T07:42:47.000Z"
    source_url: "https://financefeeds.com/crypto-etf-outflows-extend-as-bitcoin-and-ether-funds-lose-449-6-million-on-june-3/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "financefeeds.com"
        source_url: "https://financefeeds.com/crypto-etf-outflows-extend-as-bitcoin-and-ether-funds-lose-449-6-million-on-june-3/"
        retrieved_at: "2026-06-04T11:14:54+00:00"
  - type: "pm_response"
    notes: "Polymarket LADDER resolves via uma_oracle; both June 6 and June 7 contracts price near-identical recovery odds above $64k."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "financefeeds.com: Crypto ETF Outflows Extend as Bitcoin and Ether Funds Lose $449.6 Mill"
    url: "https://financefeeds.com/crypto-etf-outflows-extend-as-bitcoin-and-ether-funds-lose-449-6-million-on-june-3/"
    published_at: "2026-06-04T07:42:47.000Z"
    retrieved_at: "2026-06-04T11:14:54+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
