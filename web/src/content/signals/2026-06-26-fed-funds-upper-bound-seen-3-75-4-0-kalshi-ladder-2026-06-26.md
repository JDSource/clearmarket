---
signal_id: "CMSIG2026062607"
signal_slug: "fed-funds-upper-bound-seen-3-75-4-0-kalshi-ladder-2026-06-26"
headline: "Fed funds upper bound seen 3.75-4.0%: Kalshi ladder"
semantic_title: "Fed funds upper bound consensus anchors at 3.75 to 4.0 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-26T10:46:13.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds rate upper bound post-June 2026"
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
  - "Kalshi ladder pins the post-June Fed funds upper bound in the 3.75-4.0% range: 86% above 3.50%, 55% above 3.75%, only 36% above 4.00%."
  - "The Reuters economist consensus for a hold is directionally consistent with the ladder's modal outcome around 3.75-4.0%, below the current 4.25-4.50% range."
  - "Minneapolis Fed President Neel Kashkari penciling in one hike is not reflected in the ladder, which prices only 36% above 4.0%; market is discounting his hawkish dot."
  - "A companion Kalshi contract prices the Fed cutting by more than 25 basis points in a single meeting at 7%, and cutting before 2027 at 24%, consistent with the ladder implying gradual easing not aggressive cuts."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A Reuters poll of economists shows the Fed will hold rates for the rest of 2026, defying market bets for hikes, with Minneapolis Fed President Neel Kashkari separately penciling in one hike."
    publisher: "Thomson Reuters"
    published_at: "2026-06-26T10:46:13.000Z"
    source_url: "https://kelo.com/2026/06/26/fed-to-hold-rates-this-year-economists-say-defying-market-bets-for-hikes-reuters-poll/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Thomson Reuters"
        source_url: "https://kelo.com/2026/06/26/fed-to-hold-rates-this-year-economists-say-defying-market-bets-for-hikes-reuters-poll/"
        retrieved_at: "2026-06-29T01:46:24+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via Federal Reserve; the distribution shows economists' hold view and Kashkari's hike view are both being partially faded by the market."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Thomson Reuters: Fed to hold rates this year, economists say, defying market bets for h"
    url: "https://kelo.com/2026/06/26/fed-to-hold-rates-this-year-economists-say-defying-market-bets-for-hikes-reuters-poll/"
    published_at: "2026-06-26T10:46:13.000Z"
    retrieved_at: "2026-06-29T01:46:24+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
