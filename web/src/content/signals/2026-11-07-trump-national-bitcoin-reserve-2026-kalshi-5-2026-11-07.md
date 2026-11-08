---
signal_id: "CMSIG2026110708"
signal_slug: "trump-national-bitcoin-reserve-2026-kalshi-5-2026-11-07"
headline: "Trump National Bitcoin Reserve 2026: Kalshi 5%"
semantic_title: "National Bitcoin Reserve in 2026 stays a long shot"
telemetry: "Kalshi 5%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-07T14:22:00.000Z"
event_id: "CM-EVT-JQRXSG4ZX9"
event_slug: "kxbtcreserve-27"
event_question: "Will Trump create a National Bitcoin Reserve in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCRESERVE-27-JAN01"
  question_raw: "Will Trump create a National Bitcoin Reserve before Jan 1, 2027?"
  current_price: 0.05
  volume_24h_usd: 8.25
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only 5% on Trump creating a National Bitcoin Reserve in 2026."
  - "Volume on this contract rose 35.9x day-over-day, the largest spike tied to any single binary contract in today's data, suggesting the week's crypto-policy headlines are driving fresh attention."
  - "Treasury's MEXC sanctions and Binance regulatory pressure reflect a restrictive crypto policy posture, which is consistent with markets assigning low odds to a pro-Bitcoin reserve move."
  - "Kalshi resolves via The New York Times; a formal executive or legislative action creating the reserve would be required to settle positively."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "U.S. Treasury sanctioned MEXC Global over alleged illicit flows, while Binance faced a major hack and European regulatory closures, keeping crypto policy in focus."
    publisher: "Michael Millard"
    published_at: "2026-11-07T14:22:00.000Z"
    source_url: "https://ct.com/news/what-happened-in-crypto-today"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Michael Millard"
        source_url: "https://ct.com/news/what-happened-in-crypto-today"
        retrieved_at: "2026-11-08T14:44:20+00:00"
  - type: "pm_response"
    notes: "Kalshi contract saw 35.9x volume spike; despite elevated activity, the 5% price shows markets are not pricing a Bitcoin reserve as a likely 2026 outcome."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Michael Millard: Today in crypto: Treasury sanctions, MEXC US ban and Binance hack"
    url: "https://ct.com/news/what-happened-in-crypto-today"
    published_at: "2026-11-07T14:22:00.000Z"
    retrieved_at: "2026-11-08T14:44:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
