---
signal_id: "CMSIG2026061901"
signal_slug: "june-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-06-19"
headline: "June Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Fed funds upper bound at 3.50-3.75 percent anchors in pricing"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-19T14:42:17.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Fed funds upper bound following June 2026 FOMC"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.36
  volume_24h_usd: 3.96
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-16T18:05:00Z"
bullets:
  - "Kalshi pins the June 2026 Fed funds upper bound in the 3.50-3.75% range: 95% above 3.50% but only 36% above 3.75%."
  - "The hold outcome is fully consistent with the market distribution; the 3.75% upper bound strike sits at exactly the current rate, confirming the market priced this correctly."
  - "The hawkish shift matters for the next meeting: 16% above 4.0% and 8% above 4.25% indicate the market partially prices a hike cycle but is not yet convinced."
  - "Companion Polymarket contract (CM-EVT-PHWX2H6DM5) shows 13% above 3.75% at a later horizon versus Kalshi's 36%, a meaningful cross-venue gap on timing of any further hike."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Warsh's first FOMC held rates at 3.50-3.75%, scrapped dot plots and forward guidance, and signaled no dovish pivot."
    publisher: "Tim McMahon"
    published_at: "2026-06-19T14:42:17.000Z"
    source_url: "https://inflationdata.com/articles/2026/06/19/warsh-first-fomc-meeting/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Tim McMahon"
        source_url: "https://inflationdata.com/articles/2026/06/19/warsh-first-fomc-meeting/"
        retrieved_at: "2026-06-20T10:30:38+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder distribution confirms the hold was fully priced; the tail above 4.0% is the live risk the market is now tracking."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Tim McMahon: Warsh's First FOMC: No Dot, No Guidance, and No Dovish Pivot"
    url: "https://inflationdata.com/articles/2026/06/19/warsh-first-fomc-meeting/"
    published_at: "2026-06-19T14:42:17.000Z"
    retrieved_at: "2026-06-20T10:30:38+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
