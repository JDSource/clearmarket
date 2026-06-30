---
signal_id: "CMSIG20260630DV02"
signal_slug: "applied-intuition-ipo-k11-p18"
headline: "Applied Intuition IPO before 2027: Kalshi 11% vs Polymarket 18%"
semantic_title: "Applied Intuition IPO spread isolates across prediction venues"
telemetry: "Polymarket 18% vs Kalshi 11%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-06-30T10:55:41+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Applied Intuition IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x76d92e422d9a4c1d9ceeea7445fa709df9df03e45b6372623abec7254caee3a9"
  question_raw: "Applied Intuition IPO before 2027?"
  current_price: 0.185
  volume_cumulative_usd: 205292.0835039999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-AINTUITION"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.11
bullets:
  - "Polymarket at 18% vs Kalshi at 11%, an 8pp gap on the pre-2027 IPO claim."
  - "Polymarket carries the higher price and nearly one hundred times Kalshi's cumulative volume."
  - "Extremely low Kalshi liquidity makes the 11% quote unreliable; Polymarket's market is far better populated."
  - "Resolution requires Applied Intuition to complete a public listing before Jan 1 2027."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-52E2DEB126); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 2.75
      poly_vol_24h_usd: 27.66
sources:
  - label: "ClearMarket cross-venue record: Applied Intuition IPO before 2027?"
    url: "https://clearmarket.fyi/compare/applied-intuition-ipo-y-2026"
    retrieved_at: "2026-06-30T10:55:41+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Applied Intuition's Kalshi contract is essentially illiquid, making the 8pp discount versus Polymarket more a function of venue neglect than genuine probability disagreement, any desk view should anchor to Polymarket's 18%.
