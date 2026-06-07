---
signal_id: "CMSIG2026060503"
signal_slug: "unemployment-peak-before-2027-kalshi-implies-below-5-2026-06-05"
headline: "Unemployment peak before 2027: Kalshi implies below 5%"
semantic_title: "Peak unemployment below 5 percent holds firm in pricing"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-05T18:52:56.000Z"
event_id: "CM-EVT-RBY62SKLC0"
event_slug: "kxu3max-27"
event_question: "Peak U.S. unemployment rate before 2027"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3MAX-27-5"
  question_raw: "How high will unemployment get before 2027?"
  current_price: 0.242
  volume_24h_usd: 142.95
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-01-08T15:00:00Z"
bullets:
  - "Kalshi ladder implies peak unemployment stays below 5% before 2027; only 24% chance it hits 5% or above."
  - "May's strong payrolls are consistent with a market that sees no near-term unemployment spike."
  - "Above 6%, probabilities collapse to single digits, suggesting the market treats a severe labor deterioration as a tail event."
  - "Resolves via Bureau of Labor Statistics unemployment data; highest monthly print before January 2027 determines outcome."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Despite 172,000 jobs added in May and a resilient labor market, many Americans remain frustrated by rising prices and limited wage gains."
    publisher: "pbs.org"
    published_at: "2026-06-05T18:52:56.000Z"
    source_url: "https://www.pbs.org/newshour/economy/u-s-job-market-is-strong-but-many-americans-still-frustrated-by-prospects-and-rising-prices"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "pbs.org"
        source_url: "https://www.pbs.org/newshour/economy/u-s-job-market-is-strong-but-many-americans-still-frustrated-by-prospects-and-rising-prices"
        retrieved_at: "2026-06-07T10:26:16+00:00"
  - type: "pm_response"
    notes: "Kalshi's distribution keeps peak unemployment pricing firmly below 5%, in line with consecutive months of above-forecast payroll gains."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "pbs.org: U.S. job market is strong, but many Americans still frustrated by pros"
    url: "https://www.pbs.org/newshour/economy/u-s-job-market-is-strong-but-many-americans-still-frustrated-by-prospects-and-rising-prices"
    published_at: "2026-06-05T18:52:56.000Z"
    retrieved_at: "2026-06-07T10:26:16+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
