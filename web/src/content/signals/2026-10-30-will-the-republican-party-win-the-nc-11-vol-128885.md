---
signal_id: "CMSIG20261030VS00"
signal_slug: "will-the-republican-party-win-the-nc-11-vol-128885"
headline: "GOP NC-11: 14% as $129K floods Polymarket"
semantic_title: "Heavy trading bets against GOP holding NC-11"
telemetry: "14% · $129K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-30T14:48:27+00:00"
event_id: "CM-EVT-DFRWVBVQ98"
event_slug: "nc-11-house-election-winner"
event_question: "Who will win the NC-11 House election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xe64ec54460a1f1b250c9785968e6ebecfb0fd542a34300a161f64460c7a811df"
  question_raw: "Will the Republican Party win the NC-11 House seat?"
  current_price: 0.14
  volume_24h_usd: 128885.27625200003
  volume_cumulative_usd: 171026.78229600002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-04T00:00:00Z"
bullets:
  - "14% implies the market treats a Republican win as a heavy underdog outcome in NC-11."
  - "$129K traded in 24h, 75% of all-time contract volume, signaling a near-climactic rush."
  - "Pairing with Spike 2 (Dems at 86%) shows coordinated positioning across both sides of NC-11."
  - "Resolves on NC-11 House election result; volume surge days before Nov 3 midterm cycle."
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
      poly_vol_24h_usd: 128885.27625200003
sources:
  - label: "ClearMarket market record: Who will win the NC-11 House election?"
    url: "https://clearmarket.fyi/events/nc-11-house-election-winner"
    retrieved_at: "2026-10-30T14:48:27+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-total all-time volume in one session on the losing side of NC-11 flags a desk hedging or closing a prior Republican position ahead of final election results.
