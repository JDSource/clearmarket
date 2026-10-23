---
signal_id: "CMSIG2026102001"
signal_slug: "dec-fed-funds-upper-bound-seen-4-0-4-25-kalshi-2026-10-20"
headline: "Dec Fed funds upper bound seen 4.0-4.25%: Kalshi"
semantic_title: "December Fed hike stays near full pricing"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-20T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "December 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.11
  volume_24h_usd: 66.54
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the December 2026 Fed funds upper bound in the 4.0-4.25% range: 74% above 4.0% but only 11% above 4.25%."
  - "Reuters economist consensus for an October skip and December hike is broadly consistent with Kalshi pricing a peak near 4.0-4.25%."
  - "Companion ladder (CM-EVT-6BS28TS762) pins the current bound at 3.75-4.0%, implying markets see roughly one more hike priced into December."
  - "Resolves via Federal Reserve official rate announcement; any emergency inter-meeting action would shift the ladder sharply."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Reuters poll of nearly all economists calls for a Fed skip in October and a rate hike in December 2026."
    publisher: "Thomson Reuters"
    published_at: "2026-10-20T00:00:00.000Z"
    source_url: "https://95kqds.com/2026/10/20/fed-to-skip-october-but-raise-rates-again-in-december-nearly-all-economists-say-reuters-poll/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Thomson Reuters"
        source_url: "https://95kqds.com/2026/10/20/fed-to-skip-october-but-raise-rates-again-in-december-nearly-all-economists-say-reuters-poll/"
        retrieved_at: "2026-10-23T07:48:07+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder distribution shows the December hike is priced in but markets assign only slim odds to a second consecutive move above 4.25%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Thomson Reuters: Fed to skip October but raise rates again in December, nearly all econ"
    url: "https://95kqds.com/2026/10/20/fed-to-skip-october-but-raise-rates-again-in-december-nearly-all-economists-say-reuters-poll/"
    published_at: "2026-10-20T00:00:00.000Z"
    retrieved_at: "2026-10-23T07:48:07+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
