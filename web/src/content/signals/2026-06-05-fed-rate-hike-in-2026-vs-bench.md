---
signal_id: "CMSIG20260605BD15"
signal_slug: "fed-rate-hike-in-2026-vs-bench"
headline: "Fed hike in 2026: 39%; upper bound currently at 3.75%"
semantic_title: "Hike pricing outruns hold consensus with rate at 3.75 percent"
telemetry: "39% · Fed funds target rate, upper bound (FRED) 3.75%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-05T11:25:34+00:00"
event_id: "CM-EVT-87QV1G78C4"
event_slug: "fed-rate-hike-in-2026"
event_question: "Will the Federal Reserve raise interest rates at least once in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x80b3af88cb991980e8da1ce86b9794a0957f96ec98c29319dd7ba65e9744d82b"
  question_raw: "Fed rate hike in 2026?"
  current_price: 0.39
  volume_cumulative_usd: 1373047.202857998
  resolves_at: "2026-12-09T00:00:00Z"
bullets:
  - "Polymarket prices a 39% chance of at least one Fed rate hike somewhere in 2026."
  - "FRED: fed funds upper bound currently 3.75 percent."
  - "Market assigns meaningful hike risk despite rate already below cycle peak and no-cut dominating other contracts."
  - "Resolves if any FOMC decision in 2026 raises the target rate."
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

A 39% hike probability sits in notable tension with the 69% no-cut pricing on the same venue, together they imply the market sees the Fed as either frozen or pivoting hawkish, with very little easing expected.
