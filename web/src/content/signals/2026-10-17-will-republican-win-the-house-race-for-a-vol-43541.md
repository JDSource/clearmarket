---
signal_id: "CMSIG20261017VS01"
signal_slug: "will-republican-win-the-house-race-for-a-vol-43541"
headline: "AL-02 GOP House: 74% on heavy $44K inflow"
semantic_title: "AL-02 Republican odds hold firm through a volume surge"
telemetry: "74% · $44K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-17T07:48:43+00:00"
event_id: "CM-EVT-VNGYPPDNV9"
event_slug: "kxhouserace-al02-26"
event_question: "Will the Alabama 2nd congressional district House election winner be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-AL02-26-R"
  question_raw: "Will Republican win the House race for AL-02?"
  current_price: 0.74
  volume_24h_usd: 43541.5
  volume_cumulative_usd: 104056.51
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi marks the Republican at 74%, solid favorite territory, not a lock."
  - "$43.5K in 24h represents 42% of all-time volume, an unusually large single-session print."
  - "AL-02 was redrawn under the Voting Rights Act; elevated volume may reflect uncertainty about the new district's partisan lean."
  - "Contract resolves on 2026 general election results."
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
      kalshi_vol_24h_usd: 43541.5
sources:
  - label: "ClearMarket market record: Will the Alabama 2nd congressional district House elect"
    url: "https://clearmarket.fyi/events/kxhouserace-al02-26"
    retrieved_at: "2026-10-17T07:48:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Forty-two percent of lifetime volume in one day on a 74% contract in a newly redrawn Alabama district suggests traders are stress-testing the Republican advantage after district-map developments.
