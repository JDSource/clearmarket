---
signal_id: "CMSIG2026091707"
signal_slug: "trump-national-bitcoin-reserve-in-2026-kalshi-10-2026-09-17"
headline: "Trump National Bitcoin Reserve in 2026: Kalshi 10%"
semantic_title: "National Bitcoin Reserve in 2026 stays a long shot despite House vote"
telemetry: "Kalshi 10%"
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
  current_price: 0.095
  volume_24h_usd: 232.62
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi contract prices only a 10% chance Trump formally creates a National Bitcoin Reserve in 2026, with volume up 1,012,338% day over day, reflecting massive fresh interest."
  - "House committee passage is a positive step, but the Senate's rejection of the CLARITY Act this week illustrates the legislative difficulty facing crypto bills in the current Congress."
  - "The companion Polymarket contract on the US establishing a national Bitcoin reserve before 2027 sits at 7%, a consistent cross-venue read that the House advance is far from decisive."
  - "Resolves via The New York Times as the named resolution source; executive action versus legislation is a key settlement edge case given Trump's existing executive-order reserve."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A House committee advanced a bill to codify Trump's Bitcoin reserve policy into law on September 17, 2026, after the crypto industry's CLARITY Act failed in the Senate."
    publisher: "cointelegraph.com"
    published_at: "2026-09-17T00:00:00.000Z"
    source_url: "https://cointelegraph.com/news/us-bitcoin-reserve-bill-passes-house-committee"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cointelegraph.com"
        source_url: "https://cointelegraph.com/news/us-bitcoin-reserve-bill-passes-house-committee"
        retrieved_at: "2026-09-19T07:47:13+00:00"
  - type: "pm_response"
    notes: "Kalshi at 10% with a 1,012,338% volume surge confirms the House committee vote is generating intense market attention, but pricing treats full legislative enactment as unlikely in 2026."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cointelegraph.com: US Bitcoin reserve bill passes House Committee"
    url: "https://cointelegraph.com/news/us-bitcoin-reserve-bill-passes-house-committee"
    published_at: "2026-09-17T00:00:00.000Z"
    retrieved_at: "2026-09-19T07:47:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
