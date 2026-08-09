---
signal_id: "CMSIG2026080708"
signal_slug: "btc-trimmed-mean-by-aug-31-seen-67-5k-70k-kalshi-54-29-2026-08-07"
headline: "BTC trimmed mean by Aug 31 seen $67.5K-$70K: Kalshi 54%/29%"
semantic_title: "Bitcoin trimmed mean by August 31 priced in the $67.5K-$70K range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-07T00:00:00.000Z"
event_id: "CM-EVT-91N8R2ZK22"
event_slug: "kxbtcmaxmon-btc-26aug31"
event_question: "BTC trimmed mean price by August 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXMON-BTC-26AUG31-7000000"
  question_raw: "Will BTC trimmed mean be above $70000.00 by 11:59 PM ET on Aug 31, 2026?"
  current_price: 0.29
  volume_24h_usd: 1781.49
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2026-09-08T03:59:59Z"
bullets:
  - "Kalshi ladder puts the BTC trimmed mean by August 31 in the $67,500-$70,000 range: 54% above $67,500, 29% above $70,000."
  - "Bitcoin hit an August peak near $65,340 on the jobs miss day; the ladder implies the market is pricing modest further upside from current levels."
  - "The separate Bitcoin-above-$100,000-by-September-1 ladder (CM-EVT-ZPMYBGJP99) sits at only 1-11% across strikes, confirming the $67,500-$70,000 range as the realistic near-term consensus."
  - "Resolves via CoinDesk or equivalent price reference for BTC trimmed mean at 11:59 PM ET on August 31, 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin broke above $65,000 as the July jobs miss fueled expectations of a Fed hold, boosting risk assets including crypto."
    publisher: "cointelegraph.com"
    published_at: "2026-08-07T00:00:00.000Z"
    source_url: "https://cointelegraph.com/markets/bitcoin-price-tags-653k-august-high-as-low-us-jobs-numbers-cool-fed-rate-bets"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cointelegraph.com"
        source_url: "https://cointelegraph.com/markets/bitcoin-price-tags-653k-august-high-as-low-us-jobs-numbers-cool-fed-rate-bets"
        retrieved_at: "2026-08-09T08:36:33+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via BTC trimmed mean data by August 31; distribution suggests payrolls-driven crypto rally is priced to continue modestly but not explosively."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cointelegraph.com: US Nonfarm Payrolls Miss Sends Bitcoin Above $65,000"
    url: "https://cointelegraph.com/markets/bitcoin-price-tags-653k-august-high-as-low-us-jobs-numbers-cool-fed-rate-bets"
    published_at: "2026-08-07T00:00:00.000Z"
    retrieved_at: "2026-08-09T08:36:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
