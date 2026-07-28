---
signal_id: "CMSIG20260728VS04"
signal_slug: "will-the-number-of-distinct-us-states-do-vol-18198"
headline: "Trump all-50-states visit: 95% on $18K"
semantic_title: "Trump 50-state visit tracker prices at near-certainty"
telemetry: "95% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-28T10:31:13+00:00"
event_id: "CM-EVT-VX405770H2"
event_slug: "kxtrumpnumstates-26aug01"
event_question: "Will Trump visit more than X states in July 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPNUMSTATES-26AUG01-E10"
  question_raw: "Will the number of distinct US states Donald Trump has visited (per VISITAREA rules) be exactly 10 in Jul 2026?"
  current_price: 0.95
  volume_24h_usd: 18198.23
  volume_cumulative_usd: 29899.84
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-30T14:00:00Z"
bullets:
  - "Kalshi prices completion of Trump's 50-state visit count at 95%, the market has essentially priced this in."
  - "$18K in 24h is 61% of all-time volume, the highest all-time share in this batch, on a small absolute base."
  - "A surge on a 95%-priced contract likely reflects a specific recent visit bringing the total to the threshold."
  - "Remaining 5% prices schedule disruption or tracker verification lag before resolution."
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
      kalshi_vol_24h_usd: 18198.23
sources:
  - label: "ClearMarket market record: Will Trump visit more than X states in July 2026?"
    url: "https://clearmarket.fyi/events/kxtrumpnumstates-26aug01"
    retrieved_at: "2026-07-28T10:31:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-certainty pricing combined with a 61% all-time volume day suggests a confirming event (a logged visit) just occurred, a desk can treat this as essentially resolved pending official tracker update.
