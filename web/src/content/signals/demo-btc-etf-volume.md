---
signal_id: "CMSIGDEMO00006"
signal_slug: "demo-btc-etf-volume"
headline: "BlackRock ETH ETF Q2 approval: Kalshi 58%, +14pp on SEC staking-objection reversal"
category_tag: "MOMENTUM_REPRICING"
secondary_tags: ["VOLUME_SPIKE"]
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-05-10T11:05:00-04:00"
event_id: "CMETHETF26Q2"
event_slug: "blackrock-eth-spot-etf-q2-approval"
event_question: "Will BlackRock's spot Ethereum ETF receive SEC approval in Q2 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXETHETF-26Q2-APR"
  question_raw: "BlackRock spot ETH ETF approved by SEC by June 30, 2026"
  current_price: 0.58
  price_24h_ago: 0.44
  volume_24h_usd: 720000
  volume_7d_usd: 1940000
  volume_cumulative_usd: 4280000
  arbitration_model: "kalshi_staff"
  resolution_source: "SEC EDGAR filings"
  resolves_at: "2026-06-30T23:59:59Z"
related_markets:
  - platform: "polymarket"
    platform_market_id: "0xethetf26q2"
    question_raw: "BlackRock spot ETH ETF approved by SEC by June 30, 2026"
bullets:
  - "Kalshi 'BlackRock spot ETH ETF SEC approval by June 30, 2026' YES trades at 58.0%, up from 44.0% in 24 hours on $720K volume"
  - "Repricing tracks Reuters scoop May 10: SEC staff reportedly removed staking-feature objection from final review; Bloomberg confirms via separate sourcing"
  - "Polymarket parallel contract at 61.0% — modest 3pp cross-venue spread; cross-venue convergence supports the news read"
  - "Cumulative $4.28M makes this Kalshi's largest active crypto-regulatory contract; volume +320% on the news cycle"
  - "Resolves June 30 on SEC filing. Reversal triggers: SEC staff comment-letter requesting structural amendment, BlackRock S-1 withdrawal"
sources:
  - label: "Reuters SEC ETH ETF May 10 scoop"
    url: "https://www.reuters.com"
    retrieved_at: "2026-05-10T10:30:00-04:00"
  - label: "Bloomberg confirmation reporting"
    url: "https://www.bloomberg.com"
    retrieved_at: "2026-05-10T11:00:00-04:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  news_context: "perplexity_grounded"
  editorial_judgment: "llm_judge_cm_signal_v1"
---

Repricing event with cross-venue confirmation. Both Kalshi and Polymarket moved in tandem on the same news cycle, with the cross-venue spread compressing rather than widening — signal quality higher than single-venue repricings.
