---
signal_id: "CMSIG2026092508"
signal_slug: "eth-above-3500-by-jan-1-2027-polymarket-34-volume-up-104x-2026-09-25"
headline: "ETH above $3500 by Jan 1, 2027: Polymarket 34%, volume up 104x"
semantic_title: "Ethereum above $3500 by year-end holds below 35% odds"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-25T13:29:38.845Z"
event_id: "CM-EVT-G2G3Y09R59"
event_slug: "kxethmaxy-27jan01"
event_question: "Ethereum price by January 1, 2027"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXETHMAXY-27JAN01-3500.00"
  question_raw: "Will Ethereum reach above $3500.00 by Jan 1, 2027 at 12:00AM?"
  current_price: 0.34
  volume_24h_usd: 1410.79
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T05:00:00Z"
bullets:
  - "Polymarket ladder puts 34% on Ethereum exceeding $3500 by January 1, 2027, falling to 8% at $5000 and 6% at $6000, with trading volume up 104x day-over-day."
  - "Bitcoin's rally above $84,000 and record ETF inflows are drawing fresh attention to the ETH contract, as evidenced by the massive volume spike, but the market is not pricing a breakout."
  - "The ladder's sharp drop from 34% at $3500 to 19% at $4000 shows the market sees the $3500-$4000 range as the realistic ceiling rather than a launchpad."
  - "Resolves via UMA oracle; the contract measures Ethereum's spot price at a specific timestamp on January 1, 2027, intraday volatility on that date is the key settlement edge case."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "BlackRock's prediction for crypto is cited as coming true as Bitcoin steadies above $84,000 and crypto ETFs draw billions in inflows."
    publisher: "Billy Bambrough"
    published_at: "2026-09-25T13:29:38.845Z"
    source_url: "https://www.forbes.com/sites/digital-assets/2026/09/24/blackrock-issues-extraordinary-crypto-prediction-as-the-bitcoin-price-suddenly-soars/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Billy Bambrough"
        source_url: "https://www.forbes.com/sites/digital-assets/2026/09/24/blackrock-issues-extraordinary-crypto-prediction-as-the-bitcoin-price-suddenly-soars/"
        retrieved_at: "2026-09-27T13:30:43+00:00"
  - type: "pm_response"
    notes: "Polymarket's ETH ladder at 104x volume is the clearest sign that crypto's equity-market rally is pulling fresh prediction-market activity, even as the probability distribution stays cautious."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Billy Bambrough: BlackRock’s ‘Extraordinary’ Prediction For Crypto Is Suddenly Coming T"
    url: "https://www.forbes.com/sites/digital-assets/2026/09/24/blackrock-issues-extraordinary-crypto-prediction-as-the-bitcoin-price-suddenly-soars/"
    published_at: "2026-09-25T13:29:38.845Z"
    retrieved_at: "2026-09-27T13:30:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
