---
signal_id: "CMSIG2026102701"
signal_slug: "fed-funds-upper-bound-seen-at-4-0-4-25-kalshi-ladder-2026-10-27"
headline: "Fed funds upper bound seen at 4.0-4.25%: Kalshi ladder"
semantic_title: "Markets price Fed funds upper bound near 4 to 4.25 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-27T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound (current meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.08
  volume_24h_usd: 155.45
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices 85% above 4.0% but only 8% above 4.25%, implying a 4.0-4.25% upper bound as the consensus range."
  - "CNBC survey's 93% pause expectation is consistent with the ladder's sharp drop in probability above 4.25%."
  - "The 96% probability above 3.75% versus the 8% above 4.25% shows the market is fully pricing the hold, not pricing in an imminent hike."
  - "The Kalshi contract at 3% on a rate cut greater than 25 basis points this year (CM-EVT-RWRZ1R3SD6) confirms the market sees no easing bias either, consistent with a hawkish-hold posture."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "CNBC survey shows 93% of respondents expect a Fed pause this week, but 76% anticipate a hike at a future meeting."
    publisher: "Steve Liesman"
    published_at: "2026-10-27T00:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/10/27/federal-reserve-rate-hike-timing-expectations.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Steve Liesman"
        source_url: "https://www.cnbc.com/2026/10/27/federal-reserve-rate-hike-timing-expectations.html"
        retrieved_at: "2026-10-28T14:49:33+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder distribution is tightly clustered at 4.0-4.25%, matching the near-universal consensus for a pause reported in the CNBC survey."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Steve Liesman: Federal Reserve rate hikes are coming, but not this week: CNBC survey"
    url: "https://www.cnbc.com/2026/10/27/federal-reserve-rate-hike-timing-expectations.html"
    published_at: "2026-10-27T00:00:00.000Z"
    retrieved_at: "2026-10-28T14:49:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
