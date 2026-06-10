---
signal_id: "CMSIG2026061004"
signal_slug: "june-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-06-10"
headline: "June Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Fed funds upper bound seen pinned at 3.50-3.75 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-10T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "June 2026 Fed funds upper bound"
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
  - "Kalshi pins the June 2026 Fed funds upper bound in the 3.50-3.75% range, with 91% probability above 3.50% but only 15% above 4.00%."
  - "Blowout jobs data and rising inflation expectations are consistent with the market holding rates higher for longer, though a full hike to 4.00% or above still registers well below 20%."
  - "A separate Kalshi ladder for a subsequent meeting (CM-EVT-PHWX2H6DM5) shows 95% above 3.50% but only 14% above 3.75%, confirming the market sees 3.50-3.75% as a durable holding zone."
  - "Resolves via Federal Reserve announcement; the sharp drop from 91% to 15% at the 4.00% strike is the key distribution signal."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Blowout May jobs numbers have complicated Fed Chair Kevin Warsh's position and raised the prospect of a rate hike showdown with President Trump."
    publisher: "Keith Speights, The Motley Fool      Wed, June 10, 2026 at 3:35 AM EDT   5 min read"
    published_at: "2026-06-10T00:00:00.000Z"
    source_url: "https://finance.yahoo.com/economy/policy/articles/blowout-jobs-numbers-just-made-073500605.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Keith Speights, The Motley Fool      Wed, June 10, 2026 at 3:35 AM EDT   5 min read"
        source_url: "https://finance.yahoo.com/economy/policy/articles/blowout-jobs-numbers-just-made-073500605.html"
        retrieved_at: "2026-06-10T11:36:47+00:00"
  - type: "pm_response"
    notes: "Kalshi's distribution clusters tightly at 3.50-3.75% across multiple meeting ladders, with the strong jobs print keeping any near-term cut off the table while a hike above 4.00% remains a low-probability tail."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Keith Speights, The Motley Fool      Wed, June 10, 2026 at 3:35 AM EDT   5 min read: Blowout Jobs Numbers Just Made Kevin Warsh's Job Much Harder -- and Pu"
    url: "https://finance.yahoo.com/economy/policy/articles/blowout-jobs-numbers-just-made-073500605.html"
    published_at: "2026-06-10T00:00:00.000Z"
    retrieved_at: "2026-06-10T11:36:47+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
