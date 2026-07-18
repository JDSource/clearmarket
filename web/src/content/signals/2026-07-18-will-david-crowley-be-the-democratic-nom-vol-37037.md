---
signal_id: "CMSIG20260718VS01"
signal_slug: "will-david-crowley-be-the-democratic-nom-vol-37037"
headline: "Crowley WI Dem governor: 21% on $37K volume spike"
semantic_title: "Crowley Wisconsin Dem nomination sits at long-shot odds"
telemetry: "21% · $37K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-18T09:20:34+00:00"
event_id: "CM-EVT-GTB8QZVGM8"
event_slug: "kxgovwinomd-26"
event_question: "Will a Wisconsin Democratic Governor be nominated by the 2026 election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVWINOMD-26-DCRO"
  question_raw: "Will David Crowley be the Democratic nominee for Governor in Wisconsin?"
  current_price: 0.21
  volume_24h_usd: 37037.87
  volume_cumulative_usd: 46506.81
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-31T14:00:00Z"
bullets:
  - "Price at 21%, Kalshi traders rate Crowley a clear underdog for the Wisconsin Democratic gubernatorial nod."
  - "24h volume of $37K is 80% of all-time contract liquidity, signaling a near-complete market discovery event."
  - "Surge implies fresh entrant information, a filing deadline, rival announcement, or polling release, driving re-evaluation."
  - "Nominee resolution tied to Wisconsin Democratic primary calendar; current odds favor the field over Crowley."
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
      kalshi_vol_24h_usd: 37037.87
sources:
  - label: "ClearMarket market record: Will a Wisconsin Democratic Governor be nominated by th"
    url: "https://clearmarket.fyi/events/kxgovwinomd-26"
    retrieved_at: "2026-07-18T09:20:34+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Eighty percent of all-time volume landing in one session on a state-level primary contract suggests a specific catalyst forced rapid price discovery, and a desk should flag Wisconsin Democratic primary developments as a live political-risk input.
