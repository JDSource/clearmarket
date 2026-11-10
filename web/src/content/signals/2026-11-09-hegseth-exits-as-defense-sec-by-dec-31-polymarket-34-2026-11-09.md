---
signal_id: "CMSIG2026110905"
signal_slug: "hegseth-exits-as-defense-sec-by-dec-31-polymarket-34-2026-11-09"
headline: "Hegseth exits as Defense Sec by Dec 31: Polymarket 34%"
semantic_title: "Hegseth out by year-end holds near 34%"
telemetry: "Polymarket 34%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-09T12:20:19.000Z"
event_id: "CM-EVT-JWSH7Q94S8"
event_slug: "pete-hegseth-out-as-secretary-of-defense-by-december-31"
event_question: "Will Pete Hegseth be out as Secretary of Defense by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0fcfcfc35d71424c0693c717d2e3bc9b8992910835d124d80cd2f01498f1d3dc"
  question_raw: "Pete Hegseth out as Secretary of Defense by December 31?"
  current_price: 0.34
  volume_24h_usd: 197226.859687
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts 34% odds on Pete Hegseth leaving as Secretary of Defense before December 31, resolving via UMA oracle."
  - "Impeachment articles have been filed and a House vote is imminent, yet the market holds well below 50%, suggesting limited confidence the effort succeeds."
  - "Democrats now hold significant House majorities per news reporting, which should give them procedural leverage; the 34% price may understate near-term event risk."
  - "Resolution via UMA oracle requires confirmation of departure by December 31, 2026; a House impeachment vote alone does not resolve the contract."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "House Republicans filed articles of impeachment against Defense Secretary Pete Hegseth, with a floor vote expected as early as this week."
    publisher: "0 NBC News NBC News"
    published_at: "2026-11-09T12:20:19.000Z"
    source_url: "https://www.nbcnews.com/politics/trump-administration/live-blog/trump-2026-midterm-elections-senate-house-supreme-court-live-updates-rcna608235"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "0 NBC News NBC News"
        source_url: "https://www.nbcnews.com/politics/trump-administration/live-blog/trump-2026-midterm-elections-senate-house-supreme-court-live-updates-rcna608235"
        retrieved_at: "2026-11-10T07:47:48+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; 34% reflects the market pricing meaningful but sub-even odds despite active impeachment proceedings."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "0 NBC News NBC News: Trump administration live updates: Congress returns with government fu"
    url: "https://www.nbcnews.com/politics/trump-administration/live-blog/trump-2026-midterm-elections-senate-house-supreme-court-live-updates-rcna608235"
    published_at: "2026-11-09T12:20:19.000Z"
    retrieved_at: "2026-11-10T07:47:48+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
