---
signal_id: "CMSIG2026081907"
signal_slug: "gop-wins-fl-10-house-seat-in-2026-polymarket-94-2026-08-19"
headline: "GOP wins FL-10 House seat in 2026: Polymarket 94%"
semantic_title: "Republican wins Florida House district FL-10 stays heavily favored"
telemetry: "Polymarket 94%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-08-19T01:30:25.994Z"
event_id: "CM-EVT-T5CGMYTX62"
event_slug: "fl-10-house-election-winner"
event_question: "Will the Republican candidate win the FL-10 House seat in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x92af18b5a8e041263bdf14ba26de45aec9677fa539fb95cdb637168596703b01"
  question_raw: "Will the Democratic Party win the FL-10 House seat?"
  current_price: 0.94
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices 94% on the Republican candidate winning the FL-10 House seat in 2026, resolving via UMA oracle."
  - "Donalds vacating FL-10 for the governor's race opens the seat, yet the market treats it as a near-certain Republican hold, the seat's partisan lean is not seen as threatened."
  - "A companion contract (CM-EVT-2NN6LKDWW9) at 99% on the Democratic nominee for Florida's 27th congressional district being determined confirms Florida primary resolution is nearly complete on the Democratic side."
  - "Resolves via UMA oracle on the general election result; outcome depends on who the GOP nominates to replace Donalds in FL-10."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Byron Donalds won the Republican nomination for Florida governor, setting up the general election matchup against David Jolly for Democrats."
    publisher: "BBC"
    published_at: "2026-08-19T01:30:25.994Z"
    source_url: "https://www.bbc.com/news/articles/cpvwgym9xl9o"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "BBC"
        source_url: "https://www.bbc.com/news/articles/cpvwgym9xl9o"
        retrieved_at: "2026-08-19T08:31:28+00:00"
  - type: "pm_response"
    notes: "Polymarket at 94% treats FL-10 as a safe Republican seat despite the open-seat dynamics created by Donalds' governor run."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "BBC: Byron Donalds and David Jolly projected to win Florida primary to repl"
    url: "https://www.bbc.com/news/articles/cpvwgym9xl9o"
    published_at: "2026-08-19T01:30:25.994Z"
    retrieved_at: "2026-08-19T08:31:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
