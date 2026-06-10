---
signal_id: "CMSIG2026061007"
signal_slug: "btc-trimmed-mean-below-62-5k-by-jun-30-kalshi-61-2026-06-10"
headline: "BTC trimmed mean below $62.5K by Jun 30: Kalshi 61%"
semantic_title: "BTC end-of-June floor consensus clusters near $60K-$62.5K"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-10T08:30:31.000Z"
event_id: "CM-EVT-P48V448T55"
event_slug: "kxbtcminmon-btc-26jun30"
event_question: "BTC trimmed mean by June 30, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMINMON-BTC-26JUN30-5250000"
  question_raw: "Will BTC trimmed mean be below $52500.00 by 11:59 PM ET on Jun 30, 2026?"
  current_price: 0.1
  volume_24h_usd: 1639.31
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2026-07-01T03:59:59Z"
bullets:
  - "Kalshi's BTC ladder implies market consensus near $60,000-$62,500, with 61% below $62,500 but only 39% below $60,000 by June 30."
  - "Bitcoin trading near $58,000-$61,300 is consistent with the 39% below-$60K reading, placing spot price at the lower edge of the distribution."
  - "The above-$75,000 ladder (CM-EVT-3MXSH7KHK5) prices only 25% above $75,000 by June 30, confirming the market sees little near-term recovery runway."
  - "Resolves via CoinGecko trimmed mean; the gap between current spot near $58K-$61K and the 39% below-$60K strike suggests traders expect some mean-reversion before month-end."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin recorded its worst weekly performance since the FTX collapse, sliding near $58,000 and erasing roughly $390 billion in crypto market cap."
    publisher: "Shiraz Jagati"
    published_at: "2026-06-10T08:30:31.000Z"
    source_url: "https://news.bitcoin.com/bitcoin-worst-week-since-ftx-collapse-2026/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Shiraz Jagati"
        source_url: "https://news.bitcoin.com/bitcoin-worst-week-since-ftx-collapse-2026/"
        retrieved_at: "2026-06-10T11:36:47+00:00"
  - type: "pm_response"
    notes: "Kalshi's below-$62,500 at 61% and above-$75,000 at 25% bracket a bearish June range, with current spot price sitting near the lower tail of the distribution after the worst weekly performance since FTX."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Shiraz Jagati: Bitcoin Trades Near $61,300 After Worst Week Since FTX Collapse Wipes"
    url: "https://news.bitcoin.com/bitcoin-worst-week-since-ftx-collapse-2026/"
    published_at: "2026-06-10T08:30:31.000Z"
    retrieved_at: "2026-06-10T11:36:47+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
