---
signal_id: "CMSIG2026061407"
signal_slug: "bitcoin-above-62k-on-june-14-kalshi-ladder-91-2026-06-14"
headline: "Bitcoin above $62K on June 14: Kalshi ladder 91%"
semantic_title: "Bitcoin above $62K on June 14 commands solid majority in pricing"
telemetry: "Polymarket ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-14T08:00:05.000Z"
event_id: "CM-EVT-MGBNRL5829"
event_slug: "bitcoin-above-on-june-14-2026"
event_question: "Bitcoin price on June 14, 2026"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xf31ec47d1ab987c3cfde6c08ab9773763b83cd95cfcd5ffaf2235c4432848457"
  question_raw: "Will the price of Bitcoin be above $64,000 on June 14?"
  current_price: 0.48
  volume_24h_usd: 6752.575704
  arbitration_model: "uma_oracle"
  resolution_source: "binance.com"
  resolves_at: "2026-06-14T16:00:00Z"
bullets:
  - "Kalshi ladder prices Bitcoin above $62,000 on June 14 at 91%, but only 48% above $64,000, pinning the implied range at $62,000-$64,000."
  - "The Iran strike cancellation and oil price drop are consistent with the rebound narrative and the mid-$60K implied level."
  - "A companion June 15 ladder shows 85% above $62,000 and 43% above $64,000, suggesting the market prices continuity but not a strong breakout."
  - "The June 16 and June 17 ladders both imply $64,000-$66,000, showing a modest upward drift in the market-implied range across the week."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Bitcoin rebounded as Trump canceled Iran strikes and oil fell roughly 3%, lifting risk assets including crypto."
    publisher: "coininsider.com"
    published_at: "2026-06-14T08:00:05.000Z"
    source_url: "https://www.coininsider.com/news/bitcoin-rebounds-as-trump-cancels-iran-strike-plan-and-oil-prices-fall/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "coininsider.com"
        source_url: "https://www.coininsider.com/news/bitcoin-rebounds-as-trump-cancels-iran-strike-plan-and-oil-prices-fall/"
        retrieved_at: "2026-06-14T10:47:32+00:00"
  - type: "pm_response"
    notes: "Ladder contracts resolve via CF Benchmarks spot Bitcoin price; the $62K-$64K pinch on June 14 is the key settlement zone based on current distribution."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "coininsider.com: Bitcoin Rebounds as Trump Cancels Iran Strike, Oil Falls 3%"
    url: "https://www.coininsider.com/news/bitcoin-rebounds-as-trump-cancels-iran-strike-plan-and-oil-prices-fall/"
    published_at: "2026-06-14T08:00:05.000Z"
    retrieved_at: "2026-06-14T10:47:32+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
