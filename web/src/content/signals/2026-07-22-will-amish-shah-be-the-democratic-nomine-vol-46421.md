---
signal_id: "CMSIG20260722VS00"
signal_slug: "will-amish-shah-be-the-democratic-nomine-vol-46421"
headline: "Shah AZ-01 Dem nominee: 97% on $46K surge"
semantic_title: "Betting locks in Amish Shah as the AZ-01 Democratic pick"
telemetry: "97% · $46K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-22T10:22:39+00:00"
event_id: "CM-EVT-9M4QR764Y3"
event_slug: "kxaz01d-25"
event_question: "Will the Democratic nominee for Arizona's 1st Congressional District be determined by November 2, 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAZ01D-25-ASHA"
  question_raw: "Will Amish Shah be the Democratic nominee for AZ-01?"
  current_price: 0.97
  volume_24h_usd: 46421.15
  volume_cumulative_usd: 94935.78
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-02T15:00:00Z"
bullets:
  - "Kalshi prices Shah at 97%, market treats the Democratic nomination as effectively settled."
  - "24h volume of $46K is 49% of all-time, signaling a concentrated rush of fresh conviction."
  - "Surge likely reflects a filing deadline, withdrawal, or endorsement removing remaining challengers."
  - "Resolves on official Democratic nominee certification for Arizona's 1st congressional district."
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
      kalshi_vol_24h_usd: 46421.15
sources:
  - label: "ClearMarket market record: Will the Democratic nominee for Arizona's 1st Congressi"
    url: "https://clearmarket.fyi/events/kxaz01d-25"
    retrieved_at: "2026-07-22T10:22:39+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-unanimous odds with half of all-time volume printing in one session signals a race-defining event has cleared the field, desks should treat this as resolved-in-all-but-name.
