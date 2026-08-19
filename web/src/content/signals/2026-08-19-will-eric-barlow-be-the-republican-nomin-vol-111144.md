---
signal_id: "CMSIG20260819VS01"
signal_slug: "will-eric-barlow-be-the-republican-nomin-vol-111144"
headline: "Barlow WY GOP nominee: 100% on $111K spike"
semantic_title: "Barlow Wyoming GOP governor nod trades at certainty"
telemetry: "100% · $111K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-19T08:32:13+00:00"
event_id: "CM-EVT-SBQ8NYFV24"
event_slug: "kxgovwynomr-26"
event_question: "Will a Wyoming Republican governor nominee be determined by the 2026 election cycle?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVWYNOMR-26-EBAR"
  question_raw: "Will Eric Barlow be the Republican nominee for Governor in Wyoming?"
  current_price: 0.999
  volume_24h_usd: 111144.69
  volume_cumulative_usd: 200027.71
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-31T14:00:00Z"
bullets:
  - "Kalshi prices Eric Barlow as a lock for the Wyoming Republican gubernatorial nomination at 100%."
  - "$111K traded in 24h, 56% of the contract's entire all-time volume, suggests a result is in."
  - "Wyoming's August primary cycle aligns with today's date; fresh volume reads as settlement activity."
  - "Contract resolves on official Wyoming GOP primary certification naming the nominee."
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
      kalshi_vol_24h_usd: 111144.69
sources:
  - label: "ClearMarket market record: Will a Wyoming Republican governor nominee be determine"
    url: "https://clearmarket.fyi/events/kxgovwynomr-26"
    retrieved_at: "2026-08-19T08:32:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Majority of lifetime volume printing in one day at 100% is a strong signal the primary outcome is known and traders are collecting on resolved positions.
