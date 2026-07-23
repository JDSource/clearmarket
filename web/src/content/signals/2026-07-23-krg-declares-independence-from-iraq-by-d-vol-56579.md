---
signal_id: "CMSIG20260723VS02"
signal_slug: "krg-declares-independence-from-iraq-by-d-vol-56579"
headline: "KRG independence by Dec 31: 6% on $56.6K"
semantic_title: "KRG independence by year-end stays a long shot at 6%"
telemetry: "6% · $57K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-23T10:17:14+00:00"
event_id: "CM-EVT-SPXZBC4MN7"
event_slug: "who-will-trump-talk-to"
event_question: "Will the KRG declare independence from Iraq by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x19e4c19193bb06609b83267b5d06fbd4c45d8848ff532a66ace9e8e77e3c991d"
  question_raw: "KRG declares independence from Iraq by December 31?"
  current_price: 0.06
  volume_24h_usd: 56579.844261
  volume_cumulative_usd: 196230.13129200012
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Kurdish Regional Government independence at just 6%, the market assigns this a remote but non-trivial probability."
  - "24h volume of $56.6K is 29% of the $196K all-time total, a meaningful single-day share for a geopolitical tail risk."
  - "Fresh attention likely tied to regional security developments or diplomatic signaling in Iraq in mid-2026."
  - "Resolves December 31, 2026; any formal KRG independence declaration would trigger YES."
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
      poly_vol_24h_usd: 56579.844261
sources:
  - label: "ClearMarket market record: Will the KRG declare independence from Iraq by December"
    url: "https://clearmarket.fyi/events/who-will-trump-talk-to"
    retrieved_at: "2026-07-23T10:17:14+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 29% single-day share of lifetime volume on a 6% contract suggests a desk or risk function is buying tail coverage on Kurdish independence risk, worth flagging for anyone with Iraq or regional energy exposure.
