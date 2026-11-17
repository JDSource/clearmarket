---
signal_id: "CMSIG20261117VS01"
signal_slug: "will-the-grand-theft-auto-vi-ps5-launch-vol-15648"
headline: "GTA VI $80 launch price: 0% on $15.6K inflow"
semantic_title: "GTA VI PS5 launch at $80 stays a long shot after volume push"
telemetry: "0% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-17T07:48:39+00:00"
event_id: "CM-EVT-CFW07T0JV5"
event_slug: "gta-vi-ps5-launch-price-20260618223907119"
event_question: "Will Grand Theft Auto VI launch on PlayStation 5 at a price of $69.99 or less?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9f6499271639fa06cd6c1d0905e125fa4bdad8e5522ecc5501bd334dfd62cdef"
  question_raw: "Will the Grand Theft Auto VI PS5 launch price be at least $80?"
  current_price: 0.004
  volume_24h_usd: 15648.84
  volume_cumulative_usd: 57815.55074000001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-19T23:59:00Z"
bullets:
  - "Market holds at 0%, traders see no credible path to an $80 or higher PS5 launch price for GTA VI."
  - "27% of all-time volume arrived in 24h, lifting $15.6K into a contract the market treats as resolved against."
  - "Attention may trace to a Rockstar pricing leak, retail pre-order listing, or a confirmed price announcement below $80."
  - "Contract resolves on official Rockstar/Take-Two launch price confirmation for the PS5 version."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 15648.84
sources:
  - label: "ClearMarket market record: Will Grand Theft Auto VI launch on PlayStation 5 at a p"
    url: "https://clearmarket.fyi/events/gta-vi-ps5-launch-price-20260618223907119"
    retrieved_at: "2026-11-17T07:48:39+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume clustering at a zero price suggests a pricing announcement or credible leak has landed, desks should check Rockstar/Take-Two filings or retail pre-order data for the confirming event before any related gaming or media equity positioning.
