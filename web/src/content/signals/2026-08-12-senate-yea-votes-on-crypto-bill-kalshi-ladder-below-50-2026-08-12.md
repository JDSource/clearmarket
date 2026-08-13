---
signal_id: "CMSIG2026081207"
signal_slug: "senate-yea-votes-on-crypto-bill-kalshi-ladder-below-50-2026-08-12"
headline: "Senate Yea votes on crypto bill: Kalshi ladder below 50"
semantic_title: "Senate Yea votes on crypto structure bill seen below 50"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-12T09:06:47.420Z"
event_id: "CM-EVT-CSYS5KPXK6"
event_slug: "kxvoteclarity-26may16"
event_question: "Senate Yea votes on crypto market structure bill"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXVOTECLARITY-26MAY16-T50"
  question_raw: "How many Senate members will vote Yea on a crypto market structure bill (as defined in KXCRYPTOSTRUCTURE)?"
  current_price: 0.42
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi ladder implies fewer than 50 Senate Yea votes on a crypto market structure bill: 42% above 50 votes, only 33% above 55 votes."
  - "The September delay is consistent with sub-majority pricing, markets do not see a clear path to 60 votes needed for cloture, let alone a simple majority."
  - "Companion Polymarket contract CM-EVT-ZXN47LV744 prices 21% on the CLARITY Act being signed into law by 2026, confirming the broader market skepticism about full passage this year."
  - "Resolves based on the official Senate vote tally; the procedural September 15 vote may itself fail, making even reaching a final count uncertain."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Senate pushed the CLARITY Act procedural vote to September 15, delaying a landmark crypto market structure bill past the August recess."
    publisher: "TradingKey"
    published_at: "2026-08-12T09:06:47.420Z"
    source_url: "https://www.tradingkey.com/analysis/cryptocurrencies/btc/262095914-crypto-clarity-act-coinbase-bitcoin-btc-strategy-mstr-sec-cftc-tradingkey"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "TradingKey"
        source_url: "https://www.tradingkey.com/analysis/cryptocurrencies/btc/262095914-crypto-clarity-act-coinbase-bitcoin-btc-strategy-mstr-sec-cftc-tradingkey"
        retrieved_at: "2026-08-13T09:07:47+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder distribution; the spread from 42% above 50 votes down to 7% above 64 votes shows the market sees passage as an uphill battle even after the procedural scheduling breakthrough."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "TradingKey: Clarity Act Sees Major Breakthrough as Senate Sets First Procedural Vo"
    url: "https://www.tradingkey.com/analysis/cryptocurrencies/btc/262095914-crypto-clarity-act-coinbase-bitcoin-btc-strategy-mstr-sec-cftc-tradingkey"
    published_at: "2026-08-12T09:06:47.420Z"
    retrieved_at: "2026-08-13T09:07:47+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
