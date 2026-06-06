---
signal_id: "CMSIG2026060307"
signal_slug: "trump-national-bitcoin-reserve-by-dec-31-kalshi-23-2026-06-03"
headline: "Trump National Bitcoin Reserve by Dec 31: Kalshi 23%"
semantic_title: "National Bitcoin Reserve by year-end wavers below one-in-four pricing"
telemetry: "Kalshi 23%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-03T15:26:50.000Z"
event_id: "CM-EVT-JQRXSG4ZX9"
event_slug: "kxbtcreserve-27"
event_question: "Will Trump create a National Bitcoin Reserve by December 31, 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCRESERVE-27-JAN01"
  question_raw: "Will Trump create a National Bitcoin Reserve before Jan 1, 2027?"
  current_price: 0.23
  volume_24h_usd: 115.83
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi puts only 23% on Trump formally creating a National Bitcoin Reserve by December 31, 2026, despite Treasury signaling progress."
  - "The market is not treating Treasury commentary as a near-term commitment, pricing the reserve as more likely to miss the year-end deadline."
  - "The CLARITY Act's passage by year-end is priced at 58% on Polymarket (CM-EVT-ZXN47LV744), suggesting legislative infrastructure is seen as more likely than the reserve itself."
  - "Kalshi resolves via The New York Times confirmation of a signed executive or legislative action creating the reserve; signaling and progress reports alone do not resolve the contract."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US Treasury Secretary signaled rapid progress on a Strategic Bitcoin Reserve, with the CLARITY Act also advancing through legislative channels."
    publisher: "TokenPost"
    published_at: "2026-06-03T15:26:50.000Z"
    source_url: "https://www.tokenpost.com/news/regulation/21061"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "TokenPost"
        source_url: "https://www.tokenpost.com/news/regulation/21061"
        retrieved_at: "2026-06-06T10:00:26+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via New York Times reporting of a formal National Bitcoin Reserve creation; Treasury signals do not constitute resolution."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "TokenPost: Treasury Signals Progress on Strategic Bitcoin Reserve as U.S. Crypto"
    url: "https://www.tokenpost.com/news/regulation/21061"
    published_at: "2026-06-03T15:26:50.000Z"
    retrieved_at: "2026-06-06T10:00:26+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
