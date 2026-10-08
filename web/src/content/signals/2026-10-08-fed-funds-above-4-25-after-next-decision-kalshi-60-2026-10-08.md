---
signal_id: "CMSIG2026100803"
signal_slug: "fed-funds-above-4-25-after-next-decision-kalshi-60-2026-10-08"
headline: "Fed funds above 4.25% after next decision: Kalshi 60%"
semantic_title: "Odds climb toward another Fed hike as FOMC minutes land"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-08T00:00:00.000Z"
event_id: "CM-EVT-5P6C5JFKT9"
event_slug: "kxfed-27jan"
event_question: "Federal funds upper bound following next Fed decision"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-27JAN-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Jan 27, 2027 meeting?"
  current_price: 0.6
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2027-02-03T19:05:00Z"
bullets:
  - "Kalshi ladder prices 60% odds the federal funds upper bound exceeds 4.25% after the next decision, with 86% above 4.0%."
  - "Fed minutes citing AI-driven inflation pressure and near-unanimous support for another hike are broadly consistent with this above-4.0% skew."
  - "The Kalshi contract on cuts greater than 25 basis points this year (CM-EVT-RWRZ1R3SD6) remains at 3%, no easing scenario is priced alongside the hike expectation."
  - "The companion near-term Kalshi ladder (CM-EVT-6BS28TS762) puts only 18% on above 4.0%, confirming the market sees the terminal hike as a later-meeting event, not imminent."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed minutes pointed to a likely year-end rate hike driven by persistent inflation and AI investment pressures, triggering a crypto sell-off."
    publisher: "cryptotimes.io"
    published_at: "2026-10-08T00:00:00.000Z"
    source_url: "https://www.cryptotimes.io/2026/10/08/bitcoin-ethereum-slide-as-fed-minutes-point-to-year-end-rate-hike/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cryptotimes.io"
        source_url: "https://www.cryptotimes.io/2026/10/08/bitcoin-ethereum-slide-as-fed-minutes-point-to-year-end-rate-hike/"
        retrieved_at: "2026-10-08T07:48:09+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder; the 4.25% strike at 60% is the sharpest signal that markets are taking the minutes' year-end hike language seriously."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cryptotimes.io: Bitcoin, Ethereum Slide as Fed Minutes Point to Year-End Rate Hike"
    url: "https://www.cryptotimes.io/2026/10/08/bitcoin-ethereum-slide-as-fed-minutes-point-to-year-end-rate-hike/"
    published_at: "2026-10-08T00:00:00.000Z"
    retrieved_at: "2026-10-08T07:48:09+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
