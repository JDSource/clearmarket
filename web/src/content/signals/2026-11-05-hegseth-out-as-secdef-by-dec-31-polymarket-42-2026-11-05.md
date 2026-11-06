---
signal_id: "CMSIG2026110505"
signal_slug: "hegseth-out-as-secdef-by-dec-31-polymarket-42-2026-11-05"
headline: "Hegseth out as SecDef by Dec 31: Polymarket 42%"
semantic_title: "Hegseth out as Defense Secretary by year-end sits near 50%"
telemetry: "Polymarket 42%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-05T17:41:59.000Z"
event_id: "CM-EVT-JWSH7Q94S8"
event_slug: "pete-hegseth-out-as-secretary-of-defense-by-december-31"
event_question: "Will Pete Hegseth be out as Secretary of Defense by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0fcfcfc35d71424c0693c717d2e3bc9b8992910835d124d80cd2f01498f1d3dc"
  question_raw: "Pete Hegseth out as Secretary of Defense by December 31?"
  current_price: 0.42
  volume_24h_usd: 239984.39259699997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts 42% on Pete Hegseth departing as Secretary of Defense by December 31, 2026."
  - "Trump's public backing of Hegseth is not moving the needle to low odds; the market holds near 50%, signaling continued doubt about Hegseth's tenure through year-end."
  - "The Republican midterm drubbing and incoming Democratic Congress raise the political pressure environment that the contract is pricing."
  - "Resolves via UMA oracle; the near-50% pricing means the market is treating this as a genuine coin-flip through the end of the year."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump backed Defense Secretary Pete Hegseth publicly amid Republican midterm losses and reports of post-election political instability."
    publisher: "C By Claire Campbell"
    published_at: "2026-11-05T17:41:59.000Z"
    source_url: "https://www.abc.net.au/news/2026-11-06/us-midterm-elections-2026-live-updates/107351586"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "C By Claire Campbell"
        source_url: "https://www.abc.net.au/news/2026-11-06/us-midterm-elections-2026-live-updates/107351586"
        retrieved_at: "2026-11-06T15:37:02+00:00"
  - type: "pm_response"
    notes: "Polymarket at 42%; Trump's public endorsement of Hegseth has not pushed odds to clearly low territory, reflecting persistent departure risk."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "C By Claire Campbell: US midterm elections 2026 live updates: Trump backs Hegseth, moves to"
    url: "https://www.abc.net.au/news/2026-11-06/us-midterm-elections-2026-live-updates/107351586"
    published_at: "2026-11-05T17:41:59.000Z"
    retrieved_at: "2026-11-06T15:37:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
