---
signal_id: "CMSIG2026071307"
signal_slug: "bitcoin-crosses-100k-again-by-dec-2026-kalshi-14-2026-07-13"
headline: "Bitcoin crosses $100K again by Dec 2026: Kalshi 14%"
semantic_title: "Bitcoin above $100K by year-end wavers as conflict weighs"
telemetry: "Kalshi 14%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-13T17:53:21.000Z"
event_id: "CM-EVT-ZPMYBGJP99"
event_slug: "kxbtcmax100-26"
event_question: "Will Bitcoin cross $100,000 again?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAX100-26-DEC"
  question_raw: "Will Bitcoin be above $100000.00 by Jan 1, 2027 at 12:00AM ET?"
  current_price: 0.14
  volume_24h_usd: 293.99
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T05:00:00Z"
bullets:
  - "Kalshi prices Bitcoin crossing $100,000 again by December 2026 at only 14%, with the spot price reported near $62,000 amid the US-Iran escalation."
  - "The $62,000 spot level sits roughly 61% below the $100K strike, and the Kalshi contract reflects a market that sees that gap as unlikely to close this year."
  - "A companion Ethereum minimum price contract (CM-EVT-ZPYKMKR9X3) prices Ethereum at just 9% to reach a minimum of its target level by January 2027, consistent with broad crypto weakness."
  - "Resolves via CF Benchmarks Bitcoin price on December 31, 2026; energy-driven inflation fears from the Hormuz conflict add a structural headwind not captured in pre-conflict pricing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin fell nearly 3% to the $62,000 range as US-Iran conflict and energy fears triggered over $322 million in crypto liquidations."
    publisher: "Terence Zimwara"
    published_at: "2026-07-13T17:53:21.000Z"
    source_url: "https://news.bitcoin.com/bitcoin-slides-to-62037-as-iran-conflict-sparks-fresh-energy-fears/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Terence Zimwara"
        source_url: "https://news.bitcoin.com/bitcoin-slides-to-62037-as-iran-conflict-sparks-fresh-energy-fears/"
        retrieved_at: "2026-07-14T09:54:27+00:00"
  - type: "pm_response"
    notes: "Kalshi's 14% Bitcoin $100K contract and the companion Ethereum contract together reflect a crypto market pricing in persistent macro and geopolitical headwinds through year-end."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Terence Zimwara: Bitcoin Slides to $62,037 as Iran Conflict Sparks Fresh Energy Fears"
    url: "https://news.bitcoin.com/bitcoin-slides-to-62037-as-iran-conflict-sparks-fresh-energy-fears/"
    published_at: "2026-07-13T17:53:21.000Z"
    retrieved_at: "2026-07-14T09:54:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
