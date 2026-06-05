---
signal_id: "CMSIG20260605BD10"
signal_slug: "will-annual-inflation-be-4-3-in-may-vs-bench"
headline: "Annual CPI at 4.3% in May: 40%; FRED now 3.9%"
semantic_title: "May CPI at 4.3 percent outruns the current FRED baseline"
telemetry: "40% · CPI inflation, year-over-year (FRED) 3.9%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-05T12:04:45+00:00"
event_id: "CM-EVT-1QS9WGDYF1"
event_slug: "may-inflation-us-annual"
event_question: "Will US annual inflation be in May?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x809b695481bca7c2eddb11ad9ed9b3ca8341ee9f33d1e86fe1344ed509dea3f3"
  question_raw: "Will annual inflation be 4.3% in May?"
  current_price: 0.4
  volume_cumulative_usd: 57086.58475299995
  resolves_at: "2026-06-10T08:00:00Z"
bullets:
  - "Polymarket prices a 40% chance May CPI YoY prints exactly at 4.3%."
  - "Current FRED CPI YoY is 3.9%, a full 40 bps below the targeted exact level."
  - "A 40% probability on a single precise bucket 40 bps above current implies very high implied volatility."
  - "Resolution on the May BLS CPI release; exact-bucket contracts are highly sensitive to rounding."
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

Pricing a 40% probability on the precise 4.3% bucket when the benchmark sits at 3.9% signals the market is placing exceptional weight on a sharp one-month acceleration; combined with candidate 12's 41% at 4.2%, the market's implied distribution is heavily concentrated 30-40 bps above the current FRED print, a notable detachment from the baseline.
