---
signal_id: "CMSIG2026102004"
signal_slug: "october-jobs-added-implied-70k-80k-prediction-market-ladder-2026-10-20"
headline: "October jobs added, implied 70K-80K: prediction market ladder"
semantic_title: "October payrolls odds cluster near 70-80K implied range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-10-20T12:04:42.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "October 2026 nonfarm jobs added"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T80000"
  question_raw: "Will above 80000 jobs be added in October 2026?"
  current_price: 0.42
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "Ladder prices 51% above 70K jobs added in October and 42% above 80K, implying a market consensus near 70K-80K."
  - "The Conference Board's 'strong enough' September read is broadly consistent with this mid-range jobs outlook, not a blowout or a contraction."
  - "The 94% probability above negative 25K shows markets see near-zero risk of an outright job loss month in October."
  - "Unemployment rate ladder separately prices 71% above 4.1% for October, suggesting modest job growth alongside a slightly elevated unemployment rate."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Conference Board analysis found September employment data strong enough to shift the Fed's focus to inflation rather than labor market support."
    publisher: "Yelena Shulyatyeva"
    published_at: "2026-10-20T12:04:42.000Z"
    source_url: "https://www.conference-board.org/research/labor-markets-briefs/jobs-report-insights-sept-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Yelena Shulyatyeva"
        source_url: "https://www.conference-board.org/research/labor-markets-briefs/jobs-report-insights-sept-2026"
        retrieved_at: "2026-10-20T13:15:16+00:00"
  - type: "pm_response"
    notes: "Prediction market ladder on October payrolls; no single venue named, resolution via official BLS nonfarm payrolls release."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Yelena Shulyatyeva: Labor Market Strong Enough for Fed to Focus on Inflation"
    url: "https://www.conference-board.org/research/labor-markets-briefs/jobs-report-insights-sept-2026"
    published_at: "2026-10-20T12:04:42.000Z"
    retrieved_at: "2026-10-20T13:15:16+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
