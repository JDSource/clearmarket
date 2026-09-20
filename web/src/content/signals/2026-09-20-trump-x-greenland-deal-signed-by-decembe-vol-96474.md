---
signal_id: "CMSIG20260920VS00"
signal_slug: "trump-x-greenland-deal-signed-by-decembe-vol-96474"
headline: "Trump-Greenland deal: 96% on $96K surge"
semantic_title: "Traders back a Greenland deal closing by Dec 31"
telemetry: "96% · $96K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-20T12:50:42+00:00"
event_id: "CM-EVT-M8SXSN1YS7"
event_slug: "trump-x-greenland-deal-signed-by-december-31"
event_question: "Will a Trump-Greenland deal be signed by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6a7aed00fae37de19e0b789a6b50a7475ff1afa898c50b9da11ca733a23199fa"
  question_raw: "Trump x Greenland deal signed by December 31?"
  current_price: 0.965
  volume_24h_usd: 96474.961213
  volume_cumulative_usd: 346949.4325969998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a signed Trump-Greenland deal at 96%, near-certainty with under 100 days left in 2026."
  - "24h volume of $96K is 28% of all-time handle, signaling a sharp fresh-capital commitment to the yes side."
  - "Surge likely reflects a concrete diplomatic development or leaked framework advancing toward a formal signing."
  - "Resolves YES on a signed agreement between the U.S. and Denmark/Greenland by December 31, 2026."
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
      poly_vol_24h_usd: 96474.961213
sources:
  - label: "ClearMarket market record: Will a Trump-Greenland deal be signed by December 31?"
    url: "https://clearmarket.fyi/events/trump-x-greenland-deal-signed-by-december-31"
    retrieved_at: "2026-09-20T12:50:42+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should note that near-100% pricing plus 28% of all-time volume in a single day suggests the market is treating an imminent signing as effectively confirmed, not merely probable.
