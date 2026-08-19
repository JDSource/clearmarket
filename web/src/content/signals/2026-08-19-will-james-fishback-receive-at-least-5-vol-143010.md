---
signal_id: "CMSIG20260819VS02"
signal_slug: "will-james-fishback-receive-at-least-5-vol-143010"
headline: "Fishback FL 5% bar: 100% on $143K inflow"
semantic_title: "Fishback 5% Florida bar priced as certain after primary"
telemetry: "100% · $143K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-19T08:32:13+00:00"
event_id: "CM-EVT-3BTF9D60C9"
event_slug: "kxvoteprimary-govflnomr26jfis"
event_question: "Will James Fishback receive more than X percent of the vote in the Florida Republican Governor primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXVOTEPRIMARY-GOVFLNOMR26JFIS-52"
  question_raw: "Will James Fishback receive at least 5% of the popular vote in the 2026 Florida Republican Governor primary?"
  current_price: 0.999
  volume_24h_usd: 143010.85
  volume_cumulative_usd: 365108.08
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-08-18T14:00:00Z"
bullets:
  - "100% price implies the market considers Fishback's 5% Florida vote-share threshold already cleared."
  - "$143K in 24h represents 39% of all-time volume, notable compression of activity into one session."
  - "Paired with the 10% contract also at 100%, the pattern confirms primary results are circulating."
  - "Resolves on Florida's official canvass showing Fishback at or above 5% of the popular vote."
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
      kalshi_vol_24h_usd: 143010.85
sources:
  - label: "ClearMarket market record: Will James Fishback receive more than X percent of the "
    url: "https://clearmarket.fyi/events/kxvoteprimary-govflnomr26jfis"
    retrieved_at: "2026-08-19T08:32:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous full-odds pricing across multiple Fishback thresholds tells a desk the vote totals are public and all share-floor contracts are effectively settled.
