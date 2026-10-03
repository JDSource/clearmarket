---
signal_id: "CMSIG20261003VS04"
signal_slug: "will-the-democrats-win-the-michigan-gove-vol-20118"
headline: "Democrat MI governor: 94% on $20K volume"
semantic_title: "Heavy trading holds Michigan Democrats as firm favorite"
telemetry: "94% · $20K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-03T07:48:19+00:00"
event_id: "CM-EVT-GTDLXYMZQ7"
event_slug: "michigan-governor-winner-2026"
event_question: "Will the Michigan Governor election be won by the Democratic candidate?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x76cface9f6df604ff32447bce58656b7a72b6659324d089c73a13a99f06c8aae"
  question_raw: "Will the Democrats win the Michigan governor race in 2026?"
  current_price: 0.94
  volume_24h_usd: 20118.274651999996
  volume_cumulative_usd: 71292.86791799999
  arbitration_model: "uma_oracle"
bullets:
  - "Polymarket contract prices Michigan Democratic gubernatorial win at 94%, market treats the race as nearly decided."
  - "24h volume of $20K represents 28% of all-time contract flow, a notable single-session concentration at this late probability extreme."
  - "Michigan's open-seat 2026 race is a top-tier battleground; trading at 94% with fresh volume implies recent developments are reinforcing Democratic strength, not testing it."
  - "Resolves on 2026 Michigan general election certified result."
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
      poly_vol_24h_usd: 20118.274651999996
sources:
  - label: "ClearMarket market record: Will the Michigan Governor election be won by the Democ"
    url: "https://clearmarket.fyi/events/michigan-governor-winner-2026"
    retrieved_at: "2026-10-03T07:48:19+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should interpret this as the market digesting favorable new information for the Democratic candidate, high-confidence pricing absorbing fresh volume at 94% warrants checking for candidate news, polling, or opponent withdrawal.
