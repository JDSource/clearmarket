---
signal_id: "CMSIG20261101VS02"
signal_slug: "will-an-independent-win-the-nebraska-sen-vol-268221"
headline: "Nebraska Senate indie: 25% on $268K inflow"
semantic_title: "Independent Nebraska Senate bid stays a coin-flip near 25%"
telemetry: "25% · $268K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-01T07:49:22+00:00"
event_id: "CM-EVT-CY3W5Z2793"
event_slug: "nebraska-senate-election-winner"
event_question: "Nebraska Senate Election Winner  "
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5554740293afa7aafd5fed10fd2de43a898e2884c1f98bd65185e703f371b9db"
  question_raw: "Will an independent win the Nebraska Senate race in 2026?"
  current_price: 0.25
  volume_24h_usd: 268221.09182499995
  volume_cumulative_usd: 808570.5351510001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "At 25%, Polymarket treats an independent Senate winner as a live but uphill scenario."
  - "$268K in 24h, 33% of all-time, mirrors the concurrent Republican-leg spike, suggesting paired positioning."
  - "Nebraska's unusual political environment keeps a third-path outcome meaningfully priced."
  - "Resolves on the November 2026 election result."
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
      poly_vol_24h_usd: 268221.09182499995
sources:
  - label: "ClearMarket market record: Nebraska Senate Election Winner  "
    url: "https://clearmarket.fyi/events/nebraska-senate-election-winner"
    retrieved_at: "2026-11-01T07:49:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous spikes on both the GOP and independent legs of the Nebraska race signal desks are actively splitting exposure across the two most likely outcomes.
