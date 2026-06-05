---
signal_id: "CMSIG2026060308"
signal_slug: "bitcoin-above-75k-by-june-30-kalshi-25-2026-06-03"
headline: "Bitcoin above $75K by June 30: Kalshi 25%"
semantic_title: "Bitcoin above $75K by June 30 priced as deep tail"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-03T06:23:19.000Z"
event_id: "CM-EVT-3MXSH7KHK5"
event_slug: "kxbtcmaxmon-btc-26jun30"
event_question: "Bitcoin trimmed mean price by June 30, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXMON-BTC-26JUN30-7500000"
  question_raw: "Will BTC trimmed mean be above $75000.00 by 11:59 PM ET on Jun 30, 2026?"
  current_price: 0.25
  volume_24h_usd: 4334.16
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2026-07-01T03:59:59Z"
bullets:
  - "Kalshi's June 30 ladder prices only a 25% chance Bitcoin's trimmed mean exceeds $75,000, with just 8% above $80,000."
  - "The distribution is consistent with the reported bearish positioning: the market assigns 75% odds to BTC remaining below $75,000 by month-end."
  - "The June 5 spot ladder (CM-EVT-9VZL96QM32) implies a current price in the $67,000-$67,500 range, showing an implied gap of roughly $8,000 to the $75K strike."
  - "Resolves via Kalshi settlement using a trimmed mean Bitcoin price methodology; the trimming methodology reduces manipulation risk at settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Prediction market traders were reported betting on further Bitcoin downside, with markets implying elevated probability of sub-$55,000 prices before year-end."
    publisher: "coindesk.com"
    published_at: "2026-06-03T06:23:19.000Z"
    source_url: "https://www.coindesk.com/markets/2026/06/03/kalshi-traders-bet-bitcoin-s-selloff-has-further-to-run"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "coindesk.com"
        source_url: "https://www.coindesk.com/markets/2026/06/03/kalshi-traders-bet-bitcoin-s-selloff-has-further-to-run"
        retrieved_at: "2026-06-05T12:03:19+00:00"
  - type: "pm_response"
    notes: "Kalshi's 25% on $75K by June 30 aligns with the bearish narrative in prediction markets, with the $80K strike at just 8% confirming a decisive downside skew."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "coindesk.com: Prediction market traders bet bitcoin's selloff has further to run"
    url: "https://www.coindesk.com/markets/2026/06/03/kalshi-traders-bet-bitcoin-s-selloff-has-further-to-run"
    published_at: "2026-06-03T06:23:19.000Z"
    retrieved_at: "2026-06-05T12:03:19+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
