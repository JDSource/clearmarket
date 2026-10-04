---
signal_id: "CMSIG20261004VS00"
signal_slug: "will-luiz-in-cio-lula-da-silva-win-the-f-vol-134734"
headline: "Lula first-round win: 10% on $135K surge"
semantic_title: "Lula first-round win stays a long shot at 10%"
telemetry: "10% · $135K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-04T13:40:01+00:00"
event_id: "CM-EVT-2NF81BZ4K5"
event_slug: "brazil-presidential-election-first-round-margin-of-victory"
event_question: "Will the margin of victory in Brazil's presidential election first round be less than 5 percentage points?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5377b12dd060efd8e3597620f120648f1bf99452a95eb70374b128d9ca133227"
  question_raw: "Will Luiz Inácio Lula da Silva win the first round of the 2026 Brazilian presidential election by 5–10%?"
  current_price: 0.1
  volume_24h_usd: 134734.96659499998
  volume_cumulative_usd: 257213.7378829999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-04T00:00:00Z"
bullets:
  - "Polymarket prices Lula's first-round outright win at just 10%, implying a runoff is near-certain."
  - "$134,735 traded in 24h, 52% of this contract's entire all-time volume, an extraordinary single-session concentration."
  - "Fresh attention likely tied to emerging polling or Lula health/eligibility developments ahead of October 2026."
  - "Resolves YES only if Lula clears 50% in round one; current odds strongly favor a two-round race."
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
      poly_vol_24h_usd: 134734.96659499998
sources:
  - label: "ClearMarket market record: Will the margin of victory in Brazil's presidential ele"
    url: "https://clearmarket.fyi/events/brazil-presidential-election-first-round-margin-of-victory"
    retrieved_at: "2026-10-04T13:40:01+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The outsized share of all-time volume in a single session signals a catalyst, desks should monitor Brazilian polling releases or eligibility rulings that could rapidly reprice the runoff probability.
