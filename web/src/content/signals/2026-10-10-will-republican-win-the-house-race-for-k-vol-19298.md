---
signal_id: "CMSIG20261010VS01"
signal_slug: "will-republican-win-the-house-race-for-k-vol-19298"
headline: "KY-06 GOP House: 72% on $19K volume spike"
semantic_title: "Buyers back Republicans in KY-06 at 72%"
telemetry: "72% · $19K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-10T07:48:40+00:00"
event_id: "CM-EVT-9D5R8WC8R6"
event_slug: "kxhouserace-ky06-26"
event_question: "KY-06 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-KY06-26-R"
  question_raw: "Will Republican win the House race for KY-06?"
  current_price: 0.72
  volume_24h_usd: 19298.17
  volume_cumulative_usd: 26462.25
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices a Republican win in KY-06 at 72%, a solid but not decisive favorite."
  - "73% of all-time volume, $19K, printed in the last 24 hours, the contract's most active stretch by far."
  - "Concentration of this much lifetime activity in a single session points to a near-term catalyst, likely polling or candidate news."
  - "Resolves on 2026 KY-06 House election outcome."
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
      kalshi_vol_24h_usd: 19298.17
sources:
  - label: "ClearMarket market record: KY-06 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-ky06-26"
    retrieved_at: "2026-10-10T07:48:40+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With nearly three-quarters of lifetime handle arriving in one day, a desk should treat this as a signal that new information is circulating on the KY-06 race and monitor for fresh polling or local news.
