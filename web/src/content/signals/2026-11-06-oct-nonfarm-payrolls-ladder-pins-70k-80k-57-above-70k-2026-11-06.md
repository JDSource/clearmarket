---
signal_id: "CMSIG2026110601"
signal_slug: "oct-nonfarm-payrolls-ladder-pins-70k-80k-57-above-70k-2026-11-06"
headline: "Oct nonfarm payrolls: ladder pins 70K-80K, 57% above 70K"
semantic_title: "October payrolls seen near 70K-80K, odds long on strong rebound"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-06T05:04:41.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "October 2026 nonfarm payrolls"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T80000"
  question_raw: "Will above 80000 jobs be added in October 2026?"
  current_price: 0.39
  volume_24h_usd: 379.07
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "Ladder prices 57% above 70K and only 39% above 80K, implying a central estimate near 70K-80K, well below a robust rebound."
  - "Reuters consensus calls for a pickup in hiring after soft September; market distribution is consistent but skews toward modest, not strong, recovery."
  - "Volume on the ladder surged 163.9x day over day, signaling heavy fresh positioning ahead of Friday's data release."
  - "Companion unemployment ladder (CM-EVT-2X91TW50H2) pins October U-3 at 4.1-4.2%, with 94% above 4.0%, adding context that any payroll rebound is not expected to tighten labor supply materially."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Reuters reports October payrolls expected to rebound from a soft September, with wage growth set to moderate."
    publisher: "investing.com"
    published_at: "2026-11-06T05:04:41.000Z"
    source_url: "https://www.investing.com/news/economic-indicators/us-job-growth-expected-to-pick-up-in-october-with-moderation-in-wage-gains-5006475"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "investing.com"
        source_url: "https://www.investing.com/news/economic-indicators/us-job-growth-expected-to-pick-up-in-october-with-moderation-in-wage-gains-5006475"
        retrieved_at: "2026-11-06T07:48:14+00:00"
  - type: "pm_response"
    notes: "Ladder carries validated volume data showing 163.9x day-over-day surge; binary payroll and unemployment ladders are priced consistently with a soft but positive October print."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "investing.com: US job growth expected to pick up in October, with moderation in wage"
    url: "https://www.investing.com/news/economic-indicators/us-job-growth-expected-to-pick-up-in-october-with-moderation-in-wage-gains-5006475"
    published_at: "2026-11-06T05:04:41.000Z"
    retrieved_at: "2026-11-06T07:48:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
