---
signal_id: "CMSIGDEMO00008"
signal_slug: "demo-iran-ceasefire-cross-venue"
headline: "Iran–Israel May ceasefire: Polymarket 28%, Kalshi 14% — 14pp persistent spread"
category_tag: "CROSS_VENUE_DIVERGENCE"
secondary_tags: ["COVERAGE_GAP"]
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-05-09T08:15:00-04:00"
event_id: "CMIRILCEASEM"
event_slug: "iran-israel-ceasefire-may-2026"
event_question: "Will Iran and Israel agree to a ceasefire by May 31, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xirilcease2026"
  question_raw: "Iran-Israel ceasefire by May 31, 2026"
  current_price: 0.28
  price_24h_ago: 0.31
  volume_24h_usd: 2100000
  volume_7d_usd: 8400000
  volume_cumulative_usd: 22800000
  arbitration_model: "uma_oracle"
  resolution_source: "Credible news reporting"
  resolves_at: "2026-05-31T23:59:59Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIRIL-26MAY-CEASE"
    question_raw: "Iran-Israel ceasefire by May 31, 2026"
bullets:
  - "Polymarket YES trades at 28.0% on $22.8M cumulative volume; Kalshi parallel contract at 14.0% on $4.1M — persistent 14.0pp spread over 7 days"
  - "Spread has not narrowed despite identical resolution language and overlapping news flow — suggests structural pricing-population divergence, not information asymmetry"
  - "Polymarket order flow international, USDC-denominated, includes Middle East and EU IPs; Kalshi US-onshore, USD, accessed via IBKR and Wealthsimple under CIRO authorization"
  - "Resolution mechanism differs: Polymarket UMA oracle, 'credible news consensus'; Kalshi staff resolution with named sources. Polymarket has historically resolved Mideast ceasefire contracts more leniently than Kalshi"
  - "Resolves May 31. Watch joint statements from Qatar/Oman mediators; resolution-source divergence is the primary risk on either venue"
sources:
  - label: "Polymarket — Iran-Israel ceasefire by May 31, 2026"
    url: "https://polymarket.com/market/0xirilcease2026"
    retrieved_at: "2026-05-09T08:15:00-04:00"
  - label: "Kalshi — Iran-Israel ceasefire by May 31, 2026"
    url: "https://kalshi.com/markets/KXIRIL-26MAY-CEASE"
    retrieved_at: "2026-05-09T08:15:00-04:00"
field_provenance:
  pm_data: "polymarket_clob_api, kalshi_api"
  news_context: "perplexity_grounded"
  editorial_judgment: "llm_judge_cm_signal_v1"
---

A persistent cross-venue divergence on a high-volume geopolitical event. The 14pp spread reflects pricing-population differences (international vs US-onshore) and resolution-mechanism differences (UMA news-consensus vs Kalshi staff with named sources) rather than information asymmetry.
