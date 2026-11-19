---
signal_id: "CMSIG2026111905"
signal_slug: "putin-out-as-russia-president-by-2026-polymarket-2-2026-11-19"
headline: "Putin out as Russia president by 2026: Polymarket 2%"
semantic_title: "Putin leaving Russian presidency by year-end stays near zero"
telemetry: "Polymarket 2%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-19T00:15:49.000Z"
event_id: "CM-EVT-5WJSMVBVS7"
event_slug: "putin-out-before-2027"
event_question: "Will Vladimir Putin no longer be President of Russia by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x6bd56627aa21311850825edb27e53434a0e17a4f782be0086bc07f71eee00d0d"
  question_raw: "Putin out as President of Russia by December 31, 2026?"
  current_price: 0.015
  volume_24h_usd: 21020.388827
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T18:30:00Z"
bullets:
  - "The Polymarket contract on Putin no longer being Russian president by end of 2026 sits at 2%, near-zero odds."
  - "Putin's prominent role at the APEC trilateral is consistent with the market's near-zero pricing of a leadership change this year."
  - "The contract on a military clash between China and Japan before 2027 (CM-EVT-7XB54LHXX3) prices at 3%, a separate but related tail-risk read from the same summit context."
  - "Resolves via UMA oracle at end of 2026; contract requires Putin to formally leave the presidency, not merely be absent from an event."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Putin appeared alongside Trump and Xi at the APEC summit in Shenzhen in what was billed as a historic first trilateral, projecting full authority on the world stage."
    publisher: "bbc.com"
    published_at: "2026-11-19T00:15:49.000Z"
    source_url: "https://www.bbc.com/news/live/cmlye926e2eet"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "bbc.com"
        source_url: "https://www.bbc.com/news/live/cmlye926e2eet"
        retrieved_at: "2026-11-19T07:47:42+00:00"
  - type: "pm_response"
    notes: "Polymarket holds Putin's exit at 2% through year-end; the APEC appearance reinforces the market's strong-favorite stance on his continuity."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "bbc.com: Trump, Xi and Putin set to hold historic meeting on Apec sidelines - B"
    url: "https://www.bbc.com/news/live/cmlye926e2eet"
    published_at: "2026-11-19T00:15:49.000Z"
    retrieved_at: "2026-11-19T07:47:42+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
