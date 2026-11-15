---
signal_id: "CMSIG2026111304"
signal_slug: "fed-funds-above-4-25-later-meeting-kalshi-ladder-84-2026-11-13"
headline: "Fed funds above 4.25% (later meeting): Kalshi ladder 84%"
semantic_title: "Longer-horizon Fed funds above 4.25 percent builds toward full pricing"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-13T16:03:24.000Z"
event_id: "CM-EVT-KWX3HB7XG9"
event_slug: "kxfed-27apr"
event_question: "Fed funds upper bound (later meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-27APR-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Apr 28, 2027 meeting?"
  current_price: 0.84
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2027-05-05T18:05:00Z"
bullets:
  - "Kalshi ladder for a later Fed meeting shows 84% probability the upper bound exceeds 4.25%, versus only 10% at that same strike for the nearer meeting."
  - "The jump in probability from 10% to 84% across the two ladders reveals the market is pricing a January-or-later hike beyond 4.25% as the more likely path."
  - "Retail sales and Fed minutes due this week are the next data points that could shift pricing in either direction at that threshold."
  - "Resolution depends on the Federal Reserve's actual rate-setting decision at the relevant meeting; Fed minutes may reveal dissent appetite relevant to the companion dissent contracts."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Upcoming retail sales data, Fed minutes, and consumer sentiment readings are expected to shape the trajectory of Fed policy beyond December."
    publisher: "Damian J. Troise"
    published_at: "2026-11-13T16:03:24.000Z"
    source_url: "https://apnews.com/article/retail-sales-fed-inflation-interest-rates-336b95f88ac197f7d0e84199bda23136"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Damian J. Troise"
        source_url: "https://apnews.com/article/retail-sales-fed-inflation-interest-rates-336b95f88ac197f7d0e84199bda23136"
        retrieved_at: "2026-11-15T07:48:03+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder; 84% above 4.25% at later horizon vs. 10% for nearer meeting, term structure is the story."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Damian J. Troise: Retail sales and Fed minutes in focus next week"
    url: "https://apnews.com/article/retail-sales-fed-inflation-interest-rates-336b95f88ac197f7d0e84199bda23136"
    published_at: "2026-11-13T16:03:24.000Z"
    retrieved_at: "2026-11-15T07:48:03+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
