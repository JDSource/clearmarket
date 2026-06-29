---
signal_id: "CMSIG2026062808"
signal_slug: "btc-trimmed-mean-above-75k-by-june-30-kalshi-below-1-2026-06-28"
headline: "BTC trimmed mean above $75K by June 30: Kalshi below 1%"
semantic_title: "BTC above $75K by June 30 priced near zero on capitulation signals"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-28T00:43:00.000Z"
event_id: "CM-EVT-3MXSH7KHK5"
event_slug: "kxbtcmaxmon-btc-26jun30"
event_question: "BTC trimmed mean price, June 30 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXMON-BTC-26JUN30-7500000"
  question_raw: "Will BTC trimmed mean be above $75000.00 by 11:59 PM ET on Jun 30, 2026?"
  current_price: 0.01
  volume_24h_usd: 72.17
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2026-07-01T03:59:59Z"
bullets:
  - "Kalshi ladder implies BTC trimmed mean stays well below $75K by June 30: all strikes from $75K to $92.5K priced at just 1%."
  - "Bitcoin near $60,100 with 50,000 BTC moved at a loss is fully consistent with the market pricing no recovery to prior highs by month-end."
  - "Dedicated Kalshi binary on the Bitcoin trimmed mean price for June 30 is priced at just 2%, reinforcing the sub-$75K consensus."
  - "Resolves via CF Benchmarks trimmed mean calculation on June 30; deadline is tomorrow, making this effectively a near-zero-movement window."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Nearly 50,000 BTC moved to exchanges at a loss in a single day, with Bitcoin trading near $60,100 amid capitulation signals from short-term holders."
    publisher: "boursel.com"
    published_at: "2026-06-28T00:43:00.000Z"
    source_url: "https://boursel.com/article/bitcoin-sells-off-toward-60000-as-50000-coins-move-at-a-loss"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "boursel.com"
        source_url: "https://boursel.com/article/bitcoin-sells-off-toward-60000-as-50000-coins-move-at-a-loss"
        retrieved_at: "2026-06-29T12:28:56+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder and binary both price essentially zero chance of BTC reclaiming $75K by June 30, consistent with the on-chain capitulation data."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "boursel.com: Bitcoin Sells Off Toward $60,000 as 50,000 Coins Move at a Loss · Bour"
    url: "https://boursel.com/article/bitcoin-sells-off-toward-60000-as-50000-coins-move-at-a-loss"
    published_at: "2026-06-28T00:43:00.000Z"
    retrieved_at: "2026-06-29T12:28:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
