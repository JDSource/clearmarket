---
signal_id: "CMSIG20260605BD03"
signal_slug: "will-no-fed-rate-cuts-happen-in-2026-vs-bench"
headline: "No 2026 cuts: 69%; fed funds upper bound at 3.75%"
semantic_title: "No-cut pricing gaps above rate already at 3.75 percent"
telemetry: "69% · Fed funds target rate, upper bound (FRED) 3.75%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-05T11:25:34+00:00"
event_id: "CM-EVT-0TSMZBY6R6"
event_slug: "how-many-fed-rate-cuts-in-2026"
event_question: "Will the Federal Reserve make fewer than X rate cuts in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd4e77ba6f29fc093509d24f508631abd445ecf506bbdc9c4c80e60256a318527"
  question_raw: "Will no Fed rate cuts happen in 2026?"
  current_price: 0.688
  volume_cumulative_usd: 4596174.737886055
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 69% chance of zero Fed rate cuts in all of 2026."
  - "FRED: fed funds upper bound currently sits at 3.75 percent."
  - "Market implies the Fed holds all year despite rate already below prior cycle peak."
  - "Resolves end-2026 based on cumulative FOMC decisions."
atomic_claims:
  - type: "benchmark_divergence"
    provenance: "PM price direct from polymarket API; benchmark Fed funds target rate, upper bound (FRED) = 3.75%"
    field_provenance:
      pm_price:
        tier: "direct"
        method: "polymarket_api"
      benchmark_value:
        tier: "mediated"
        method: "Fed funds target rate, upper bound (FRED)"
        source_url: "https://fred.stlouisfed.org/series/DFEDTARU"
        retrieved_at: "2026-06-05T11:25:34+00:00"
sources:
  - label: "Fed funds target rate, upper bound (FRED): 3.75%"
    url: "https://fred.stlouisfed.org/series/DFEDTARU"
    retrieved_at: "2026-06-05T11:25:34+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

At 69%, the market prices near-certainty of a full-year hold even though the rate has already been cut from its peak, suggesting traders see no catalyst for further easing through year-end.
