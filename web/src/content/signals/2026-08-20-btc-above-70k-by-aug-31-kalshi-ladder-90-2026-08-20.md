---
signal_id: "CMSIG2026082001"
signal_slug: "btc-above-70k-by-aug-31-kalshi-ladder-90-2026-08-20"
headline: "BTC above $70K by Aug 31: Kalshi ladder 90%"
semantic_title: "Bitcoin above $70K stays heavily favored through August"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-20T06:38:13.000Z"
event_id: "CM-EVT-91N8R2ZK22"
event_slug: "kxbtcmaxmon-btc-26aug31"
event_question: "BTC trimmed mean price by Aug 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXMON-BTC-26AUG31-7250000"
  question_raw: "Will BTC trimmed mean be above $72500.00 by 11:59 PM ET on Aug 31, 2026?"
  current_price: 0.46
  volume_24h_usd: 71125.96
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2026-09-08T03:59:59Z"
bullets:
  - "Kalshi ladder prices BTC above $70K at 90% by Aug 31, implying consensus near $70K-$72.5K range; $75K only 20%."
  - "News of Bitcoin reaching $70K is consistent with the Kalshi distribution, which already had $70K as its near-consensus floor."
  - "The $72.5K-$75K gap, 46% vs 20%, signals markets see the current level as a ceiling test, not a breakout."
  - "Companion Kalshi contract prices only 14% on BTC above $100K by Dec 31, 2026, suggesting conviction fades sharply at higher strikes."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin hit $70,000 driven by Trump hints at government BTC accumulation and a White House crypto summit."
    publisher: "news18.com"
    published_at: "2026-08-20T06:38:13.000Z"
    source_url: "https://www.news18.com/business/markets/bitcoin-hits-70000-why-is-bitcoin-rising-today-whats-driving-the-crypto-rally-ws-l-10283527.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "news18.com"
        source_url: "https://www.news18.com/business/markets/bitcoin-hits-70000-why-is-bitcoin-rising-today-whats-driving-the-crypto-rally-ws-l-10283527.html"
        retrieved_at: "2026-08-20T08:32:51+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via CF Benchmarks trimmed mean; the distribution is tight around $70K-$72.5K with sharp drop-off above $75K."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "news18.com: Bitcoin Hits $70,000: Why Is Bitcoin Rising Today? What's Driving the"
    url: "https://www.news18.com/business/markets/bitcoin-hits-70000-why-is-bitcoin-rising-today-whats-driving-the-crypto-rally-ws-l-10283527.html"
    published_at: "2026-08-20T06:38:13.000Z"
    retrieved_at: "2026-08-20T08:32:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
