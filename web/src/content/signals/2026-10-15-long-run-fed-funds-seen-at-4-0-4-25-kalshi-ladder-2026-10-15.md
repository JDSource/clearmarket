---
signal_id: "CMSIG2026101501"
signal_slug: "long-run-fed-funds-seen-at-4-0-4-25-kalshi-ladder-2026-10-15"
headline: "Long-run Fed funds seen at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen near 4.0-4.25% long term"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-15T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Long-run federal funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.14
  volume_24h_usd: 14.98
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the long-run federal funds upper bound in the 4.0-4.25% range, with 83% above 4.0% but only 14% above 4.25%."
  - "Warsh's deliberate ambiguity on rate timing is consistent with a market that sees the cycle peak near 4.0-4.25%, not materially higher."
  - "A separate near-term Kalshi ladder (CM-EVT-6BS28TS762) prices the upper bound firmly at 3.75-4.0%, with 99% above 3.75% but only 16% above 4.0%, suggesting the market sees one more hike before the long-run level."
  - "Resolves via the Federal Reserve's official rate announcements; the gap between the two ladders implies the market prices a single incremental hike to reach the longer-run ceiling."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Chair Kevin Warsh declined to signal the timing of a rate hike despite hotter-than-expected inflation data setting the stage for a potential move sooner than expected."
    publisher: "Steve Kopack"
    published_at: "2026-10-15T00:00:00.000Z"
    source_url: "https://www.nbcnews.com/business/economy/will-fed-raise-interest-rates-kevin-warsh-offer-clues-rcna603661"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Steve Kopack"
        source_url: "https://www.nbcnews.com/business/economy/will-fed-raise-interest-rates-kevin-warsh-offer-clues-rcna603661"
        retrieved_at: "2026-10-18T07:47:28+00:00"
  - type: "pm_response"
    notes: "Kalshi hosts both the near-term and long-run funds rate ladders; the 69-percentage-point gap between the 4.0% strikes on each ladder is the market's implied hike premium."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Steve Kopack: Will the Fed raise interest rates? Kevin Warsh gives no clues"
    url: "https://www.nbcnews.com/business/economy/will-fed-raise-interest-rates-kevin-warsh-offer-clues-rcna603661"
    published_at: "2026-10-15T00:00:00.000Z"
    retrieved_at: "2026-10-18T07:47:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
