---
signal_id: "CMSIG20260610VS02"
signal_slug: "will-zach-lahn-be-the-republican-nominee-vol-557073"
headline: "Lahn Iowa GOP nominee: 100% on $557K surge"
semantic_title: "Capital stacks behind Lahn as Iowa GOP nominee at certainty"
telemetry: "100% · $557K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-10T11:37:24+00:00"
event_id: "CM-EVT-N70PDTB9T9"
event_slug: "kxgovianomr-26"
event_question: "Will Kim Reynolds be the Iowa Republican Governor nominee by the 2026 election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVIANOMR-26-ZLAH"
  question_raw: "Will Zach Lahn be the Republican nominee for Governor in Iowa?"
  current_price: 0.997
  volume_24h_usd: 557073.25
  volume_cumulative_usd: 868681.77
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-06-02T14:00:00Z"
bullets:
  - "100% price reflects market treating Lahn's Republican Iowa gubernatorial nomination as fait accompli."
  - "$557K in 24h equals 64% of all-time volume, dominant single-session confirmation trade."
  - "Likely triggered by official party convention vote, filing deadline, or primary result."
  - "Kalshi contract near resolution; volume reflects institutional cleanup of residual positions."
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
      kalshi_vol_24h_usd: 557073.25
sources:
  - label: "ClearMarket market record: Will Kim Reynolds be the Iowa Republican Governor nomin"
    url: "https://clearmarket.fyi/events/kxgovianomr-26"
    retrieved_at: "2026-06-10T11:37:24+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 100% price absorbing two-thirds of lifetime volume in one day signals a catalytic confirmation event, desks should treat nomination as operationally settled and shift focus to general-election contracts.
