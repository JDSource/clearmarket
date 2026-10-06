---
signal_id: "CMSIG2026100502"
signal_slug: "fed-cut-above-25bp-this-year-kalshi-3-volume-up-81x-2026-10-05"
headline: "Fed cut above 25bp this year: Kalshi 3%, volume up 81x"
semantic_title: "Odds on a jumbo Fed cut stay near long-shot territory"
telemetry: "Kalshi 3%"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-10-05T00:00:00.000Z"
event_id: "CM-EVT-RWRZ1R3SD6"
event_slug: "kxlargecut-26"
event_question: "Will the Federal Reserve do a rate cut greater than 25 basis points this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLARGECUT-26"
  question_raw: "Will the Fed cut rates more than 25 bps in 2026?"
  current_price: 0.03
  volume_24h_usd: 17.45
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi contract on a Fed cut greater than 25 basis points in 2026 sits at just 3%, a deep long shot."
  - "Trading volume on this contract surged 8,057% day over day, signaling the FOMC minutes release is drawing sharp fresh attention."
  - "Chicago Fed President Austan Goolsbee's comment that inflation remains the Fed's priority despite a stable labor market is consistent with the 3% pricing against a jumbo cut."
  - "Resolves via Federal Reserve announcement; a 50bp-or-larger cut at any 2026 meeting would be required for a YES."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "FOMC minutes from the September 15-16 meeting are due Wednesday, with markets watching for tone on the pace of any future rate adjustments."
    publisher: "Admirals Expert Verified"
    published_at: "2026-10-05T00:00:00.000Z"
    source_url: "https://admiralmarkets.com/analytics/traders-blog/fomc-minutes-october-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Admirals Expert Verified"
        source_url: "https://admiralmarkets.com/analytics/traders-blog/fomc-minutes-october-2026"
        retrieved_at: "2026-10-06T14:42:27+00:00"
  - type: "pm_response"
    notes: "Kalshi shows near-zero pricing on an outsized cut even as volume spikes ahead of Wednesday's minutes release."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Admirals Expert Verified: FOMC Minutes October 2026: Release Time and Preview"
    url: "https://admiralmarkets.com/analytics/traders-blog/fomc-minutes-october-2026"
    published_at: "2026-10-05T00:00:00.000Z"
    retrieved_at: "2026-10-06T14:42:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
