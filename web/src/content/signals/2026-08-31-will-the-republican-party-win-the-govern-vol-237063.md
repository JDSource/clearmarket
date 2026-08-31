---
signal_id: "CMSIG20260831VS00"
signal_slug: "will-the-republican-party-win-the-govern-vol-237063"
headline: "FL GOP governor: 81% on $237K surge"
semantic_title: "Buyers back the GOP hold on Florida's governorship"
telemetry: "81% · $237K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-31T15:48:06+00:00"
event_id: "CM-EVT-4HX1NKV2L1"
event_slug: "govpartyfl-26"
event_question: "Florida Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYFL-26-R"
  question_raw: "Will the Republican party win the governorship in Florida"
  current_price: 0.81
  volume_24h_usd: 237063.39
  volume_cumulative_usd: 383796.46
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-08T15:00:00Z"
bullets:
  - "Kalshi prices Republicans at 81%, a strong favorite for the Florida governorship."
  - "24h volume of $237K is 62% of all-time handle, signaling a major fresh-money event."
  - "End-of-August positioning likely tied to candidate filing deadlines or early polling drops."
  - "Resolves on 2026 Florida general election night."
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
      kalshi_vol_24h_usd: 237063.39
sources:
  - label: "ClearMarket market record: Florida Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyfl-26"
    retrieved_at: "2026-08-31T15:48:06+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A dominant share of lifetime volume arriving in one session flags that the Florida governor race is moving from background to active book, desks should watch for a polling or candidate event driving the conviction.
