---
signal_id: "CMSIG2026111602"
signal_slug: "nov-cpi-above-0-0-m-m-kalshi-ladder-55-2026-11-16"
headline: "Nov CPI above 0.0% m/m: Kalshi ladder 55%"
semantic_title: "November CPI above zero remains a long shot"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-16T19:29:12.000Z"
event_id: "CM-EVT-T57DHL6V48"
event_slug: "kxcpi-26nov"
event_question: "November 2026 CPI month-over-month"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26NOV-T-0.1"
  question_raw: "Will CPI rise more than -0.1% in November 2026?"
  current_price: 0.45
  volume_24h_usd: 8361.43
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-03-11T14:56:00Z"
bullets:
  - "The Kalshi ladder implies a 45% chance CPI prints below -0.1% in November 2026, with only 12% on exactly 0.0% and just 3% on a 0.1% or higher print."
  - "Kansas City Fed President Jeff Schmid's warning that inflation remains too high sits in tension with a distribution that assigns the highest single probability to a negative monthly print."
  - "The October CPI running at a 5.7% annualized three-month pace per Schmid contrasts sharply with a market distribution skewed heavily toward flat or negative November readings."
  - "Resolution is via the Bureau of Labor Statistics CPI release; the ladder's sharp left skew suggests the market may be pricing in seasonal or base-effect relief that offsets the hot trailing trend."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Kansas City Fed President Jeff Schmid cited a 5.7% annualized three-month CPI pace through October and flagged oil, tariffs, AI infrastructure, and healthcare as ongoing inflation drivers."
    publisher: "Miriam Hart"
    published_at: "2026-11-16T19:29:12.000Z"
    source_url: "https://econotimes.com/Kansas-City-Fed-President-Jeff-Schmid-Says-Inflation-Remains-Too-High-1777799"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Miriam Hart"
        source_url: "https://econotimes.com/Kansas-City-Fed-President-Jeff-Schmid-Says-Inflation-Remains-Too-High-1777799"
        retrieved_at: "2026-11-17T07:48:04+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder on November 2026 CPI m/m; the distribution's heavy weighting below -0.1% puts the market at odds with recent Fedspeak on persistent inflation."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Miriam Hart: Kansas City Fed President Jeff Schmid Says Inflation Remains Too High"
    url: "https://econotimes.com/Kansas-City-Fed-President-Jeff-Schmid-Says-Inflation-Remains-Too-High-1777799"
    published_at: "2026-11-16T19:29:12.000Z"
    retrieved_at: "2026-11-17T07:48:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
