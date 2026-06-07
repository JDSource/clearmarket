---
signal_id: "CMSIG20260607VS03"
signal_slug: "who-will-win-los-angeles-mayoral-electio-vol-1168668"
headline: "LA mayoral winner: 79% Bass on $1.2M inflow"
semantic_title: "Heavy flows defend Bass at 79% in the LA mayoral race"
telemetry: "79% · $1.2M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-07T10:26:54+00:00"
event_id: "CM-EVT-X27NWLJN20"
event_slug: "kxmayorla-26"
event_question: "Will there be a Los Angeles Mayor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMAYORLA-26-KBAS"
  question_raw: "Who will win Los Angeles Mayoral Election?"
  current_price: 0.79
  volume_24h_usd: 1168668.91
  volume_cumulative_usd: 4455417.91
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-06-02T14:00:00Z"
bullets:
  - "79% on Kalshi implies Bass holds strong favorite status heading into the mayoral contest."
  - "24h volume $1.2M is 26% of all-time, reflecting a meaningful but not climactic surge."
  - "Fresh capital arrival suggests a recent polling print, endorsement, or opponent stumble driving conviction."
  - "Tied to Spike 7 on nominee confirmation; winner-market repricing follows nominee lock-in."
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
      kalshi_vol_24h_usd: 1168668.91
sources:
  - label: "ClearMarket market record: Will there be a Los Angeles Mayor winner?"
    url: "https://clearmarket.fyi/events/kxmayorla-26"
    retrieved_at: "2026-06-07T10:26:54+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should cross-reference with the nominee-confirmation contract, if Bass-Pratt ballot is confirmed at 79%, the winner market at 79% for Bass implies the conditional probability of a Bass victory is effectively near-certain given that pairing.
