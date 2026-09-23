---
signal_id: "CMSIG2026092307"
signal_slug: "trump-national-bitcoin-reserve-in-2026-kalshi-4-2026-09-23"
headline: "Trump National Bitcoin Reserve in 2026: Kalshi 4%"
semantic_title: "National Bitcoin Reserve odds remain a long shot at 4%"
telemetry: "Kalshi 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-23T04:16:08.935Z"
event_id: "CM-EVT-JQRXSG4ZX9"
event_slug: "kxbtcreserve-27"
event_question: "Will Trump create a National Bitcoin Reserve in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCRESERVE-27-JAN01"
  question_raw: "Will Trump create a National Bitcoin Reserve before Jan 1, 2027?"
  current_price: 0.042
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices just 4% on Trump creating a National Bitcoin Reserve in 2026, treating the committee passage as far short of a done deal."
  - "The bitcoin reserve bill clearing committee is the most advanced this type of legislation has been, yet the Kalshi contract is unmoved at 4%, suggesting markets see the full passage path as very unlikely."
  - "Bitcoin's rally to near $87,000 is a market price move in the spot asset; the prediction market contract specifically tracks whether Trump formally creates a reserve, a higher legal bar."
  - "Resolution is via The New York Times as the named source, meaning the contract settles on confirmed published reporting of a formal executive or legislative creation, not just committee action."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin neared $87,000 and Zcash surged 10% as a US bitcoin reserve bill cleared a congressional committee, advancing further than any prior bitcoin legislation."
    publisher: "CoinDesk"
    published_at: "2026-09-23T04:16:08.935Z"
    source_url: "https://www.coindesk.com/markets/2026/09/23/zcash-leads-crypto-majors-with-a-10-gain-as-bitcoin-holds-near-usd87-000"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "CoinDesk"
        source_url: "https://www.coindesk.com/markets/2026/09/23/zcash-leads-crypto-majors-with-a-10-gain-as-bitcoin-holds-near-usd87-000"
        retrieved_at: "2026-09-23T13:17:11+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 4%; the divergence between a strong bitcoin spot price rally and a flat 4% reserve-creation probability reflects markets pricing the asset itself separately from the policy outcome."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "CoinDesk: Bitcoin nears $87,000, Zcash zooms 10% as U.S. bitcoin reserve bill cl"
    url: "https://www.coindesk.com/markets/2026/09/23/zcash-leads-crypto-majors-with-a-10-gain-as-bitcoin-holds-near-usd87-000"
    published_at: "2026-09-23T04:16:08.935Z"
    retrieved_at: "2026-09-23T13:17:11+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
