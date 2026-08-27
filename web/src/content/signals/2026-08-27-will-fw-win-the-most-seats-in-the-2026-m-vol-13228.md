---
signal_id: "CMSIG20260827VS06"
signal_slug: "will-fw-win-the-most-seats-in-the-2026-m-vol-13228"
headline: "FW most seats MV 2026: 0% on $13K flow"
semantic_title: "FW winning Mecklenburg-Vorpommern seats priced out entirely"
telemetry: "0% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-27T18:47:16+00:00"
event_id: "CM-EVT-N815VR9GY5"
event_slug: "mecklenburg-vorpommern-parliamentary-election-winner"
event_question: "Will the SPD win the most seats in the Mecklenburg-Vorpommern state parliament election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6dd7680c4606a46e08df25bca6c4318b1bc30c9f4306a5ab8e79932c9e2147d8"
  question_raw: "Will FW win the most seats in the 2026 Mecklenburg-Vorpommern parliamentary elections?"
  current_price: 0.001
  volume_24h_usd: 13228.0
  volume_cumulative_usd: 49936.849096
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-20T00:00:00Z"
bullets:
  - "Polymarket prices FW at 0%, the market has fully priced out any chance of FW leading the 2026 Mecklenburg-Vorpommern parliament."
  - "24h volume of $13K is 26% of all-time, a meaningful fresh-trading day for a German state election contract."
  - "FW is a minor regional force; polling and structural dynamics in MV make AfD or SPD the dominant contenders."
  - "Resolves on seat totals from the 2026 Mecklenburg-Vorpommern parliamentary election."
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
      poly_vol_24h_usd: 13228.0
sources:
  - label: "ClearMarket market record: Will the SPD win the most seats in the Mecklenburg-Vorp"
    url: "https://clearmarket.fyi/events/mecklenburg-vorpommern-parliamentary-election-winner"
    retrieved_at: "2026-08-27T18:47:16+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume into a 0% contract on a German state election suggests either speculative zero-hunting or cross-contract positioning, desks with German political exposure should treat this as a background signal, not a directional one.
