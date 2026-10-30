---
signal_id: "CMSIG2026102903"
signal_slug: "negative-us-gdp-growth-in-2026-polymarket-3-2026-10-29"
headline: "Negative US GDP growth in 2026: Polymarket 3%"
semantic_title: "Negative US GDP growth in 2026 stays a long shot"
telemetry: "Polymarket 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-10-29T16:00:00.000Z"
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
  - "The Polymarket contract on negative GDP growth in 2026 sits at just 3%, resolving via UMA oracle."
  - "A 3.4% Q3 print, better than expected, is squarely inconsistent with a recession scenario, and the market's 3% probability reflects that."
  - "With inflation at 3.7% and the Fed on hold, the economy is running hot; recession pricing has little catalytic support from current data."
  - "The companion ladder event CM-EVT-NN523F6SZ3 shows inflation above 4.5% in 2026 is priced below 16%, suggesting the market sees strong but not runaway growth."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US GDP grew 3.4% in Q3 2026, beating expectations, driven by business investment and consumer spending despite high gas prices."
    publisher: "Konrad Putzier"
    published_at: "2026-10-29T16:00:00.000Z"
    source_url: "https://www.wsj.com/economy/us-gdp-report-q3-2026-87eb755d"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Konrad Putzier"
        source_url: "https://www.wsj.com/economy/us-gdp-report-q3-2026-87eb755d"
        retrieved_at: "2026-10-30T07:48:00+00:00"
  - type: "pm_response"
    notes: "Polymarket assigns near-negligible odds to a 2026 recession even after a strong GDP print, fully consistent with the bullish economic data."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Konrad Putzier: U.S. Economy Accelerated This Summer Despite High Gas Prices"
    url: "https://www.wsj.com/economy/us-gdp-report-q3-2026-87eb755d"
    published_at: "2026-10-29T16:00:00.000Z"
    retrieved_at: "2026-10-30T07:48:00+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
