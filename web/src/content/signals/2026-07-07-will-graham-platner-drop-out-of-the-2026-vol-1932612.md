---
signal_id: "CMSIG20260707VS00"
signal_slug: "will-graham-platner-drop-out-of-the-2026-vol-1932612"
headline: "Platner ME Senate dropout: 91% on $1.9M surge"
semantic_title: "Traders price Platner exit as near-certain in Maine Senate"
telemetry: "91% · $1.9M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-07T10:52:51+00:00"
event_id: "CM-EVT-5YRQP7DDC2"
event_slug: "kxplatnerdropout-26"
event_question: "Will Graham Platner drop out?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPLATNERDROPOUT-26"
  question_raw: "Will Graham Platner drop out of the 2026 United States Senate election in Maine before Jul 14, 2026?"
  current_price: 0.906
  volume_24h_usd: 1932612.07
  volume_cumulative_usd: 2921454.31
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-07-14T14:00:00Z"
bullets:
  - "91% implies capital treats Platner's exit as effectively resolved, not speculative."
  - "Kalshi sees $1.93M in 24h, 66% of all-time volume, a near-total conviction flush."
  - "Surge suggests a credible private signal or imminent public announcement circulating."
  - "Contract resolves on Platner formally withdrawing from the 2026 Maine Senate race."
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
      kalshi_vol_24h_usd: 1932612.07
sources:
  - label: "ClearMarket market record: Will Graham Platner drop out?"
    url: "https://clearmarket.fyi/events/kxplatnerdropout-26"
    retrieved_at: "2026-07-07T10:52:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should treat this as event-driven confirmation flow rather than directional speculation, someone with high-confidence information is closing exposure at 91%, making the dropout highly probable within a short window.
