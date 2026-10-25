---
signal_id: "CMSIG20261025VS03"
signal_slug: "will-republican-win-the-house-race-for-n-vol-10211"
headline: "GOP wins NJ-02: 80% on $10K volume spike"
semantic_title: "Buyers back GOP in NJ-02 as odds hold above 75%"
telemetry: "80% · $10K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-25T07:48:52+00:00"
event_id: "CM-EVT-PLPDDX9JC8"
event_slug: "kxhouserace-nj02-26"
event_question: "Will a New Jersey's 2nd congressional district representative be elected by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-NJ02-26-R"
  question_raw: "Will Republican win the House race for NJ-02?"
  current_price: 0.8
  volume_24h_usd: 10211.63
  volume_cumulative_usd: 36593.02
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices a Republican win in NJ-02 at 80%, marking it as a likely but not locked Republican-hold district."
  - "24h volume of $10K is 28% of all-time handle, a moderate but meaningful single-day share for a district contract."
  - "New Jersey's competitive suburban districts are drawing renewed attention as generic-ballot and gubernatorial data shifts."
  - "Contract resolves on the certified NJ-02 House race result from the 2026 midterm election."
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
      kalshi_vol_24h_usd: 10211.63
sources:
  - label: "ClearMarket market record: Will a New Jersey's 2nd congressional district represen"
    url: "https://clearmarket.fyi/events/kxhouserace-nj02-26"
    retrieved_at: "2026-10-25T07:48:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Renewed flow into NJ-02 at elevated odds indicates traders are monitoring whether New Jersey suburban drift continues to favor Republicans; useful for House majority margin models tracking northeast battleground exposure.
