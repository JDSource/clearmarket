---
signal_id: "CMSIG20261010VS05"
signal_slug: "will-democratic-win-the-house-race-for-n-vol-10413"
headline: "NY-21 Dem House: 25% on $10K surge"
semantic_title: "Democrats slip under 25% in NY-21 on busy session"
telemetry: "25% · $10K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-10T07:48:40+00:00"
event_id: "CM-EVT-H11V46ZQN5"
event_slug: "kxhouserace-ny21-26"
event_question: "Will the winner of the New York's 21st Congressional District House election be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-NY21-26-D"
  question_raw: "Will Democratic win the House race for NY-21?"
  current_price: 0.25
  volume_24h_usd: 10413.42
  volume_cumulative_usd: 21331.57
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi places Democratic odds of winning NY-21 at 25%, at the outer edge of long-shot territory."
  - "49% of all-time volume, $10K, cleared in the last 24 hours, compressing roughly half of lifetime activity."
  - "NY-21 has historically been competitive; fresh volume at 25% suggests the market is now treating it as a lean-Republican seat."
  - "Resolves on 2026 NY-21 House election result."
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
      kalshi_vol_24h_usd: 10413.42
sources:
  - label: "ClearMarket market record: Will the winner of the New York's 21st Congressional Di"
    url: "https://clearmarket.fyi/events/kxhouserace-ny21-26"
    retrieved_at: "2026-10-10T07:48:40+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Half of lifetime volume arriving in one session at 25% is a strong signal that new district-level information is shifting the competitive assessment; a desk should review recent NY-21 polling and candidate fundraising.
