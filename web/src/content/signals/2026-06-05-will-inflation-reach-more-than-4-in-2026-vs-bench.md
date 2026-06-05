---
signal_id: "CMSIG20260605BD04"
signal_slug: "will-inflation-reach-more-than-4-in-2026-vs-bench"
headline: "CPI above 4% in 2026: 98%; current YoY at 3.9%"
semantic_title: "Inflation above 4% nears full pricing despite sub-4 CPI read"
telemetry: "98% · CPI inflation, year-over-year (FRED) 3.9%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-05T12:04:45+00:00"
event_id: "CM-EVT-NN523F6SZ3"
event_slug: "how-high-will-inflation-get-in-2026"
event_question: "US inflation rate, 2026"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x1f61db83c47fc787f44997af53d517cc4775e813b169d0b8ae2ad3bff316d052"
  question_raw: "Will inflation reach more than 4% in 2026?"
  current_price: 0.978
  volume_cumulative_usd: 247436.1943099977
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 98% chance CPI exceeds 4% at some point in 2026."
  - "Current US CPI YoY (FRED) stands at 3.9%, just below the 4% threshold."
  - "Market implies near-certainty of a threshold breach from a starting point 10 bps below it."
  - "Resolution requires any single month's YoY print to exceed 4% before year-end."
atomic_claims:
  - type: "benchmark_divergence"
    provenance: "PM price direct from polymarket API; benchmark CPI inflation, year-over-year (FRED) = 3.9%"
    field_provenance:
      pm_price:
        tier: "direct"
        method: "polymarket_api"
      benchmark_value:
        tier: "mediated"
        method: "CPI inflation, year-over-year (FRED)"
        source_url: "https://fred.stlouisfed.org/series/CPIAUCSL"
        retrieved_at: "2026-06-05T12:04:45+00:00"
sources:
  - label: "CPI inflation, year-over-year (FRED): 3.9%"
    url: "https://fred.stlouisfed.org/series/CPIAUCSL"
    retrieved_at: "2026-06-05T12:04:45+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "benchmark_api"
  editorial_judgment: "cm_signal_llm_judge"
---

With CPI currently at 3.9%, the market's 98% pricing of a 4%-plus breach implies the desk sees the current reading as essentially already at the line, but a single month's rounding or seasonal push could cross it, the near-certainty premium appears stretched given how close the benchmark sits to but still below the trigger.
