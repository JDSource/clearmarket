---
signal_id: "CMSIG2026111803"
signal_slug: "trump-endorses-vance-for-2028-by-year-end-polymarket-5-2026-11-18"
headline: "Trump endorses Vance for 2028 by year-end: Polymarket 5%"
semantic_title: "Trump endorsing Vance for 2028 stays a long shot on Polymarket"
telemetry: "Polymarket 5%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-18T16:54:29.000Z"
event_id: "CM-EVT-VYGG3P41R5"
event_slug: "will-trump-endorse-jd-vance-for-president-before-2027"
event_question: "Will Trump endorse JD Vance for president before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9c414cb64000dc7645b2bba8d7586746f3ddb1cfd1b564769188b81cd63ad667"
  question_raw: "Will Trump endorse JD Vance for president before 2027?"
  current_price: 0.048
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts only 5% on Trump endorsing JD Vance for president before 2027, keeping it a heavy long shot."
  - "Reported Trump frustration with Vance over Iran war commentary is consistent with the market's low-odds stance on a near-term endorsement."
  - "A companion Polymarket contract (CM-EVT-Q16SDF41Z3) prices only 3% on Vance announcing he will not run in 2028 this year, leaving the 2028 race structurally open."
  - "Resolves via UMA oracle; contract likely requires a verifiable public Trump endorsement of Vance as a 2028 presidential candidate before January 1, 2027."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump has grown frustrated with Vice President JD Vance over Vance's public criticism of the Iran war, complicating Vance's 2028 ambitions."
    publisher: "Tyler Pager"
    published_at: "2026-11-18T16:54:29.000Z"
    source_url: "https://www.nytimes.com/2026/11/18/us/politics/vance-trump-iran-2028-election-rubio.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Tyler Pager"
        source_url: "https://www.nytimes.com/2026/11/18/us/politics/vance-trump-iran-2028-election-rubio.html"
        retrieved_at: "2026-11-20T07:47:31+00:00"
  - type: "pm_response"
    notes: "Polymarket prices 5%; the market is not moving on the tension report, treating endorsement before year-end as a remote scenario."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Tyler Pager: Trump Grows Frustrated With Vance Over Iran War Critique"
    url: "https://www.nytimes.com/2026/11/18/us/politics/vance-trump-iran-2028-election-rubio.html"
    published_at: "2026-11-18T16:54:29.000Z"
    retrieved_at: "2026-11-20T07:47:31+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
