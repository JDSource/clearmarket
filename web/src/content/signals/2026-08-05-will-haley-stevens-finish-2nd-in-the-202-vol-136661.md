---
signal_id: "CMSIG20260805VS04"
signal_slug: "will-haley-stevens-finish-2nd-in-the-202-vol-136661"
headline: "Stevens 2nd-place MI primary: 99% on $137K"
semantic_title: "Betting picks up on Stevens finishing 2nd in MI primary"
telemetry: "99% · $137K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-05T10:31:36+00:00"
event_id: "CM-EVT-KW32LYSWB7"
event_slug: "kxprimaryplace-senatemid26-2"
event_question: "Who will finish in second place in the Michigan Senate Democratic primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPRIMARYPLACE-SENATEMID26-2-HSTE"
  question_raw: "Will Haley Stevens finish 2nd in the 2026 Michigan Senate Democratic primary?"
  current_price: 0.99
  volume_24h_usd: 136661.19
  volume_cumulative_usd: 162955.5
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-08-04T14:00:00Z"
bullets:
  - "Kalshi prices Stevens finishing second at 99%, field has narrowed to two viable candidates."
  - "84% of all-time volume in 24h; market conviction on placement is as high as on the winner."
  - "Implies a clean two-candidate race where Stevens is the only credible runner-up to El-Sayed."
  - "Resolves on official Michigan primary results reporting candidate vote shares."
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
      kalshi_vol_24h_usd: 136661.19
sources:
  - label: "ClearMarket market record: Who will finish in second place in the Michigan Senate "
    url: "https://clearmarket.fyi/events/kxprimaryplace-senatemid26-2"
    retrieved_at: "2026-08-05T10:31:36+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 99% second-place contract alongside a 2% nominee contract confirms the market's complete picture of the race, useful for desks modeling the general-election Democratic coalition.
