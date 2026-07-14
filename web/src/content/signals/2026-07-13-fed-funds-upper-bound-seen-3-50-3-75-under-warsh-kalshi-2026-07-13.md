---
signal_id: "CMSIG2026071303"
signal_slug: "fed-funds-upper-bound-seen-3-50-3-75-under-warsh-kalshi-2026-07-13"
headline: "Fed funds upper bound seen 3.50-3.75% under Warsh: Kalshi"
semantic_title: "Rate path under Chair Warsh wavers near 3.5-3.75 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-13T22:26:56.000Z"
event_id: "CM-EVT-6BS28TS762"
event_slug: "kxfed-26oct"
event_question: "Fed funds upper bound under Chair Warsh horizon"
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
  - "Kalshi prices the relevant Fed funds upper bound in the 3.50-3.75% range: 91% above 3.50% but only 46% above 3.75%, with a notable 23% tail above 4.0%."
  - "Warsh's House testimony comes as Waller's hike signal raised expectations; the 23% above-4.0% tail is elevated relative to the near-term Waller ladder's 8% tail."
  - "The higher tail in this contract versus the Waller-linked ladder may reflect uncertainty about Chair Warsh's own policy leanings beyond the near term."
  - "Resolves via Federal Reserve official rate decision; the 94% above 2.75% floor confirms no market expectation of cuts under this scenario."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Chair Kevin Warsh testified on monetary policy before the House, with markets closely watching his guidance on inflation and the rate path."
    publisher: "pbs.org"
    published_at: "2026-07-13T22:26:56.000Z"
    source_url: "https://www.pbs.org/newshour/politics/watch-live-fed-chair-kevin-warsh-testifies-on-monetary-policy-in-house-hearing"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "pbs.org"
        source_url: "https://www.pbs.org/newshour/politics/watch-live-fed-chair-kevin-warsh-testifies-on-monetary-policy-in-house-hearing"
        retrieved_at: "2026-07-14T09:54:27+00:00"
  - type: "pm_response"
    notes: "Kalshi's Warsh-horizon ladder carries a fatter upper tail than the Governor Waller near-term ladder, suggesting added uncertainty about the Chair's terminal guidance."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "pbs.org: WATCH LIVE: Fed chair Kevin Warsh testifies on monetary policy in Hous"
    url: "https://www.pbs.org/newshour/politics/watch-live-fed-chair-kevin-warsh-testifies-on-monetary-policy-in-house-hearing"
    published_at: "2026-07-13T22:26:56.000Z"
    retrieved_at: "2026-07-14T09:54:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
