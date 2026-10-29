---
signal_id: "CMSIG2026102904"
signal_slug: "negative-us-gdp-growth-in-2026-polymarket-3-2026-10-29"
headline: "Negative US GDP growth in 2026: Polymarket 3%"
semantic_title: "US recession odds in 2026 slip to long-shot territory"
telemetry: "Polymarket 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-29T14:25:00.000Z"
event_id: "CM-EVT-36YHF72CQ8"
event_slug: "negative-gdp-growth-in-2026"
event_question: "Will there be negative GDP growth in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd8c1b0a73653b1fb4fb6e8d13d0063d25810870d7ddf83e61fffb4de4522edf1"
  question_raw: "Negative GDP growth in 2026?"
  current_price: 0.029
  volume_24h_usd: 153.9
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-29T00:00:00Z"
bullets:
  - "The Polymarket contract on negative US GDP growth in 2026 prices at just 3%, a strong long-shot read."
  - "A 3.4% Q3 annualized growth print, above consensus, is directly consistent with this near-zero recession probability."
  - "Surging imports widened the trade deficit but were offset by domestic demand; the underlying growth picture reinforces the market's benign view."
  - "Resolves via UMA oracle; with three quarters of 2026 now reported positive, the bar for full-year negative growth is nearly insurmountable."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US Q3 2026 GDP grew at a 3.4% annualized pace, beating expectations, driven by investment, consumer spending, and government expenditure."
    publisher: "Rachel Barber"
    published_at: "2026-10-29T14:25:00.000Z"
    source_url: "https://www.usatoday.com/story/money/economy/2026/10/29/us-gdp-third-quarter-2026-advance-estimate/92464164007/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Rachel Barber"
        source_url: "https://www.usatoday.com/story/money/economy/2026/10/29/us-gdp-third-quarter-2026-advance-estimate/92464164007/"
        retrieved_at: "2026-10-29T14:55:20+00:00"
  - type: "pm_response"
    notes: "Polymarket's UMA oracle resolution means any annual GDP figure confirmed positive renders the contract worthless to YES holders; 3% reflects near-certainty of a NO outcome."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Rachel Barber: US GDP growth accelerated in third quarter, surpassing expectations"
    url: "https://www.usatoday.com/story/money/economy/2026/10/29/us-gdp-third-quarter-2026-advance-estimate/92464164007/"
    published_at: "2026-10-29T14:25:00.000Z"
    retrieved_at: "2026-10-29T14:55:20+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
