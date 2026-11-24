---
signal_id: "CMSIG2026112301"
signal_slug: "fed-funds-upper-bound-seen-at-4-0-4-25-kalshi-ladder-2026-11-23"
headline: "Fed funds upper bound seen at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds stays near 4.0-4.25 percent range on hike talk"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-23T21:05:46.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound (next hike cycle)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.05
  volume_24h_usd: 2210.81
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the federal funds upper bound near 4.0-4.25%, with 97% above 4.0% but only 5% above 4.25%."
  - "New York Fed President John Williams called for more hikes, but the Kalshi distribution shows very limited pricing of a move above 4.25%, suggesting markets are treating the hawkish posture as incomplete guidance."
  - "The sharp cutoff between 97% at 4.0% and 5% at 4.25% signals the market sees the current range as a likely ceiling, not a steppingstone."
  - "Resolution follows the FOMC target rate announcement; any surprise hike above 4.25% would reprice the ladder sharply given the current 5% tail."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "New York Fed President John Williams said inflation remains too high and signaled further rate hikes are possible over time."
    publisher: "investing.com"
    published_at: "2026-11-23T21:05:46.000Z"
    source_url: "https://www.investing.com/news/economy-news/fed-has-work-to-do-to-lower-inflation-williams-says-5046374"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "investing.com"
        source_url: "https://www.investing.com/news/economy-news/fed-has-work-to-do-to-lower-inflation-williams-says-5046374"
        retrieved_at: "2026-11-24T07:47:50+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder data is the resolution source; the implied range reflects the full strike distribution, not a single outcome."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "investing.com: Fed’s Williams says inflation still too high, signals more rate hikes"
    url: "https://www.investing.com/news/economy-news/fed-has-work-to-do-to-lower-inflation-williams-says-5046374"
    published_at: "2026-11-23T21:05:46.000Z"
    retrieved_at: "2026-11-24T07:47:50+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
