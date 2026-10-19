---
signal_id: "CMSIG20261019VS00"
signal_slug: "will-the-democratic-party-win-the-attorn-vol-47001"
headline: "NY AG race: 92% on $47K Kalshi surge"
semantic_title: "Buyers back NY AG staying Democratic by a wide margin"
telemetry: "92% · $47K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-19T15:15:12+00:00"
event_id: "CM-EVT-2WVDLYDTS5"
event_slug: "kxattygenny-26"
event_question: "Will the New York Attorney General race be decided by January 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXATTYGENNY-26-D"
  question_raw: "Will the Democratic party win the Attorney General race in New York?"
  current_price: 0.915
  volume_24h_usd: 47001.06
  volume_cumulative_usd: 172426.05
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-02T15:00:00Z"
bullets:
  - "At 92%, the market treats a Democratic hold of the New York AG seat as near-certain."
  - "Today's $47K inflow is 27% of all-time volume, a sharp concentration of fresh conviction."
  - "Renewed activity may track a candidate filing deadline, polling drop, or Republican field development."
  - "Contract resolves on the 2026 New York Attorney General election result."
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
      kalshi_vol_24h_usd: 47001.06
sources:
  - label: "ClearMarket market record: Will the New York Attorney General race be decided by J"
    url: "https://clearmarket.fyi/events/kxattygenny-26"
    retrieved_at: "2026-10-19T15:15:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The heavy one-day skew toward maximum probability signals a desk positioning against any residual tail risk of a Republican upset in the NY AG race.
