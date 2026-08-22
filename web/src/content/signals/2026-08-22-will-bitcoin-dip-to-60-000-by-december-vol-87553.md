---
signal_id: "CMSIG20260822VS02"
signal_slug: "will-bitcoin-dip-to-60-000-by-december-vol-87553"
headline: "BTC dip to $60K by Dec 31: 36% on $88K"
semantic_title: "Fresh volume returns to the BTC $60K dip-by-year-end bet"
telemetry: "36% · $88K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-22T08:24:03+00:00"
event_id: "CM-EVT-2S263KKBP2"
event_slug: "what-price-will-bitcoin-hit-before-2027"
event_question: "What price will Bitcoin reach by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6c8bc8cd9b2d64358ad995ccee8e998cf0f81a89c4be0b8e51eadf09c6be60ba"
  question_raw: "Will Bitcoin dip to $60,000 by December 31, 2026?"
  current_price: 0.36
  volume_24h_usd: 87553.873032
  volume_cumulative_usd: 245996.577195
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "Polymarket prices 36%, meaningful downside risk priced but not the base case."
  - "24h volume $88K is 36% of all-time, a notable single-day share for a multi-month contract."
  - "Renewed attention to downside tail hedges amid concurrent heavy BTC month-end trading."
  - "Resolves December 31, 2026."
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
      poly_vol_24h_usd: 87553.873032
sources:
  - label: "ClearMarket market record: What price will Bitcoin reach by the end of 2026?"
    url: "https://clearmarket.fyi/events/what-price-will-bitcoin-hit-before-2027"
    retrieved_at: "2026-08-22T08:24:03+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous volume spikes across BTC upside and downside contracts indicate a two-sided hedging environment, desks should assess whether this reflects spread trades or independent directional flow.
