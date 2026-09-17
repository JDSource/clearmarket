---
signal_id: "CMSIG20260917DV02"
signal_slug: "us-economy-soft-landing-k32-p23"
headline: "US economy in recession end-2026: Kalshi 32% vs Polymarket 23%"
semantic_title: "Economy-in-recession odds carry a premium on one major desk"
telemetry: "Polymarket 23% vs Kalshi 32%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-09-17T13:06:01+00:00"
event_id: "CM-EVT-ZRG5DFDMZ8"
event_slug: "kxeconpath-26"
event_question: "State of the economy at the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x50e3ee8f93a464d04ea2cea6efff45c902f43642aedbf43f7afdc899e10f71d8"
  question_raw: "Will the US economy be in a soft landing at the end of 2026?"
  current_price: 0.23
  volume_cumulative_usd: 40485.110639000006
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXECONPATH-26-SOFT"
    question_raw: "State of the economy at the end of 2026?"
    current_price: 0.32
bullets:
  - "Kalshi prices recession by end-2026 at 32%, Polymarket at 23%, a 9pp gap on an identical horizon."
  - "Kalshi is the higher venue; Polymarket's book is roughly five times deeper by cumulative volume."
  - "Resolution ambiguity is the likely driver, 'state of the economy' lacks a crisp trigger, and thinner venues tend to price softer definitions more generously."
  - "Resolution likely depends on an official NBER declaration or a Kalshi-specified GDP/definition threshold by Dec 31, 2026."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-534611296D); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 125.51
      poly_vol_24h_usd: 768.723551
sources:
  - label: "ClearMarket cross-venue record: State of the economy at the end of 2026?"
    url: "https://clearmarket.fyi/compare/us-economy-soft-landing-y-2026"
    retrieved_at: "2026-09-17T13:06:01+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 9pp spread on a macro claim with a fuzzy resolution criterion is a red flag for desks, divergent contract wording across venues, not genuine disagreement on fundamentals, is the probable source of the gap.
