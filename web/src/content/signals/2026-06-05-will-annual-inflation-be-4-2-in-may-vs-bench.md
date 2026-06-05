---
signal_id: "CMSIG20260605BD12"
signal_slug: "will-annual-inflation-be-4-2-in-may-vs-bench"
headline: "Annual CPI at 4.2% in May: 41%; FRED now 3.9%"
semantic_title: "May CPI at 4.2% challenges the FRED anchor"
telemetry: "41% · CPI inflation, year-over-year (FRED) 3.9%"
category_tag: "VS_BENCHMARK_DRIFT"
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-06-05T12:04:45+00:00"
event_id: "CM-EVT-1QS9WGDYF1"
event_slug: "may-inflation-us-annual"
event_question: "Will US annual inflation be in May?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x1f916787432121b23c3fd09ad2b309a34888bf1c98f304f0d1cc40c95d052ca0"
  question_raw: "Will annual inflation be 4.2% in May?"
  current_price: 0.41
  volume_cumulative_usd: 44404.737547000026
  resolves_at: "2026-06-10T08:00:00Z"
bullets:
  - "Polymarket prices a 41% chance May CPI YoY prints exactly at 4.2%."
  - "Current FRED CPI YoY is 3.9%, placing the target bucket 30 bps above the live reading."
  - "Adjacent buckets at 4.2% and 4.3% together command roughly 81% of market probability."
  - "Resolution on the May BLS release; exact-level contracts collapse quickly post-print."
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

The market is pricing the 4.2% exact bucket at 41% from a 3.9% baseline, implying a 30 bps month-over-month acceleration as the modal outcome, a meaningful divergence from the current FRED benchmark that warrants close monitoring ahead of the May CPI print.
