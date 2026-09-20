---
signal_id: "CMSIG20260920VS03"
signal_slug: "will-the-liberal-democratic-party-of-rus-vol-13096"
headline: "LDPR Duma third seat: 28% on $13K inflow"
semantic_title: "LDPR holding third place in the Duma is a long shot at 28%"
telemetry: "28% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-20T07:47:56+00:00"
event_id: "CM-EVT-CJPNXB53C5"
event_slug: "russia-parliamentary-election-3rd-place"
event_question: "Will a party other than United Russia or the Communist Party of the Russian Federation finish in third place in the next Russian parliamentary election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x57f80a71fd7c470dfe2fc625e6b24168acfc95138396c248d6e85392cd0b344c"
  question_raw: "Will the Liberal Democratic Party of Russia (LDPR) win the third-most seats in the next Russian parliamentary election?"
  current_price: 0.28
  volume_24h_usd: 13096.961173999998
  volume_cumulative_usd: 47467.91497700001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-20T00:00:00Z"
bullets:
  - "28% odds mark LDPR as the underdog against New People for third place in the Duma."
  - "$13K in 24h represents 28% of all-time volume, moving in tandem with the New People spike."
  - "The paired surge across both contracts points to active spread trading on seat-order risk."
  - "Resolution at next Russian parliamentary election; no firm date set."
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
      poly_vol_24h_usd: 13096.961173999998
sources:
  - label: "ClearMarket market record: Will a party other than United Russia or the Communist "
    url: "https://clearmarket.fyi/events/russia-parliamentary-election-3rd-place"
    retrieved_at: "2026-09-20T07:47:56+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous volume on both the LDPR and New People third-place contracts signals structured spread activity, a desk should treat these as a single Russian election positioning theme.
