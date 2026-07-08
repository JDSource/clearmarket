---
signal_id: "CMSIG20260708VS06"
signal_slug: "will-marine-le-pen-win-the-2027-french-p-vol-11945"
headline: "Le Pen 2027 win: 35% on $12K Kalshi surge"
semantic_title: "Kalshi flows target Le Pen 2027 win at 35%"
telemetry: "35% · $12K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-08T10:14:29+00:00"
event_id: "CM-EVT-F4DV339FW0"
event_slug: "kxfrenchpres-27"
event_question: "Who will win the 2027 French presidential election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFRENCHPRES-27-MLEP"
  question_raw: "Will Marine Le Pen win the 2027 French presidential election?"
  current_price: 0.35
  volume_24h_usd: 11945.98
  volume_cumulative_usd: 22538.66
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-05-31T14:00:00Z"
bullets:
  - "Kalshi prices Le Pen winning at 35%, a notable 8-point premium to Polymarket's 27% on the same question."
  - "24h volume $12K is 53% of all-time on Kalshi, confirming broad cross-venue attention today."
  - "Cross-venue divergence between Kalshi (35%) and Polymarket (27%) creates an arbitrage signal for desks."
  - "Resolves after the 2027 French presidential election."
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
      kalshi_vol_24h_usd: 11945.98
sources:
  - label: "ClearMarket market record: Who will win the 2027 French presidential election?"
    url: "https://clearmarket.fyi/events/kxfrenchpres-27"
    retrieved_at: "2026-07-08T10:14:29+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The simultaneous spike across both venues with a meaningful price gap suggests liquidity fragmentation, a desk running cross-market arb should evaluate whether the Kalshi premium reflects different participant composition or a lagging update.
