---
signal_id: "CMSIG2026100808"
signal_slug: "satoshi-identity-revealed-by-2026-polymarket-99-2026-10-08"
headline: "Satoshi identity revealed by 2026: Polymarket 99%"
semantic_title: "Satoshi identity revealed by 2026 nears full pricing"
telemetry: "Polymarket 99%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-08T00:00:00.000Z"
event_id: "CM-EVT-24JSNTN2D5"
event_slug: "nothing-ever-happens-satoshi-nakamoto"
event_question: "Will Satoshi Nakamoto's identity be publicly revealed by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb00e791c299299858a0e333a31b841f51038e6f14321f25eba03c41a5b6f58f7"
  question_raw: "Nothing Ever Happens: Satoshi Nakamoto"
  current_price: 0.99
  volume_24h_usd: 2.0201000000000002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 99% chance Satoshi Nakamoto's identity will be publicly revealed by 2026, with trading volume up over 10,000% day-over-day, a 102.7x surge."
  - "The AI cryptographic security warning story appears to have catalyzed fresh attention on this contract, driving the extreme volume spike even as the price itself is already near ceiling."
  - "A companion Kalshi contract (CM-EVT-77NC57P468) prices only a 3% chance Satoshi moves any Bitcoin by 2027, suggesting the market separates identity revelation from on-chain action."
  - "Resolves via UMA oracle; the contract likely requires a credible, broadly accepted public identification, not an unverified claim."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Ethereum researchers warned that AI could break the cryptographic signatures guarding bitcoin and ether wallets in months rather than years, stirring debate across the crypto community."
    publisher: "Shaurya Malwa"
    published_at: "2026-10-08T00:00:00.000Z"
    source_url: "https://www.coindesk.com/tech/2026/10/08/bitcoin-and-ether-holders-urged-to-prepare-bunker-mode-against-possible-ai-attacks"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Shaurya Malwa"
        source_url: "https://www.coindesk.com/tech/2026/10/08/bitcoin-and-ether-holders-urged-to-prepare-bunker-mode-against-possible-ai-attacks"
        retrieved_at: "2026-10-08T15:10:10+00:00"
  - type: "pm_response"
    notes: "Polymarket's 99% with a 102.7x volume surge signals extreme same-day activity, likely tied to the AI-breaks-crypto narrative prompting traders to revisit Satoshi-related contracts."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Shaurya Malwa: Bitcoin and ether holders urged to prepare ‘bunker mode’ against possi"
    url: "https://www.coindesk.com/tech/2026/10/08/bitcoin-and-ether-holders-urged-to-prepare-bunker-mode-against-possible-ai-attacks"
    published_at: "2026-10-08T00:00:00.000Z"
    retrieved_at: "2026-10-08T15:10:10+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
