---
signal_id: "CMSIG20260905VS01"
signal_slug: "will-bloom-energy-be-added-to-the-s-p-50-vol-20768"
headline: "Bloom Energy S&P 500 Q3 add: 99% on $20K volume surge"
semantic_title: "Bloom Energy S&P 500 inclusion by Q3 locks near certainty on heavy flow"
telemetry: "99% · $21K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-05T11:35:07+00:00"
event_id: "CM-EVT-5V26ZRYCT7"
event_slug: "kxsp500addq-26sep30"
event_question: "Which companies will be added to the S&P 500 in Q3?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSP500ADDQ-26SEP30-BE"
  question_raw: "Will Bloom Energy be added to the S&P 500 in Q3 2026?"
  current_price: 0.99
  volume_24h_usd: 20768.37
  volume_cumulative_usd: 39204.14
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-30T14:00:00Z"
bullets:
  - "Kalshi prices Bloom Energy's Q3 2026 S&P 500 inclusion at 99%, market treats the outcome as effectively settled."
  - "24h volume of $20.8K represents 53% of the contract's entire all-time volume, a massive single-session concentration."
  - "Q3 ends Sept 30; with the deadline days away, late traders are either locking in gains or taking a final position before resolution."
  - "Contract resolves on whether S&P Dow Jones Indices officially adds Bloom Energy to the S&P 500 before Q3 close."
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
      kalshi_vol_24h_usd: 20768.37
sources:
  - label: "ClearMarket market record: Which companies will be added to the S&P 500 in Q3?"
    url: "https://clearmarket.fyi/events/kxsp500addq-26sep30"
    retrieved_at: "2026-09-05T11:35:07+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

More than half the contract's lifetime volume printing in one session at 99% signals end-of-quarter position squaring, a desk closing out or topping up ahead of near-certain resolution.
