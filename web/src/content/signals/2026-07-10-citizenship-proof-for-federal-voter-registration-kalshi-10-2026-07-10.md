---
signal_id: "CMSIG2026071008"
signal_slug: "citizenship-proof-for-federal-voter-registration-kalshi-10-2026-07-10"
headline: "Citizenship proof for federal voter registration: Kalshi 10%"
semantic_title: "Proof of citizenship for federal registration holds at low odds"
telemetry: "Kalshi 10%"
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
  current_price: 0.1
  volume_24h_usd: 605.59
  arbitration_model: "kalshi_staff"
  resolution_source: "White House"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi contract prices only 10% on proof of citizenship being required for federal voter registration, resolved via White House announcement."
  - "Trump's EAC purge signals aggressive intent on voting rules, yet the market's 10% price shows prediction-market capital is skeptical the specific citizenship-proof requirement becomes law."
  - "The SAVE Act, a related Kalshi contract (CM-EVT-QFC5QGJS96), sits at 8%, confirming the market sees the legislative and regulatory pathway for citizenship requirements as largely blocked."
  - "Resolves via White House official announcement of a federal regulation or enacted law; executive orders that are enjoined by courts would complicate resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump fired all members of the bipartisan Election Assistance Commission as part of a broader push to reshape US voting rules, including threats to arrest election officials over noncitizen voter rolls."
    publisher: "pbs.org"
    published_at: "2026-07-10T17:01:06.000Z"
    source_url: "https://www.pbs.org/newshour/politics/trump-ousts-election-commission-members-in-latest-push-to-reshape-u-s-voting"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "pbs.org"
        source_url: "https://www.pbs.org/newshour/politics/trump-ousts-election-commission-members-in-latest-push-to-reshape-u-s-voting"
        retrieved_at: "2026-07-11T09:24:13+00:00"
  - type: "pm_response"
    notes: "Kalshi covers this via White House resolution source; the 8% SAVE Act companion contract confirms cross-event consistency and no arbitrage gap between the two related questions."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "pbs.org: Trump ousts election commission members in latest push to reshape U.S."
    url: "https://www.pbs.org/newshour/politics/trump-ousts-election-commission-members-in-latest-push-to-reshape-u-s-voting"
    published_at: "2026-07-10T17:01:06.000Z"
    retrieved_at: "2026-07-11T09:24:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
