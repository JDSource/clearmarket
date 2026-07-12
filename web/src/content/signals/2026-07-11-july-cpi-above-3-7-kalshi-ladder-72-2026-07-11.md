---
signal_id: "CMSIG2026071103"
signal_slug: "july-cpi-above-3-7-kalshi-ladder-72-2026-07-11"
headline: "July CPI above 3.7%: Kalshi ladder 72%"
semantic_title: "CPI above 3.7 percent consensus anchors on tariff shock"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-11T15:32:15.000Z"
event_id: "CM-EVT-FC6YNQPJV4"
event_slug: "kxcpiyoy-26jun"
event_question: "CPI inflation rate (year ending July 2026)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPIYOY-26JUN-T3.8"
  question_raw: "Will the rate of CPI inflation be above 3.8% for the year ending in June 2026?"
  current_price: 0.24
  volume_24h_usd: 1246.45
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-10-13T14:00:00Z"
bullets:
  - "Kalshi ladder prices 72% on CPI above 3.7% for the year ending July 2026, with probability collapsing to 24% above 3.8% and 4% above 3.9%."
  - "Fed officials divided on inflation views is consistent with a distribution clustered tightly between 3.7% and 3.8%, not at a clean consensus level."
  - "The sharp drop from 72% to 24% between 3.7% and 3.8% shows the market has a narrow modal range, not broad uncertainty."
  - "Resolves via official CPI data from the Bureau of Labor Statistics for the 12-month period ending in July 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed officials are divided on US inflation views even as home prices hit all-time highs, adding to the Fed's policy dilemma."
    publisher: "MICHELLE CHAPMAN - AP Business Writer"
    published_at: "2026-07-11T15:32:15.000Z"
    source_url: "https://www.yoursourceone.com/news/national_news/america-in-focus-fed-officials-divided-on-us-inflation-views-us-home-prices-hit-all/article_c409781b-cb70-5e9b-a6e5-16c769a248fa.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "MICHELLE CHAPMAN - AP Business Writer"
        source_url: "https://www.yoursourceone.com/news/national_news/america-in-focus-fed-officials-divided-on-us-inflation-views-us-home-prices-hit-all/article_c409781b-cb70-5e9b-a6e5-16c769a248fa.html"
        retrieved_at: "2026-07-12T09:47:51+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder covers 21 strikes from 2.5% to 4.5%; probability mass is tightly clustered at the 3.7-3.8% band."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "MICHELLE CHAPMAN - AP Business Writer: America In Focus: Fed officials divided on US inflation views; US home"
    url: "https://www.yoursourceone.com/news/national_news/america-in-focus-fed-officials-divided-on-us-inflation-views-us-home-prices-hit-all/article_c409781b-cb70-5e9b-a6e5-16c769a248fa.html"
    published_at: "2026-07-11T15:32:15.000Z"
    retrieved_at: "2026-07-12T09:47:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
