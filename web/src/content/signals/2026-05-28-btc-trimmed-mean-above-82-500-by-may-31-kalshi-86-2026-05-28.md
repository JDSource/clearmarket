---
signal_id: "CMSIG2026052805"
signal_slug: "btc-trimmed-mean-above-82-500-by-may-31-kalshi-86-2026-05-28"
headline: "BTC trimmed mean above $82,500 by May 31: Kalshi 86%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-05-28T04:25:42.000Z"
event_id: "CM-EVT-54WMWQX518"
event_slug: "kxbtcmaxmon-btc-26may31"
event_question: "BTC trimmed mean by May 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXMON-BTC-26MAY31-8500000"
  question_raw: "Will BTC trimmed mean be above $85000.00 by 11:59 PM ET on May 31, 2026?"
  current_price: 0.01
  volume_24h_usd: 320.93
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2026-06-01T03:59:59Z"
bullets:
  - "The Kalshi BTC trimmed-mean ladder implies a market-consensus range of $82,500-$85,000 by May 31, 2026, with 86% probability above $82,500 but only 1% above $85,000 -- a sharp cliff that pins the expected outcome just above the lower bound."
  - "News of Bitcoin falling below $73,000 following US airstrikes on Iran and $1 billion in liquidations represents a spot price significantly below the Kalshi ladder's implied range, suggesting a meaningful disconnect between current spot levels and the trimmed-mean settlement mechanism or a rapid expected recovery priced in."
  - "The trimmed-mean methodology used for settlement removes outlier prices, which may explain why the Kalshi ladder's implied level ($82,500-$85,000) appears well above the reported spot price of $73,000 -- the contract may have been calibrated or last-traded before the geopolitical shock."
  - "A companion Kalshi ladder (CM-EVT-NHW1YL14S9) on Bitcoin being below $40,000 by January 1, 2027 shows only 24% probability at that strike level, consistent with longer-horizon markets not pricing a structural breakdown even after the Iran-driven selloff."
  - "The Kalshi contract resolves via CF Benchmarks trimmed-mean calculation at 11:59 PM ET on May 31, 2026; the trimmed-mean methodology excludes extreme price prints, so flash-crash levels during the Iran strike news cycle may not fully affect the final settlement price."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin dropped below $73,000 as US airstrikes on an Iranian military site near the Strait of Hormuz reignited geopolitical risk and triggered roughly $1 billion in leveraged liquidations."
    publisher: "coindesk.com"
    published_at: "2026-05-28T04:25:42.000Z"
    source_url: "https://www.coindesk.com/markets/2026/05/28/bitcoin-drops-below-usd73-000-as-us-strikes-on-iran-spark-usd1-billion-liquidations"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "coindesk.com"
        source_url: "https://www.coindesk.com/markets/2026/05/28/bitcoin-drops-below-usd73-000-as-us-strikes-on-iran-spark-usd1-billion-liquidations"
        retrieved_at: "2026-05-29T21:01:04+00:00"
  - type: "pm_response"
    notes: "Kalshi's May 31 BTC trimmed-mean ladder and the January 2027 below-$40,000 ladder together show near-term pricing tension against spot but no long-run structural collapse priced."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "coindesk.com: Bitcoin drops below $73,000 as U.S. strikes on Iran spark $1 billion l"
    url: "https://www.coindesk.com/markets/2026/05/28/bitcoin-drops-below-usd73-000-as-us-strikes-on-iran-spark-usd1-billion-liquidations"
    published_at: "2026-05-28T04:25:42.000Z"
    retrieved_at: "2026-05-29T21:01:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
