---
signal_id: "CMSIG20261007DV01"
signal_slug: "discord-ipo-k12-p4"
headline: "Discord IPO before 2027: Kalshi 12% vs Polymarket 5%"
semantic_title: "Discord IPO odds carry a premium on the smaller desk"
telemetry: "Polymarket 5% vs Kalshi 12%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-07T07:49:04+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Discord IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x48fcbf6bb8eceff817ba48b56211e4f8a4cf6896570d847d8d115e63c3abf36a"
  question_raw: "Discord IPO before 2027?"
  current_price: 0.048
  volume_cumulative_usd: 487506.1268200002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DISCORD"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.12
bullets:
  - "Kalshi prices a Discord IPO before 2027 at 12%, Polymarket at 5%, a 7pp spread with the horizon closing in under three months."
  - "Kalshi is the higher venue; cumulative volume stands at $15,979 versus Polymarket's $487,506."
  - "Polymarket's price likely reflects stronger consensus given 30x the liquidity, while Kalshi's 12% may reflect limited arbitrage correcting the thin book."
  - "Resolves YES only on a confirmed public IPO, SPAC, direct listing, or private placement would require careful review of contract terms."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-26DA00133D); prices direct from venue APIs"
    field_provenance:
      kalshi_price:
        tier: "direct"
        method: "kalshi_api"
      poly_price:
        tier: "direct"
        method: "polymarket_clob_api"
      divergence_pp:
        tier: "derived"
        method: "arithmetic"
        inputs: ["kalshi_price", "poly_price"]
    liquidity_context:
      kalshi_vol_24h_usd: 135.49
      poly_vol_24h_usd: 268.54999999999995
sources:
  - label: "ClearMarket cross-venue record: Discord IPO before 2027?"
    url: "https://clearmarket.fyi/compare/discord-ipo-y-2026"
    retrieved_at: "2026-10-07T07:49:04+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 7pp gap with a hard year-end deadline and 30x volume disparity points to Polymarket's 5% as the more reliable estimate, and the spread represents a structural inefficiency in Kalshi's shallow market rather than genuine informational disagreement.
