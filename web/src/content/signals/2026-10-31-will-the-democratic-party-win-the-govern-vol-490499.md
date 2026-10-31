---
signal_id: "CMSIG20261031VS02"
signal_slug: "will-the-democratic-party-win-the-govern-vol-490499"
headline: "Nevada Dem governor: 75% on $490K volume spike"
semantic_title: "Nevada governor's race tilts Democratic at 75% ahead of vote"
telemetry: "75% · $490K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-31T07:49:19+00:00"
event_id: "CM-EVT-TNC2QWG2J9"
event_slug: "govpartynv-26"
event_question: "Nevada Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYNV-26-D"
  question_raw: "Will the Democratic party win the governorship in Nevada"
  current_price: 0.75
  volume_24h_usd: 490499.18
  volume_cumulative_usd: 1594491.66
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-02T15:00:00Z"
bullets:
  - "Kalshi marks Democrats at 75%, a clear but not overwhelming favorite in a historically swing state."
  - "$490K in 24h is 31% of all-time volume, reflecting sharp pre-election conviction building."
  - "Nevada gubernatorial races consistently tighten late; the 25% Republican tail retains real capital."
  - "Resolves on Nevada 2026 gubernatorial election result."
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
      kalshi_vol_24h_usd: 490499.18
sources:
  - label: "ClearMarket market record: Nevada Governor winner?"
    url: "https://clearmarket.fyi/events/govpartynv-26"
    retrieved_at: "2026-10-31T07:49:19+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 75% price paired with a 31% daily volume share signals desks are treating Nevada as a key bellwether, the 25% tail is attractively priced for anyone with a contrarian read on turnout.
