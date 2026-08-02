---
signal_id: "CMSIG20260802VS00"
signal_slug: "iran-leadership-change-by-august-31-vol-233112"
headline: "Iran leadership change: 3% on $233K surge"
semantic_title: "Iran regime change by Aug 31 stays a long shot at 3%"
telemetry: "3% · $233K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-02T09:53:38+00:00"
event_id: "CM-EVT-TYRP27H901"
event_slug: "iran-leadership-change-by"
event_question: "Will Iran's leadership change by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x43e12647a58ee0b20d2539d23764b0d561ea7be322acb8823f7bb126e67c115e"
  question_raw: "Iran leadership change by August 31?"
  current_price: 0.026
  volume_24h_usd: 233112.047679
  volume_cumulative_usd: 581052.6296620002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-08-31T00:00:00Z"
bullets:
  - "Polymarket prices an Iran leadership change by Aug 31 at just 3%, near-zero odds with 29 days left."
  - "24h volume of $233K is 40% of all-time handle, signaling an acute burst of fresh attention on a thin-probability contract."
  - "Spike likely reflects geopolitical news flow, regional tensions or Israeli/U.S. escalation chatter driving traders to define tail-risk exposure."
  - "Contract resolves Aug 31; any unresolved escalation rolls into the September contract (Spike 1)."
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
      poly_vol_24h_usd: 233112.047679
sources:
  - label: "ClearMarket market record: Will Iran's leadership change by 2026?"
    url: "https://clearmarket.fyi/events/iran-leadership-change-by"
    retrieved_at: "2026-08-02T09:53:38+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 40%-of-all-time volume burst into a 3% contract signals desks are paying premium for tail-risk definition on a near-term Iran scenario, not expressing directional conviction.
