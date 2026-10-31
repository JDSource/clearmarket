---
signal_id: "CMSIG20261031VS03"
signal_slug: "will-republican-win-the-house-race-for-n-vol-47241"
headline: "NY-02 GOP House win: 82% on 81% all-time share"
semantic_title: "Traders pile into NY-02 Republican hold near election close"
telemetry: "82% · $47K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-31T07:49:19+00:00"
event_id: "CM-EVT-M23Y1W2P93"
event_slug: "kxhouserace-ny02-26"
event_question: "Will the winner of the New York's 2nd Congressional District House race be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-NY02-26-R"
  question_raw: "Will Republican win the House race for NY-02?"
  current_price: 0.82
  volume_24h_usd: 47241.0
  volume_cumulative_usd: 58428.34
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices Republicans at 82% in NY-02, strong favorite with little residual doubt priced in."
  - "81% of all-time contract volume landed in 24h, an extraordinary concentration signaling last-minute certainty trades."
  - "The near-complete volume flush implies late entrants view the race as effectively decided; thin opposing liquidity remains."
  - "Resolves on NY-02 2026 House election result."
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
      kalshi_vol_24h_usd: 47241.0
sources:
  - label: "ClearMarket market record: Will the winner of the New York's 2nd Congressional Dis"
    url: "https://clearmarket.fyi/events/kxhouserace-ny02-26"
    retrieved_at: "2026-10-31T07:49:19+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

When 81% of all-time volume prints in a single day at an 82% price, desks should treat this as a market closing itself out, resolution risk is low but liquidity is thin on the losing side.
