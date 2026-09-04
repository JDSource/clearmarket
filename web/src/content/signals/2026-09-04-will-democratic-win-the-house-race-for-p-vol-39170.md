---
signal_id: "CMSIG20260904VS01"
signal_slug: "will-democratic-win-the-house-race-for-p-vol-39170"
headline: "Democrat PA-7 House: 78% on $39K volume spike"
semantic_title: "Buyers back the Democrat to hold PA-7 at 78%"
telemetry: "78% · $39K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-04T12:29:08+00:00"
event_id: "CM-EVT-6S7C40J637"
event_slug: "housepa7-26"
event_question: "Will the winner of Pennsylvania's 7th congressional district House race be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "HOUSEPA7-26-D"
  question_raw: "Will Democratic win the House race for PA-7?"
  current_price: 0.78
  volume_24h_usd: 39170.09
  volume_cumulative_usd: 57457.94
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi marks the Democratic candidate at 78%, a meaningful but not decisive lead heading into November."
  - "$39K in 24h represents 68% of all-time contract volume, a sharp concentration of late capital."
  - "PA-7 is a swing-district bellwether; fresh attention here often precedes new polling or redistricting news."
  - "Contract resolves on the certified winner of the PA-7 U.S. House general election."
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
      kalshi_vol_24h_usd: 39170.09
sources:
  - label: "ClearMarket market record: Will the winner of Pennsylvania's 7th congressional dis"
    url: "https://clearmarket.fyi/events/housepa7-26"
    retrieved_at: "2026-09-04T12:29:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Deploying two-thirds of a contract's lifetime volume in a single session on a competitive House seat signals a desk that new district-level information, polling, endorsement, or candidate development, is driving a conviction update.
