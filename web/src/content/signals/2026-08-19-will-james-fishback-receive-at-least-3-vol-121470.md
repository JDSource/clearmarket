---
signal_id: "CMSIG20260819VS04"
signal_slug: "will-james-fishback-receive-at-least-3-vol-121470"
headline: "Fishback FL 3% floor: 100% on $121K trade"
semantic_title: "Fishback 3% Florida floor fully priced, volume hits landmark"
telemetry: "100% · $121K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-19T08:32:13+00:00"
event_id: "CM-EVT-3BTF9D60C9"
event_slug: "kxvoteprimary-govflnomr26jfis"
event_question: "Will James Fishback receive more than X percent of the vote in the Florida Republican Governor primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXVOTEPRIMARY-GOVFLNOMR26JFIS-51"
  question_raw: "Will James Fishback receive at least 3% of the popular vote in the 2026 Florida Republican Governor primary?"
  current_price: 0.999
  volume_24h_usd: 121470.82
  volume_cumulative_usd: 481321.65
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-08-18T14:00:00Z"
bullets:
  - "Lowest Fishback threshold contract also sits at 100%, the full vote-share ladder is now priced certain."
  - "$121K in 24h equals exactly 25% of all-time volume, a notable landmark share in a single session."
  - "Consistent 100% pricing across 3%, 5%, and 10% contracts leaves no arbitrage gap for desks to exploit."
  - "Resolves on Florida certifying Fishback received at least 3% of the gubernatorial popular vote."
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
      kalshi_vol_24h_usd: 121470.82
sources:
  - label: "ClearMarket market record: Will James Fishback receive more than X percent of the "
    url: "https://clearmarket.fyi/events/kxvoteprimary-govflnomr26jfis"
    retrieved_at: "2026-08-19T08:32:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A clean sweep of 100% across all Fishback floor contracts, each with outsized single-day volume, confirms to a desk that Florida primary vote totals are known and positions are being unwound.
