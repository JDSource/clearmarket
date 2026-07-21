---
signal_id: "CMSIG2026072108"
signal_slug: "bitcoin-crosses-100k-again-kalshi-19-2026-07-21"
headline: "Bitcoin crosses $100K again: Kalshi 19%"
semantic_title: "Bitcoin above $100K again holds at deep discount in Kalshi pricing"
telemetry: "Kalshi 19%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-21T00:14:46.000Z"
event_id: "CM-EVT-ZPMYBGJP99"
event_slug: "kxbtcmax100-26"
event_question: "Will Bitcoin cross $100,000 again?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAX100-26-DEC"
  question_raw: "Will Bitcoin be above $100000.00 by Jan 1, 2027 at 12:00AM ET?"
  current_price: 0.19
  volume_24h_usd: 1953.08
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T05:00:00Z"
bullets:
  - "Kalshi prices a 19% probability that Bitcoin crosses $100,000 again, with the Kalshi ladder showing only 14% above $100K by December 31."
  - "Whale accumulation and ETF inflow recovery are bullish signals, but the market prices Bitcoin reclaiming $100K as a low-probability outcome from current levels near $65K."
  - "The Kalshi contract on Bitcoin minimum price above a floor by January 1, 2027 sits at 28%, providing a lower-bound read that reinforces the modest recovery consensus."
  - "Resolves via CF Benchmarks; the $65K current spot price implies a roughly 54% gain required to hit $100K, making the 19% pricing appear calibrated rather than dismissive."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin whales posted their largest five-month accumulation of 66,700 BTC while mid-tier holders sold, with ETF inflows surging to $273 million after a two-month rout."
    publisher: "Jinju Hong"
    published_at: "2026-07-21T00:14:46.000Z"
    source_url: "https://www.digitaltoday.co.kr/en/view/83411/bitcoin-whales-post-biggest-accumulation-in-five-months-buy-66700-btc-as-mid-tier-holders-sell"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jinju Hong"
        source_url: "https://www.digitaltoday.co.kr/en/view/83411/bitcoin-whales-post-biggest-accumulation-in-five-months-buy-66700-btc-as-mid-tier-holders-sell"
        retrieved_at: "2026-07-21T10:22:25+00:00"
  - type: "pm_response"
    notes: "Kalshi at 19% on Bitcoin recrossing $100K; the whale accumulation news is constructive but the market prices significant distance between current spot and the $100K threshold."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jinju Hong: Bitcoin whales post biggest accumulation in five months, buying 66,700"
    url: "https://www.digitaltoday.co.kr/en/view/83411/bitcoin-whales-post-biggest-accumulation-in-five-months-buy-66700-btc-as-mid-tier-holders-sell"
    published_at: "2026-07-21T00:14:46.000Z"
    retrieved_at: "2026-07-21T10:22:25+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
