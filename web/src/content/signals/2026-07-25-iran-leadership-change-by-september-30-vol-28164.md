---
signal_id: "CMSIG20260725VS07"
signal_slug: "iran-leadership-change-by-september-30-vol-28164"
headline: "Iran leadership change by Sept 30: 11% on $28K"
semantic_title: "Iran leadership change by September 30 sits at 11% on fresh bets"
telemetry: "11% · $28K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-25T09:43:16+00:00"
event_id: "CM-EVT-TYRP27H901"
event_slug: "iran-leadership-change-by"
event_question: "Will Iran's leadership change by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x094772b3529f455e881a4483eaf1c24266384f55e97c23f24f638f5726ba9920"
  question_raw: "Iran leadership change by September 30?"
  current_price: 0.11
  volume_24h_usd: 28164.611718999997
  volume_cumulative_usd: 110712.40616899998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-30T00:00:00Z"
bullets:
  - "Polymarket prices an Iran leadership change by September 30 at 11%, elevated tail risk but not a base case."
  - "$28K in 24h marks 25% of all-time volume, exactly at the quarter-lifetime threshold, indicating renewed interest."
  - "Re-engagement at 11% likely reflects escalating regional tension, sanctions news, or internal political reporting."
  - "Contract resolves on a confirmed change in Iran's supreme leader or presidential office before September 30, 2026."
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
      poly_vol_24h_usd: 28164.611718999997
sources:
  - label: "ClearMarket market record: Will Iran's leadership change by 2026?"
    url: "https://clearmarket.fyi/events/iran-leadership-change-by"
    retrieved_at: "2026-07-25T09:43:16+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 25% lifetime-share day on an 11% geopolitical contract is an early-warning signal, macro and EM desks should cross-reference with Iran-related news flow to identify whether this is informed or reactive volume.
