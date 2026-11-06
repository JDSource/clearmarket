---
signal_id: "CMSIG20261106VS06"
signal_slug: "will-dan-sullivan-win-the-2026-alaska-se-vol-19387"
headline: "Sullivan Alaska Senate win: 4% on $19K at Kalshi"
semantic_title: "Dan Sullivan Alaska Senate odds collapse to 4% on fresh volume"
telemetry: "4% · $19K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-06T15:37:54+00:00"
event_id: "CM-EVT-6KJ40RJZP3"
event_slug: "kxaksenate-26nov03"
event_question: "Who will win the Alaska Senate election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAKSENATE-26NOV03-DSUL"
  question_raw: "Will Dan Sullivan win the 2026 Alaska Senate race?"
  current_price: 0.037
  volume_24h_usd: 19387.34
  volume_cumulative_usd: 64988.74
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-10T15:00:00Z"
bullets:
  - "At 4%, Kalshi has effectively ruled out a Sullivan victory in the 2026 Alaska Senate race."
  - "$19K in 24h is 30% of all-time volume, meaningful fresh engagement on an extreme-probability contract."
  - "Volume at 4% pricing may reflect late hedging, closing positions, or a news event cementing the outcome."
  - "Resolution at the certified result of the 2026 Alaska Senate election."
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
      kalshi_vol_24h_usd: 19387.34
sources:
  - label: "ClearMarket market record: Who will win the Alaska Senate election?"
    url: "https://clearmarket.fyi/events/kxaksenate-26nov03"
    retrieved_at: "2026-11-06T15:37:54+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Fresh volume entering a 4% contract is unusual and likely reflects position liquidation or a late-breaking development that has closed off any remaining path for Sullivan, desks tracking Senate control math should update accordingly.
