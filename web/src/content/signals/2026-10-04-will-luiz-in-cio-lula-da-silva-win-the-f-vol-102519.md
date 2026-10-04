---
signal_id: "CMSIG20261004VS01"
signal_slug: "will-luiz-in-cio-lula-da-silva-win-the-f-vol-102519"
headline: "Lula first-round win: 9% on $103K spike"
semantic_title: "Lula first-round win stays a long shot at 9%"
telemetry: "9% · $103K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-04T07:48:35+00:00"
event_id: "CM-EVT-2NF81BZ4K5"
event_slug: "brazil-presidential-election-first-round-margin-of-victory"
event_question: "Will the margin of victory in Brazil's presidential election first round be less than 5 percentage points?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5377b12dd060efd8e3597620f120648f1bf99452a95eb70374b128d9ca133227"
  question_raw: "Will Luiz Inácio Lula da Silva win the first round of the 2026 Brazilian presidential election by 5–10%?"
  current_price: 0.09
  volume_24h_usd: 102519.20886400001
  volume_cumulative_usd: 223196.18924799995
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-04T00:00:00Z"
bullets:
  - "Polymarket prices Lula winning outright in round one at just 9%, the market expects a runoff."
  - "46% of all-time volume hit in 24h, one of the heaviest single-day surges relative to history on this contract."
  - "Fresh attention likely driven by Brazilian polling releases or coalition signals ahead of the 2026 election."
  - "Contract resolves on Brazil's first-round result date in 2026."
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
      poly_vol_24h_usd: 102519.20886400001
sources:
  - label: "ClearMarket market record: Will the margin of victory in Brazil's presidential ele"
    url: "https://clearmarket.fyi/events/brazil-presidential-election-first-round-margin-of-victory"
    retrieved_at: "2026-10-04T07:48:35+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Nearly half of all-time volume clearing in one day at 9% odds tells a desk the market is firmly ruling out a Lula first-round knockout, a runoff is now the consensus trade.
