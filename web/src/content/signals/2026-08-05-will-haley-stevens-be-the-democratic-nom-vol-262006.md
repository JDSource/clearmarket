---
signal_id: "CMSIG20260805VS03"
signal_slug: "will-haley-stevens-be-the-democratic-nom-vol-262006"
headline: "Stevens MI Senate nominee: 2% on $262K volume"
semantic_title: "Haley Stevens as MI Senate nominee slips to 2%"
telemetry: "2% · $262K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-05T10:31:36+00:00"
event_id: "CM-EVT-ZMWFMPNXD9"
event_slug: "kxsenatemid-26"
event_question: "Will the Michigan Democratic Senate nominee be determined by the 2026 election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSENATEMID-26-HSTE"
  question_raw: "Will Haley Stevens be the Democratic nominee for the Senate in Michigan?"
  current_price: 0.018
  volume_24h_usd: 262006.97
  volume_cumulative_usd: 354519.48
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi prices Stevens nomination at 2%, market has effectively ruled her out."
  - "74% of all-time volume concentrated in 24h as primary results clarify."
  - "Volume surge on the 'No' side mirrors El-Sayed's 99% contract, same event, inverse side."
  - "Resolves on Michigan Democratic Senate primary certification."
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
      kalshi_vol_24h_usd: 262006.97
sources:
  - label: "ClearMarket market record: Will the Michigan Democratic Senate nominee be determin"
    url: "https://clearmarket.fyi/events/kxsenatemid-26"
    retrieved_at: "2026-08-05T10:31:36+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Residual 2% pricing with heavy volume is classic settlement activity, desks should read this as the market flushing out any remaining long exposure on a losing candidate.
