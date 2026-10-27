---
signal_id: "CMSIG20261027VS03"
signal_slug: "will-gadi-eizenkot-become-prime-minister-vol-107460"
headline: "Eizenkot PM Israel: 50% on $107K surge"
semantic_title: "Eizenkot PM odds sit at even money after heavy volume"
telemetry: "50% · $107K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-27T07:49:11+00:00"
event_id: "CM-EVT-XQ3FKH3GZ5"
event_slug: "kxisraelpm-26oct27"
event_question: "Will Benjamin Netanyahu be Prime Minister of Israel after the 2026 election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXISRAELPM-26OCT27-GEIZ"
  question_raw: "Will Gadi Eizenkot become Prime Minister of Israel following the 2026 Israeli legislative election?"
  current_price: 0.5
  volume_24h_usd: 107460.28
  volume_cumulative_usd: 204549.89
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-10-27T14:00:00Z"
bullets:
  - "50% price makes Eizenkot a true coin-flip for Prime Minister following the 2026 Israeli election, maximum uncertainty."
  - "$107K in 24h is 53% of all-time volume on Kalshi, meaning more than half the contract's history traded in one day."
  - "That volume concentration at 50% signals a genuine information contest, new polling, coalition talks, or bloc-realignment news."
  - "Resolves on who assumes the Prime Minister role following the 2026 Israeli legislative election."
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
      kalshi_vol_24h_usd: 107460.28
sources:
  - label: "ClearMarket market record: Will Benjamin Netanyahu be Prime Minister of Israel aft"
    url: "https://clearmarket.fyi/events/kxisraelpm-26oct27"
    retrieved_at: "2026-10-27T07:49:11+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Half of all-time volume printing at exactly 50% is a textbook signal of contested information, desks should monitor Israeli coalition negotiation headlines closely as this contract is live and directional.
