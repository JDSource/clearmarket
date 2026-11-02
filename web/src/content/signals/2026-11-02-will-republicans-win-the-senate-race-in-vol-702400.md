---
signal_id: "CMSIG20261102VS02"
signal_slug: "will-republicans-win-the-senate-race-in-vol-702400"
headline: "Michigan Senate GOP: 22% on $702K surge"
semantic_title: "Republicans face long odds in the Michigan Senate race"
telemetry: "22% · $702K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-02T07:49:23+00:00"
event_id: "CM-EVT-GBSY094P67"
event_slug: "senatemi-26"
event_question: "Michigan Senate winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEMI-26-R"
  question_raw: "Will Republicans win the Senate race in Michigan?"
  current_price: 0.22
  volume_24h_usd: 702400.46
  volume_cumulative_usd: 2604006.98
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Republicans at 22%, consistent underdog status, below the 25% threshold."
  - "$702K in 24h is 27% of all-time volume, running in near-lockstep with the Democratic-side contract."
  - "Mirror volume on both sides of the Michigan Senate market points to two-sided hedging into election eve."
  - "Contract resolves opposite SPIKE 0; combined flows reveal a contested close-out."
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
      kalshi_vol_24h_usd: 702400.46
sources:
  - label: "ClearMarket market record: Michigan Senate winner?"
    url: "https://clearmarket.fyi/events/senatemi-26"
    retrieved_at: "2026-11-02T07:49:23+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The near-identical volume on both the Democratic and Republican Michigan Senate contracts confirms active two-sided positioning, desks are hedging paired exposure rather than expressing a directional view.
