---
signal_id: "CMSIG20260830VS02"
signal_slug: "will-chris-pappas-be-the-democratic-nomi-vol-12726"
headline: "Pappas NH Dem Senate nominee: 94% on $12.7K surge"
semantic_title: "Pappas NH Democratic Senate nomination stays a strong bet"
telemetry: "94% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-30T13:31:03+00:00"
event_id: "CM-EVT-HY8R70V952"
event_slug: "new-hampshire-democratic-senate-primary-winner"
event_question: "Will the Democratic Party winner of the New Hampshire Senate primary be determined by the 2026 primary election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xf78be595172a9db8c6323e1927aa44b2fa2d52805d97bf4a9664593b42326534"
  question_raw: "Will Chris Pappas be the Democratic nominee for Senate in New Hampshire?"
  current_price: 0.94
  volume_24h_usd: 12726.623945
  volume_cumulative_usd: 47277.236447999996
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-08T00:00:00Z"
bullets:
  - "Market prices 94%, traders see Pappas as the near-certain Democratic Senate nominee in New Hampshire."
  - "24h volume of $12.7K is 27% of all-time handle, a meaningful but not exhaustive capital deployment."
  - "Fresh attention likely tied to primary filing deadlines or a rival's decision not to challenge."
  - "At 94%, residual 6% reflects tail risk of a late entrant or Pappas withdrawal before the primary."
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
      poly_vol_24h_usd: 12726.623945
sources:
  - label: "ClearMarket market record: Will the Democratic Party winner of the New Hampshire S"
    url: "https://clearmarket.fyi/events/new-hampshire-democratic-senate-primary-winner"
    retrieved_at: "2026-08-30T13:31:03+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The volume surge at 94% suggests new information, a credible challenger standing down or a filing deadline passing, is drawing confirmation trades on Polymarket; relevant for desks modeling New Hampshire general-election dynamics.
