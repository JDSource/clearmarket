---
signal_id: "CMSIG2026103003"
signal_slug: "fed-funds-upper-bound-above-4-kalshi-72-2026-10-30"
headline: "Fed funds upper bound above 4%: Kalshi 72%"
semantic_title: "Fed funds above 4 percent stays likely after next decision"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-30T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound after next FOMC decision"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.03
  volume_24h_usd: 130.98
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder puts 72% on the federal funds upper bound exceeding 4.0% after the next FOMC decision, but only 3% above 4.25%."
  - "PCE inflation accelerated to 3.6% in September; the news is hawkish, yet the market prices only a narrow slice of probability above 4.25%, suggesting one 25bp hike is priced but not a sustained hiking sequence."
  - "The article in Investing.com notes the Fed's December hike is roughly 63% priced in, consistent with the Kalshi ladder's concentration between 4.0% and 4.25%."
  - "Strikes below 4.0% are 98-99% priced as already-exceeded floors, confirming markets see no path back to prior accommodation in the near term."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "New PCE inflation and spending data show the economy running too hot, raising pressure on the Fed after its October wait-and-see decision by Chair Kevin Warsh."
    publisher: "Bryan Cutsinger"
    published_at: "2026-10-30T00:00:00.000Z"
    source_url: "https://thedailyeconomy.org/article/the-fed-wanted-more-data-it-got-more-inflation/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Bryan Cutsinger"
        source_url: "https://thedailyeconomy.org/article/the-fed-wanted-more-data-it-got-more-inflation/"
        retrieved_at: "2026-11-02T07:48:26+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder covers the federal funds upper bound distribution post-next-FOMC; the market is consistent with one additional hike but sharply fades any aggressive tightening beyond 4.25%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Bryan Cutsinger: The Fed Wanted More Data. It Got More Inflation. | The Daily Economy"
    url: "https://thedailyeconomy.org/article/the-fed-wanted-more-data-it-got-more-inflation/"
    published_at: "2026-10-30T00:00:00.000Z"
    retrieved_at: "2026-11-02T07:48:26+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
