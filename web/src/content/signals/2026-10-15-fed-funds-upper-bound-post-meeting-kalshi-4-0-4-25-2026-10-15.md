---
signal_id: "CMSIG2026101503"
signal_slug: "fed-funds-upper-bound-post-meeting-kalshi-4-0-4-25-2026-10-15"
headline: "Fed funds upper bound post-meeting: Kalshi 4.0-4.25%"
semantic_title: "Fed funds upper bound seen at 4.0-4.25 percent after next meeting"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-15T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound after next FOMC meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.14
  volume_24h_usd: 19.18
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder puts the post-meeting federal funds upper bound in the 4.0-4.25% range: 83% above 4.0%, only 14% above 4.25%."
  - "Fed Chair Kevin Warsh gave no forward guidance, but the Kalshi distribution shows markets have already priced a move to 4.0-4.25%, independent of his posture."
  - "A companion Kalshi ladder on a subsequent meeting implies 3.75-4.0% as the central range: 99% above 3.75%, only 15% above 4.0%, suggesting a one-and-done hike is the base case."
  - "Resolution via the Federal Reserve's official rate announcement; the gap between the two ladders reveals the market is pricing one hike and then a pause, not a sustained tightening cycle."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Federal Reserve Chairman Kevin Warsh declined to signal rate intentions after two hot inflation reports this week raised expectations for a sooner-than-expected rate hike."
    publisher: "Steve Kopack"
    published_at: "2026-10-15T00:00:00.000Z"
    source_url: "https://www.nbcnews.com/business/economy/will-fed-raise-interest-rates-kevin-warsh-offer-clues-rcna603661"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Steve Kopack"
        source_url: "https://www.nbcnews.com/business/economy/will-fed-raise-interest-rates-kevin-warsh-offer-clues-rcna603661"
        retrieved_at: "2026-10-18T12:25:52+00:00"
  - type: "pm_response"
    notes: "Kalshi rate ladder spans 2.75% to 5.25% strikes; the sharp drop from 83% to 14% between the 4.0% and 4.25% strikes pins the consensus tightly at a single 25bp hike."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Steve Kopack: Will the Fed raise interest rates? Kevin Warsh gives no clues"
    url: "https://www.nbcnews.com/business/economy/will-fed-raise-interest-rates-kevin-warsh-offer-clues-rcna603661"
    published_at: "2026-10-15T00:00:00.000Z"
    retrieved_at: "2026-10-18T12:25:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
