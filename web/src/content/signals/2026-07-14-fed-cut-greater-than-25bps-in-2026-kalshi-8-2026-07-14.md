---
signal_id: "CMSIG2026071405"
signal_slug: "fed-cut-greater-than-25bps-in-2026-kalshi-8-2026-07-14"
headline: "Fed cut greater than 25bps in 2026: Kalshi 8%"
semantic_title: "Large Fed cut consensus collapses as hawkish posture holds"
telemetry: "Kalshi 8%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-14T12:36:10.000Z"
event_id: "CM-EVT-RWRZ1R3SD6"
event_slug: "kxlargecut-26"
event_question: "Will the Federal Reserve do a rate cut greater than 25 basis points this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLARGECUT-26"
  question_raw: "Will the Fed cut rates more than 25 bps in 2026?"
  current_price: 0.085
  volume_24h_usd: 434.08
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only an 8% chance the Federal Reserve cuts by more than 25 basis points at any point in 2026."
  - "Warsh's hawkish 'no tolerance' inflation rhetoric is fully consistent with a market that has nearly priced out aggressive easing."
  - "Polymarket simultaneously prices a 51% chance of a hike this year, creating a market picture skewed toward tightening rather than relief."
  - "Resolution is determined by the Federal Reserve's own policy announcement; any cut must exceed 25 basis points at a single meeting to qualify."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Chair nominee Kevin Warsh declared the Fed has 'no tolerance' for high inflation while offering no signals on the next policy move."
    publisher: "apnews.com"
    published_at: "2026-07-14T12:36:10.000Z"
    source_url: "https://apnews.com/article/warsh-federal-reserve-inflation-4a1da547d64ae3d54fba29161b213601"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/warsh-federal-reserve-inflation-4a1da547d64ae3d54fba29161b213601"
        retrieved_at: "2026-07-16T17:20:43+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via Federal Reserve official policy decision; a series of 25bp cuts would not trigger resolution."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: Warsh vows to crush inflation but offers no hint on the Fed’s next mov"
    url: "https://apnews.com/article/warsh-federal-reserve-inflation-4a1da547d64ae3d54fba29161b213601"
    published_at: "2026-07-14T12:36:10.000Z"
    retrieved_at: "2026-07-16T17:20:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
