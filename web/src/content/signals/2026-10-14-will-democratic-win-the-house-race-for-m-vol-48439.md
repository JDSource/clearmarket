---
signal_id: "CMSIG20261014VS02"
signal_slug: "will-democratic-win-the-house-race-for-m-vol-48439"
headline: "MN-05 Dem seat: 93% on $48K one-day spike"
semantic_title: "MN-05 Democratic hold trades near certainty on fresh volume"
telemetry: "93% · $48K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-14T07:48:34+00:00"
event_id: "CM-EVT-1F7LPV1P19"
event_slug: "kxhouserace-mn05-26"
event_question: "MN-05 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-MN05-26-D"
  question_raw: "Will Democratic win the House race for MN-05?"
  current_price: 0.931
  volume_24h_usd: 48439.41
  volume_cumulative_usd: 91489.88
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "93% price leaves just 7 cents of doubt, market treats a Democratic hold in Minneapolis's deep-blue district as nearly resolved."
  - "24h volume of $48K is 53% of all-time handle, suggesting fresh capital is testing, and confirming, the consensus."
  - "Attention here may reflect broader midterm portfolio hedging rather than genuine district uncertainty."
  - "Resolves on 2026 election night; only a dramatic national wave scenario would reprice this contract."
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
      kalshi_vol_24h_usd: 48439.41
sources:
  - label: "ClearMarket market record: MN-05 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-mn05-26"
    retrieved_at: "2026-10-14T07:48:34+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

High volume at 93% on a non-competitive seat suggests traders are using MN-05 as a baseline anchor for Democratic House floor estimates, useful context for broader seat-count models.
