---
signal_id: "CMSIG20260813VS05"
signal_slug: "will-the-democratic-party-win-the-govern-vol-62204"
headline: "NV governor Dem win: 41% on $62K volume spike"
semantic_title: "Nevada governor odds lean Republican as fresh volume tests the Dem line"
telemetry: "41% · $62K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-13T09:08:38+00:00"
event_id: "CM-EVT-TNC2QWG2J9"
event_slug: "govpartynv-26"
event_question: "Nevada Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYNV-26-D"
  question_raw: "Will the Democratic party win the governorship in Nevada"
  current_price: 0.41
  volume_24h_usd: 62204.71
  volume_cumulative_usd: 186338.35
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-02T15:00:00Z"
bullets:
  - "Kalshi prices a Democratic Nevada governorship win at 41%, a modest Republican lean in the implied odds."
  - "$62K over 24 hours represents 33% of all-time volume, consistent with a competitive-cycle attention surge."
  - "Pricing below 50% with rising volume indicates fresh capital tilting toward the Republican side of the trade."
  - "Resolves on the Nevada 2026 gubernatorial general election outcome."
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
      kalshi_vol_24h_usd: 62204.71
sources:
  - label: "ClearMarket market record: Nevada Governor winner?"
    url: "https://clearmarket.fyi/events/govpartynv-26"
    retrieved_at: "2026-08-13T09:08:38+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A sub-50% Democratic price drawing a third of lifetime volume in one session signals Nevada's governor race is moving into active swing-state territory for 2026 cycle models.
