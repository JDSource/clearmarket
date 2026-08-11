---
signal_id: "CMSIG20260811VS01"
signal_slug: "will-james-fishback-receive-at-least-3-vol-55153"
headline: "Fishback FL 3% threshold: 98% on $55K surge"
semantic_title: "Fishback clears 3% FL popular vote threshold at 98%"
telemetry: "98% · $55K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-11T08:50:18+00:00"
event_id: "CM-EVT-3BTF9D60C9"
event_slug: "kxvoteprimary-govflnomr26jfis"
event_question: "Will James Fishback receive more than X percent of the vote in the Florida Republican Governor primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXVOTEPRIMARY-GOVFLNOMR26JFIS-51"
  question_raw: "Will James Fishback receive at least 3% of the popular vote in the 2026 Florida Republican Governor primary?"
  current_price: 0.977
  volume_24h_usd: 55153.78
  volume_cumulative_usd: 137819.68
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-08-18T14:00:00Z"
bullets:
  - "Market prices Fishback exceeding 3% of the Florida popular vote as near-certain at 98%."
  - "$55K in 24h volume, 40% of all-time, shows a sharp acceleration in conviction."
  - "Fresh attention may follow updated polling or ballot access confirmation tightening the distribution."
  - "Resolves YES if Fishback clears 3% of the total 2026 Florida popular vote."
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
      kalshi_vol_24h_usd: 55153.78
sources:
  - label: "ClearMarket market record: Will James Fishback receive more than X percent of the "
    url: "https://clearmarket.fyi/events/kxvoteprimary-govflnomr26jfis"
    retrieved_at: "2026-08-11T08:50:18+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume at 98% suggests traders are treating a 3% Florida floor as essentially settled, possibly on fresh polling, desks monitoring third-party ballot viability in Florida should note this as a consensus signal.
