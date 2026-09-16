---
signal_id: "CMSIG20260916VS01"
signal_slug: "will-democratics-win-the-senate-race-in-vol-94724"
headline: "NH Senate Dem win: 82% on $95K volume surge"
semantic_title: "Democrats heavily favored in New Hampshire Senate race"
telemetry: "82% · $95K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-16T13:03:41+00:00"
event_id: "CM-EVT-NF2DF1TXH9"
event_slug: "senatenh-26"
event_question: "New Hampshire Senate winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATENH-26-D"
  question_raw: "Will Democratics win the Senate race in New Hampshire?"
  current_price: 0.82
  volume_24h_usd: 94724.94
  volume_cumulative_usd: 210932.64
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices Democratic victory at 82%, a strong lean that leaves meaningful tail risk for a Republican upset."
  - "$94.7K in 24h represents 45% of all-time volume, signaling a sharp spike in market attention."
  - "Fresh conviction at this level likely tracks new polling, candidate news, or early-vote data from New Hampshire."
  - "Race resolves on 2026 midterm election night; pricing above 80% invites hedging interest on the 18% Republican side."
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
      kalshi_vol_24h_usd: 94724.94
sources:
  - label: "ClearMarket market record: New Hampshire Senate winner?"
    url: "https://clearmarket.fyi/events/senatenh-26"
    retrieved_at: "2026-09-16T13:03:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy one-session volume at an 82% Democratic price flags this NH Senate contest as a key midterm bellwether, desks should monitor for catalyst news driving the conviction surge.
