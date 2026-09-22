---
signal_id: "CMSIG20260922VS00"
signal_slug: "will-russia-enter-dopropillia-by-decembe-vol-102081"
headline: "Russia in Dopropillia by Dec 31: 97% on $102K surge"
semantic_title: "Traders back Russia taking Dopropillia by year-end"
telemetry: "97% · $102K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-22T13:04:04+00:00"
event_id: "CM-EVT-7G3FWY0RL4"
event_slug: "which-cities-will-russia-enter-by-december-31"
event_question: "Will Russia enter any additional cities by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6557ff312837c0707d82bc2def893572289e012cff21a264593c6551f85d7e50"
  question_raw: "Will Russia enter Dopropillia by December 31, 2026?"
  current_price: 0.966
  volume_24h_usd: 102081.180747
  volume_cumulative_usd: 358238.12304799986
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "At 97%, Polymarket treats Russian entry into Dopropillia before December 31 as near-certain."
  - "24h volume of $102K is 28% of all-time handle, a sharp one-day concentration of capital."
  - "Fresh attention likely trails battlefield reporting; a contract this deep needs active sellers to stay liquid."
  - "Resolves December 31, 2026, little time for a reversal to matter at these odds."
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
      poly_vol_24h_usd: 102081.180747
sources:
  - label: "ClearMarket market record: Will Russia enter any additional cities by December 31?"
    url: "https://clearmarket.fyi/events/which-cities-will-russia-enter-by-december-31"
    retrieved_at: "2026-09-22T13:04:04+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-unanimous pricing at 97% with a heavy single-day volume share signals the desk should treat Dopropillia as a consensus-captured geopolitical input and watch for any seller willing to fade near the ceiling.
