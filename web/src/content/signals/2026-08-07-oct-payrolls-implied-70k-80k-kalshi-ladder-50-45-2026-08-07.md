---
signal_id: "CMSIG2026080704"
signal_slug: "oct-payrolls-implied-70k-80k-kalshi-ladder-50-45-2026-08-07"
headline: "Oct payrolls implied 70K-80K: Kalshi ladder 50%/45%"
semantic_title: "October payrolls implied range stays at 70K-80K on the ladder"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-07T00:00:00.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "U.S. nonfarm payroll jobs added, October 2026"
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
  - "Kalshi ladder puts the October 2026 payroll print in the 70,000-80,000 range: 50% above 70,000, 45% above 80,000."
  - "July's minus 23,000 print is a sharp outlier; the October ladder still prices positive job growth as the modal outcome."
  - "The 85% probability above minus 25,000 and 78% above zero confirm markets do not expect sustained job losses through autumn."
  - "Resolves via the Bureau of Labor Statistics nonfarm payroll release for October 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The U.S. shed 23,000 jobs in July, far below the 95,000 economist forecast, sparking concern about a lasting slowdown."
    publisher: "Reuters"
    published_at: "2026-08-07T00:00:00.000Z"
    source_url: "https://www.marketscreener.com/news/us-suffers-unexpected-job-losses-in-july-markets-dial-back-rate-hike-expectations-ce7f50d2de88f227"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Reuters"
        source_url: "https://www.marketscreener.com/news/us-suffers-unexpected-job-losses-in-july-markets-dial-back-rate-hike-expectations-ce7f50d2de88f227"
        retrieved_at: "2026-08-09T08:36:33+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via BLS payroll release; current distribution implies markets treat July's loss as a one-month anomaly, not a trend."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Reuters: US suffers unexpected job losses in July, markets dial back rate hike"
    url: "https://www.marketscreener.com/news/us-suffers-unexpected-job-losses-in-july-markets-dial-back-rate-hike-expectations-ce7f50d2de88f227"
    published_at: "2026-08-07T00:00:00.000Z"
    retrieved_at: "2026-08-09T08:36:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
