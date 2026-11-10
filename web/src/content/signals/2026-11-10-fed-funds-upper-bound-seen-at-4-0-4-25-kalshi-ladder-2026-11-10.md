---
signal_id: "CMSIG2026111001"
signal_slug: "fed-funds-upper-bound-seen-at-4-0-4-25-kalshi-ladder-2026-11-10"
headline: "Fed funds upper bound seen at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds near 4 percent stays heavily priced in"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-10T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound (next meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.01
  volume_24h_usd: 0.52
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the Fed funds upper bound in the 4.0-4.25% range: 83% chance above 4.0%, collapsing to just 1% above 4.25%."
  - "October CPI at 3.8% and a strong jobs report are consistent with the market's near-certain pricing of at least one more hike."
  - "The sharp cliff between 4.0% (83%) and 4.25% (1%) signals the market sees one hike as nearly certain but a double-move as near-impossible."
  - "On Kalshi, the contract for a rate cut greater than 25 basis points this year sits at just 3%, confirming the market is pricing hikes, not pivots."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "October CPI came in at 3.8% year-over-year, hotter than September's 3.7%, cementing market bets on a December Fed rate hike."
    publisher: "next-edition.com"
    published_at: "2026-11-10T00:00:00.000Z"
    source_url: "https://next-edition.com/articles/business-us-inflation-edges-up-to-3-8-in-october-as-core-prices-firm-cementing-bets-on-december-fed-rate-hike-2026-11-10"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "next-edition.com"
        source_url: "https://next-edition.com/articles/business-us-inflation-edges-up-to-3-8-in-october-as-core-prices-firm-cementing-bets-on-december-fed-rate-hike-2026-11-10"
        retrieved_at: "2026-11-10T07:47:48+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via Federal Reserve official rate decision; the 4.0-to-4.25% cliff is the dominant pricing signal."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "next-edition.com: US inflation edges up to 3.8% in October as core prices firm, cementin"
    url: "https://next-edition.com/articles/business-us-inflation-edges-up-to-3-8-in-october-as-core-prices-firm-cementing-bets-on-december-fed-rate-hike-2026-11-10"
    published_at: "2026-11-10T00:00:00.000Z"
    retrieved_at: "2026-11-10T07:47:48+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
