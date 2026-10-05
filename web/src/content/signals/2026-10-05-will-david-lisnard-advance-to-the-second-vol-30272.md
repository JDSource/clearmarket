---
signal_id: "CMSIG20261005VS06"
signal_slug: "will-david-lisnard-advance-to-the-second-vol-30272"
headline: "Lisnard French pres. R2: 16% on $30K"
semantic_title: "Lisnard French presidential second-round odds hold at 16%"
telemetry: "16% · $30K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-05T16:45:18+00:00"
event_id: "CM-EVT-GZ9M6X8G64"
event_slug: "next-french-presidential-election-who-will-advance-to-the-2nd-round"
event_question: "Will Emmanuel Macron and Marine Le Pen advance to the second round of the next French Presidential Election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xcc100766ebc6f6f29b53aed3867d6b4457f28681878b3c09ca93da28dca7a6df"
  question_raw: "Will David Lisnard advance to the second round of the next French presidential election?"
  current_price: 0.165
  volume_24h_usd: 30272.464904999993
  volume_cumulative_usd: 111300.04240299998
  arbitration_model: "uma_oracle"
  resolves_at: "2027-04-30T00:00:00Z"
bullets:
  - "Polymarket prices David Lisnard advancing to the French presidential second round at 16%."
  - "$30K in 24h is 27% of all-time volume, notable for a non-frontrunner French candidacy."
  - "Lisnard's LR positioning and French right-wing realignment chatter are likely driving fresh looks."
  - "Resolves on French presidential election first-round results."
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
      poly_vol_24h_usd: 30272.464904999993
sources:
  - label: "ClearMarket market record: Will Emmanuel Macron and Marine Le Pen advance to the s"
    url: "https://clearmarket.fyi/events/next-french-presidential-election-who-will-advance-to-the-2nd-round"
    retrieved_at: "2026-10-05T16:45:18+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Growing volume on a long-shot French candidacy suggests macro desks are beginning to map the full distribution of French political outcomes beyond the Macron-successor and Le Pen scenarios.
