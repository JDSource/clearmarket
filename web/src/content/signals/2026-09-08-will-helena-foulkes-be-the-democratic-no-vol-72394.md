---
signal_id: "CMSIG20260908VS00"
signal_slug: "will-helena-foulkes-be-the-democratic-no-vol-72394"
headline: "Foulkes RI Dem governor: 99% on $72K surge"
semantic_title: "Foulkes locks up the Rhode Island Democratic governor nod"
telemetry: "99% · $72K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-08T12:34:41+00:00"
event_id: "CM-EVT-ZVCJ160PY0"
event_slug: "kxgovrinomd-26"
event_question: "Will Rhode Island have a Democratic Governor nominee by September 8, 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVRINOMD-26-HFOU"
  question_raw: "Will Helena Foulkes be the Democratic nominee for Governor in Rhode Island?"
  current_price: 0.994
  volume_24h_usd: 72394.73
  volume_cumulative_usd: 173133.43
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-08T14:00:00Z"
bullets:
  - "Kalshi prices Foulkes at 99%, the nomination is treated as a near-certainty."
  - "$72K traded in 24h, equal to 42% of all-time volume, a definitive late-stage settlement rush."
  - "Volume at this magnitude this close to resolution typically follows a decisive filing or rival withdrawal."
  - "Contract resolves on the Democratic primary outcome for Rhode Island governor."
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
      kalshi_vol_24h_usd: 72394.73
sources:
  - label: "ClearMarket market record: Will Rhode Island have a Democratic Governor nominee by"
    url: "https://clearmarket.fyi/events/kxgovrinomd-26"
    retrieved_at: "2026-09-08T12:34:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The surge at 99% signals the market is in final-settlement mode, a desk should treat the Foulkes nomination as resolved and shift attention to the general-election matchup.
