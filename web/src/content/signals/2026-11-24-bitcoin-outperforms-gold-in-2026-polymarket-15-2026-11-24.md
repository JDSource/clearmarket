---
signal_id: "CMSIG2026112407"
signal_slug: "bitcoin-outperforms-gold-in-2026-polymarket-15-2026-11-24"
headline: "Bitcoin outperforms Gold in 2026: Polymarket 15%"
semantic_title: "Bitcoin outperforming Gold in 2026 stays below 25 percent"
telemetry: "Polymarket 15%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-24T02:21:14.000Z"
event_id: "CM-EVT-TKKW1QZRK9"
event_slug: "will-bitcoin-outperform-gold-in-2026"
event_question: "Will Bitcoin outperform Gold in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xdcae9573d5680a2c958cca4676ed28df7a06861572124f3396cc60ab6b92b9c2"
  question_raw: "Will Bitcoin outperform Gold in 2026?"
  current_price: 0.15
  volume_24h_usd: 273.32039299999997
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "Polymarket prices 15% on Bitcoin outperforming Gold in 2026, resolving via UMA oracle, keeping the claim well under 25% odds."
  - "Bitcoin's inability to sustain a rally on a major positive risk catalyst, the Nasdaq up 6% on Huang's return, is consistent with the low outperformance odds the market assigns."
  - "The companion Polymarket contract on Bitcoin outperforming both Gold and the S&P 500 (CM-EVT-3HDQG11JV0) prices only 3%, a wider gap that reflects the equity benchmark's additional hurdle."
  - "Resolves via UMA oracle at year-end 2026 on total return comparison; the current ~$60,000 Bitcoin price and the Fed's hawkish posture are the two headwinds most visible in the pricing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Bitcoin failed to hold gains from Jensen Huang's Nvidia reinstatement rally even as the Nasdaq soared 6%, with rate and regulatory jitters weighing on crypto."
    publisher: "Matthew Brockett"
    published_at: "2026-11-24T02:21:14.000Z"
    source_url: "https://www.bloomberg.com/news/articles/2026-11-24/bitcoin-fails-to-hold-nvidia-bump-with-crypto-headwinds-in-focus"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Matthew Brockett"
        source_url: "https://www.bloomberg.com/news/articles/2026-11-24/bitcoin-fails-to-hold-nvidia-bump-with-crypto-headwinds-in-focus"
        retrieved_at: "2026-11-24T07:47:50+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; the 12-percentage-point gap between the Gold-only (15%) and the combined Gold-plus-S&P (3%) contract quantifies how much of the drag is attributed to equities versus crypto-specific headwinds."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Matthew Brockett: Bitcoin Fails to Hold Nvidia Bump With Crypto Headwinds in Focus"
    url: "https://www.bloomberg.com/news/articles/2026-11-24/bitcoin-fails-to-hold-nvidia-bump-with-crypto-headwinds-in-focus"
    published_at: "2026-11-24T02:21:14.000Z"
    retrieved_at: "2026-11-24T07:47:50+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
