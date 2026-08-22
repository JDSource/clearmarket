---
signal_id: "CMSIG2026082002"
signal_slug: "fed-funds-upper-bound-seen-3-75-4-kalshi-2026-08-20"
headline: "Fed funds upper bound seen 3.75-4%: Kalshi"
semantic_title: "Next Fed funds upper bound stays near 3.75 to 4 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-20T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Next Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.17
  volume_24h_usd: 0.17
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the next Fed funds upper bound in the 3.75-4.0% range: 55% above 3.75% but only 17% above 4.0%."
  - "July FOMC minutes confirming a hike-leaning majority are broadly consistent with the ladder's modal outcome near 3.75-4.0%."
  - "A separate near-term Kalshi ladder (CM-EVT-4ZQLQPNH91) shows 99% above 3.5% but only 31% above 3.75%, suggesting the market sees 3.5-3.75% as the floor for the prior meeting, with the next step pushing modestly higher."
  - "Resolution is set by the actual Federal Reserve policy announcement; the 17% above 4.0% tail reflects residual risk if inflation data deteriorates before the next meeting."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed July minutes showed many governors favoring rate hikes rather than cuts, while Treasury rushed into the bond market with expanded buybacks."
    publisher: "The Associated Press"
    published_at: "2026-08-20T00:00:00.000Z"
    source_url: "https://fortune.com/2026/08/20/warsh-fed-treasury-bond-buybacks-yields/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "The Associated Press"
        source_url: "https://fortune.com/2026/08/20/warsh-fed-treasury-bond-buybacks-yields/"
        retrieved_at: "2026-08-22T08:23:10+00:00"
  - type: "pm_response"
    notes: "Two Kalshi ladders with overlapping strike ranges both center near 3.75-4.0%, providing consistent cross-contract corroboration on the near-term rate path."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "The Associated Press: Treasury rushes into bond market as Fed minutes show many governors wa"
    url: "https://fortune.com/2026/08/20/warsh-fed-treasury-bond-buybacks-yields/"
    published_at: "2026-08-20T00:00:00.000Z"
    retrieved_at: "2026-08-22T08:23:10+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
