---
signal_id: "CMSIG2026092701"
signal_slug: "fed-funds-upper-bound-at-4-25-4-5-kalshi-50-2026-09-27"
headline: "Fed funds upper bound at 4.25-4.5%: Kalshi 50%"
semantic_title: "Fed funds upper bound stays near 4.25% after September hike"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-27T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound after September 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.50"
  question_raw: "Will the upper bound of the federal funds rate be above 4.50% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.1
  volume_24h_usd: 1.6
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the Fed funds upper bound in the 4.25-4.50% range: 50% above 4.25%, only 10% above 4.50%."
  - "J.P. Morgan's September hike call is consistent with the ladder's sharp drop above 4.25%, but markets give only 10% odds to a second consecutive hike landing above 4.50%."
  - "The distribution implies the market is pricing one-and-done at 4.25-4.50%, not the full December follow-through J.P. Morgan forecasts."
  - "A companion Kalshi ladder (CM-EVT-6BS28TS762) puts 66% above 4.00% but only 2% above 4.25%, suggesting that contract covers an earlier meeting window where the upper bound was lower."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "J.P. Morgan economists confirm the Fed hiked rates in September, its first hike in three years, and forecast one more hike at the December meeting in line with revised FOMC median projections."
    publisher: "Stephen Innes 🇨🇦 🇹🇭"
    published_at: "2026-09-27T00:00:00.000Z"
    source_url: "https://thedarksideoftheboom.substack.com/p/jpm-answers-whats-the-feds-next-move"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Stephen Innes 🇨🇦 🇹🇭"
        source_url: "https://thedarksideoftheboom.substack.com/p/jpm-answers-whats-the-feds-next-move"
        retrieved_at: "2026-09-28T07:47:41+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolution is tied to the Federal Reserve's official post-meeting rate announcement; any inter-meeting action would settle at that new bound."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Stephen Innes 🇨🇦 🇹🇭: J.P. Morgan Answers: What’s the Fed’s next move?"
    url: "https://thedarksideoftheboom.substack.com/p/jpm-answers-whats-the-feds-next-move"
    published_at: "2026-09-27T00:00:00.000Z"
    retrieved_at: "2026-09-28T07:47:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
