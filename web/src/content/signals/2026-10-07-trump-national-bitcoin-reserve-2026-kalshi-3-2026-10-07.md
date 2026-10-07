---
signal_id: "CMSIG2026100708"
signal_slug: "trump-national-bitcoin-reserve-2026-kalshi-3-2026-10-07"
headline: "Trump National Bitcoin Reserve 2026: Kalshi 3%"
semantic_title: "Trump National Bitcoin Reserve in 2026 stays a near-certain long shot"
telemetry: "Kalshi 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-07T00:00:00.000Z"
event_id: "CM-EVT-JQRXSG4ZX9"
event_slug: "kxbtcreserve-27"
event_question: "Will Trump create a National Bitcoin Reserve in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCRESERVE-27-JAN01"
  question_raw: "Will Trump create a National Bitcoin Reserve before Jan 1, 2027?"
  current_price: 0.034
  volume_24h_usd: 3.59
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only 3% that Trump creates a National Bitcoin Reserve in 2026."
  - "The government crypto transfer drew on-chain attention but the market treats it as routine custody, not a policy signal toward a reserve."
  - "Bitcoin was simultaneously falling below $84,000 on oil and geopolitical pressures, adding macro headwinds inconsistent with a reserve announcement."
  - "Resolves via The New York Times reporting confirmation of a formal National Bitcoin Reserve creation in 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US government wallets moved over $103 million in Bitcoin and BNB to Coinbase Prime and an unlabeled address, with no sale confirmed."
    publisher: "Omkar Godbole"
    published_at: "2026-10-07T00:00:00.000Z"
    source_url: "https://www.coindesk.com/markets/2026/10/07/u-s-government-moves-over-usd100-million-in-btc-and-bnb-a-sale-hasn-t-been-confirmed"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Omkar Godbole"
        source_url: "https://www.coindesk.com/markets/2026/10/07/u-s-government-moves-over-usd100-million-in-btc-and-bnb-a-sale-hasn-t-been-confirmed"
        retrieved_at: "2026-10-07T07:47:51+00:00"
  - type: "pm_response"
    notes: "Kalshi at 3%; the market is treating the wallet movement as operationally neutral with no upward pricing pressure on the reserve contract."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Omkar Godbole: U.S. government moves over $100 million in bitcoin (BTC) and BNB."
    url: "https://www.coindesk.com/markets/2026/10/07/u-s-government-moves-over-usd100-million-in-btc-and-bnb-a-sale-hasn-t-been-confirmed"
    published_at: "2026-10-07T00:00:00.000Z"
    retrieved_at: "2026-10-07T07:47:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
