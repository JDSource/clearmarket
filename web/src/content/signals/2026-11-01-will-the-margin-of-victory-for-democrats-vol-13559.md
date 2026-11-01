---
signal_id: "CMSIG20261101VS06"
signal_slug: "will-the-margin-of-victory-for-democrats-vol-13559"
headline: "NC Senate Dem margin >X%: 59% on $14K surge"
semantic_title: "Heavy trading tests the Democratic margin band in North Carolina Senate"
telemetry: "59% · $14K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-01T14:43:30+00:00"
event_id: "CM-EVT-22Y3TGXT19"
event_slug: "kxmidtermmov-ncsend"
event_question: "Will the North Carolina Senate margin of victory be less than 5 percentage points?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMIDTERMMOV-NCSEND-P13"
  question_raw: "Will the margin of victory for Democrats in the U.S. Senate election in North Carolina be at least 13 percentage points?"
  current_price: 0.59
  volume_24h_usd: 13559.14
  volume_cumulative_usd: 34229.55
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-11-03T15:00:00Z"
bullets:
  - "At 59% on Kalshi, a Democratic victory margin above the specified threshold in North Carolina is slightly favored."
  - "$14K in 24h equals 40% of all-time volume, concentrated Election Day flow on a margin-of-victory contract."
  - "Margin contracts attract late-cycle attention as trackers and modelers refine turnout assumptions on Election Day."
  - "Resolves on the certified vote margin from North Carolina's 2026 U.S. Senate race."
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
      kalshi_vol_24h_usd: 13559.14
sources:
  - label: "ClearMarket market record: Will the North Carolina Senate margin of victory be les"
    url: "https://clearmarket.fyi/events/kxmidtermmov-ncsend"
    retrieved_at: "2026-11-01T14:43:30+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Forty percent of lifetime volume on a margin-band contract closing on Election Day signals desks are pricing turnout uncertainty in North Carolina rather than just a binary win/loss.
