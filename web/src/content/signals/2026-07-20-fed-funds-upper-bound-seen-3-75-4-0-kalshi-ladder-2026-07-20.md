---
signal_id: "CMSIG2026072001"
signal_slug: "fed-funds-upper-bound-seen-3-75-4-0-kalshi-ladder-2026-07-20"
headline: "Fed funds upper bound seen 3.75-4.0%: Kalshi ladder"
semantic_title: "Fed funds upper bound consensus wavers near 3.75-4.0 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-20T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound (future meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.29
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the Fed funds upper bound in the 3.75-4.0% range: 94% above 3.50%, 60% above 3.75%, only 29% above 4.0%."
  - "TD Securities on-hold call aligns with the distribution's center of mass, but the 60% at-or-above 3.75% shows meaningful hike risk priced in."
  - "The 29% above 4.0% reflects a non-trivial tail for a hike beyond 3.75%, consistent with Warsh-era upside risk commentary circulating this week."
  - "A separate Kalshi ladder for an earlier meeting (CM-EVT-PHWX2H6DM5) shows 99% above 3.50% but only 6% above 3.75%, pointing to a later-dated hike as the market's preferred scenario."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "TD Securities expects the Fed to hold rates unchanged through 2026, citing above-target inflation and a stabilizing labor market, but flags upside hike risk."
    publisher: "fxstreet.com"
    published_at: "2026-07-20T00:00:00.000Z"
    source_url: "https://www.fxstreet.com/news/fed-on-hold-stance-with-upside-hike-risk-td-securities-202607201337"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "fxstreet.com"
        source_url: "https://www.fxstreet.com/news/fed-on-hold-stance-with-upside-hike-risk-td-securities-202607201337"
        retrieved_at: "2026-07-21T10:22:25+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder distribution covers the full range from 2.75% to 5.25%; the 3.75-4.0% modal range is consistent with a hold-with-hike-risk consensus."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "fxstreet.com: Fed: On-hold stance with upside hike risk, TD Securities"
    url: "https://www.fxstreet.com/news/fed-on-hold-stance-with-upside-hike-risk-td-securities-202607201337"
    published_at: "2026-07-20T00:00:00.000Z"
    retrieved_at: "2026-07-21T10:22:25+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
