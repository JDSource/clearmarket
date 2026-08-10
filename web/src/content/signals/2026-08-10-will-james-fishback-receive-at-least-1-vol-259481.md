---
signal_id: "CMSIG20260810VS00"
signal_slug: "will-james-fishback-receive-at-least-1-vol-259481"
headline: "Fishback FL popular vote: 100% on $259K surge"
semantic_title: "Fishback Florida 1% threshold locked in at full odds"
telemetry: "100% · $259K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-10T09:15:14+00:00"
event_id: "CM-EVT-3BTF9D60C9"
event_slug: "kxvoteprimary-govflnomr26jfis"
event_question: "Will James Fishback receive more than X percent of the vote in the Florida Republican Governor primary?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXVOTEPRIMARY-GOVFLNOMR26JFIS-50"
  question_raw: "Will James Fishback receive at least 1% of the popular vote in the 2026 Florida Republican Governor primary?"
  current_price: 0.998
  volume_24h_usd: 259481.24
  volume_cumulative_usd: 821858.08
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-08-18T14:00:00Z"
bullets:
  - "Kalshi prices Fishback clearing the 1% Florida popular-vote bar at 100%, effectively resolved."
  - "24h volume of $259K equals 32% of the contract's entire all-time handle, a late-stage rush."
  - "Near-certainty pricing suggests the vote count is in or nearly certified, drawing settlement traders."
  - "Contract resolves on certified Florida 2026 election results; no meaningful outcome risk remains."
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
      kalshi_vol_24h_usd: 259481.24
sources:
  - label: "ClearMarket market record: Will James Fishback receive more than X percent of the "
    url: "https://clearmarket.fyi/events/kxvoteprimary-govflnomr26jfis"
    retrieved_at: "2026-08-10T09:15:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should treat this as a near-resolved settlement flow event, not a live directional trade, the volume reflects final reconciliation, not fresh speculation.
