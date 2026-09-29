---
signal_id: "CMSIG2026092807"
signal_slug: "bitcoin-outperforms-gold-and-s-p-500-in-2026-polymarket-27-2026-09-28"
headline: "Bitcoin outperforms gold and S&P 500 in 2026: Polymarket 27%"
semantic_title: "Bitcoin outperforming gold and the S&P 500 in 2026 stays a long shot"
telemetry: "Polymarket 27%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-28T00:00:00.000Z"
event_id: "CM-EVT-3HDQG11JV0"
event_slug: "bitcoin-vs-gold-vs-sp-500-in-2026"
event_question: "Will Bitcoin outperform Gold and the S&P 500 in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xb276435811dc77171602f790db2b5900e780adfadb7cff57e547d58fb1a8215f"
  question_raw: "Will Bitcoin have the best performance in 2026?"
  current_price: 0.27
  volume_24h_usd: 277.54889099999997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Bitcoin outperforming both gold and the S&P 500 in 2026 sits at 27%."
  - "Goldman Sachs's institutional crypto integration is a bullish adoption signal, yet the Polymarket contract remains well below 50%, reflecting Bitcoin's relative underperformance amid elevated Treasury yields."
  - "Bitcoin is currently trading near $83,000-$84,000 while the 10-year yield hit 5.22%, a headwind for risk assets that the market appears to be pricing."
  - "Resolves via Polymarket's UMA oracle comparing Bitcoin's 2026 full-year return against documented gold and S&P 500 returns."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Goldman Sachs is bringing its roughly $100 billion Treasury fund into institutional crypto infrastructure without creating a tokenized version, marking a major adoption milestone."
    publisher: "coindesk.com"
    published_at: "2026-09-28T00:00:00.000Z"
    source_url: "https://www.coindesk.com/markets/2026/09/28/goldman-sachs-brings-usd100-billion-treasury-fund-into-crypto-s-institutional-plumbing"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "coindesk.com"
        source_url: "https://www.coindesk.com/markets/2026/09/28/goldman-sachs-brings-usd100-billion-treasury-fund-into-crypto-s-institutional-plumbing"
        retrieved_at: "2026-09-29T14:34:30+00:00"
  - type: "pm_response"
    notes: "Polymarket contract on Bitcoin outperforming gold and S&P 500 in 2026; 27% pricing shows institutional adoption news has not shifted the macro-driven consensus."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "coindesk.com: Goldman Sachs brings $100 billion Treasury fund into crypto’s institut"
    url: "https://www.coindesk.com/markets/2026/09/28/goldman-sachs-brings-usd100-billion-treasury-fund-into-crypto-s-institutional-plumbing"
    published_at: "2026-09-28T00:00:00.000Z"
    retrieved_at: "2026-09-29T14:34:30+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
