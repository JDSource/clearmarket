---
signal_id: "CMSIG2026062602"
signal_slug: "fed-funds-upper-bound-seen-at-3-75-4-0-kalshi-ladder-2026-06-26"
headline: "Fed funds upper bound seen at 3.75-4.0%: Kalshi ladder"
semantic_title: "Fed funds upper bound consensus anchors at 3.75 to 4.0 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-26T10:46:13.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds rate upper bound after next Fed decision"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.36
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-09T19:05:00Z"
bullets:
  - "Kalshi ladder pins the Fed funds upper bound in the 3.75-4.0% range: 65% above 3.75% but only 36% above 4.0%, and just 8% above 4.25%."
  - "The market-implied range is broadly consistent with economists' hold view but stops short of fully pricing the two hikes that financial markets reportedly expect."
  - "The sharp drop from 65% at 3.75% to 8% at 4.25% shows the market sees hikes as a low-probability tail, not a base case."
  - "The Kalshi contract on Fed cutting more than 25 basis points in a single meeting sits at only 7%, reinforcing the market's view that the next move, if any, is a modest hike or hold."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A Reuters poll shows economists expect the Fed to hold rates through year-end, while financial markets price in two hikes as inflation runs above 4%."
    publisher: "tradevae.com"
    published_at: "2026-06-26T10:46:13.000Z"
    source_url: "http://www.tradevae.com/news/economy/economists-predict-fed-will-pause-rate-moves-for-remainder-of-year-despite-market-betting-on-hikes/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "tradevae.com"
        source_url: "http://www.tradevae.com/news/economy/economists-predict-fed-will-pause-rate-moves-for-remainder-of-year-despite-market-betting-on-hikes/"
        retrieved_at: "2026-06-27T10:02:20+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder contract on Fed funds upper bound; the distribution reveals a market anchored near 3.75-4.0%, diverging from the two-hike scenario cited by financial markets in the Reuters report."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "tradevae.com: Economists Predict Fed Will Pause Rate Moves for Remainder of Year Des"
    url: "http://www.tradevae.com/news/economy/economists-predict-fed-will-pause-rate-moves-for-remainder-of-year-despite-market-betting-on-hikes/"
    published_at: "2026-06-26T10:46:13.000Z"
    retrieved_at: "2026-06-27T10:02:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
