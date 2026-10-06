---
signal_id: "CMSIG20261006VS04"
signal_slug: "will-the-republican-party-win-the-govern-vol-35615"
headline: "Iowa GOP governor: 13% on $36K volume surge"
semantic_title: "Iowa governor odds price a long-shot Democratic upset on Kalshi"
telemetry: "13% · $36K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-06T07:48:59+00:00"
event_id: "CM-EVT-8D7ZTR8991"
event_slug: "govpartyia-26"
event_question: "Will the Iowa gubernatorial election result be determined by January 14, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYIA-26-R"
  question_raw: "Will the Republican party win the governorship in Iowa"
  current_price: 0.13
  volume_24h_usd: 35615.77
  volume_cumulative_usd: 89758.28
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-14T15:00:00Z"
bullets:
  - "Kalshi prices Republicans at 13%, an unusually low figure that implies the market is pricing a strong likelihood of a Democratic win in Iowa."
  - "$36K in 24h volume equals 40% of all-time, a sharp burst of activity on a contract that had been dormant."
  - "A 13% Republican price in a historically red state points to fresh information, a weak candidate, a scandal, or a late primary shift, driving reassessment."
  - "Resolves on the Iowa gubernatorial election result, November 2026."
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
      kalshi_vol_24h_usd: 35615.77
sources:
  - label: "ClearMarket market record: Will the Iowa gubernatorial election result be determin"
    url: "https://clearmarket.fyi/events/govpartyia-26"
    retrieved_at: "2026-10-06T07:48:59+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 40% all-time volume day pushing Republicans to 13% in Iowa is a high-conviction signal for a desk, this market is pricing a near-collapse of GOP odds and warrants immediate fundamental review of the Iowa race.
