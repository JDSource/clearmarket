---
signal_id: "CMSIG2026101008"
signal_slug: "record-crypto-liquidation-in-2026-polymarket-8-2026-10-10"
headline: "Record crypto liquidation in 2026: Polymarket 8%"
semantic_title: "Record crypto liquidation event in 2026 stays under 10% on Polymarket"
telemetry: "Polymarket 8%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-10T00:00:00.000Z"
event_id: "CM-EVT-V55KP87122"
event_slug: "record-crypto-liquidation-in-2026"
event_question: "Will there be a record crypto liquidation in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x8aea4707af4ca2b029db4143bb020f0c8bf95d2c0d088186009471fb588f2f4a"
  question_raw: "Record crypto liquidation in 2026?"
  current_price: 0.08
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "Polymarket prices only an 8% chance of a record crypto liquidation event in 2026, despite the multi-billion-dollar long flush reported this week."
  - "The current liquidation wave is large but the market is not pricing it as a record-breaking event; Polymarket is not treating this week's action as disqualifying or qualifying at 8%."
  - "Bitcoin rebounded toward 82,800 dollars after the sell-off, with resistance near 84,400 dollars; the partial recovery tempers the case for a historic capitulation read."
  - "Resolution via UMA oracle on Polymarket; the precise definition of what constitutes a record liquidation event is the key settlement edge case."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Over 1 billion dollars in long positions were liquidated as Bitcoin tested 81,000 dollar support, with ETF redemptions and forced derivatives liquidations removing spot demand."
    publisher: "Silke Schütters"
    published_at: "2026-10-10T00:00:00.000Z"
    source_url: "https://cryptoticker.io/en/us-government-bitcoin-coinbase-prime/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Silke Schütters"
        source_url: "https://cryptoticker.io/en/us-government-bitcoin-coinbase-prime/"
        retrieved_at: "2026-10-10T14:11:44+00:00"
  - type: "pm_response"
    notes: "Polymarket resolves via UMA oracle; at 8% the contract signals the market does not view this week's liquidations as a record-setting threshold event."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Silke Schütters: 17,733 Bitcoin From US Wallets at Coinbase Prime"
    url: "https://cryptoticker.io/en/us-government-bitcoin-coinbase-prime/"
    published_at: "2026-10-10T00:00:00.000Z"
    retrieved_at: "2026-10-10T14:11:44+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
