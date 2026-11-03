---
signal_id: "CMSIG20261103VS06"
signal_slug: "will-republicans-win-the-senate-race-in-vol-142075"
headline: "Louisiana GOP Senate: 87% on $142K surge"
semantic_title: "Louisiana Senate race heavily backed for Republicans at 87%"
telemetry: "87% · $142K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-03T07:49:22+00:00"
event_id: "CM-EVT-862GRMT4M0"
event_slug: "kxsenatela-26nov"
event_question: "Will there be a Louisiana Senate winner by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSENATELA-26NOV-R"
  question_raw: "Will Republicans win the Senate race in Louisiana?"
  current_price: 0.87
  volume_24h_usd: 142075.44
  volume_cumulative_usd: 267671.13
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Republican Louisiana Senate win at 87%, a near-lock but with residual uncertainty."
  - "53% of all-time volume arrived today as Election Night flow concentrates into settled races."
  - "At 87%, the market is pricing a strong but not certain outcome, leaving room for a surprise."
  - "Resolves on certified Louisiana Senate results."
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
      kalshi_vol_24h_usd: 142075.44
sources:
  - label: "ClearMarket market record: Will there be a Louisiana Senate winner by January 4, 2"
    url: "https://clearmarket.fyi/events/kxsenatela-26nov"
    retrieved_at: "2026-11-03T07:49:22+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume into an 87% Republican contract on Election Day signals desks are treating Louisiana as resolved but keeping a small tail position open pending official results.
