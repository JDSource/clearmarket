---
signal_id: "CMSIG2026071305"
signal_slug: "fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-07-13"
headline: "Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Fed funds upper bound seen holding in the 3.50-3.75 percent band"
telemetry: "Kalshi ladder"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-07-13T02:06:29.000Z"
event_id: "CM-EVT-6BS28TS762"
event_slug: "kxfed-26oct"
event_question: "Federal funds rate upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26OCT-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Oct 28, 2026 meeting?"
  current_price: 0.46
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-11-04T18:05:00Z"
bullets:
  - "Kalshi ladder places the federal funds rate upper bound most likely in the 3.50-3.75% range: 91% above 3.50%, but only 46% above 3.75%."
  - "Despite hawkish inflation language in the July Fed Monetary Policy Report and Warsh testimony expectations, the market does not price a breakout above 3.75% as the base case."
  - "Companion ladder CM-EVT-4ZQLQPNH91 is broadly consistent: 92% above 3.50%, 46% above 3.75%, suggesting cross-contract coherence on the 3.50-3.75% pin."
  - "Resolves via Federal Reserve official rate announcement; the sharp drop from 91% to 46% between the 3.50% and 3.75% strikes marks the market's line in the sand."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Chair Kevin Warsh's congressional testimony this week is expected to signal the direction of rate hikes after a weak June jobs report and elevated inflation."
    publisher: "Estefano Gomez"
    published_at: "2026-07-13T02:06:29.000Z"
    source_url: "https://cryptobriefing.com/fed-chair-warshs-testimony-this-week-may-signal-rate-hike-direction/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Estefano Gomez"
        source_url: "https://cryptobriefing.com/fed-chair-warshs-testimony-this-week-may-signal-rate-hike-direction/"
        retrieved_at: "2026-07-13T10:56:18+00:00"
  - type: "pm_response"
    notes: "Kalshi's two independent Fed funds ladders are tightly aligned, both pricing the upper bound in the 3.50-3.75% range and fading the case for a move above 3.75%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Estefano Gomez: Fed Chair Warsh's testimony this week may signal rate hike direction"
    url: "https://cryptobriefing.com/fed-chair-warshs-testimony-this-week-may-signal-rate-hike-direction/"
    published_at: "2026-07-13T02:06:29.000Z"
    retrieved_at: "2026-07-13T10:56:18+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
