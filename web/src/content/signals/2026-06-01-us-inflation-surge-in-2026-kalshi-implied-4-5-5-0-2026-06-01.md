---
signal_id: "CMSIG2026060103"
signal_slug: "us-inflation-surge-in-2026-kalshi-implied-4-5-5-0-2026-06-01"
headline: "US inflation surge in 2026: Kalshi implied 4.5-5.0%"
semantic_title: "US inflation surge in 2026 skeptically priced"
telemetry: "Kalshi 37%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-01T04:01:46.000Z"
event_id: "CM-EVT-H50NT0MZ04"
event_slug: "kxlcpimaxyoy-27"
event_question: "US inflation surge level 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLCPIMAXYOY-27-P5"
  question_raw: "Inflation surge in 2026?"
  current_price: 0.371
  volume_24h_usd: 26.12
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-14T15:00:00Z"
bullets:
  - "Kalshi ladder prices 65% above 4.5% inflation surge threshold and 37% above 5.0%, implying a market-expected range of 4.5-5.0%."
  - "Rising Treasury yields and bond market inflation warnings are consistent with the ladder's elevated upper-tail pricing above 5.0%."
  - "April CPI already at 3.8% with energy costs up 17.9% annually narrows the gap to the 4.5% strike significantly."
  - "Resolves via Bureau of Labor Statistics CPI data; the ladder strikes represent year-over-year CPI thresholds at defined future dates."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bond market inflation warnings mount as Trump faces midterm headwinds, with Treasury yields rising on strong data and geopolitical risk from the Iran war."
    publisher: "ABC News"
    published_at: "2026-06-01T04:01:46.000Z"
    source_url: "https://abcnews.com/US/wireStory/trump-facing-new-inflation-warning-bond-market-adding-133475094"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ABC News"
        source_url: "https://abcnews.com/US/wireStory/trump-facing-new-inflation-warning-bond-market-adding-133475094"
        retrieved_at: "2026-06-03T01:50:17+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder shows a wide distribution above 4.5% with meaningful tail above 5.5% and 6.0%, reflecting genuine uncertainty about the inflation trajectory given the Iran war energy shock."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ABC News: Trump is facing a new inflation warning from the bond market, adding t"
    url: "https://abcnews.com/US/wireStory/trump-facing-new-inflation-warning-bond-market-adding-133475094"
    published_at: "2026-06-01T04:01:46.000Z"
    retrieved_at: "2026-06-03T01:50:17+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
