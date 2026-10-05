---
signal_id: "CMSIG20261005VS01"
signal_slug: "will-luiz-in-cio-lula-da-silva-win-the-2-vol-139134"
headline: "Lula 2026 Brazil win: 18% on $139K vol"
semantic_title: "Lula 2026 re-election stays a long shot at 18%"
telemetry: "18% · $139K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-05T16:45:18+00:00"
event_id: "CM-EVT-DKSKHZR435"
event_slug: "kxbrpres-26"
event_question: "Will the winner of Brazil's next presidential election be determined by October 25, 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBRPRES-26-LULA"
  question_raw: "Will Luiz Inácio Lula da Silva win the 2026 Brazilian presidential election?"
  current_price: 0.18
  volume_24h_usd: 139134.09
  volume_cumulative_usd: 407466.25
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-25T14:00:00Z"
bullets:
  - "Kalshi prices Lula at just 18%, the market treats a second term as an outside scenario."
  - "34% of all-time volume landed in 24 hours, the sharpest single-session concentration on this contract."
  - "Brazil political headlines, coalition stress, approval ratings, are likely driving fresh positioning."
  - "Resolves on the 2026 Brazilian presidential election outcome."
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
      kalshi_vol_24h_usd: 139134.09
sources:
  - label: "ClearMarket market record: Will the winner of Brazil's next presidential election "
    url: "https://clearmarket.fyi/events/kxbrpres-26"
    retrieved_at: "2026-10-05T16:45:18+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 34% all-time share in one session on an 18% contract suggests a desk is either building or unwinding a meaningful Brazil political-risk position ahead of expected news flow.
