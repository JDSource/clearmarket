---
signal_id: "CMSIG2026072104"
signal_slug: "fed-funds-upper-bound-seen-3-25-3-50-kalshi-ladder-2026-07-21"
headline: "Fed funds upper bound seen 3.25-3.50%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen settling near 3.25 to 3.5 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-21T00:00:00.000Z"
event_id: "CM-EVT-V37TZKN222"
event_slug: "kxfed-27mar"
event_question: "Federal funds rate upper bound (current cycle)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-27MAR-T3.50"
  question_raw: "Will the upper bound of the federal funds rate be above 3.50% following the Fed's Mar 17, 2027 meeting?"
  current_price: 0.35
  volume_24h_usd: 1.05
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2027-03-24T18:05:00Z"
bullets:
  - "Kalshi's ladder prices the federal funds upper bound most likely in the 3.25-3.50% range: 89% above 3.25%, but only 35% above 3.50%, with volume up 1,764% day over day."
  - "Goldman Sachs flags a 'new Fed era' of uncertainty; the ladder's sharp break at 3.50% shows markets pricing a high bar for further cuts."
  - "The separate Kalshi binary at 7% for a cut greater than 25 basis points this year reinforces that incremental easing, not bold action, is the dominant expectation."
  - "Resolves via the Federal Reserve's official rate announcement; the upper bound of the target range, not the effective rate, is the settlement metric."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Goldman Sachs midyear outlook highlights deep uncertainty around the new Fed chair's first policy moves amid easing inflation and escalating Middle East tensions."
    publisher: "goldmansachs.com"
    published_at: "2026-07-21T00:00:00.000Z"
    source_url: "https://www.goldmansachs.com/insights/goldman-sachs-exchanges/us-midyear-outlook-geopolitical-shocks-the-new-fed-era-and-growth"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "goldmansachs.com"
        source_url: "https://www.goldmansachs.com/insights/goldman-sachs-exchanges/us-midyear-outlook-geopolitical-shocks-the-new-fed-era-and-growth"
        retrieved_at: "2026-07-23T10:16:46+00:00"
  - type: "pm_response"
    notes: "The 1,764% volume surge on the Kalshi rate ladder signals sharply elevated trading activity around the new Fed chair's policy path."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "goldmansachs.com: US Midyear Outlook: Geopolitical Shocks, the New Fed Era, and Growth |"
    url: "https://www.goldmansachs.com/insights/goldman-sachs-exchanges/us-midyear-outlook-geopolitical-shocks-the-new-fed-era-and-growth"
    published_at: "2026-07-21T00:00:00.000Z"
    retrieved_at: "2026-07-23T10:16:46+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
