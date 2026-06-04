---
signal_id: "CMSIG2026060208"
signal_slug: "us-iran-nuclear-deal-by-june-30-polymarket-28-2026-06-02"
headline: "US-Iran nuclear deal by June 30: Polymarket 28%"
semantic_title: "US-Iran nuclear deal by June 30 priced a long shot"
telemetry: "Polymarket 28%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-02T00:00:00.000Z"
event_id: "CM-EVT-LG47Z78CF2"
event_slug: "us-iran-nuclear-deal-by-june-30"
event_question: "Will the US and Iran reach a nuclear deal by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa70fc3695a65833b91b45df6db6015096f3e1471b70352ca411b4209010e7633"
  question_raw: "US-Iran nuclear deal by June 30?"
  current_price: 0.28
  volume_24h_usd: 207316.77510300005
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices 28% on a US-Iran nuclear deal by June 30."
  - "Public demand for a deal is high per polling, but the prediction market remains well below 50%, signaling skepticism about a June deadline."
  - "A companion Polymarket contract prices only 21% on Iran agreeing to end uranium enrichment by June 30, consistent with the low deal odds."
  - "Resolves via uma_oracle; the contract requires a confirmed deal by June 30, not merely ongoing talks."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "An Economist/YouGov poll found 68% of Americans want a deal to end the Iran war quickly, while Trump's approval on inflation hit new lows."
    publisher: "David Montgomery   Senior data journalist"
    published_at: "2026-06-02T00:00:00.000Z"
    source_url: "https://yougov.com/en-us/articles/54886-donald-trump-approval-new-lows-inflation-iran-ai-e-jean-carroll-may-29-june-1-2026-economist-yougov-poll"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "David Montgomery   Senior data journalist"
        source_url: "https://yougov.com/en-us/articles/54886-donald-trump-approval-new-lows-inflation-iran-ai-e-jean-carroll-may-29-june-1-2026-economist-yougov-poll"
        retrieved_at: "2026-06-04T11:14:54+00:00"
  - type: "pm_response"
    notes: "Polymarket resolves via uma_oracle; the 7-point gap between deal odds (28%) and enrichment-halt odds (21%) implies the market sees partial deals as also unlikely."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "David Montgomery   Senior data journalist: Trump approval hits new lows on inflation and Iran, AI, E. Jean Carrol"
    url: "https://yougov.com/en-us/articles/54886-donald-trump-approval-new-lows-inflation-iran-ai-e-jean-carroll-may-29-june-1-2026-economist-yougov-poll"
    published_at: "2026-06-02T00:00:00.000Z"
    retrieved_at: "2026-06-04T11:14:54+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
