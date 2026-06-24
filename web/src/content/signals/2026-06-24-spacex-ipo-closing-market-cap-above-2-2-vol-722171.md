---
signal_id: "CMSIG20260624VS02"
signal_slug: "spacex-ipo-closing-market-cap-above-2-2-vol-722171"
headline: "SpaceX IPO above $2.2T: 67% on $722K inflow"
semantic_title: "SpaceX IPO cap above $2.2T sits in contested territory"
telemetry: "67% · $722K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-24T10:46:26+00:00"
event_id: "CM-EVT-FDQNXYNKT6"
event_slug: "spacex-ipo-closing-market-cap-above"
event_question: "SpaceX IPO closing market cap, 2027"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x93f2e17cfd239c4667eb3d41ff04e2cd1ae6f3f663210cbc42ec1296ff880805"
  question_raw: "SpaceX IPO closing market cap above $2.2T?"
  current_price: 0.67
  volume_24h_usd: 722171.8124839996
  volume_cumulative_usd: 1298448.1545060014
  arbitration_model: "uma_oracle"
  resolves_at: "2027-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 67%, the market leans toward a $2.2T close but with material doubt."
  - "56% of all-time volume in 24h signals concentrated fresh interest around IPO pricing discovery."
  - "The $2.2T level is the swing threshold in the SpaceX cap ladder; flows reflect active position-taking."
  - "Resolves at IPO close; correlated heavily with the $2T and $2.4T contracts below and above."
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
      poly_vol_24h_usd: 722171.8124839996
sources:
  - label: "ClearMarket market record: SpaceX IPO closing market cap, 2027"
    url: "https://clearmarket.fyi/events/spacex-ipo-closing-market-cap-above"
    retrieved_at: "2026-06-24T10:46:26+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Cross-contract SpaceX IPO flow is mapping the market's implied valuation distribution; a desk should read the $2T/$2.2T/$2.4T ladder jointly to extract the consensus landing zone.
