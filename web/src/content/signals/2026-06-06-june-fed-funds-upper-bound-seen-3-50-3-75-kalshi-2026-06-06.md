---
signal_id: "CMSIG2026060601"
signal_slug: "june-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-06-06"
headline: "June Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Fed funds upper bound hardens around 3.50-3.75 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-06T00:59:05.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Fed funds upper bound (next meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.34
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-16T18:05:00Z"
bullets:
  - "Kalshi pins the Fed funds upper bound in the 3.50-3.75% range: 91% above 3.50% but only 34% above 3.75%."
  - "Hot 172K May payrolls print and hike-talk headlines are consistent with the distribution, market sees 3.50% as near-certain floor, 4.00% as a long shot at 15%."
  - "The sharp cliff from 91% to 34% at the 3.75% strike signals markets price a hold or modest move, not an aggressive hike cycle."
  - "A companion Kalshi ladder (CM-EVT-RJ6SMJGK50) prices 98% above 3.50% but collapses to 2% above 3.75%, confirming the 3.50-3.75% consensus is robust across contracts."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A strong May jobs report of 172,000 payrolls has fueled bets that new Fed Chair Kevin Warsh faces pressure to hike rates rather than cut."
    publisher: "by"
    published_at: "2026-06-06T00:59:05.000Z"
    source_url: "https://latimesnow.com/2026/06/06/hot-jobs-report-puts-fed-cuts-further-out-of-reach-as-chair-warsh-faces-policy-tests/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "by"
        source_url: "https://latimesnow.com/2026/06/06/hot-jobs-report-puts-fed-cuts-further-out-of-reach-as-chair-warsh-faces-policy-tests/"
        retrieved_at: "2026-06-08T12:25:51+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via the Federal Reserve's official rate announcement; the tight 3.50-3.75% consensus persists across multiple Fed-rate contracts."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "by: Hot jobs report puts Fed cuts further out of reach as Chair Warsh face"
    url: "https://latimesnow.com/2026/06/06/hot-jobs-report-puts-fed-cuts-further-out-of-reach-as-chair-warsh-faces-policy-tests/"
    published_at: "2026-06-06T00:59:05.000Z"
    retrieved_at: "2026-06-08T12:25:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
