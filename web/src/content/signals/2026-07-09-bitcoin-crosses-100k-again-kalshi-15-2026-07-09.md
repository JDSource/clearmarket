---
signal_id: "CMSIG2026070907"
signal_slug: "bitcoin-crosses-100k-again-kalshi-15-2026-07-09"
headline: "Bitcoin crosses $100K again: Kalshi 15%"
semantic_title: "Bitcoin above 100K consensus fractures under geopolitical weight"
telemetry: "Kalshi 15%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-09T18:35:52.000Z"
event_id: "CM-EVT-ZPMYBGJP99"
event_slug: "kxbtcmax100-26"
event_question: "Will Bitcoin cross $100,000 again?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAX100-26-DEC"
  question_raw: "Will Bitcoin be above $100000.00 by Jan 1, 2027 at 12:00AM ET?"
  current_price: 0.15
  volume_24h_usd: 366.98
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T05:00:00Z"
bullets:
  - "The Kalshi prediction market prices 15% on Bitcoin crossing $100,000 again, resolving via CF Benchmarks."
  - "Bitcoin stabilizing near $63,000 after a ceasefire collapse-driven drop to under $61,500 shows resilience, but the $100K threshold remains nearly 60% above current spot, explaining the low probability."
  - "A companion Polymarket ladder (CM-EVT-0MWN62PNG9) prices only 13% on Bitcoin above $99,999 by December 31, 2026, confirming cross-venue alignment on the $100K level as a tail outcome."
  - "Resolution via CF Benchmarks requires a confirmed close above the threshold; escalating US-Iran military activity and risk-off pressure from equities are the primary near-term headwinds the market is pricing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin rebounded to near $63,000 after a 3% slide triggered by Trump declaring the US-Iran ceasefire over, with the recovery coming despite ongoing military exchanges."
    publisher: "Terence Zimwara"
    published_at: "2026-07-09T18:35:52.000Z"
    source_url: "https://news.bitcoin.com/bitcoin-bulls-reclaim-63000-after-3-slide-as-traders-bet-the-sell-off-has-ended/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Terence Zimwara"
        source_url: "https://news.bitcoin.com/bitcoin-bulls-reclaim-63000-after-3-slide-as-traders-bet-the-sell-off-has-ended/"
        retrieved_at: "2026-07-10T10:49:37+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via CF Benchmarks; the 15% price and cross-venue Polymarket alignment at 13% frame $100K as a consensus tail risk, not a base case."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Terence Zimwara: Bitcoin Bulls Reclaim $63,000 After 3% Slide as Traders Bet the Sell-O"
    url: "https://news.bitcoin.com/bitcoin-bulls-reclaim-63000-after-3-slide-as-traders-bet-the-sell-off-has-ended/"
    published_at: "2026-07-09T18:35:52.000Z"
    retrieved_at: "2026-07-10T10:49:37+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
