---
signal_id: "CMSIG20261004VS02"
signal_slug: "will-luiz-in-cio-lula-da-silva-win-the-f-vol-46793"
headline: "Lula first-round: 64% on $47K Kalshi spike"
semantic_title: "Kalshi traders back Lula first-round victory at 64%"
telemetry: "64% · $47K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-04T13:40:01+00:00"
event_id: "CM-EVT-NWN8Q06H64"
event_slug: "kxbrpres1r-26oct04"
event_question: "Will there be a first round winner in the Brazil presidential election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBRPRES1R-26OCT04-LSIL"
  question_raw: "Will Luiz Inácio Lula da Silva win the first round of the 2026 Brazilian presidential election?"
  current_price: 0.64
  volume_24h_usd: 46793.7
  volume_cumulative_usd: 123252.89
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-04T14:00:00Z"
bullets:
  - "Kalshi prices a Lula first-round majority at 64%, a meaningful favorite, contrasting sharply with Polymarket's 10% on the same question."
  - "$46,794 in 24h is 38% of all-time volume on this Kalshi contract, signaling focused fresh conviction."
  - "The wide cross-venue spread (64% vs. 10%) suggests different contract definitions, likely differing thresholds or resolution criteria."
  - "Resolves YES if Lula exceeds 50% of valid votes in round one."
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
      kalshi_vol_24h_usd: 46793.7
sources:
  - label: "ClearMarket market record: Will there be a first round winner in the Brazil presid"
    url: "https://clearmarket.fyi/events/kxbrpres1r-26oct04"
    retrieved_at: "2026-10-04T13:40:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The stark price divergence between Kalshi (64%) and Polymarket (10%) on an apparently similar question demands immediate contract-spec review, desks should confirm resolution criteria before treating either as a benchmark.
