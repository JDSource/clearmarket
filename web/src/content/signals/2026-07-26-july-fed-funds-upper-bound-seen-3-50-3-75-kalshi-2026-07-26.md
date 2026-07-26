---
signal_id: "CMSIG2026072601"
signal_slug: "july-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-07-26"
headline: "July Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Fed pause firmly priced in at 3.5 to 3.75 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-26T00:00:00.000Z"
event_id: "CM-EVT-PHWX2H6DM5"
event_slug: "kxfed-26jul"
event_question: "July 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUL-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Jul 29, 2026 meeting?"
  current_price: 0.22
  volume_24h_usd: 2650.32
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-08-05T18:05:00Z"
bullets:
  - "Kalshi ladder prices the July 2026 Fed funds upper bound firmly in the 3.50-3.75% range: 99% above 3.50%, only 22% above 3.75%."
  - "Consensus pricing is fully consistent with the 'hold' headline, the market had already priced out any July hike."
  - "The 22% probability above 3.75% reflects residual uncertainty about a surprise hike, not a cut, the lower tail is negligible."
  - "The Polymarket contract on the Fed raising rates at all in 2026 sits at 71%, suggesting longer-horizon hike risk remains on the table even as July is settled."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Federal Reserve is widely expected to hold rates at 3.5-3.75% for a fifth straight meeting amid swirling inflation pressures."
    publisher: "straitstimes.com"
    published_at: "2026-07-26T00:00:00.000Z"
    source_url: "https://www.straitstimes.com/business/us-federal-reserve-expected-to-hold-rates-steady-as-inflation-swirls"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "straitstimes.com"
        source_url: "https://www.straitstimes.com/business/us-federal-reserve-expected-to-hold-rates-steady-as-inflation-swirls"
        retrieved_at: "2026-07-26T09:55:47+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolution pins the upper bound range; the July meeting outcome will settle this contract directly."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "straitstimes.com: US Federal Reserve expected to hold rates steady as inflation swirls |"
    url: "https://www.straitstimes.com/business/us-federal-reserve-expected-to-hold-rates-steady-as-inflation-swirls"
    published_at: "2026-07-26T00:00:00.000Z"
    retrieved_at: "2026-07-26T09:55:47+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
