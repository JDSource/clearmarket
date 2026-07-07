---
signal_id: "CMSIG20260707VS07"
signal_slug: "will-the-upper-bound-of-the-federal-fund-vol-15843"
headline: "Fed funds above 3.75% post-July: 15% on $16K"
semantic_title: "Fed funds upper bound above 3.75% post-July sits at long-shot odds"
telemetry: "15% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-07T10:52:51+00:00"
event_id: "CM-EVT-PHWX2H6DM5"
event_slug: "kxfed-26jul"
event_question: "Federal funds rate upper bound, July 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUL-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Jul 29, 2026 meeting?"
  current_price: 0.15
  volume_24h_usd: 15843.69
  volume_cumulative_usd: 38956.44
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-05T18:05:00Z"
bullets:
  - "15% implies Kalshi traders see residual but minority risk of the Fed funds upper bound clearing 3.75% after July."
  - "$15.8K in 24h, 41% of all-time, is modest in absolute terms but signals renewed rate-path attention."
  - "Consistent with Spike 2 (50+ bps hike at 0%): the market prices a constrained hiking path, not zero risk."
  - "Resolves on the Fed funds upper bound exceeding 3.75% following the July 2026 FOMC decision."
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
      kalshi_vol_24h_usd: 15843.69
sources:
  - label: "ClearMarket market record: Federal funds rate upper bound, July 2026 meeting"
    url: "https://clearmarket.fyi/events/kxfed-26jul"
    retrieved_at: "2026-07-07T10:52:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 15% price alongside the 0% on 50+ bps hikes creates a coherent picture, a desk should read this as the market pricing a small chance of incremental tightening, not a shock move, making it a useful calibration point for rates curve positioning.
