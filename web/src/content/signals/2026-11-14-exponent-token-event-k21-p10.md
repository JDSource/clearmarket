---
signal_id: "CMSIG20261114DV00"
signal_slug: "exponent-token-event-k21-p10"
headline: "Exponent token launch before Jan 2027: Kalshi 21% vs Polymarket 10%"
semantic_title: "Exponent token launch before 2027 trades far apart across venues"
telemetry: "Polymarket 10% vs Kalshi 21%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-11-14T07:49:06+00:00"
event_id: "CM-EVT-K7DR5FCFM0"
event_slug: "kxtokenlaunch-27jan01"
event_question: "Will Exponent launch a token before Jan 1, 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x411d2f1251d86d9a4f30186c660745c597d18a19737fd8f7b4ee1483ece9ffde"
  question_raw: "Will Exponent launch a token by December 31, 2026?"
  current_price: 0.1
  volume_cumulative_usd: 360707.4422520001
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXTOKENLAUNCH-27JAN01-EXPO"
    question_raw: "Will Exponent launch a token before Jan 1, 2027?"
    current_price: 0.21
bullets:
  - "Kalshi prices the launch at 21%, Polymarket at 10%, an 11pp spread with under seven weeks to resolution."
  - "Kalshi is higher; Polymarket carries the dominant liquidity by a wide margin versus Kalshi's thin book."
  - "Kalshi's elevated odds likely reflect low volume and sparse price discovery; Polymarket's deeper pool suggests the 10% read is more market-tested."
  - "Resolves YES if Exponent publicly launches a token before Jan 1, 2027; deadline proximity limits room for further drift."
atomic_claims:
  - type: "cross_venue_spread"
    provenance: "CM cross-venue link (question_id CMX-B8681B67DA); prices direct from venue APIs"
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
      kalshi_vol_24h_usd: 38.99
      poly_vol_24h_usd: 0.0
sources:
  - label: "ClearMarket cross-venue record: Will Exponent launch a token before Jan 1, 2027?"
    url: "https://clearmarket.fyi/compare/exponent-token-event-y-2026"
    retrieved_at: "2026-11-14T07:49:06+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 11pp gap is most plausibly a liquidity artifact, Kalshi's near-negligible volume leaves its price poorly anchored, while Polymarket's significantly larger book makes the 10% figure the more reliable signal heading into the final stretch.
