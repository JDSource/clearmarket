---
signal_id: "CMSIG20260919VS07"
signal_slug: "will-the-liberal-democratic-party-of-rus-vol-10091"
headline: "LDPR third in Duma: 18% on $10K volume"
semantic_title: "LDPR finishing third in the Duma vote faces long odds"
telemetry: "18% · $10K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-19T12:15:36+00:00"
event_id: "CM-EVT-CJPNXB53C5"
event_slug: "russia-parliamentary-election-3rd-place"
event_question: "Will a party other than United Russia or the Communist Party of the Russian Federation finish in third place in the next Russian parliamentary election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x57f80a71fd7c470dfe2fc625e6b24168acfc95138396c248d6e85392cd0b344c"
  question_raw: "Will the Liberal Democratic Party of Russia (LDPR) win the third-most seats in the next Russian parliamentary election?"
  current_price: 0.18
  volume_24h_usd: 10091.406735
  volume_cumulative_usd: 39704.35493400002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-20T00:00:00Z"
bullets:
  - "Polymarket prices LDPR winning the third-most Duma seats at 18%, a distant second to New People's 78%."
  - "24h volume of $10K is 25% of all-time, consistent with the broader Russian parliamentary suite seeing simultaneous action."
  - "At 18%, the market treats LDPR as a live but unlikely alternative to NL for the third-place slot."
  - "Resolves on official Russian State Duma election seat tallies, tied to Spikes 3, 4, and 5."
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
      poly_vol_24h_usd: 10091.406735
sources:
  - label: "ClearMarket market record: Will a party other than United Russia or the Communist "
    url: "https://clearmarket.fyi/events/russia-parliamentary-election-3rd-place"
    retrieved_at: "2026-09-19T12:15:36+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Concurrent volume across all Russian Duma seat contracts indicates desks are stress-testing the full distribution of parliamentary outcomes, with LDPR holding residual but modest third-place probability.
