---
signal_id: "CMSIG20260828VS03"
signal_slug: "will-fw-win-the-most-seats-in-the-2026-m-vol-26261"
headline: "FW MV most seats: 0% on $26K volume"
semantic_title: "FW winning most Mecklenburg-Vorpommern seats priced at zero"
telemetry: "0% · $26K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-28T19:52:39+00:00"
event_id: "CM-EVT-N815VR9GY5"
event_slug: "mecklenburg-vorpommern-parliamentary-election-winner"
event_question: "Will the SPD win the most seats in the Mecklenburg-Vorpommern state parliament election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6dd7680c4606a46e08df25bca6c4318b1bc30c9f4306a5ab8e79932c9e2147d8"
  question_raw: "Will FW win the most seats in the 2026 Mecklenburg-Vorpommern parliamentary elections?"
  current_price: 0.001
  volume_24h_usd: 26261.7
  volume_cumulative_usd: 89509.549096
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-20T00:00:00Z"
bullets:
  - "0% price means the market treats a FW plurality in Mecklenburg-Vorpommern as essentially impossible."
  - "Today's $26K is 29% of all-time handle, notable activity for a contract already pinned at the floor."
  - "Fresh volume at zero likely reflects arbitrage cleanup or hedgers confirming the outcome post-polling."
  - "Resolves on official 2026 Mecklenburg-Vorpommern state election seat count."
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
      poly_vol_24h_usd: 26261.7
sources:
  - label: "ClearMarket market record: Will the SPD win the most seats in the Mecklenburg-Vorp"
    url: "https://clearmarket.fyi/events/mecklenburg-vorpommern-parliamentary-election-winner"
    retrieved_at: "2026-08-28T19:52:39+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Volume into a zero-priced outcome signals position squaring or arb activity, not genuine belief, desks modeling German state coalition arithmetic can remove FW from any plurality scenario entirely.
