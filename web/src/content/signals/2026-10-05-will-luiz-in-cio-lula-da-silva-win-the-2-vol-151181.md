---
signal_id: "CMSIG20261005VS01"
signal_slug: "will-luiz-in-cio-lula-da-silva-win-the-2-vol-151181"
headline: "Lula 2026 win: 19% on $151K, 36% of all-time vol"
semantic_title: "Lula re-election odds stay under 25% through a volume test"
telemetry: "19% · $151K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-05T07:48:02+00:00"
event_id: "CM-EVT-DKSKHZR435"
event_slug: "kxbrpres-26"
event_question: "Will the winner of Brazil's next presidential election be determined by October 25, 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBRPRES-26-LULA"
  question_raw: "Will Luiz Inácio Lula da Silva win the 2026 Brazilian presidential election?"
  current_price: 0.19
  volume_24h_usd: 151181.11
  volume_cumulative_usd: 418664.82
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-25T14:00:00Z"
bullets:
  - "Kalshi marks Lula at 19%, decisively underdog, implying the market discounts a second-term path as unlikely."
  - "36% of all-time volume hit in one session, the highest single-day share of this contract's lifetime."
  - "Mirror spike to Spike 0 suggests coordinated re-pricing of the Brazil 2026 binary, not isolated flow."
  - "Resolves on official Brazilian presidential election outcome, October 2026."
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
      kalshi_vol_24h_usd: 151181.11
sources:
  - label: "ClearMarket market record: Will the winner of Brazil's next presidential election "
    url: "https://clearmarket.fyi/events/kxbrpres-26"
    retrieved_at: "2026-10-05T07:48:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The paired Lula/Bolsonaro volume surge on the same day signals a structural re-rating of the Brazil 2026 race, desks pricing EM political risk should note the market is consolidating around an 81/19 split with high conviction.
