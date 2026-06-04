---
signal_id: "CMSIG2026060301"
signal_slug: "us-iran-nuclear-deal-before-2027-polymarket-63-2026-06-03"
headline: "US-Iran nuclear deal before 2027: Polymarket 63%"
semantic_title: "US-Iran nuclear deal before 2027 leans likely in pricing"
telemetry: "Polymarket 63%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-03T08:13:16.000Z"
event_id: "CM-EVT-VP51KKLQH2"
event_slug: "us-iran-nuclear-deal-before-2027"
event_question: "Will the US and Iran reach a nuclear deal before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x182390641d3b1b47cc64274b9da290efd04221c586651ba190880713da6347d9"
  question_raw: "US-Iran nuclear deal before 2027?"
  current_price: 0.63
  volume_24h_usd: 28317.249848
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket contract puts 63% on a US-Iran nuclear deal before 2027, despite stalled talks."
  - "House vote to curb Trump on Iran is symbolic; markets still assign majority odds to an eventual deal."
  - "Companion Polymarket contract on a US-Iran nuclear deal by June 30 sits at 20%, implying most deal probability is weighted to H2 2026."
  - "Resolves via uma_oracle based on a publicly announced US-Iran nuclear agreement before Jan 1, 2027."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US House passed a war-powers resolution to halt military action in Iran as peace talks stalled and ceasefire frayed."
    publisher: "france24.com"
    published_at: "2026-06-03T08:13:16.000Z"
    source_url: "https://www.france24.com/en/live-news/20260603-drone-strikes-close-kuwait-airport-as-iran-and-us-clash-in-gulf"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "france24.com"
        source_url: "https://www.france24.com/en/live-news/20260603-drone-strikes-close-kuwait-airport-as-iran-and-us-clash-in-gulf"
        retrieved_at: "2026-06-04T03:24:20+00:00"
  - type: "pm_response"
    notes: "Polymarket prices 63% on a pre-2027 deal even as the House rebukes Trump and ceasefire talks stall."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "france24.com: US House votes to curb Trump on Iran war as talks stall"
    url: "https://www.france24.com/en/live-news/20260603-drone-strikes-close-kuwait-airport-as-iran-and-us-clash-in-gulf"
    published_at: "2026-06-03T08:13:16.000Z"
    retrieved_at: "2026-06-04T03:24:20+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
