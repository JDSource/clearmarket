---
signal_id: "CMSIG2026070402"
signal_slug: "fed-cut-over-25bp-in-single-move-kalshi-10-2026-07-04"
headline: "Fed cut over 25bp in single move: Kalshi 10%"
semantic_title: "Outsized Fed cut consensus wavers despite weak payrolls"
telemetry: "Kalshi 10%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-04T04:02:00.000Z"
event_id: "CM-EVT-RWRZ1R3SD6"
event_slug: "kxlargecut-26"
event_question: "Will the Federal Reserve cut interest rates by more than 25 basis points in a single action this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLARGECUT-26"
  question_raw: "Will the Fed cut rates more than 25 bps in 2026?"
  current_price: 0.096
  volume_24h_usd: 157.87
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only a 10% chance the Fed cuts by more than 25 basis points in any single meeting."
  - "Warsh's inflation-first posture, even after the jobs miss, is consistent with the market's low probability on an outsized cut."
  - "The Fed funds ladder separately implies the current upper bound holds near 3.50-3.75%, reinforcing a gradualist path."
  - "Resolves via the official Federal Reserve post-meeting rate decision; a 50bp-or-larger cut in any 2026 meeting would trigger a YES."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "June payrolls missed badly at 57,000 with downward revisions, yet Federal Reserve Governor Kevin Warsh maintained an inflation-first stance."
    publisher: "Shaun Connell"
    published_at: "2026-07-04T04:02:00.000Z"
    source_url: "https://livegoldprices.com/june-payrolls-miss-by-half-but-warshs-fed-stays-locked-on-inflation/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Shaun Connell"
        source_url: "https://livegoldprices.com/june-payrolls-miss-by-half-but-warshs-fed-stays-locked-on-inflation/"
        retrieved_at: "2026-07-06T12:00:14+00:00"
  - type: "pm_response"
    notes: "Kalshi at 10% reflects the market absorbing weak payrolls without repricing for aggressive easing, consistent with the hawkish Fed communications."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Shaun Connell: June Jobs Miss: Fed's Warsh Holds Inflation-First Stance"
    url: "https://livegoldprices.com/june-payrolls-miss-by-half-but-warshs-fed-stays-locked-on-inflation/"
    published_at: "2026-07-04T04:02:00.000Z"
    retrieved_at: "2026-07-06T12:00:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
