---
signal_id: "CMSIG20260715VS02"
signal_slug: "will-helder-barbalho-finish-in-second-pl-vol-11017"
headline: "Barbalho Brazil R1 second: 0% on $11K volume spike"
semantic_title: "Barbalho second-place finish written off, capital stacks against"
telemetry: "0% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-15T10:00:41+00:00"
event_id: "CM-EVT-Z8ZNQ1C002"
event_slug: "brazil-presidential-election-first-round-2nd-place"
event_question: "Will the second-place finisher in the first round of the 2026 Brazil Presidential Election be determined?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x2366a6b980302d1a20c47d3bf5a2ce1d86a488197b83730554aab7d9c96e72cf"
  question_raw: "Will Helder Barbalho finish in second place in the first round of the 2026 Brazilian presidential election?"
  current_price: 0.003
  volume_24h_usd: 11017.59794
  volume_cumulative_usd: 19959.58794
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-04T00:00:00Z"
bullets:
  - "Polymarket assigns 0% probability Helder Barbalho finishes second in Brazil's 2026 first-round presidential vote."
  - "24h volume of $11,018 is 55% of all-time handle, a concentrated, conviction-heavy settlement flow."
  - "Surge at zero price suggests new polling or candidate field data has definitively closed off this outcome."
  - "Resolves YES only if Barbalho places second in Round 1; market has effectively ruled this out."
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
      poly_vol_24h_usd: 11017.59794
sources:
  - label: "ClearMarket market record: Will the second-place finisher in the first round of th"
    url: "https://clearmarket.fyi/events/brazil-presidential-election-first-round-2nd-place"
    retrieved_at: "2026-07-15T10:00:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 55% all-time volume flush to zero is a strong signal that Brazil political desks have absorbed disqualifying information, warrants cross-checking against updated Datafolha or TSE filings.
