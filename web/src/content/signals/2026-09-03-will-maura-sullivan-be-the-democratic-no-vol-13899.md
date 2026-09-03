---
signal_id: "CMSIG20260903VS06"
signal_slug: "will-maura-sullivan-be-the-democratic-no-vol-13899"
headline: "Sullivan NH-01 Dem nominee: 83% on $13K flow"
semantic_title: "Maura Sullivan holds at 83% for NH-01 Democratic spot"
telemetry: "83% · $14K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-03T12:31:50+00:00"
event_id: "CM-EVT-BHSCBSRT91"
event_slug: "nh-01-democratic-primary-winner"
event_question: "Will a Democrat win the NH-01 primary election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x8e0c12663aac3ff057b2b3954864e2370ec1a9c94992104996f79f7da097cda1"
  question_raw: "Will Maura Sullivan be the Democratic nominee for NH-01?"
  current_price: 0.83
  volume_24h_usd: 13899.070746000001
  volume_cumulative_usd: 31931.830377000002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-08T00:00:00Z"
bullets:
  - "Polymarket prices Sullivan at 83%, market views her as the likely Democratic nominee for NH-01."
  - "24h volume of $13K is 44% of all-time flow, indicating a sharp uptick in attention to the race."
  - "Primary dynamics in NH-01, potentially linked to the DiLorenzo spike on the Republican side, are drawing bilateral interest."
  - "Resolves on the Democratic nominee for New Hampshire's 1st Congressional District primary."
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
      poly_vol_24h_usd: 13899.070746000001
sources:
  - label: "ClearMarket market record: Will a Democrat win the NH-01 primary election?"
    url: "https://clearmarket.fyi/events/nh-01-democratic-primary-winner"
    retrieved_at: "2026-09-03T12:31:50+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Concurrent volume spikes on both the Democratic and Republican NH-01 contracts suggest the primary landscape is shifting, warranting a paired look at both contracts as a congressional race pair.
