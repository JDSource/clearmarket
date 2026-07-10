---
signal_id: "CMSIG20260710VS05"
signal_slug: "will-the-2026-united-left-primary-for-th-vol-13434"
headline: "United Left 2026 primary confirmed: 74% on $13K"
semantic_title: "French left primary flows defend a confirmed primary outcome at 74%"
telemetry: "74% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-10T10:50:20+00:00"
event_id: "CM-EVT-WGPTXTJYH0"
event_slug: "france-united-left-primary-winner"
event_question: "Will the France United Left Primary produce a winner by the settlement date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4a8be083c607742c3ab1493d01075009865f5fc8cfbb0563370a8f0bea8cae74"
  question_raw: "Will the 2026 United Left primary for the 2027 French presidential election be canceled?"
  current_price: 0.74
  volume_24h_usd: 13434.830312999999
  volume_cumulative_usd: 46578.095281000016
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-11T00:00:00Z"
bullets:
  - "Polymarket at 74%, majority of capital expects the 2026 United Left primary for 2027 French presidential race to be confirmed."
  - "24h volume $13.4K is 29% of all-time; renewed attention points to a fresh organizational or political signal."
  - "French left coalition talks or a public announcement likely catalyzed fresh positioning in this contract."
  - "Resolves on whether the primary is officially convened; 26% residual reflects fragmentation risk."
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
      poly_vol_24h_usd: 13434.830312999999
sources:
  - label: "ClearMarket market record: Will the France United Left Primary produce a winner by"
    url: "https://clearmarket.fyi/events/france-united-left-primary-winner"
    retrieved_at: "2026-07-10T10:50:20+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 29% all-time volume day at 74% suggests news from French left coalition negotiations is pulling in fresh speculative capital, warranting attention from European political-risk desks.
