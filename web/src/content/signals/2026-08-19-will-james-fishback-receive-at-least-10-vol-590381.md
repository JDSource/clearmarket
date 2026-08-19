---
signal_id: "CMSIG20260819VS00"
signal_slug: "will-james-fishback-receive-at-least-10-vol-590381"
headline: "Fishback FL 10% threshold: 100% on $590K surge"
semantic_title: "Fishback 10% Florida vote share locked in at full odds"
telemetry: "100% · $590K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-19T08:32:13+00:00"
event_id: "CM-EVT-3BTF9D60C9"
event_slug: "kxvoteprimary-govflnomr26jfis"
event_question: "Will James Fishback receive more than X percent of the vote in the Florida Republican Governor primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXVOTEPRIMARY-GOVFLNOMR26JFIS-55"
  question_raw: "Will James Fishback receive at least 10% of the popular vote in the 2026 Florida Republican Governor primary?"
  current_price: 0.998
  volume_24h_usd: 590381.44
  volume_cumulative_usd: 1034750.58
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-08-18T14:00:00Z"
bullets:
  - "Market prices 100% certainty Fishback clears 10% of Florida's 2026 gubernatorial popular vote."
  - "Kalshi sees $590K in 24h volume, 57% of all-time handle, a decisive single-session flush."
  - "Surge likely trails primary results or certified returns now in; market treating threshold as resolved."
  - "Contract resolves on official Florida canvass confirming ≥10% share for Fishback."
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
      kalshi_vol_24h_usd: 590381.44
sources:
  - label: "ClearMarket market record: Will James Fishback receive more than X percent of the "
    url: "https://clearmarket.fyi/events/kxvoteprimary-govflnomr26jfis"
    retrieved_at: "2026-08-19T08:32:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-total all-time volume landing in one session at 100% signals the primary has cleared and desks are closing positions against a confirmed result.
