---
signal_id: "CMSIG20260726VS06"
signal_slug: "will-samuel-alito-announce-his-retiremen-vol-15204"
headline: "Alito retirement by Jun 2027: 35% on $15K"
semantic_title: "Buyers back Alito retirement odds at 35%"
telemetry: "35% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-26T09:56:30+00:00"
event_id: "CM-EVT-XDBQBGP715"
event_slug: "will-samuel-alito-announce-his-retirement-by"
event_question: "Will Samuel Alito announce his retirement by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x559b8224c2ae858342c0617ba278b46242e51071950f9a9d04bc3147dc374440"
  question_raw: "Will Samuel Alito announce his retirement by June 30, 2027?"
  current_price: 0.35
  volume_24h_usd: 15204.865841
  volume_cumulative_usd: 39397.78489300002
  arbitration_model: "uma_oracle"
  resolves_at: "2027-06-30T23:59:00Z"
bullets:
  - "Polymarket prices a Samuel Alito retirement announcement by Jun 30, 2027 at 35%, a meaningful minority probability."
  - "39% of all-time volume arrived in 24h, a notable single-session share for a slow-moving SCOTUS contract."
  - "Senate dynamics, Trump judicial agenda, or Alito public statements likely refreshed trader interest."
  - "Resolution deadline is Jun 30, 2027; odds imply roughly one-in-three chance of an announcement inside a year."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 15204.865841
sources:
  - label: "ClearMarket market record: Will Samuel Alito announce his retirement by the end of"
    url: "https://clearmarket.fyi/events/will-samuel-alito-announce-his-retirement-by"
    retrieved_at: "2026-07-26T09:56:30+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 39% all-time volume concentration at a non-trivial 35% price suggests desks view Alito retirement as a live scenario worth pricing properly, likely driven by fresh commentary on SCOTUS composition risk.
