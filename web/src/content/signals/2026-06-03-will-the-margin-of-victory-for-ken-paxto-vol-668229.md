---
signal_id: "CMSIG20260603VS01"
signal_slug: "will-the-margin-of-victory-for-ken-paxto-vol-668229"
headline: "Paxton TX Senate runoff margin: 99% on $668K"
semantic_title: "Paxton Texas runoff margin above 20 percent near-certain on big flows"
telemetry: "99% · $668K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-03T01:46:55+00:00"
event_id: "CM-EVT-WDW9695BR8"
event_slug: "kxtxrsenrunoffmov-26may26"
event_question: "Will the margin of victory for Ken Paxton in the 2026 Texas Republican Senate runoff be between 20% and 100%?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTXRSENRUNOFFMOV-26MAY26-KPAX-P60"
  question_raw: "Will the margin of victory for Ken Paxton in the 2026 Texas Republican Senate runoff be between 20% and 100%?"
  current_price: 0.994
  volume_24h_usd: 668229.94
  volume_cumulative_usd: 1148801.09
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-05-26T14:00:00Z"
bullets:
  - "Kalshi consensus at 99% implies Paxton runoff victory is near-certain."
  - "$668K in 24h represents 58% of all-time volume, dominant single-session flow."
  - "Runoff outcome likely imminent or just concluded, prompting settlement-driven volume."
  - "Resolution tied to certified runoff result; residual 1% reflects tail/administrative risk."
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
      kalshi_vol_24h_usd: 668229.94
sources:
  - label: "ClearMarket market record: Will the margin of victory for Ken Paxton in the 2026 T"
    url: "https://clearmarket.fyi/events/kxtxrsenrunoffmov-26may26"
    retrieved_at: "2026-06-03T01:46:55+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-total probability with majority of lifetime volume printing today points to a resolving event, desks tracking Texas political landscape should treat outcome as effectively confirmed.
