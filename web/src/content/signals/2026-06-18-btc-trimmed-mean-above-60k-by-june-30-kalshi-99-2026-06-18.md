---
signal_id: "CMSIG2026061808"
signal_slug: "btc-trimmed-mean-above-60k-by-june-30-kalshi-99-2026-06-18"
headline: "BTC trimmed mean above $60K by June 30: Kalshi 99%"
semantic_title: "Bitcoin trimmed mean above $60K by June 30 commands near certainty"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-18T13:50:00.000Z"
event_id: "CM-EVT-P48V448T55"
event_slug: "kxbtcminmon-btc-26jun30"
event_question: "BTC trimmed mean price by June 30, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMINMON-BTC-26JUN30-5250000"
  question_raw: "Will BTC trimmed mean be below $52500.00 by 11:59 PM ET on Jun 30, 2026?"
  current_price: 0.08
  volume_24h_usd: 637.72
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2026-07-01T03:59:59Z"
bullets:
  - "Kalshi's ladder shows 99% probability BTC trimmed mean stays above $60,000 by June 30, with the distribution implying a range near $62,500-$65,000."
  - "Bitcoin trading near $63,600 is fully consistent with the ladder; the CME-CFTC legal dispute is a regulatory headline that the current price level absorbs without a downside pricing shift."
  - "The year-end ladder (CM-EVT-NHW1YL14S9) shows only 32% probability BTC falls below $40,000 by January 1, 2027, anchoring a broadly constructive medium-term pricing consensus."
  - "Resolves via the Kalshi trimmed mean calculation at 11:59 PM ET on June 30, 2026; the trimmed mean methodology, not spot price, is the settlement metric."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "CME Group announced plans to sue the CFTC over approval of Bitcoin perpetual futures, raising regulatory classification questions under Dodd-Frank, as Bitcoin trades near $63,000-$63,600."
    publisher: "Micah Zimmerman"
    published_at: "2026-06-18T13:50:00.000Z"
    source_url: "https://bitcoinmagazine.com/news/cme-group-to-sue-cftc-over-bitcoin"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Micah Zimmerman"
        source_url: "https://bitcoinmagazine.com/news/cme-group-to-sue-cftc-over-bitcoin"
        retrieved_at: "2026-06-20T10:30:38+00:00"
  - type: "pm_response"
    notes: "Kalshi's near-term ladder confirms Bitcoin's current level is deeply embedded in the distribution; regulatory noise around perpetual futures has not shifted the pricing consensus."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Micah Zimmerman: CME Group To Sue CFTC Over Bitcoin Perpetual Futures Approval In Clash"
    url: "https://bitcoinmagazine.com/news/cme-group-to-sue-cftc-over-bitcoin"
    published_at: "2026-06-18T13:50:00.000Z"
    retrieved_at: "2026-06-20T10:30:38+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
