---
signal_id: "CMSIG2026102008"
signal_slug: "bitcoin-outperforms-gold-in-2026-polymarket-41-2026-10-20"
headline: "Bitcoin outperforms gold in 2026: Polymarket 41%"
semantic_title: "Bitcoin outperforming gold in 2026 holds near 50%"
telemetry: "Polymarket 41%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-20T12:00:00.000Z"
event_id: "CM-EVT-TKKW1QZRK9"
event_slug: "will-bitcoin-outperform-gold-in-2026"
event_question: "Will Bitcoin outperform Gold in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xdcae9573d5680a2c958cca4676ed28df7a06861572124f3396cc60ab6b92b9c2"
  question_raw: "Will Bitcoin outperform Gold in 2026?"
  current_price: 0.41
  volume_24h_usd: 1199.764187
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "The Polymarket contract puts 41% odds on bitcoin outperforming gold in 2026, resolved via uma_oracle; the Kalshi equivalent (CM-EVT-FMPY92KRH8) sits at 45%."
  - "JPMorgan's bullish decade-long bitcoin projection is not fully priced in: both Polymarket and Kalshi still put the outcome as a slight underdog for 2026 specifically."
  - "Bitcoin trading near $83,000 with gold still strongly positioned year-to-date means the market is not dismissing JPMorgan's view but is not treating it as a 2026 near-term call either."
  - "The Polymarket contract on bitcoin outperforming both gold and the S&P 500 (CM-EVT-3HDQG11JV0) sits at only 21%, showing the market sees a two-front outperformance as significantly harder than beating gold alone."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "JPMorgan projected 10% annual bitcoin returns over the next decade in its first long-term BTC forecast, arguing bitcoin would top stocks, bonds, and gold, though the bank cautioned on portfolio sizing."
    publisher: "Jamie Crawley"
    published_at: "2026-10-20T12:00:00.000Z"
    source_url: "https://www.coindesk.com/markets/2026/10/20/jpmorgan-sees-10-annual-bitcoin-returns-topping-stocks-bonds-and-gold-over-next-decade"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jamie Crawley"
        source_url: "https://www.coindesk.com/markets/2026/10/20/jpmorgan-sees-10-annual-bitcoin-returns-topping-stocks-bonds-and-gold-over-next-decade"
        retrieved_at: "2026-10-21T07:48:07+00:00"
  - type: "pm_response"
    notes: "Polymarket at 41% and Kalshi at 45% on bitcoin beating gold in 2026 show the two venues are closely aligned; the JPMorgan long-term call has not moved the 2026-specific contract materially above 50%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jamie Crawley: JPMorgan sees 10% annual bitcoin returns, topping stocks, bonds and go"
    url: "https://www.coindesk.com/markets/2026/10/20/jpmorgan-sees-10-annual-bitcoin-returns-topping-stocks-bonds-and-gold-over-next-decade"
    published_at: "2026-10-20T12:00:00.000Z"
    retrieved_at: "2026-10-21T07:48:07+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
