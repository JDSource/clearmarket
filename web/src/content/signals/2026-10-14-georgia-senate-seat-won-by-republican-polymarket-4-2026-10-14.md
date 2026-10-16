---
signal_id: "CMSIG2026101408"
signal_slug: "georgia-senate-seat-won-by-republican-polymarket-4-2026-10-14"
headline: "Georgia Senate seat won by Republican: Polymarket 4%"
semantic_title: "Republican win in Georgia Senate race priced as a long shot"
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
  current_price: 0.04
  volume_24h_usd: 1872.35
  arbitration_model: "uma_oracle"
bullets:
  - "The Polymarket contract prices only 4% on the Republican candidate winning the Georgia Senate election."
  - "Democratic super PAC spending surge in Georgia is consistent with the market's heavy lean toward the Democratic candidate at 96% implied."
  - "A companion Polymarket contract on FL-10 (CM-EVT-T5CGMYTX62) prices 94% on the Republican candidate, showing the two races are pricing near-opposite outcomes."
  - "Resolves via Polymarket's UMA oracle on certified Georgia Senate election results; a recount or runoff scenario could delay resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump is rallying for Republican Senate candidates while top Democratic super PACs pour millions into key races including Georgia, with Election Day on November 3."
    publisher: "Cecilia Nowell"
    published_at: "2026-10-14T00:00:00.000Z"
    source_url: "https://www.theguardian.com/us-news/live/2026/oct/14/donald-trump-us-midterms-arizona-montana-politics-latest-news-updates"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Cecilia Nowell"
        source_url: "https://www.theguardian.com/us-news/live/2026/oct/14/donald-trump-us-midterms-arizona-montana-politics-latest-news-updates"
        retrieved_at: "2026-10-16T07:47:56+00:00"
  - type: "pm_response"
    notes: "Polymarket at 4% makes a Republican Georgia Senate win one of the longest-shot outcomes in the midterm slate covered by prediction markets."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Cecilia Nowell: Trump tries to rally support for Republican candidates as top Super Pa"
    url: "https://www.theguardian.com/us-news/live/2026/oct/14/donald-trump-us-midterms-arizona-montana-politics-latest-news-updates"
    published_at: "2026-10-14T00:00:00.000Z"
    retrieved_at: "2026-10-16T07:47:56+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
