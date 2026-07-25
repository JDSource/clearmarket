---
signal_id: "CMSIG2026072401"
signal_slug: "july-fed-funds-upper-bound-seen-3-75-4-0-kalshi-ladder-2026-07-24"
headline: "July Fed funds upper bound seen 3.75-4.0%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen settling near 3.75 to 4 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-24T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "July 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.12
  volume_24h_usd: 4.32
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder pins the July 2026 Fed funds upper bound in the 3.75-4.0% range: 65% above 3.75%, only 12% above 4.0%."
  - "News portrays the July decision as genuinely unpredictable; the Kalshi distribution confirms it, with sharp probability drop-off above 3.75% signaling majority bets on a hold near current levels."
  - "Trading volume on this Kalshi ladder surged 396x day-over-day, the strongest signal of fresh market attention in this batch."
  - "A companion Kalshi ladder (CM-EVT-PHWX2H6DM5) implies a tighter 3.5-3.75% range at 99% above 3.5% but only 26% above 3.75%, suggesting some disagreement on the precise terminal level across contracts."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Media coverage highlights deep uncertainty over whether the Fed under Chair Kevin Warsh will hike or hold at its July meeting, with mixed economic signals fueling the debate."
    publisher: "usatoday.com"
    published_at: "2026-07-24T00:00:00.000Z"
    source_url: "https://www.usatoday.com/story/money/economy/2026/07/24/july-fed-meeting-interest-rates-what-to-expect/91007839007/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "usatoday.com"
        source_url: "https://www.usatoday.com/story/money/economy/2026/07/24/july-fed-meeting-interest-rates-what-to-expect/91007839007/"
        retrieved_at: "2026-07-25T09:42:27+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder pricing, supported by a massive 39,567% volume surge, shows the market is treating the July Fed decision as nearly resolved around 3.75%, not 4.0%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "usatoday.com: Hike or hold? Why the Fed's July interest rate decision is hard to pre"
    url: "https://www.usatoday.com/story/money/economy/2026/07/24/july-fed-meeting-interest-rates-what-to-expect/91007839007/"
    published_at: "2026-07-24T00:00:00.000Z"
    retrieved_at: "2026-07-25T09:42:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
