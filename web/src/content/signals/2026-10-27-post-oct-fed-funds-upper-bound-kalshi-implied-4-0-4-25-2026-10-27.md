---
signal_id: "CMSIG2026102701"
signal_slug: "post-oct-fed-funds-upper-bound-kalshi-implied-4-0-4-25-2026-10-27"
headline: "Post-Oct Fed funds upper bound: Kalshi implied 4.0, 4.25%"
semantic_title: "Fed funds upper bound seen near 4.0, 4.25 percent after October"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-27T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Post-October 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.08
  volume_24h_usd: 157.45
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the post-October Fed funds upper bound in the 4.0, 4.25% range: 85% above 4.0%, only 8% above 4.25%."
  - "CNBC survey's 93% pause call aligns with the ladder's sharp drop-off above 4.0%, but the 76% expecting a future hike is consistent with the 85% above-4.0% read."
  - "The distribution's fat left tail, 96% above 3.75%, rules out any near-term cut scenario the news has not flagged."
  - "Companion Kalshi ladder CM-EVT-6BS28TS762 implies a slightly lower mode of 3.75, 4.0%, suggesting some residual disagreement on whether the current cycle has already peaked."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A CNBC survey shows 93% of respondents expect a Fed pause this week, but 76% anticipate a rate hike coming later, consistent with a hawkish hold posture."
    publisher: "Steve Liesman"
    published_at: "2026-10-27T00:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/10/27/federal-reserve-rate-hike-timing-expectations.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Steve Liesman"
        source_url: "https://www.cnbc.com/2026/10/27/federal-reserve-rate-hike-timing-expectations.html"
        retrieved_at: "2026-10-28T15:33:55+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder covers the post-October 2026 Fed funds upper bound; the distribution is the signal, not any single strike."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Steve Liesman: Federal Reserve rate hikes are coming, but not this week: CNBC survey"
    url: "https://www.cnbc.com/2026/10/27/federal-reserve-rate-hike-timing-expectations.html"
    published_at: "2026-10-27T00:00:00.000Z"
    retrieved_at: "2026-10-28T15:33:55+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
