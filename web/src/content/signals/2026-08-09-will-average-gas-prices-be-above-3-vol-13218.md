---
signal_id: "CMSIG20260809VS06"
signal_slug: "will-average-gas-prices-be-above-3-vol-13218"
headline: "Gas above $3.980: 99% on $13K inflow"
semantic_title: "Gas prices above $3.98 priced at 99% on Kalshi"
telemetry: "99% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-09T08:37:25+00:00"
event_id: "CM-EVT-FCL1JMT0V9"
event_slug: "kxaaagasw-26aug10"
event_question: "AAA national average gas price, August 17, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAAAGASW-26AUG10-3.980"
  question_raw: "Will average **gas prices** be above $3.980?"
  current_price: 0.99
  volume_24h_usd: 13218.63
  volume_cumulative_usd: 27523.21
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-17T14:00:00Z"
bullets:
  - "Kalshi prices average national gas above $3.980 at 99%, traders see the threshold as already cleared."
  - "24h volume of $13K is 48% of all-time handle, pulling in fresh capital as the data window approaches close."
  - "At ceiling-adjacent pricing, the volume surge is likely late position-taking ahead of the official EIA or AAA price read."
  - "Contract resolves against the relevant weekly average gas price benchmark."
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
      kalshi_vol_24h_usd: 13218.63
sources:
  - label: "ClearMarket market record: AAA national average gas price, August 17, 2026"
    url: "https://clearmarket.fyi/events/kxaaagasw-26aug10"
    retrieved_at: "2026-08-09T08:37:25+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-certain pricing drawing half a contract's lifetime volume signals last-minute confirmation trading, useful context for desks monitoring consumer energy cost pass-through ahead of the official print.
