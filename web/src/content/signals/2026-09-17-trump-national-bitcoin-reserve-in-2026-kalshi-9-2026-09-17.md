---
signal_id: "CMSIG2026091706"
signal_slug: "trump-national-bitcoin-reserve-in-2026-kalshi-9-2026-09-17"
headline: "Trump national Bitcoin reserve in 2026: Kalshi 9%"
semantic_title: "Trump creating a national Bitcoin reserve in 2026 stays a long shot"
telemetry: "Kalshi 9%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-17T00:00:00.000Z"
event_id: "CM-EVT-JQRXSG4ZX9"
event_slug: "kxbtcreserve-27"
event_question: "Will Trump create a National Bitcoin Reserve in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCRESERVE-27-JAN01"
  question_raw: "Will Trump create a National Bitcoin Reserve before Jan 1, 2027?"
  current_price: 0.094
  volume_24h_usd: 30.34
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi contract on Trump creating a National Bitcoin Reserve in 2026 prices at 9%."
  - "Committee passage is a legislative milestone, but the market puts only 9% on full enactment this calendar year, signaling Senate passage is the key obstacle."
  - "A Polymarket contract on establishing a national Bitcoin reserve before 2027 (CM-EVT-0F2G0B8X49) also prices at 7%, closely tracking the Kalshi read."
  - "The Kalshi contract resolves via The New York Times confirmation of enactment; committee approval alone does not trigger resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The House Financial Services Committee advanced a bill to codify Trump's Bitcoin reserve policy into law on a party-line vote."
    publisher: "cointelegraph.com"
    published_at: "2026-09-17T00:00:00.000Z"
    source_url: "https://cointelegraph.com/news/us-bitcoin-reserve-bill-passes-house-committee"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cointelegraph.com"
        source_url: "https://cointelegraph.com/news/us-bitcoin-reserve-bill-passes-house-committee"
        retrieved_at: "2026-09-17T13:04:18+00:00"
  - type: "pm_response"
    notes: "Kalshi at 9% and Polymarket at 7% both price Senate enactment as the primary barrier; resolves via New York Times and UMA oracle respectively."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cointelegraph.com: US Bitcoin reserve bill passes House Committee"
    url: "https://cointelegraph.com/news/us-bitcoin-reserve-bill-passes-house-committee"
    published_at: "2026-09-17T00:00:00.000Z"
    retrieved_at: "2026-09-17T13:04:18+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
