---
signal_id: "CMSIG2026111801"
signal_slug: "fed-funds-upper-bound-above-4-kalshi-ladder-96-2026-11-18"
headline: "Fed funds upper bound above 4%: Kalshi ladder 96%"
semantic_title: "Fed funds above 4 percent stays near full pricing"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-18T06:52:35.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound post-next meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.06
  volume_24h_usd: 166.85
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices 96% probability the fed funds upper bound clears 4.0%, with the sharp drop to 6% above 4.25% pinning the implied level squarely at 4.0-4.25%."
  - "October CPI running 0.4% month-over-month and multiple Fed officials calling for further hikes are consistent with the ladder's near-certain pricing above 4.0%."
  - "The cliff from 96% above 4.0% to just 6% above 4.25% signals markets see one more hike as nearly certain but the next step as a live debate, not a done deal."
  - "Companion Kalshi contract on a National Bitcoin Reserve sits at just 2%, suggesting crypto-specific policy tailwinds are not what is moving rate pricing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin rebounds near $64,400 as traders weigh hawkish Fed rhetoric and uncertain US monetary policy amid hot October inflation data."
    publisher: "Rahul Dhingra, Rohan Pal"
    published_at: "2026-11-18T06:52:35.000Z"
    source_url: "https://www.gadgets360.com/cryptocurrency/news/bitcoin-trades-near-usd-64400-as-nvidia-earnings-offer-crypto-market-relief-crypto-markets-prices-btc-ethereum-altcoins-eth-12342716"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Rahul Dhingra, Rohan Pal"
        source_url: "https://www.gadgets360.com/cryptocurrency/news/bitcoin-trades-near-usd-64400-as-nvidia-earnings-offer-crypto-market-relief-crypto-markets-prices-btc-ethereum-altcoins-eth-12342716"
        retrieved_at: "2026-11-18T07:48:08+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder on the fed funds upper bound is tightly clustered at the 4.0-4.25% band; the resolution source is the FOMC decision itself."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Rahul Dhingra, Rohan Pal: Bitcoin Trades Near $64,400 as Nvidia Earnings Offer Crypto Market Rel"
    url: "https://www.gadgets360.com/cryptocurrency/news/bitcoin-trades-near-usd-64400-as-nvidia-earnings-offer-crypto-market-relief-crypto-markets-prices-btc-ethereum-altcoins-eth-12342716"
    published_at: "2026-11-18T06:52:35.000Z"
    retrieved_at: "2026-11-18T07:48:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
