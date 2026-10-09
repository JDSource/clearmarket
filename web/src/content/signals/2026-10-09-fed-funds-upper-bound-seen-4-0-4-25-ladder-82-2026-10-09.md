---
signal_id: "CMSIG2026100901"
signal_slug: "fed-funds-upper-bound-seen-4-0-4-25-ladder-82-2026-10-09"
headline: "Fed funds upper bound seen 4.0-4.25%: ladder 82%"
semantic_title: "Fed funds near 4 percent stays favored despite soft jobs data"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-09T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound (next meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.19
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Ladder prices 82% the upper bound ends above 4.0%, but drops sharply to 19% above 4.25%, implying 4.0-4.25% as the consensus range."
  - "September payrolls printed just 29,000, well below expectations, softening the near-term hike case, consistent with the sharp drop at the 4.25% strike."
  - "Trading volume on this Kalshi ladder surged 147x day over day, signaling fresh positioning in response to the jobs data."
  - "A separate near-term Kalshi ladder (CM-EVT-6BS28TS762) implies a lower bound of 3.75-4.0%, suggesting some contracts price a pause scenario; the spread between the two ladders captures timeline uncertainty."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A weak September jobs report adding only 29,000 payrolls has cooled expectations for an October Fed rate hike, yet prediction markets still imply a terminal rate in the 4.0-4.25% range."
    publisher: "blog.e8markets.com"
    published_at: "2026-10-09T00:00:00.000Z"
    source_url: "https://blog.e8markets.com/article/soft-us-jobs-report-tilts-october-fed-odds-toward-a-pause"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "blog.e8markets.com"
        source_url: "https://blog.e8markets.com/article/soft-us-jobs-report-tilts-october-fed-odds-toward-a-pause"
        retrieved_at: "2026-10-09T07:48:13+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder volume up 147x day over day; implied range 4.0-4.25% with tail risk fading above 4.25% after the weak jobs print."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "blog.e8markets.com: Soft U.S. Jobs Report Tilts October Fed Odds Toward a Pause | E8 Marke"
    url: "https://blog.e8markets.com/article/soft-us-jobs-report-tilts-october-fed-odds-toward-a-pause"
    published_at: "2026-10-09T00:00:00.000Z"
    retrieved_at: "2026-10-09T07:48:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
