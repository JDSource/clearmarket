---
signal_id: "CMSIG2026101606"
signal_slug: "democrats-win-us-house-2026-kalshi-90-2026-10-16"
headline: "Democrats win US House 2026: Kalshi 90%"
semantic_title: "Democrats winning the House in 2026 stays heavily favored"
telemetry: "Kalshi 90%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-16T00:00:00.000Z"
event_id: "CM-EVT-FV8MR86S63"
event_slug: "controlh-2026"
event_question: "Will the Democratic Party win the U.S. House in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "CONTROLH-2026-D"
  question_raw: "Will Democrats win the House in 2026?"
  current_price: 0.902
  volume_24h_usd: 113572.65
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices 90% odds that Democrats win the US House in the next election, resolving via Library of Congress official records."
  - "Debate clashes and Trump's record-low approval ratings are consistent with the market's strong tilt toward a Democratic House takeover."
  - "The GOP retains-one-chamber contract (CM-EVT-T5VXKJT451) sits at 62%, implying the market prices a split Congress as the dominant scenario with the Senate remaining Republican."
  - "Resolves via Library of Congress certification; contested or delayed results in close districts could push resolution past Election Night."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "With less than three weeks to Election Day, House and Senate candidates clashed in debates as both parties contest control of Congress in the 2026 midterms."
    publisher: "Alex Nitzberg, Paul Steinhauser, Charles Creitz, Robert Schmad, Ashley J. DiMella"
    published_at: "2026-10-16T00:00:00.000Z"
    source_url: "https://www.foxnews.com/live-news/midterm-elections-2026-less-than-three-weeks-away-october-16"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Alex Nitzberg, Paul Steinhauser, Charles Creitz, Robert Schmad, Ashley J. DiMella"
        source_url: "https://www.foxnews.com/live-news/midterm-elections-2026-less-than-three-weeks-away-october-16"
        retrieved_at: "2026-10-18T07:47:28+00:00"
  - type: "pm_response"
    notes: "Kalshi hosts both the House and the multi-chamber contracts; their joint pricing implies a high-confidence Democratic House flip paired with a Senate hold for Republicans."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Alex Nitzberg, Paul Steinhauser, Charles Creitz, Robert Schmad, Ashley J. DiMella: As midterm Election Day approaches, candidates clash in debates  | Liv"
    url: "https://www.foxnews.com/live-news/midterm-elections-2026-less-than-three-weeks-away-october-16"
    published_at: "2026-10-16T00:00:00.000Z"
    retrieved_at: "2026-10-18T07:47:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
