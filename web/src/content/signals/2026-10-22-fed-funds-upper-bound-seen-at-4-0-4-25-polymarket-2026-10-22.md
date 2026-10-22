---
signal_id: "CMSIG2026102203"
signal_slug: "fed-funds-upper-bound-seen-at-4-0-4-25-polymarket-2026-10-22"
headline: "Fed funds upper bound seen at 4.0-4.25%: Polymarket"
semantic_title: "Fed funds rate seen peaking near 4 to 4.25 percent after next meeting"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-22T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds rate upper bound after next meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.14
  volume_24h_usd: 64.42
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Polymarket ladder implies the federal funds upper bound in the 4.0-4.25% range: 70% above 4.0% but only 14% above 4.25%."
  - "September CPI at 3.7% year-over-year, above the 3.6% consensus, is consistent with markets pricing continued restrictive policy rather than imminent cuts."
  - "A separate Kalshi contract prices only 2% odds on a Fed rate cut greater than 25 basis points this year, reinforcing the hawkish-hold read."
  - "New York Fed President John Williams signaled one more 2026 hike may be appropriate, broadly in line with the ladder's 4.0-4.25% modal outcome."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "September CPI rose to 3.7% year-over-year, overshooting expectations, putting pressure on Fed Chair Kevin Warsh and stock markets."
    publisher: "Anthony Di Pizio"
    published_at: "2026-10-22T00:00:00.000Z"
    source_url: "https://www.fool.com/investing/2026/10/22/inflation-data-bad-news-kevin-warsh-stock-market/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Anthony Di Pizio"
        source_url: "https://www.fool.com/investing/2026/10/22/inflation-data-bad-news-kevin-warsh-stock-market/"
        retrieved_at: "2026-10-22T13:24:33+00:00"
  - type: "pm_response"
    notes: "Polymarket resolves via uma_oracle; the ladder distribution shows strong consensus for 4.0-4.25% with thin tail above 4.25%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Anthony Di Pizio: The Latest Inflation Data Spells Bad News for Fed Chair Kevin Warsh an"
    url: "https://www.fool.com/investing/2026/10/22/inflation-data-bad-news-kevin-warsh-stock-market/"
    published_at: "2026-10-22T00:00:00.000Z"
    retrieved_at: "2026-10-22T13:24:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
