---
signal_id: "CMSIG2026061204"
signal_slug: "fed-holds-at-4-25-4-50-with-dissent-at-june-kalshi-67-2026-06-12"
headline: "Fed holds at 4.25-4.50% with dissent at June: Kalshi 67%"
semantic_title: "Fed hold with dissent at June meeting commands majority pricing"
telemetry: "Kalshi 67%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-12T00:00:00.000Z"
event_id: "CM-EVT-MZGHWX20T0"
event_slug: "kxfedcombo-26jun"
event_question: "Will the Federal Reserve hold rates at 4.25%-4.50% with at least one dissent at its June 2026 meeting?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDCOMBO-26JUN-0-0"
  question_raw: "Will Federal Funds Rate Decision be No change AND Dissents be 0 for Jun 2026?"
  current_price: 0.67
  volume_24h_usd: 238.04
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-06-17T19:00:00Z"
bullets:
  - "Kalshi prices a Fed hold at 4.25-4.50% with at least one dissent at the June meeting at 67%."
  - "With inflation at multi-year highs and Warsh signaled as hawkish, a dissent appears consensus-expected even as the hold dominates."
  - "The Kalshi ladder for the June Fed funds upper bound shows 95% probability above 3.50% but only 36% above 3.75%, anchoring the likely outcome at 3.50-3.75% for a later meeting."
  - "Resolution is via the Bureau of Labor Statistics entry for the meeting outcome; dissent requires at least one FOMC member to vote against the hold."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Rising inflationary pressures ahead of new Fed Chair Kevin Warsh's first policy meeting fueled debate over the rate path."
    publisher: "aa.com.tr"
    published_at: "2026-06-12T00:00:00.000Z"
    source_url: "https://www.aa.com.tr/en/features/inflationary-pressures-rise-in-us-as-new-fed-chair-prepares-for-1st-meeting/3964939"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "aa.com.tr"
        source_url: "https://www.aa.com.tr/en/features/inflationary-pressures-rise-in-us-as-new-fed-chair-prepares-for-1st-meeting/3964939"
        retrieved_at: "2026-06-14T10:47:32+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via Bureau of Labor Statistics records; the 67% reflects hawkish dissent risk as near-consensus even without a hike."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "aa.com.tr: Inflationary pressures rise in US as new Fed chair prepares for 1st me"
    url: "https://www.aa.com.tr/en/features/inflationary-pressures-rise-in-us-as-new-fed-chair-prepares-for-1st-meeting/3964939"
    published_at: "2026-06-12T00:00:00.000Z"
    retrieved_at: "2026-06-14T10:47:32+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
