---
signal_id: "CMSIG2026082803"
signal_slug: "october-nonfarm-payrolls-seen-70k-80k-range-kalshi-ladder-2026-08-28"
headline: "October nonfarm payrolls seen 70K-80K range: Kalshi ladder"
semantic_title: "Payroll odds stay near even around 70K-80K jobs for October"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-28T00:00:00.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "October 2026 nonfarm payrolls"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T80000"
  question_raw: "Will above 80000 jobs be added in October 2026?"
  current_price: 0.45
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "The Kalshi ladder market-implied mode for October payrolls sits in the 70K-80K range, with 50% above 70K and 45% above 80K."
  - "RBC's 16K August forecast is far below the ladder's implied range, suggesting the prediction market currently prices a stronger payroll trajectory than the bank's near-term estimate implies."
  - "The 85% probability above minus-25K shows the market strongly discounts an outright contraction, even amid tariff and Fed headwinds."
  - "Resolution uses the Bureau of Labor Statistics official nonfarm payroll release for October; benchmark revisions (as in the recent BLS annual revision) can shift the final print after initial release."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "RBC Economics forecasts only 16K jobs added in August, arguing labor market tightness persists despite a payroll slowdown."
    publisher: "viktoriyapanahova"
    published_at: "2026-08-28T00:00:00.000Z"
    source_url: "https://www.rbc.com/en/economics/us-week-ahead/labor-market-tightness-to-persist-despite-payroll-slowdown/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "viktoriyapanahova"
        source_url: "https://www.rbc.com/en/economics/us-week-ahead/labor-market-tightness-to-persist-despite-payroll-slowdown/"
        retrieved_at: "2026-08-30T13:30:27+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder shows a wide distribution; the market-implied range is meaningfully above RBC's August estimate, flagging a divergence worth watching into the September jobs report."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "viktoriyapanahova: Labor market tightness to persist despite payroll slowdown - RBC Econo"
    url: "https://www.rbc.com/en/economics/us-week-ahead/labor-market-tightness-to-persist-despite-payroll-slowdown/"
    published_at: "2026-08-28T00:00:00.000Z"
    retrieved_at: "2026-08-30T13:30:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
