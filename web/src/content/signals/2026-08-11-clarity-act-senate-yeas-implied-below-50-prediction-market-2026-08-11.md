---
signal_id: "CMSIG2026081106"
signal_slug: "clarity-act-senate-yeas-implied-below-50-prediction-market-2026-08-11"
headline: "Clarity Act Senate yeas implied below 50: prediction market"
semantic_title: "Clarity Act Senate yea vote count stays below 50 seats"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-11T12:06:42.685Z"
event_id: "CM-EVT-CSYS5KPXK6"
event_slug: "kxvoteclarity-26may16"
event_question: "Senate yea votes on crypto market structure bill"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXVOTECLARITY-26MAY16-T50"
  question_raw: "How many Senate members will vote Yea on a crypto market structure bill (as defined in KXCRYPTOSTRUCTURE)?"
  current_price: 0.42
  volume_24h_usd: 9.24
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The prediction market ladder implies fewer than 50 Senate yea votes on the CLARITY Act, with the 50-vote rung at only 42% and all higher rungs well below that."
  - "Thune setting a September 15 procedural vote is a meaningful step forward, but the market prices the bill falling short of a filibuster-proof majority."
  - "The 42% at 50 votes and 34% at 55 votes suggests real doubt about reaching 60 votes needed to advance, consistent with ongoing bipartisan friction."
  - "Resolves based on the official Senate vote tally; the procedural cloture vote on September 15 may itself serve as an early resolution trigger."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Senate Majority Leader John Thune scheduled a procedural vote on the CLARITY Act for September 15, marking the bill's first formal Senate action."
    publisher: "TradingKey"
    published_at: "2026-08-11T12:06:42.685Z"
    source_url: "https://www.tradingkey.com/analysis/cryptocurrencies/btc/262095914-crypto-clarity-act-coinbase-bitcoin-btc-strategy-mstr-sec-cftc-tradingkey"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "TradingKey"
        source_url: "https://www.tradingkey.com/analysis/cryptocurrencies/btc/262095914-crypto-clarity-act-coinbase-bitcoin-btc-strategy-mstr-sec-cftc-tradingkey"
        retrieved_at: "2026-08-12T09:07:43+00:00"
  - type: "pm_response"
    notes: "This ladder carries priced data; the distribution is centered below the 50-vote threshold, suggesting passage is not the market's base case."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "TradingKey: Clarity Act Sees Major Breakthrough as Senate Sets First Procedural Vo"
    url: "https://www.tradingkey.com/analysis/cryptocurrencies/btc/262095914-crypto-clarity-act-coinbase-bitcoin-btc-strategy-mstr-sec-cftc-tradingkey"
    published_at: "2026-08-11T12:06:42.685Z"
    retrieved_at: "2026-08-12T09:07:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
