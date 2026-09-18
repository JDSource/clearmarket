---
signal_id: "CMSIG2026091708"
signal_slug: "national-bitcoin-reserve-in-2026-kalshi-10-2026-09-17"
headline: "National Bitcoin Reserve in 2026: Kalshi 10%"
semantic_title: "National Bitcoin Reserve creation this year stays a long shot"
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
  volume_24h_usd: 193.33
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi prediction market prices the creation of a National Bitcoin Reserve in 2026 at 10%."
  - "House committee passage of the Bitcoin reserve bill is a step forward, but Kalshi's 10% reflects how far full enactment remains from committee action alone."
  - "A Polymarket contract on the US establishing a national Bitcoin reserve before 2027 sits at 7%, slightly below Kalshi, suggesting cross-venue agreement on long-shot odds."
  - "Resolution: Kalshi settles via ABC News confirmation of formal reserve establishment."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A US House committee advanced legislation that would codify Trump's Bitcoin reserve policy into law, locking up Bitcoin acquired through forfeitures."
    publisher: "cointelegraph.com"
    published_at: "2026-09-17T00:00:00.000Z"
    source_url: "https://cointelegraph.com/news/us-bitcoin-reserve-bill-passes-house-committee"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cointelegraph.com"
        source_url: "https://cointelegraph.com/news/us-bitcoin-reserve-bill-passes-house-committee"
        retrieved_at: "2026-09-18T12:38:42+00:00"
  - type: "pm_response"
    notes: "Both Kalshi at 10% and Polymarket at 7% treat committee passage as insufficient to materially shift the probability of full legislative enactment this year."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cointelegraph.com: US Bitcoin reserve bill passes House Committee"
    url: "https://cointelegraph.com/news/us-bitcoin-reserve-bill-passes-house-committee"
    published_at: "2026-09-17T00:00:00.000Z"
    retrieved_at: "2026-09-18T12:38:42+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
