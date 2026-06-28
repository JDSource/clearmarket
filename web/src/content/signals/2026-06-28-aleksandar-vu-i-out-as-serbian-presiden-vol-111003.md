---
signal_id: "CMSIG20260628VS02"
signal_slug: "aleksandar-vu-i-out-as-serbian-presiden-vol-111003"
headline: "Vučić out as Serbia president: 96% on $111K"
semantic_title: "Capital stacks deep on Vučić exit as Serbian presidency nears resolution"
telemetry: "96% · $111K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-28T10:25:52+00:00"
event_id: "CM-EVT-01R21H5GP2"
event_slug: "aleksandar-vui-out-as-serbian-president-by"
event_question: "Will Aleksandar Vučić cease to be Serbian President by end of 2025?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xf47e8cc490e9fd5f0ac8bd36aa4bc3b1abf12025dd145baac6cd95ee58e2d286"
  question_raw: "Aleksandar Vučić out as Serbian President by June 30, 2026?"
  current_price: 0.961
  volume_24h_usd: 111003.07495499995
  volume_cumulative_usd: 128883.40743500007
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices Vučić's departure from the Serbian presidency at 96%, near-certainty with hours left."
  - "$111K in 24h is 86% of all-time volume, compressing into final resolution window."
  - "Constitutional transition or formal resignation is already underway; market reflects fait accompli rather than forecast."
  - "Resolves June 30; residual 4% is pure optionality on a procedural reversal."
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
      poly_vol_24h_usd: 111003.07495499995
sources:
  - label: "ClearMarket market record: Will Aleksandar Vučić cease to be Serbian President by "
    url: "https://clearmarket.fyi/events/aleksandar-vui-out-as-serbian-president-by"
    retrieved_at: "2026-06-28T10:25:52+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The 86% all-time volume surge at 96% is a late settlement rush, desks pricing sovereign political transition risk in the Balkans should treat this as near-resolved and focus on successor-government positioning.
