---
signal_id: "CMSIG20260725VS06"
signal_slug: "will-average-gas-prices-be-above-4-vol-17791"
headline: "Gas above $4.110: 80% on $18K; most lifetime vol"
semantic_title: "Gas above $4.110 holds at 80% as traders back the threshold"
telemetry: "80% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-25T09:43:16+00:00"
event_id: "CM-EVT-7BTG22H1X4"
event_slug: "kxaaagasw-26jul27"
event_question: "Average **gas prices**"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAAAGASW-26JUL27-4.110"
  question_raw: "Will average **gas prices** be above $4.110?"
  current_price: 0.8
  volume_24h_usd: 17791.9
  volume_cumulative_usd: 26544.23
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-03T14:00:00Z"
bullets:
  - "Kalshi prices average gas above $4.110 at 80%, a strong lean, but 20% residual uncertainty remains."
  - "$18K in 24h is 67% of all-time volume, the highest lifetime-share of any spike today, on a thin contract."
  - "Paired with the $4.10 contract at 98%, the spread reveals traders are pricing genuine uncertainty in the 1-cent band."
  - "The $4.110 threshold is the live decision point; this is where new information about pump prices will move odds."
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
      kalshi_vol_24h_usd: 17791.9
sources:
  - label: "ClearMarket market record: Average **gas prices**"
    url: "https://clearmarket.fyi/events/kxaaagasw-26jul27"
    retrieved_at: "2026-07-25T09:43:16+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 67% lifetime-share on a thin contract means today's flow is the dominant price signal, a desk tracking gasoline inflation should watch this contract as the live marginal indicator between $4.10 and $4.110.
