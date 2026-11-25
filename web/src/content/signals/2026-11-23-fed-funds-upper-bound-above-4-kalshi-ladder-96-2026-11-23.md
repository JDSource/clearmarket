---
signal_id: "CMSIG2026112301"
signal_slug: "fed-funds-upper-bound-above-4-kalshi-ladder-96-2026-11-23"
headline: "Fed funds upper bound above 4%: Kalshi ladder 96%"
semantic_title: "Fed funds above 4 percent stays near full pricing"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-23T21:05:46.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound (post-meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.04
  volume_24h_usd: 666.32
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices 96% odds the federal funds upper bound clears 4.00%, implying a market-implied range of roughly 4.00-4.25%."
  - "Williams flagged persistent inflation and possible further hikes, consistent with the ladder's near-certain pricing above 4.00%; trading volume surged roughly 1,000x day-over-day, signaling fresh attention."
  - "The sharp cliff at 4.25% (only 4% odds) shows markets agree hikes are likely but cap the terminal rate close to current levels."
  - "The core CPI Kalshi contract (CM-EVT-BXDL61HVR9) implies core inflation near 2.8-2.9%, slightly above the Fed's 2% target, lending support to the hawkish posture."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "New York Fed President John Williams said inflation remains too high and signaled further rate hikes are possible."
    publisher: "investing.com"
    published_at: "2026-11-23T21:05:46.000Z"
    source_url: "https://www.investing.com/news/economy-news/fed-has-work-to-do-to-lower-inflation-williams-says-5046374"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "investing.com"
        source_url: "https://www.investing.com/news/economy-news/fed-has-work-to-do-to-lower-inflation-williams-says-5046374"
        retrieved_at: "2026-11-25T07:47:45+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder on federal funds upper bound; volume spike confirms the Williams speech drew significant market attention."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "investing.com: Fed’s Williams says inflation still too high, signals more rate hikes"
    url: "https://www.investing.com/news/economy-news/fed-has-work-to-do-to-lower-inflation-williams-says-5046374"
    published_at: "2026-11-23T21:05:46.000Z"
    retrieved_at: "2026-11-25T07:47:45+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
