---
signal_id: "CMSIG2026082608"
signal_slug: "trump-creates-national-bitcoin-reserve-in-2026-kalshi-10-2026-08-26"
headline: "Trump creates National Bitcoin Reserve in 2026: Kalshi 10%"
semantic_title: "National Bitcoin Reserve in 2026 stays a long shot"
telemetry: "Kalshi 10%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-26T00:00:00.000Z"
event_id: "CM-EVT-JQRXSG4ZX9"
event_slug: "kxbtcreserve-27"
event_question: "Will Trump create a National Bitcoin Reserve in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCRESERVE-27-JAN01"
  question_raw: "Will Trump create a National Bitcoin Reserve before Jan 1, 2027?"
  current_price: 0.099
  volume_24h_usd: 88.4
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only 10% odds that Trump establishes a National Bitcoin Reserve in 2026, resolves via the New York Times."
  - "Surging institutional ETF demand and 5 billion dollars in tax-deferred Bitcoin-to-ETF swaps signal strong private-sector Bitcoin adoption, but this has not shifted the Kalshi reserve contract meaningfully."
  - "The Kalshi contract for Bitcoin's next halving by 2028 sits at 72%, showing market confidence in Bitcoin's long-term structure regardless of the reserve question."
  - "Resolves via the New York Times confirmation of a formal Trump executive action establishing a National Bitcoin Reserve before year-end 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin whales moved 5 billion dollars into BlackRock's IBIT ETF via tax-deferred swaps, with the fund recording its highest year-to-date weekly cash inflow of 1.33 billion dollars."
    publisher: "Varinder Singh"
    published_at: "2026-08-26T00:00:00.000Z"
    source_url: "https://coingape.com/bitcoin-whales-have-moved-into-blackrock-etfs-tax-deferred-swaps/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Varinder Singh"
        source_url: "https://coingape.com/bitcoin-whales-have-moved-into-blackrock-etfs-tax-deferred-swaps/"
        retrieved_at: "2026-08-27T18:46:25+00:00"
  - type: "pm_response"
    notes: "Kalshi at 10% shows the market treats a formal Bitcoin reserve as a tail event despite record ETF inflows and legislative activity in Congress."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Varinder Singh: Bitcoin Whales Have Moved $5B into BlackRock ETFs in Tax-Deferred Swap"
    url: "https://coingape.com/bitcoin-whales-have-moved-into-blackrock-etfs-tax-deferred-swaps/"
    published_at: "2026-08-26T00:00:00.000Z"
    retrieved_at: "2026-08-27T18:46:25+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
