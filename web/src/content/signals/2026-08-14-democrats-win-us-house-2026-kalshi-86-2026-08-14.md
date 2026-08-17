---
signal_id: "CMSIG2026081405"
signal_slug: "democrats-win-us-house-2026-kalshi-86-2026-08-14"
headline: "Democrats win US House 2026: Kalshi 86%"
semantic_title: "Democrats taking back the House stays heavily favored at 86%"
telemetry: "Kalshi 86%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-14T00:00:00.000Z"
event_id: "CM-EVT-FV8MR86S63"
event_slug: "controlh-2026"
event_question: "Will the Democratic Party win the U.S. House in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "CONTROLH-2026-D"
  question_raw: "Will Democrats win the House in 2026?"
  current_price: 0.86
  volume_24h_usd: 3679.22
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices an 86% probability that the Democratic Party wins the US House in the next election, resolves via Library of Congress."
  - "Election-security concerns and state-level Democratic mobilization are consistent with a market strongly favoring a Democratic House flip."
  - "Companion Kalshi contract on Republicans holding at least one chamber of Congress after the 2026 midterms sits at 47%, suggesting Senate control is far less certain."
  - "Polymarket contract on a blue wave in 2026 is at 76%, broadly consistent with the Kalshi House reading and pointing to a Democratic sweep scenario as the market consensus."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "State Democratic officials are preparing election-integrity defenses ahead of November as Trump pushes for more federal involvement in local voting."
    publisher: "Kevin Hardy"
    published_at: "2026-08-14T00:00:00.000Z"
    source_url: "https://stateline.org/2026/08/14/no-more-hypothetical-situations-state-officials-work-to-protect-elections-from-the-feds/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Kevin Hardy"
        source_url: "https://stateline.org/2026/08/14/no-more-hypothetical-situations-state-officials-work-to-protect-elections-from-the-feds/"
        retrieved_at: "2026-08-17T08:37:49+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via Library of Congress; the 86% price reflects a strong structural lean toward Democrats in the current generic-ballot environment."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Kevin Hardy: No more 'hypothetical situations': States move to fortify elections ag"
    url: "https://stateline.org/2026/08/14/no-more-hypothetical-situations-state-officials-work-to-protect-elections-from-the-feds/"
    published_at: "2026-08-14T00:00:00.000Z"
    retrieved_at: "2026-08-17T08:37:49+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
