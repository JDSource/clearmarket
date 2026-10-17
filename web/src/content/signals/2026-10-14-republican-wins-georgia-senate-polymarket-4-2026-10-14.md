---
signal_id: "CMSIG2026101405"
signal_slug: "republican-wins-georgia-senate-polymarket-4-2026-10-14"
headline: "Republican wins Georgia Senate: Polymarket 4%"
semantic_title: "Republican candidate winning Georgia Senate stays a long shot"
telemetry: "Polymarket 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-14T00:00:00.000Z"
event_id: "CM-EVT-301LWVGPR3"
event_slug: "georgia-senate-election-winner"
event_question: "Will the Georgia Senate election be won by the Republican candidate?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x54e4e816cc5868e2f933c6bbc597e3313bdad382be3ecf7eaa4d8fa5c3f1a1bd"
  question_raw: "Will the Republicans win the Georgia Senate race in 2026?"
  current_price: 0.043
  volume_24h_usd: 5858.87
  arbitration_model: "uma_oracle"
bullets:
  - "The Polymarket contract on a Republican winning the Georgia Senate seat sits at 4%, resolving via UMA oracle."
  - "Despite Trump's active campaigning in Georgia, the market assigns near-zero probability to a Republican Senate win in the state."
  - "The Kalshi contract (CM-EVT-1V0WDTXHT9) puts the same-party sweep of Georgia's Governor and Senate elections at 46%, suggesting split-ticket outcomes are the market base case."
  - "A companion Kalshi contract (CM-EVT-4DFCBXLZN6) puts Republicans holding more governorships than Democrats after midterms at 69%, showing state-level strength does not translate to the Georgia Senate race."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump rallied Republican candidates and Democratic Super PACs poured millions into key Senate races including Georgia."
    publisher: "Cecilia Nowell"
    published_at: "2026-10-14T00:00:00.000Z"
    source_url: "https://www.theguardian.com/us-news/live/2026/oct/14/donald-trump-us-midterms-arizona-montana-politics-latest-news-updates"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Cecilia Nowell"
        source_url: "https://www.theguardian.com/us-news/live/2026/oct/14/donald-trump-us-midterms-arizona-montana-politics-latest-news-updates"
        retrieved_at: "2026-10-17T07:47:54+00:00"
  - type: "pm_response"
    notes: "Polymarket at 4% on a Republican Georgia Senate win is near the floor of plausible probability, the market is not moving on Trump's rally presence."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Cecilia Nowell: Trump tries to rally support for Republican candidates as top Super Pa"
    url: "https://www.theguardian.com/us-news/live/2026/oct/14/donald-trump-us-midterms-arizona-montana-politics-latest-news-updates"
    published_at: "2026-10-14T00:00:00.000Z"
    retrieved_at: "2026-10-17T07:47:54+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
