---
signal_id: "CMSIG2026071006"
signal_slug: "proof-of-citizenship-for-voter-registration-kalshi-12-2026-07-10"
headline: "Proof of citizenship for voter registration: Kalshi 12%"
semantic_title: "Proof-of-citizenship voter registration pricing absorbs EAC firings"
telemetry: "Kalshi 12%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-10T17:01:06.000Z"
event_id: "CM-EVT-G8CYMWNWC6"
event_slug: "kxelectionbill"
event_question: "Will proof of citizenship be required for federal voter registration?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXELECTIONBILL-27JAN01"
  question_raw: "Will legislation that requires proof of U.S. citizenship as a condition of registering to vote in federal elections become law before Jan 1, 2027?"
  current_price: 0.12
  volume_24h_usd: 267.06
  arbitration_model: "kalshi_staff"
  resolution_source: "White House"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices 12% on proof of citizenship being required for federal voter registration, resolves via White House; trading volume up 12,096% day over day."
  - "The EAC firings drew massive fresh trading volume, signaling the market is absorbing the news as a potential pathway toward stricter voter ID rules."
  - "Despite the volume surge, the Kalshi price holds at just 12%, meaning the market views the EAC action as insufficient on its own to lock in the outcome."
  - "A companion Polymarket contract (CM-EVT-SGDQ0483R0) prices only 18% on Trump declaring election interference a national emergency, consistent with the low voter ID odds."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump fired all members of the bipartisan Election Assistance Commission, leaving the agency unable to act as he reshapes federal voting rules following a Supreme Court ruling allowing removal of independent agency board members."
    publisher: "pbs.org"
    published_at: "2026-07-10T17:01:06.000Z"
    source_url: "https://www.pbs.org/newshour/politics/trump-ousts-election-commission-members-in-latest-push-to-reshape-u-s-voting"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "pbs.org"
        source_url: "https://www.pbs.org/newshour/politics/trump-ousts-election-commission-members-in-latest-push-to-reshape-u-s-voting"
        retrieved_at: "2026-07-12T09:47:51+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via White House confirmation; the 122x volume spike is the real signal here, not the price level."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "pbs.org: Trump ousts election commission members in latest push to reshape U.S."
    url: "https://www.pbs.org/newshour/politics/trump-ousts-election-commission-members-in-latest-push-to-reshape-u-s-voting"
    published_at: "2026-07-10T17:01:06.000Z"
    retrieved_at: "2026-07-12T09:47:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
