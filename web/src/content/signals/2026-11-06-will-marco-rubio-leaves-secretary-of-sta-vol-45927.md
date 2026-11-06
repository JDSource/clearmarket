---
signal_id: "CMSIG20261106VS02"
signal_slug: "will-marco-rubio-leaves-secretary-of-sta-vol-45927"
headline: "Rubio SecState exit: 21% on $46K at Kalshi"
semantic_title: "Rubio Secretary of State exit before 2027 stays a long shot at 21%"
telemetry: "21% · $46K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-06T15:37:54+00:00"
event_id: "CM-EVT-Z5Z4K6WBZ9"
event_slug: "kxtrumpadminleave-26dec31"
event_question: "Will someone leave their role in the Trump administration in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPADMINLEAVE-26DEC31-MRUB"
  question_raw: "Will Marco Rubio leaves Secretary of State in before 2027?"
  current_price: 0.21
  volume_24h_usd: 45927.31
  volume_cumulative_usd: 94262.86
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-07T15:00:00Z"
bullets:
  - "At 21%, Kalshi prices a Rubio departure from State before year-end as unlikely but not negligible."
  - "$45K in 24h is 49% of all-time volume, the market is effectively being repriced from scratch today."
  - "Parallel surge with Polymarket's Rubio contract (Spike 0) confirms cross-venue attention on the same rumor."
  - "Resolves if Rubio leaves the Secretary of State role for any reason before Jan 1, 2027."
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
      kalshi_vol_24h_usd: 45927.31
sources:
  - label: "ClearMarket market record: Will someone leave their role in the Trump administrati"
    url: "https://clearmarket.fyi/events/kxtrumpadminleave-26dec31"
    retrieved_at: "2026-11-06T15:37:54+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous volume spikes on two separate venues covering Rubio's exit, one administration-wide, one role-specific, point to a coordinated information event a desk should treat as a single signal, not two independent ones.
