---
signal_id: "CMSIGDEMO00007"
signal_slug: "demo-ceo-resign-pre-news"
headline: "Citi CEO Fraser resign 2026: Polymarket 22%, +13.5pp on flow with no public catalyst"
category_tag: "PRE_NEWS_PRICING"
secondary_tags: ["VOLUME_SPIKE"]
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-05-09T16:55:00-04:00"
event_id: "CMCITICEOEOY"
event_slug: "citigroup-ceo-resign-2026"
event_question: "Will Citigroup CEO Jane Fraser resign by December 31, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xciticeo2026"
  question_raw: "Citigroup CEO Jane Fraser resigns by Dec 31, 2026"
  current_price: 0.22
  price_24h_ago: 0.085
  volume_24h_usd: 380000
  volume_7d_usd: 510000
  volume_cumulative_usd: 720000
  arbitration_model: "uma_oracle"
  resolution_source: "Citigroup 8-K filing or official press release"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets: []
bullets:
  - "Polymarket 'Citigroup CEO Jane Fraser resigns by Dec 31, 2026' YES trades at 22.0%, up from 8.5% over 24 hours on $380K volume"
  - "Volume 4.7× the trailing 7-day daily baseline; price move dominantly buy-side flow (12 wallets responsible for 78% of YES purchases)"
  - "No public catalyst identified: no FT, WSJ, Bloomberg, or Reuters reporting; no SEC 8-K filed; no Citigroup press release. Perplexity scan shows zero matching news May 4-9"
  - "Pattern matches Pre-News window: informed flow ahead of public disclosure. Two prior Polymarket CEO-resignation contracts in 2025 (Boeing, BP) moved similarly 3-7 days before announcement"
  - "Watch for: Citigroup 8-K filing, surprise earnings call announcement, board governance leak. Resolves Dec 31; tracking window suggests catalyst within 2-3 weeks if pattern holds"
sources:
  - label: "Polymarket order flow (CLOB)"
    url: "https://polymarket.com"
    retrieved_at: "2026-05-09T16:50:00-04:00"
field_provenance:
  pm_data: "polymarket_clob_api"
  news_context: "perplexity_grounded_negative_scan"
  editorial_judgment: "llm_judge_cm_signal_v1"
---

Pre-News pattern — large directional flow with no identifiable public catalyst. Two historical 2025 analogs (Boeing, BP) preceded actual announcements by 3-7 days. Flag for monitoring, not as actionable conviction.
