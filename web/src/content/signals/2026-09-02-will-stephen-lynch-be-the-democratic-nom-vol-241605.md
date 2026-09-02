---
signal_id: "CMSIG20260902VS01"
signal_slug: "will-stephen-lynch-be-the-democratic-nom-vol-241605"
headline: "Lynch MA-08 Dem nominee: 99% on $242K volume"
semantic_title: "Lynch MA-08 Democratic nomination holds near certainty"
telemetry: "99% · $242K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-02T12:29:56+00:00"
event_id: "CM-EVT-P60CT5ZLG0"
event_slug: "kxmaprimary-08d26"
event_question: "Will the Democratic nominee for Massachusetts's 8th congressional district be decided by the 2026 general election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMAPRIMARY-08D26-SLYN"
  question_raw: "Will Stephen Lynch be the Democratic nominee for MA-08?"
  current_price: 0.99
  volume_24h_usd: 241605.64
  volume_cumulative_usd: 357281.21
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi prices Lynch as a 99% lock for the MA-08 Democratic nomination, effectively a resolved outcome."
  - "$242K traded in 24h represents 68% of the contract's all-time volume, a major single-session concentration."
  - "Heavy late-stage volume often reflects traders harvesting residual basis rather than expressing new directional views."
  - "Contract resolves upon certification of the Democratic primary winner."
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
      kalshi_vol_24h_usd: 241605.64
sources:
  - label: "ClearMarket market record: Will the Democratic nominee for Massachusetts's 8th con"
    url: "https://clearmarket.fyi/events/kxmaprimary-08d26"
    retrieved_at: "2026-09-02T12:29:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A $242K session at 99% suggests the market has reached consensus and volume is being driven by basis traders closing positions, not new uncertainty.
