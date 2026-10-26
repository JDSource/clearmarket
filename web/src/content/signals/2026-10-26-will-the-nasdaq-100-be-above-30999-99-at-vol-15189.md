---
signal_id: "CMSIG20261026VS06"
signal_slug: "will-the-nasdaq-100-be-above-30999-99-at-vol-15189"
headline: "Nasdaq-100 above 31K Dec 31: 99% on $15K"
semantic_title: "Nasdaq-100 above 31K by year-end stays a near-certain bet at 99%"
telemetry: "99% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-26T07:48:41+00:00"
event_id: "CM-EVT-HYFSJ2CNW7"
event_slug: "kxnasdaq100maxy-26dec31h1600"
event_question: "What will be the highest price reached by the Nasdaq-100 in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXNASDAQ100MAXY-26DEC31H1600-T30999.99"
  question_raw: "Will the Nasdaq-100 be above 30999.99 at the end of Dec 31, 2026 at 4pm EST?"
  current_price: 0.99
  volume_24h_usd: 15189.78
  volume_cumulative_usd: 36468.52
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-08T00:00:00Z"
bullets:
  - "Market prices a 99% chance the Nasdaq-100 clears 30,999.99 at the Dec 31 close."
  - "42% of all-time Kalshi volume on this contract arrived in one session."
  - "At current index levels well above the threshold, fresh volume likely reflects hedging or yield-seeking on near-certain contracts."
  - "Resolves at 4 pm EST on December 31, 2026."
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
      kalshi_vol_24h_usd: 15189.78
sources:
  - label: "ClearMarket market record: What will be the highest price reached by the Nasdaq-10"
    url: "https://clearmarket.fyi/events/kxnasdaq100maxy-26dec31h1600"
    retrieved_at: "2026-10-26T07:48:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-certainty pricing with a fresh volume spike on a deep in-the-money index contract signals carry or hedge activity rather than directional conviction, a desk should note the implied floor level as a market-consensus support reference.
