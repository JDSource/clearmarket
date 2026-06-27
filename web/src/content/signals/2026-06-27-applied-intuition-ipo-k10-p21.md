---
signal_id: "CMSIG20260627DV01"
signal_slug: "applied-intuition-ipo-k10-p21"
headline: "Applied Intuition IPO before 2027: Kalshi 10% vs Polymarket 22%"
semantic_title: "Applied Intuition IPO timeline decouples on the major prediction desks"
telemetry: "Polymarket 22% vs Kalshi 10%"
category_tag: "CROSS_VENUE_DIVERGENCE"
detection_path: "cross_venue_divergence"
pre_news_classification: "concurrent"
published_at: "2026-06-27T10:03:41+00:00"
event_id: "CM-EVT-858NYLKF97"
event_slug: "kxipo-26"
event_question: "Applied Intuition IPO before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x76d92e422d9a4c1d9ceeea7445fa709df9df03e45b6372623abec7254caee3a9"
  question_raw: "Applied Intuition IPO before 2027?"
  current_price: 0.218
  volume_cumulative_usd: 204947.5835039999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
related_markets:
  - platform: "kalshi"
    platform_market_id: "KXIPO-26-AINTUITION"
    question_raw: "Who will IPO before 2027?"
    current_price: 0.1
bullets:
  - "Polymarket marks the IPO at 22%, Kalshi at 10%, a 12pp spread on an end-of-year horizon."
  - "Polymarket carries the higher price and vastly deeper liquidity; Kalshi's book is lightly traded."
  - "Thin Kalshi volume makes its 10% print less reliable as a consensus signal; Polymarket's larger crowd may better aggregate private-market intelligence on the company's readiness."
  - "Resolution typically ties to an effective S-1 filing or first day of public trading before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 0.0
      poly_vol_24h_usd: 1079.548393
sources:
  - label: "ClearMarket cross-venue record: Applied Intuition IPO before 2027?"
    url: "https://clearmarket.fyi/compare/applied-intuition-ipo-y-2026"
    retrieved_at: "2026-06-27T10:03:41+00:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 12pp gap alongside a 100-to-1 volume disparity means Kalshi's price is likely noise from a shallow book, and desks should weight Polymarket's 22% as the more informed estimate while monitoring for filing signals.
