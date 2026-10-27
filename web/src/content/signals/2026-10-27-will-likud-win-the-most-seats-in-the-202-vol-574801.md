---
signal_id: "CMSIG20261027VS01"
signal_slug: "will-likud-win-the-most-seats-in-the-202-vol-574801"
headline: "Likud most seats: 30% on $575K surge"
semantic_title: "Likud leading-party odds stay at 30% through heavy trading"
telemetry: "30% · $575K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-27T07:49:11+00:00"
event_id: "CM-EVT-SV1SCXFSY0"
event_slug: "israeli-legislative-election-winner"
event_question: "Will the Israeli legislative election result in a clear winner by the next scheduled election date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xf77fa3e63014f1f76ea4433dac66b3860493ed7f1a9fee3dfbef9104d7f1eee3"
  question_raw: "Will Likud win the most seats in the 2026 Israeli legislative election?"
  current_price: 0.3
  volume_24h_usd: 574801.1617079999
  volume_cumulative_usd: 1907354.28375
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "30% price means Likud is seen as a live contender but not the plurality leader heading into the 2026 Knesset vote."
  - "$575K in 24h represents 30% of all-time volume, deep re-engagement by the market on Israeli election composition."
  - "Surge likely tied to fresh polling or coalition signaling out of Israel; attention on this contract precedes news flow."
  - "Resolves on official Knesset seat count following the 2026 Israeli legislative election."
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
      poly_vol_24h_usd: 574801.1617079999
sources:
  - label: "ClearMarket market record: Will the Israeli legislative election result in a clear"
    url: "https://clearmarket.fyi/events/israeli-legislative-election-winner"
    retrieved_at: "2026-10-27T07:49:11+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy two-sided volume at a 30% price on Likud's plurality suggests desks are actively hedging Israeli political exposure ahead of a near-term information event.
