---
signal_id: "CMSIG2026102301"
signal_slug: "fed-funds-upper-bound-at-4-0-4-25-kalshi-ladder-2026-10-23"
headline: "Fed funds upper bound at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound climbs to 4 percent after rate hike"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-23T19:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound (post-hike)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.11
  volume_24h_usd: 11.22
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the Fed funds upper bound firmly in the 4.00-4.25% range: 96% above 3.75%, 76% above 4.00%, but only 11% above 4.25%."
  - "The unanimous 25-basis-point hike to 3.75-4.00% is consistent with the ladder's distribution, which concentrates probability mass right at the new policy band."
  - "The Kalshi contract pricing 3% on a cut greater than 25 basis points this year confirms the market sees no reversal ahead, only a tight tightening path."
  - "Resolution via the Federal Reserve's official policy statement; settlement edge case would arise only if an emergency inter-meeting move altered the upper bound before the contract closes."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Federal Reserve voted unanimously to raise its benchmark rate 25 basis points to the 3.75%-4.00% range, with Chair Kevin Warsh defying White House pressure."
    publisher: "BigGo Finance"
    published_at: "2026-10-23T19:00:00.000Z"
    source_url: "https://finance.biggo.com/news/c8c1ef5f-3d1a-4430-a7dd-0998f38a9982"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "BigGo Finance"
        source_url: "https://finance.biggo.com/news/c8c1ef5f-3d1a-4430-a7dd-0998f38a9982"
        retrieved_at: "2026-10-24T12:26:12+00:00"
  - type: "pm_response"
    notes: "The Kalshi ladder is broadly consistent with the announced hike, with the modal implied range matching the new 4.00-4.25% band and volume on the 'cut greater than 25 bps' contract up 7,152% day-over-day, signaling fresh attention on the policy direction."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "BigGo Finance: Federal Reserve Votes Unanimously to Raise Rates 25 Basis Points to 3."
    url: "https://finance.biggo.com/news/c8c1ef5f-3d1a-4430-a7dd-0998f38a9982"
    published_at: "2026-10-23T19:00:00.000Z"
    retrieved_at: "2026-10-24T12:26:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
