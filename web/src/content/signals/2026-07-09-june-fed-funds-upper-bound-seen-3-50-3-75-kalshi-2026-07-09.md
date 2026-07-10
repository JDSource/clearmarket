---
signal_id: "CMSIG2026070901"
signal_slug: "june-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-07-09"
headline: "June Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Fed funds upper bound consensus anchors near 3.5 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-09T13:25:27.000Z"
event_id: "CM-EVT-PHWX2H6DM5"
event_slug: "kxfed-26jul"
event_question: "Fed funds upper bound (post-June 2026 meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUL-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Jul 29, 2026 meeting?"
  current_price: 0.14
  volume_24h_usd: 4493.01
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-08-05T18:05:00Z"
bullets:
  - "Kalshi ladder prices the Fed funds upper bound firmly in the 3.50-3.75% range: 98% above 3.50% but only 14% above 3.75%."
  - "Hawkish Fed minutes citing inflation worry align with the pricing floor above 3.50%, but the market is not pricing meaningful odds of a hike above 3.75%."
  - "Retail sales beating expectations and jobless claims at 215,000 both reduce urgency for cuts, consistent with the rate staying in this corridor."
  - "Resolution turns on the official post-meeting Federal Reserve rate announcement; the sharp drop from 98% to 14% between the 3.50% and 3.75% strikes marks the market's conviction boundary."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed minutes show growing inflation worry under Chair Kevin Warsh, with hawkish commentary keeping pressure on borrowing costs including in commercial real estate financing."
    publisher: "Matt Wasielewski, National"
    published_at: "2026-07-09T13:25:27.000Z"
    source_url: "https://www.bisnow.com/national/news/capital-markets/hot-inflation-led-some-fed-officials-to-float-a-rate-hike-in-june-minutes-show-135359"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Matt Wasielewski, National"
        source_url: "https://www.bisnow.com/national/news/capital-markets/hot-inflation-led-some-fed-officials-to-float-a-rate-hike-in-june-minutes-show-135359"
        retrieved_at: "2026-07-10T10:49:37+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder covers the full upper-bound distribution; the 84-percentage-point gap between the 3.50% and 3.75% strikes is the defining signal in this contract."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Matt Wasielewski, National: Fed's Hawkish Minutes Keep Pressure On CRE Financing"
    url: "https://www.bisnow.com/national/news/capital-markets/hot-inflation-led-some-fed-officials-to-float-a-rate-hike-in-june-minutes-show-135359"
    published_at: "2026-07-09T13:25:27.000Z"
    retrieved_at: "2026-07-10T10:49:37+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
