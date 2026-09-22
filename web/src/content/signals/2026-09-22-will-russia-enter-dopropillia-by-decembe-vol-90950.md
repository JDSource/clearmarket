---
signal_id: "CMSIG20260922VS01"
signal_slug: "will-russia-enter-dopropillia-by-decembe-vol-90950"
headline: "Russia enters Dopropillia by Dec 31: 97% on $91K"
semantic_title: "Traders back Russia taking Dopropillia by year-end at 97%"
telemetry: "97% · $91K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-22T07:48:31+00:00"
event_id: "CM-EVT-7G3FWY0RL4"
event_slug: "which-cities-will-russia-enter-by-december-31"
event_question: "Will Russia enter any additional cities by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6557ff312837c0707d82bc2def893572289e012cff21a264593c6551f85d7e50"
  question_raw: "Will Russia enter Dopropillia by December 31, 2026?"
  current_price: 0.97
  volume_24h_usd: 90950.499542
  volume_cumulative_usd: 342032.09405599994
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Russian entry into Dopropillia by Dec 31 at 97%, near-certain resolution already priced."
  - "$90.9K in 24h is 27% of the contract's all-time volume, suggesting a discrete field update is prompting position closes or late entry."
  - "At 97%, fresh volume likely reflects confirmed battlefield movement driving traders to lock in the consensus before resolution."
  - "Resolves Dec 31, 2026; residual 3% reflects settlement/definition risk, not strategic uncertainty."
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
      poly_vol_24h_usd: 90950.499542
sources:
  - label: "ClearMarket market record: Will Russia enter any additional cities by December 31?"
    url: "https://clearmarket.fyi/events/which-cities-will-russia-enter-by-december-31"
    retrieved_at: "2026-09-22T07:48:31+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-limit pricing with a 27% all-time volume day points to a ground-truth update on Dopropillia that desks should verify against open-source military feeds immediately.
