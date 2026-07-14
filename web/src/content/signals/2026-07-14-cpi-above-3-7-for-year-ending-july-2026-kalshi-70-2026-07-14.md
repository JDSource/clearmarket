---
signal_id: "CMSIG2026071405"
signal_slug: "cpi-above-3-7-for-year-ending-july-2026-kalshi-70-2026-07-14"
headline: "CPI above 3.7% for year ending July 2026: Kalshi 70%"
semantic_title: "CPI above 3.7 percent for year ending July nears consensus"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-14T05:01:05.000Z"
event_id: "CM-EVT-FC6YNQPJV4"
event_slug: "kxcpiyoy-26jun"
event_question: "CPI year-over-year rate for year ending July 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUN-T3.8"
  question_raw: "Will the rate of CPI inflation be above 3.8% for the year ending in June 2026?"
  current_price: 0.29
  volume_24h_usd: 22275.43
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-10-13T14:00:00Z"
bullets:
  - "Kalshi prices CPI for the year ending July 2026 at 70% above 3.7% and 29% above 3.8%, with the distribution anchored firmly in the 3.7-3.8% range."
  - "With May CPI already at 4.2%, the market is pricing meaningful disinflation into July while still keeping the headline well above the Fed's 2% target."
  - "The 3.7-3.8% modal range is consistent with the core CPI ladder's sub-3% read: headline inflation seen falling faster than core, likely via energy base effects."
  - "Resolves via Bureau of Labor Statistics CPI release for the 12 months ending July 2026; any print above 3.9% represents a significant upside surprise against current pricing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "South Korea is advancing digital asset legislation this year, but the CPI ladder tied to July 2026 data reflects the dominant macro narrative of persistent inflation above 3.7%."
    publisher: "en.bloomingbit.io"
    published_at: "2026-07-14T05:01:05.000Z"
    source_url: "https://en.bloomingbit.io/feed/news/116190"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "en.bloomingbit.io"
        source_url: "https://en.bloomingbit.io/feed/news/116190"
        retrieved_at: "2026-07-14T09:54:27+00:00"
  - type: "pm_response"
    notes: "Kalshi's July CPI ladder is the longest-dated inflation read in this batch, showing the market expects headline to fall roughly 40-50 basis points from the May 4.2% print by next month."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "en.bloomingbit.io: South Korea to Push Digital Asset Law This Year, Speed Rules for Won S"
    url: "https://en.bloomingbit.io/feed/news/116190"
    published_at: "2026-07-14T05:01:05.000Z"
    retrieved_at: "2026-07-14T09:54:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
