---
signal_id: "CMSIG2026060905"
signal_slug: "fed-funds-above-3-50-at-next-meeting-kalshi-98-2026-06-09"
headline: "Fed funds above 3.50% at next meeting: Kalshi 98%"
semantic_title: "Fed above 3.50 percent hardens to near-certainty on blowout jobs"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-09T10:27:00.000Z"
event_id: "CM-EVT-RJ6SMJGK50"
event_slug: "kxfed-26jun"
event_question: "Next FOMC meeting Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUN-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Jun 17, 2026 meeting?"
  current_price: 0.02
  volume_24h_usd: 1599.49
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-06-17T18:05:00Z"
bullets:
  - "Kalshi prices the Fed funds upper bound remaining above 3.50% at the next FOMC meeting at 98%, essentially fully priced."
  - "The blowout jobs print is fully consistent with this near-certainty; any near-term rate cut has been priced out of this ladder entirely."
  - "The critical information is the sharp cliff: probability above 3.75% collapses to just 2%, meaning the market is holding rates steady rather than pricing a hike."
  - "Resolves via Federal Reserve; a surprise emergency cut or hike would be the only resolution scenarios that deviate from the 3.50-3.75% consensus."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "May job growth topped all forecasts, boosting bets on a Fed rate hike and pressuring newly installed Fed Chair Kevin Warsh."
    publisher: "- By Mark NIQUETTE AND AUGUSTA SARAIVA"
    published_at: "2026-06-09T10:27:00.000Z"
    source_url: "https://www.magzter.com/stories/newspaper/Los-Angeles-Times/HIRING-SURGE-IN-MAY-BOOSTS-BETS-ON-FED-RATE-HIKE"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "- By Mark NIQUETTE AND AUGUSTA SARAIVA"
        source_url: "https://www.magzter.com/stories/newspaper/Los-Angeles-Times/HIRING-SURGE-IN-MAY-BOOSTS-BETS-ON-FED-RATE-HIKE"
        retrieved_at: "2026-06-10T11:36:47+00:00"
  - type: "pm_response"
    notes: "Kalshi's 98% above-3.50% read with only 2% above 3.75% signals strong conviction on a hold, not a hike, even as the jobs headline boosted rate-hike narrative coverage."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "- By Mark NIQUETTE AND AUGUSTA SARAIVA: Hiring surge in May boosts bets on Fed rate hike | Los Angeles Times -"
    url: "https://www.magzter.com/stories/newspaper/Los-Angeles-Times/HIRING-SURGE-IN-MAY-BOOSTS-BETS-ON-FED-RATE-HIKE"
    published_at: "2026-06-09T10:27:00.000Z"
    retrieved_at: "2026-06-10T11:36:47+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
