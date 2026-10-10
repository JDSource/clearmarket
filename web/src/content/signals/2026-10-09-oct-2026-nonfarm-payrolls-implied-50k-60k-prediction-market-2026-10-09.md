---
signal_id: "CMSIG2026100902"
signal_slug: "oct-2026-nonfarm-payrolls-implied-50k-60k-prediction-market-2026-10-09"
headline: "Oct 2026 nonfarm payrolls implied 50K-60K: prediction market ladder"
semantic_title: "October payroll growth odds stay near 50-60K implied range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-09T00:00:00.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "October 2026 nonfarm payrolls added"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T60000"
  question_raw: "Will above 60000 jobs be added in October 2026?"
  current_price: 0.46
  volume_24h_usd: 0.46
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "The prediction market ladder implies a central payroll range of 50,000-60,000 for October, with 53% above 50K and 46% above 60K."
  - "September's 29K print is well below the implied median, suggesting the market expects a modest rebound but not a strong labor recovery."
  - "Weekly jobless claims at 197,000 for four straight weeks are consistent with limited layoffs but not a sharp hiring reacceleration."
  - "Resolution via Bureau of Labor Statistics Employment Situation release; any print below 30K would shift tail probabilities sharply leftward."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "September payrolls rose only 29,000, and the October 14 CPI print is now framed as the decisive test for the Fed's next policy move."
    publisher: "Sarah Chen"
    published_at: "2026-10-09T00:00:00.000Z"
    source_url: "https://marketintellabs.com/research/september-payrolls-cpi-fed-test"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Sarah Chen"
        source_url: "https://marketintellabs.com/research/september-payrolls-cpi-fed-test"
        retrieved_at: "2026-10-10T14:11:44+00:00"
  - type: "pm_response"
    notes: "Prediction market ladder covers the full distribution of October payroll outcomes; no single venue attribution available from provided data."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Sarah Chen: September Payrolls Rose 29K: October 14 CPI Is the Fed Test | MarketIn"
    url: "https://marketintellabs.com/research/september-payrolls-cpi-fed-test"
    published_at: "2026-10-09T00:00:00.000Z"
    retrieved_at: "2026-10-10T14:11:44+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
