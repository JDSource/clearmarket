---
signal_id: "CMSIG20261002VS01"
signal_slug: "will-the-republican-party-win-the-oh-13-vol-14352"
headline: "GOP OH-13 House seat: 1% on $14K volume spike"
semantic_title: "Republican win in OH-13 stays a long shot at 1% through heavy trading"
telemetry: "1% · $14K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-02T14:26:08+00:00"
event_id: "CM-EVT-WMKKZW90K3"
event_slug: "oh-13-house-election-winner"
event_question: "OH-13 House Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x484b9d64f4b8c3b00a8f455bfac9b84d889236ec419edc636c0e50ad33b2c3dd"
  question_raw: "Will the Republican Party win the OH-13 House seat?"
  current_price: 0.013
  volume_24h_usd: 14352.917167
  volume_cumulative_usd: 27870.538192999997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-04T00:00:00Z"
bullets:
  - "Price of 1% on Polymarket leaves virtually no probability of a Republican flip in OH-13."
  - "24h volume of $14.4K is 51% of all-time handle, meaning half the contract's lifetime liquidity arrived today."
  - "Surge at near-zero odds suggests either late arbitrage activity or a final positioning flush ahead of race resolution."
  - "Resolves on certified Ohio 13th District House race outcome."
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
      poly_vol_24h_usd: 14352.917167
sources:
  - label: "ClearMarket market record: OH-13 House Election Winner"
    url: "https://clearmarket.fyi/events/oh-13-house-election-winner"
    retrieved_at: "2026-10-02T14:26:08+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume into a 1% contract signals the desk should watch for a resolution trigger, this is likely late-stage settlement flow rather than genuine directional disagreement.
