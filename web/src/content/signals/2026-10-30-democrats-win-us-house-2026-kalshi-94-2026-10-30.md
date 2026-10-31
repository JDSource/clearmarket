---
signal_id: "CMSIG2026103005"
signal_slug: "democrats-win-us-house-2026-kalshi-94-2026-10-30"
headline: "Democrats win US House 2026: Kalshi 94%"
semantic_title: "Democrats winning U.S. House stays heavily favored"
telemetry: "Kalshi 94%"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-10-30T00:00:00.000Z"
event_id: "CM-EVT-FV8MR86S63"
event_slug: "controlh-2026"
event_question: "Will the Democratic Party win the U.S. House in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "CONTROLH-2026-D"
  question_raw: "Will Democrats win the House in 2026?"
  current_price: 0.939
  volume_24h_usd: 626061.29
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "The Kalshi contract on Democrats winning the U.S. House is priced at 94%, placing heavy odds on a Democratic flip."
  - "News of Trump's tele-rally push to limit GOP losses and a Democratic Michigan intraparty feud has not shifted this contract off its heavily favored position."
  - "At 94%, the market is pricing near-certainty of a Democratic House, the 6% residual captures upset risk, counting errors, or unresolved close races."
  - "Resolves via the Library of Congress; the Kansas Senate Kalshi contract (CM-EVT-S6Y29BSL46) sits at 49%, suggesting Senate control remains genuinely contested."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "With the midterm campaign entering its final weekend, market attention centers on whether Democrats can flip the House amid Republican efforts to stem losses."
    publisher: "Thomson Reuters"
    published_at: "2026-10-30T00:00:00.000Z"
    source_url: "https://wtvbam.com/2026/10/30/take-five-midterms-meet-earnings/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Thomson Reuters"
        source_url: "https://wtvbam.com/2026/10/30/take-five-midterms-meet-earnings/"
        retrieved_at: "2026-10-31T14:15:55+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via Library of Congress; pairing with the 70% Republicans-hold-one-chamber contract implies the market's base case is a split Congress."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Thomson Reuters: Take Five: Midterms meet earnings"
    url: "https://wtvbam.com/2026/10/30/take-five-midterms-meet-earnings/"
    published_at: "2026-10-30T00:00:00.000Z"
    retrieved_at: "2026-10-31T14:15:55+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
