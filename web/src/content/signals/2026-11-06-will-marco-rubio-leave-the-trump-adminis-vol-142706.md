---
signal_id: "CMSIG20261106VS00"
signal_slug: "will-marco-rubio-leave-the-trump-adminis-vol-142706"
headline: "Rubio leaves Trump admin: 16% on $143K surge"
semantic_title: "Rubio exit odds stay low despite heavy trading"
telemetry: "16% · $143K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-06T07:48:47+00:00"
event_id: "CM-EVT-KZSP2MGN63"
event_slug: "who-will-leave-trump-administration-before-2027"
event_question: "Will anyone leave the Trump Administration before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x48a3e95c0bc1b9305e56445a7affcb857fd61e0ae0d78a4778310a1108ceb08a"
  question_raw: "Will Marco Rubio leave the Trump administration before 2027?"
  current_price: 0.16
  volume_24h_usd: 142706.212101
  volume_cumulative_usd: 173106.12953900005
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Market prices only a 16% chance Rubio exits the Trump administration before 2027, implying strong tenure odds."
  - "Polymarket logged $143K in 24h volume, 82% of the contract's entire all-time volume, signaling a sharp burst of fresh attention."
  - "Surge likely triggered by recent reports or political developments around Rubio's standing; fresh volume often precedes news."
  - "Contract resolves if Rubio leaves any Trump administration role before January 1, 2027."
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
      poly_vol_24h_usd: 142706.212101
sources:
  - label: "ClearMarket market record: Will anyone leave the Trump Administration before 2027?"
    url: "https://clearmarket.fyi/events/who-will-leave-trump-administration-before-2027"
    retrieved_at: "2026-11-06T07:48:47+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

An 82% all-time volume flush into a 16% 'yes' price means desks are actively stress-testing Rubio's tenure stability against a specific near-term catalyst, not repricing him as gone.
