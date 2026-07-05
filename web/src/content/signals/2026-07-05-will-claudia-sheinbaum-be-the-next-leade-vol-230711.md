---
signal_id: "CMSIG20260705VS02"
signal_slug: "will-claudia-sheinbaum-be-the-next-leade-vol-230711"
headline: "Sheinbaum next out: 0% on $231K, 74% ATH vol"
semantic_title: "Sheinbaum exit risk faded to zero, 74% of all-time volume deployed"
telemetry: "0% · $231K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-05T10:08:17+00:00"
event_id: "CM-EVT-2FLCV9PNS4"
event_slug: "next-leader-out-of-power-before-2027-no-orban"
event_question: "Will a current leader lose power before 2027, excluding Viktor Orbán?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x2e396a95e62ab942c0ed58ab5c7841c8dc42f4a471f78f66830158670112881b"
  question_raw: "Will Claudia Sheinbaum be the next leader out before 2027?"
  current_price: 0.001
  volume_24h_usd: 230711.19999999998
  volume_cumulative_usd: 311219.452276
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Contract at 0%, traders assign negligible probability Sheinbaum is next leader to exit before 2027."
  - "74% of all-time volume printed in 24h, the most concentrated single-session flow in this contract."
  - "Smaller absolute size but highest ATH share in the series flags targeted position clearing."
  - "Resolves before 2027; zero price consistent with series-wide repricing of who exits first."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 230711.19999999998
sources:
  - label: "ClearMarket market record: Will a current leader lose power before 2027, excluding"
    url: "https://clearmarket.fyi/events/next-leader-out-of-power-before-2027-no-orban"
    retrieved_at: "2026-07-05T10:08:17+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Despite smaller dollar volume, the 74% all-time concentration ratio is the sharpest in the batch, suggesting a discrete informed unwind rather than retail noise, worth flagging for Latin America sovereign desks.
