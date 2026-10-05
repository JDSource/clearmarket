---
signal_id: "CMSIG20261005VS00"
signal_slug: "will-fl-vio-bolsonaro-win-the-2026-brazi-vol-436702"
headline: "F. Bolsonaro 2026: 81% on $437K single-day surge"
semantic_title: "Traders pile into Flávio Bolsonaro as Brazil frontrunner"
telemetry: "81% · $437K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-05T07:48:02+00:00"
event_id: "CM-EVT-DKSKHZR435"
event_slug: "kxbrpres-26"
event_question: "Will the winner of Brazil's next presidential election be determined by October 25, 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBRPRES-26-FBOL"
  question_raw: "Will Flávio Bolsonaro win the 2026 Brazilian presidential election?"
  current_price: 0.81
  volume_24h_usd: 436702.65
  volume_cumulative_usd: 1689210.77
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-25T14:00:00Z"
bullets:
  - "Kalshi prices Flávio Bolsonaro at 81%, strong favorite status, implying near-consensus on a first-round lead."
  - "24h volume of $437K equals 26% of all-time contract volume, the largest single-day deployment on record."
  - "Fresh capital arrives roughly one year before the October 2026 vote, typically when polling and coalition signals sharpen."
  - "Contract resolves on official Brazilian electoral results; 81% leaves meaningful tail risk unpriced."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from kalshi API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "kalshi_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      kalshi_vol_24h_usd: 436702.65
sources:
  - label: "ClearMarket market record: Will the winner of Brazil's next presidential election "
    url: "https://clearmarket.fyi/events/kxbrpres-26"
    retrieved_at: "2026-10-05T07:48:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should treat this as a directional conviction flush, the contract is becoming a primary vehicle for Brazil political-risk hedging, and the volume weight at 81% suggests the market is not expecting a Lula comeback narrative to gain traction near-term.
