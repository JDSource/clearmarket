---
signal_id: "CMSIG2026100801"
signal_slug: "fed-funds-upper-bound-4-0-4-25-kalshi-ladder-2026-10-08"
headline: "Fed funds upper bound ~4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen peaking near 4 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-08T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound following next FOMC meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.19
  volume_24h_usd: 10.78
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the federal funds upper bound in the 4.00-4.25% range, with 78% above 4.00% but only 19% above 4.25%."
  - "Fed minutes signaling further tightening are broadly consistent with the ladder's implied peak, though the market sees the hike cycle ending near 4.00-4.25%, not higher."
  - "A companion Kalshi ladder (CM-EVT-6BS28TS762, volume up 8,346% day-over-day) implies a lower peak near 3.75-4.00%, with only 15% above 4.00%, a notable split across the two contracts drawing heavy fresh attention."
  - "The separate Kalshi contract on a Fed cut greater than 25 basis points this year (CM-EVT-RWRZ1R3SD6) sits at just 3%, reinforcing that cuts are firmly off the table in the near term."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed minutes signal most officials expect another rate hike, with inflation fears tied to energy and AI investment pressures."
    publisher: "James Picerno"
    published_at: "2026-10-08T00:00:00.000Z"
    source_url: "https://seekingalpha.com/article/4952772-fed-minutes-signal-more-tightening-amid-mixed-inflation-data"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "James Picerno"
        source_url: "https://seekingalpha.com/article/4952772-fed-minutes-signal-more-tightening-amid-mixed-inflation-data"
        retrieved_at: "2026-10-08T15:10:10+00:00"
  - type: "pm_response"
    notes: "Two Kalshi ladder contracts disagree on the peak rate by roughly 25 basis points; the lower-strike ladder saw volume surge over 84x day-over-day, signaling active repositioning."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "James Picerno: Fed Minutes Signal More Tightening Amid Mixed Inflation Data | Seeking"
    url: "https://seekingalpha.com/article/4952772-fed-minutes-signal-more-tightening-amid-mixed-inflation-data"
    published_at: "2026-10-08T00:00:00.000Z"
    retrieved_at: "2026-10-08T15:10:10+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
