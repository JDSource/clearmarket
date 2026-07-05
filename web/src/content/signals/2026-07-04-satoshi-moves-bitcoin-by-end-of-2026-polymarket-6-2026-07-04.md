---
signal_id: "CMSIG2026070407"
signal_slug: "satoshi-moves-bitcoin-by-end-of-2026-polymarket-6-2026-07-04"
headline: "Satoshi moves Bitcoin by end of 2026: Polymarket 6%"
semantic_title: "Satoshi Bitcoin movement by year-end consensus holds deeply skeptical"
telemetry: "Polymarket 6%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-04T18:00:00.000Z"
event_id: "CM-EVT-3030994QH5"
event_slug: "will-satoshi-move-any-bitcoin-in-2026"
event_question: "Will Satoshi move any Bitcoin by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x3b0107a80edd066fe987784d7ab5963c177888433efbec10689951c17320606c"
  question_raw: "Will Satoshi move any Bitcoin in 2026?"
  current_price: 0.06
  volume_24h_usd: 17731.994784
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "Polymarket prices only a 6% probability that Satoshi moves any Bitcoin by end of 2026, resolved via UMA oracle."
  - "The quantum freeze debate draws fresh attention to dormant Satoshi coins, but the market treats voluntary movement by Satoshi as a very low-probability event regardless of the external threat."
  - "A companion Kalshi contract (CM-EVT-77NC57P468) puts only 5% on Satoshi moving any Bitcoin by 2027, showing near-identical skepticism across venues and a slightly longer horizon."
  - "The near-zero pricing across both venues implies the market is not pricing in the quantum threat as a trigger for Satoshi action, the proposal itself is the news, not evidence of movement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Binance founder Changpeng Zhao proposed freezing Satoshi Nakamoto's 1.1 million Bitcoin before quantum computers can compromise them, sparking fierce industry debate."
    publisher: "coindesk.com"
    published_at: "2026-07-04T18:00:00.000Z"
    source_url: "https://www.coindesk.com/business/2026/07/04/bitcoin-experts-split-over-plan-to-freeze-satoshi-s-1-1-million-bitcoin-as-quantum-threat-grows"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "coindesk.com"
        source_url: "https://www.coindesk.com/business/2026/07/04/bitcoin-experts-split-over-plan-to-freeze-satoshi-s-1-1-million-bitcoin-as-quantum-threat-grows"
        retrieved_at: "2026-07-05T10:07:52+00:00"
  - type: "pm_response"
    notes: "Polymarket binary contract resolving via UMA oracle; cross-venue agreement at 5-6% makes this one of the most consensus-bound outcomes in the crypto prediction market landscape."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "coindesk.com: A plan to freeze the creator's Bitcoin sparks fierce debate over crypt"
    url: "https://www.coindesk.com/business/2026/07/04/bitcoin-experts-split-over-plan-to-freeze-satoshi-s-1-1-million-bitcoin-as-quantum-threat-grows"
    published_at: "2026-07-04T18:00:00.000Z"
    retrieved_at: "2026-07-05T10:07:52+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
