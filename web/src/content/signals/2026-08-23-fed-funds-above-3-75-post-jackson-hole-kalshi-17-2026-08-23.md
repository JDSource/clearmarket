---
signal_id: "CMSIG2026082302"
signal_slug: "fed-funds-above-3-75-post-jackson-hole-kalshi-17-2026-08-23"
headline: "Fed funds above 3.75% post-Jackson Hole: Kalshi 17%"
semantic_title: "Rate cut odds build but market stays short of full pricing"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-23T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Post-Jackson Hole Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.17
  volume_24h_usd: 3.4
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder implies the post-Jackson Hole Fed funds upper bound in the 3.75-4.0% range, with 54% above 3.75% but only 17% above 4.00%."
  - "The distribution is consistent with a market leaning toward a cut from current 3.75% ceiling, not a hike, as Warsh navigates stagflationary pressures."
  - "The sharp drop from 54% at 3.75% to 17% at 4.00% reveals strong market resistance to any hike scenario despite Warsh's hawkish reputation."
  - "Resolves via the FOMC's formal rate announcement; the PCE print due this week may shift the distribution before the meeting."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Markets and analysts are focused on Fed Chair Kevin Warsh's Jackson Hole keynote and upcoming PCE data as key inputs to the rate path."
    publisher: "Dow Jones"
    published_at: "2026-08-23T00:00:00.000Z"
    source_url: "https://hk.marketscreener.com/news/week-ahead-for-fx-bonds-warsh-speech-at-jackson-hole-u-s-pce-data-in-focus-ce7858dad181f22d"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Dow Jones"
        source_url: "https://hk.marketscreener.com/news/week-ahead-for-fx-bonds-warsh-speech-at-jackson-hole-u-s-pce-data-in-focus-ce7858dad181f22d"
        retrieved_at: "2026-08-26T08:38:02+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder shows 54% above 3.75% collapsing to 17% above 4.00%, strongly suggesting a cut bias in the market ahead of Warsh's keynote."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Dow Jones: Week Ahead for FX, Bonds : Warsh Speech at Jackson Hole, U.S. PCE Data"
    url: "https://hk.marketscreener.com/news/week-ahead-for-fx-bonds-warsh-speech-at-jackson-hole-u-s-pce-data-in-focus-ce7858dad181f22d"
    published_at: "2026-08-23T00:00:00.000Z"
    retrieved_at: "2026-08-26T08:38:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
