---
signal_id: "CMSIG2026071105"
signal_slug: "bitcoin-above-100k-by-dec-31-kalshi-14-2026-07-11"
headline: "Bitcoin above $100K by Dec 31: Kalshi 14%"
semantic_title: "Bitcoin above $100K by year-end wavers below 15 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-11T05:29:06.000Z"
event_id: "CM-EVT-0MWN62PNG9"
event_slug: "kxbtcmaxy-26dec31"
event_question: "Bitcoin price, Dec 31 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXY-26DEC31-99999.99"
  question_raw: "Will Bitcoin be above $99,999.99 by Dec 31, 2026 at 11:59 PM ET?"
  current_price: 0.14
  volume_24h_usd: 1052.18
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T04:59:00Z"
bullets:
  - "Kalshi ladder prices only 14% on Bitcoin above $100,000 by December 31, 2026, with 10% above $110K and 7% above $120K; trading volume rose 170x day over day."
  - "Bitcoin trading near $62,000 after the ceasefire breakdown puts the $100K target roughly 60% above spot, and the ladder's sub-15% pricing reflects that distance."
  - "Standard Chartered's maintained $100K target (Story 32) sits far outside the current Kalshi consensus, illustrating the gap between sell-side forecasts and prediction-market capital."
  - "Resolves via CF Benchmarks end-of-day price on December 31, 2026; the companion Kalshi contract (CM-EVT-ZPMYBGJP99) prices a separate 'cross $100K at any point' question at only 13%."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin fell below $62,000 after Trump declared the Iran ceasefire over, with geopolitical risk weighing on crypto sentiment."
    publisher: "AInvest"
    published_at: "2026-07-11T05:29:06.000Z"
    source_url: "https://www.ainvest.com/news/bitcoin-62k-trump-ceasefire-call-crypto-flush-shakeout-2607/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "AInvest"
        source_url: "https://www.ainvest.com/news/bitcoin-62k-trump-ceasefire-call-crypto-flush-shakeout-2607/"
        retrieved_at: "2026-07-11T09:24:13+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder with 170x volume surge is the primary year-end Bitcoin contract; the 13% on any-time crossing (CM-EVT-ZPMYBGJP99) confirms the market sees $100K as a tail event."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "AInvest: Bitcoin Below $62K After Trump's \"Ceasefire Is Over\" Call: Crypto Flus"
    url: "https://www.ainvest.com/news/bitcoin-62k-trump-ceasefire-call-crypto-flush-shakeout-2607/"
    published_at: "2026-07-11T05:29:06.000Z"
    retrieved_at: "2026-07-11T09:24:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
