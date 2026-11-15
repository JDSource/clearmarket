---
signal_id: "CMSIG20261115VS00"
signal_slug: "will-gold-gc-dip-to-low-3-000-by-en-vol-64489"
headline: "Gold $3K dip: 3% on $64K surge"
semantic_title: "Gold $3K floor stays a long shot through December"
telemetry: "3% · $64K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-15T07:48:41+00:00"
event_id: "CM-EVT-S8YXVVG6F4"
event_slug: "what-will-gold-gc-hit-by-end-of-december"
event_question: "Will Gold (GC) hit $____ by the end of December?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x39605ffa16456a7b84b238d7a2305443fbc971cbbf94bf84c34c76cd5410180a"
  question_raw: "Will Gold (GC) dip to (LOW) $3,000 by end of December?"
  current_price: 0.026
  volume_24h_usd: 64489.254042
  volume_cumulative_usd: 93785.38103600002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 3% odds on gold falling to $3K by end of December, market sees the floor as remote."
  - "24h volume of $64K is 69% of all-time handle, a near-exhaustive volume flush into a single session."
  - "Fresh activity likely triggered by gold's recent price action or macro data drawing attention to downside tail risk."
  - "Contract resolves end of December; sustained GC weakness needed to shift odds meaningfully."
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
      poly_vol_24h_usd: 64489.254042
sources:
  - label: "ClearMarket market record: Will Gold (GC) hit $____ by the end of December?"
    url: "https://clearmarket.fyi/events/what-will-gold-gc-hit-by-end-of-december"
    retrieved_at: "2026-11-15T07:48:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should read this as the options market's tail-risk analog, the surge is a sentiment check, not a directional call, and the 3% print confirms consensus views a $3K gold print as a low-probability macro shock scenario.
