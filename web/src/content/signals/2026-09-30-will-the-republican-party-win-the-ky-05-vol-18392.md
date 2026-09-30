---
signal_id: "CMSIG20260930VS06"
signal_slug: "will-the-republican-party-win-the-ky-05-vol-18392"
headline: "KY-05 GOP House: 97% on $18K, 49% of all-time"
semantic_title: "KY-05 GOP at 97% as buyers back the heavy favorite"
telemetry: "97% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-30T07:48:11+00:00"
event_id: "CM-EVT-BL7L8MBY65"
event_slug: "ky-05-house-election-winner"
event_question: "KY-05 House Election Winner"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7282c5b2ced91d830069f1dbb54feb75c3088b63035714a0b6d1ed35056e4745"
  question_raw: "Will the Republican Party win the KY-05 House seat?"
  current_price: 0.971
  volume_24h_usd: 18392.549666
  volume_cumulative_usd: 37824.75348200001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Republicans at 97% to win Kentucky's 5th House seat, effectively a resolved outcome in the market's view."
  - "$18K in 24h is 49% of all-time volume, meaning nearly half of all lifetime liquidity arrived in one session."
  - "KY-05 is one of the most Republican districts in the country; volume may reflect arbitrage or contract settlement positioning."
  - "Contract resolves on the November 2026 KY-05 general election; outcome broadly viewed as a foregone conclusion."
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
      poly_vol_24h_usd: 18392.549666
sources:
  - label: "ClearMarket market record: KY-05 House Election Winner"
    url: "https://clearmarket.fyi/events/ky-05-house-election-winner"
    retrieved_at: "2026-09-30T07:48:11+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 97% contract drawing half its all-time volume in one day is likely settlement arbitrage or mechanical positioning rather than genuine uncertainty, useful as a baseline for district-level market efficiency checks.
