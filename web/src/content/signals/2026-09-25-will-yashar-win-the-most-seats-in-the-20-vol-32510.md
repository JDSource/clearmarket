---
signal_id: "CMSIG20260925VS03"
signal_slug: "will-yashar-win-the-most-seats-in-the-20-vol-32510"
headline: "Yashar most Knesset seats: 56% on $32K surge"
semantic_title: "Yashar leads Israeli Knesset seat race at 56%"
telemetry: "56% · $33K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-25T13:13:41+00:00"
event_id: "CM-EVT-SV1SCXFSY0"
event_slug: "israeli-legislative-election-winner"
event_question: "Will the Israeli legislative election result in a clear winner by the next scheduled election date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd05da9807740aa0f5bc9e9232daabe87a21e5012c19e283abf414f1c1651118b"
  question_raw: "Will Yashar win the most seats in the 2026 Israeli legislative election?"
  current_price: 0.56
  volume_24h_usd: 32510.539004
  volume_cumulative_usd: 124765.450613
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "Polymarket prices Yashar winning the most seats at 56%, a slim majority-odds lead in a highly fragmented multi-party race."
  - "24h volume of $32K is 26% of all-time handle, a meaningful single-session share for an international legislative contract."
  - "Israeli coalition politics make seat-plurality outcomes volatile; fresh volume at 56% suggests a new poll or coalition signal is circulating."
  - "Resolves on the 2026 Israeli legislative election final seat count."
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
      poly_vol_24h_usd: 32510.539004
sources:
  - label: "ClearMarket market record: Will the Israeli legislative election result in a clear"
    url: "https://clearmarket.fyi/events/israeli-legislative-election-winner"
    retrieved_at: "2026-09-25T13:13:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A geopolitically sensitive contract trading at near-even odds with a fresh volume surge warrants monitoring for new Israeli polling data or a coalition realignment announcement.
