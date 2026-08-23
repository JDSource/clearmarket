---
signal_id: "CMSIG2026082003"
signal_slug: "peak-us-unemployment-before-2027-ladder-below-4-5-2026-08-20"
headline: "Peak US unemployment before 2027: ladder below 4.5%"
semantic_title: "Peak unemployment below 4.5% stays the consensus call"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-20T00:00:00.000Z"
event_id: "CM-EVT-RBY62SKLC0"
event_slug: "kxu3max-27"
event_question: "Peak US unemployment rate before 2027"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3MAX-27-4.5"
  question_raw: "How high will unemployment get before 2027?"
  current_price: 0.21
  volume_24h_usd: 1.47
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-03-09T15:00:00Z"
bullets:
  - "Ladder pricing puts peak unemployment below 4.5% as the base case: only 21% of probability sits at 4.5% or above."
  - "Claims at 206,000 are consistent with this subdued tail, the market is not pricing a significant unemployment spike."
  - "The distribution has a long, flat tail from 5.0% to 20.0%, each capturing only 1-5%, reflecting low-probability recession scenarios."
  - "A companion ladder (CM-EVT-720DZC17Y9) implies the September U-3 rate near 4.2-4.3%, consistent with modest upward drift from the July 4.1% print."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Initial jobless claims fell to 206,000, with layoffs remaining comparatively sparse across the labor market."
    publisher: "apnews.com"
    published_at: "2026-08-20T00:00:00.000Z"
    source_url: "https://apnews.com/article/unemployment-claims-jobs-economy-layoffs-5d623586cbcf1eeeaa6ee6cc084ed566"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/unemployment-claims-jobs-economy-layoffs-5d623586cbcf1eeeaa6ee6cc084ed566"
        retrieved_at: "2026-08-23T08:24:02+00:00"
  - type: "pm_response"
    notes: "Ladder resolved via FRED unemployment data; the 21% at 4.5% is the first meaningful probability mass above the current rate."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: US unemployment claims fall with layoffs still comparatively sparse |"
    url: "https://apnews.com/article/unemployment-claims-jobs-economy-layoffs-5d623586cbcf1eeeaa6ee6cc084ed566"
    published_at: "2026-08-20T00:00:00.000Z"
    retrieved_at: "2026-08-23T08:24:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
