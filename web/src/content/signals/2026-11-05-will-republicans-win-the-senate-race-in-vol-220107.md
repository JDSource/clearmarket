---
signal_id: "CMSIG20261105VS05"
signal_slug: "will-republicans-win-the-senate-race-in-vol-220107"
headline: "MS Senate GOP win: 4% as $220K pours in today"
semantic_title: "Mississippi GOP Senate odds sit at 4% through fresh volume"
telemetry: "4% · $220K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-05T07:49:08+00:00"
event_id: "CM-EVT-6R8L57X0Y4"
event_slug: "senatems-26"
event_question: "Will the Mississippi Senate race be decided by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "SENATEMS-26-R"
  question_raw: "Will Republicans win the Senate race in Mississippi?"
  current_price: 0.037
  volume_24h_usd: 220107.02
  volume_cumulative_usd: 528005.14
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices a Republican Mississippi Senate win at 4%, consistent with the 96% Democratic pricing on the companion contract."
  - "42% of all-time volume, $220K, cleared in one session, a notable Election Day commitment to the 'no' side."
  - "Volume at this price level suggests traders are either closing long Democratic positions or making final directional bets."
  - "Resolves on certified Mississippi Senate result; a 4% tail is not zero in a close-count environment."
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
      kalshi_vol_24h_usd: 220107.02
sources:
  - label: "ClearMarket market record: Will the Mississippi Senate race be decided by January "
    url: "https://clearmarket.fyi/events/senatems-26"
    retrieved_at: "2026-11-05T07:49:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Consistent with the companion Spike 1 pricing, the 4% Republican read leaves the desk little edge in hedging a Mississippi GOP win, treat as priced resolved unless results deviate sharply.
