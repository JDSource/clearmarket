---
signal_id: "CMSIG2026100707"
signal_slug: "trump-creates-national-bitcoin-reserve-in-2026-kalshi-3-2026-10-07"
headline: "Trump creates National Bitcoin Reserve in 2026: Kalshi 3%"
semantic_title: "National Bitcoin Reserve in 2026 stays a distant long shot"
telemetry: "Kalshi 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-07T00:00:00.000Z"
event_id: "CM-EVT-JQRXSG4ZX9"
event_slug: "kxbtcreserve-27"
event_question: "Will Trump create a National Bitcoin Reserve in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCRESERVE-27-JAN01"
  question_raw: "Will Trump create a National Bitcoin Reserve before Jan 1, 2027?"
  current_price: 0.034
  volume_24h_usd: 3.59
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only 3% odds on Trump creating a National Bitcoin Reserve in 2026, resolving via The New York Times."
  - "Bitcoin's drop below $84,000 on geopolitical risk and ETF outflows is consistent with a market not pricing any near-term US government Bitcoin accumulation catalyst."
  - "Separately, Kalshi's CM-EVT-5Z1MKFCSL8 prices only 4% on a Fed emergency meeting in 2026, suggesting markets see macro stress as elevated but not crisis-level."
  - "Resolves via New York Times confirmation of an official National Bitcoin Reserve establishment by year-end 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin fell below $84,000 as oil prices jumped on Iranian tanker attacks, with risk-off sentiment and ETF outflows amplifying the move."
    publisher: "Shaurya Malwa"
    published_at: "2026-10-07T00:00:00.000Z"
    source_url: "https://www.coindesk.com/markets/2026/10/07/bitcoin-dips-below-usd84-000-as-oil-jumps-on-iranian-tanker-attacks"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Shaurya Malwa"
        source_url: "https://www.coindesk.com/markets/2026/10/07/bitcoin-dips-below-usd84-000-as-oil-jumps-on-iranian-tanker-attacks"
        retrieved_at: "2026-10-07T15:02:04+00:00"
  - type: "pm_response"
    notes: "Kalshi at 3% signals that prediction markets treat a formal US Bitcoin Reserve as a near-impossibility in 2026 despite ongoing crypto policy discussion."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Shaurya Malwa: Bitcoin dips below $84,000 as oil jumps on Iranian tanker attacks"
    url: "https://www.coindesk.com/markets/2026/10/07/bitcoin-dips-below-usd84-000-as-oil-jumps-on-iranian-tanker-attacks"
    published_at: "2026-10-07T00:00:00.000Z"
    retrieved_at: "2026-10-07T15:02:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
