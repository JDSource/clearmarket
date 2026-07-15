---
signal_id: "CMSIG20260715VS00"
signal_slug: "will-china-gdp-growth-in-q2-2026-be-betw-vol-35776"
headline: "China Q2 GDP 4.3, 4.6% band: 100% on $35K surge"
semantic_title: "China Q2 GDP 4.3, 4.6% band locked in at full conviction"
telemetry: "100% · $36K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-15T10:00:41+00:00"
event_id: "CM-EVT-ZX9NJMKMD0"
event_slug: "china-gdp-growth-yy-in-q2-2026"
event_question: "Will China's year-over-year GDP growth in Q2 2026 be above 5%?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7ccef198fac90ac8a29aed052fc8c5c08b16bff84b3b4ded112248a9d8f885c2"
  question_raw: "Will China GDP growth in Q2 2026 be between 4.3% and 4.6%?"
  current_price: 0.996
  volume_24h_usd: 35776.64350300001
  volume_cumulative_usd: 64882.21696699998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-07-16T00:00:00Z"
bullets:
  - "Market prices 100% certainty the 4.3, 4.6% band captured official Q2 GDP, contract effectively settled."
  - "24h volume of $35,777 equals 55% of all-time handle, signaling a decisive resolution flush."
  - "China's Q2 2026 GDP release has likely landed within the band, collapsing residual uncertainty."
  - "Resolves YES; remaining flow is arb-driven redemption or hedging of correlated macro positions."
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
      poly_vol_24h_usd: 35776.64350300001
sources:
  - label: "ClearMarket market record: Will China's year-over-year GDP growth in Q2 2026 be ab"
    url: "https://clearmarket.fyi/events/china-gdp-growth-yy-in-q2-2026"
    retrieved_at: "2026-07-15T10:00:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The surge at 100% marks a near-certain post-print resolution trade, desks should treat this as a confirmed data point for China growth narratives rather than a live market signal.
