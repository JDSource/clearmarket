---
signal_id: "CMSIG20261105VS04"
signal_slug: "will-republicans-win-the-senate-race-in-vol-303832"
headline: "AK Senate GOP win: 5% as half of all-time vol clears"
semantic_title: "Republican Alaska Senate odds stay under 10% at 50% volume mark"
telemetry: "5% · $304K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-05T07:49:08+00:00"
event_id: "CM-EVT-KQWMXB6NX7"
event_slug: "senateak-26"
event_question: "Will a new senator be elected to represent Alaska in the U.S. Senate?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEAK-26-R"
  question_raw: "Will Republicans win the Senate race in Alaska?"
  current_price: 0.049
  volume_24h_usd: 303832.33
  volume_cumulative_usd: 611931.67
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Republican Alaska Senate win at just 5%, reflecting near-total market rejection of the outcome."
  - "50% of all-time volume on this contract, $303K, cleared in 24 hours, a significant Election Day flush."
  - "Counterpart 'Democrats win' contract (Spike 0) is at 95%, confirming the two contracts are pricing consistently."
  - "Resolves on certified Alaska result; the 5% tail represents tail risk on late or contested counts."
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
      kalshi_vol_24h_usd: 303832.33
sources:
  - label: "ClearMarket market record: Will a new senator be elected to represent Alaska in th"
    url: "https://clearmarket.fyi/events/senateak-26"
    retrieved_at: "2026-11-05T07:49:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The mirror of the Democratic Alaska contract, heavy volume at 5% confirms the market is not hedging a GOP upset; the desk can treat Alaska as priced closed barring anomalous results.
