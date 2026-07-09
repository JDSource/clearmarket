---
signal_id: "CMSIG20260709VS01"
signal_slug: "will-miguel-d-az-canel-be-the-next-leade-vol-615135"
headline: "Díaz-Canel out before 2027: 0% on $615K volume"
semantic_title: "Díaz-Canel departure before 2027 seen as remote by heavy flows"
telemetry: "0% · $615K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-09T10:57:00+00:00"
event_id: "CM-EVT-2FLCV9PNS4"
event_slug: "next-leader-out-of-power-before-2027-no-orban"
event_question: "Will the next leader out of power before 2027 be someone other than Orban?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x068b8f7779e1f0a778778cd4e4add33b6c5076fc7350c32f11785bae56c4cd7b"
  question_raw: "Will Miguel Díaz-Canel be the next leader out before 2027?"
  current_price: 0.002
  volume_24h_usd: 615135.7200000001
  volume_cumulative_usd: 1262190.5171629998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Price at 0%, market assigns no realistic probability to a Díaz-Canel exit this year."
  - "$615K in 24h is 49% of all-time; substantial two-sided conviction collapsing to zero."
  - "Cuba's economic and political stress has drawn speculative positioning; volume reflects washout of that thesis."
  - "Resolves before 2027; desks appear to be clearing Cuba regime-change exposure."
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
      poly_vol_24h_usd: 615135.7200000001
sources:
  - label: "ClearMarket market record: Will the next leader out of power before 2027 be someon"
    url: "https://clearmarket.fyi/events/next-leader-out-of-power-before-2027-no-orban"
    retrieved_at: "2026-07-09T10:57:00+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Nearly half the contract's lifetime volume printing in a single session at zero indicates a rapid consensus flush, traders who held regime-change optionality on Cuba are exiting en masse.
