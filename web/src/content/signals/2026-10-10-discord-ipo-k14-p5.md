---
signal_id: "CMSIG20261010DV01"
signal_slug: "discord-ipo-k14-p5"
headline: "Discord IPO before 2027: Kalshi 14% vs Polymarket 6%"
semantic_title: "Discord IPO pricing builds a wide gap across the major desks"
telemetry: "Polymarket 6% vs Kalshi 14%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-10-10T14:13:22+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Discord IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x48fcbf6bb8eceff817ba48b56211e4f8a4cf6896570d847d8d115e63c3abf36a"
  question_raw: "Discord IPO before 2027?"
  current_price: 0.058
  volume_cumulative_usd: 489522.268499
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-DISCORD"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.14
bullets:
  - "Kalshi prices a Discord IPO before 2027 at 14%, Polymarket at 6%, an 8pp spread on the same claim."
  - "Kalshi is higher at 14% on $19K cumulative volume; Polymarket holds 6% on $490K volume."
  - "Polymarket's dominant liquidity makes its 6% the consensus anchor; Kalshi's 14% likely overstates the probability given its shallow order depth."
  - "Resolves YES if Discord completes a public market listing before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 0.0
      poly_vol_24h_usd: 546.892653
sources:
  - label: "ClearMarket cross-venue record: Discord IPO before 2027?"
    url: "https://clearmarket.fyi/compare/discord-ipo-y-2026"
    retrieved_at: "2026-10-10T14:13:22+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With Polymarket carrying roughly 26 times Kalshi's traded volume, the 8pp gap is best read as Kalshi mispricing a low-probability event, a desk should treat Polymarket's 6% as the credible baseline and view Kalshi as a potential arb venue if contracts are liquid enough to execute.
