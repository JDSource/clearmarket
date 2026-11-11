---
signal_id: "CMSIG2026110904"
signal_slug: "hegseth-out-by-dec-31-polymarket-13-2026-11-09"
headline: "Hegseth out by Dec 31: Polymarket 13%"
semantic_title: "Hegseth out as Defense Secretary by year-end holds near long-shot odds"
telemetry: "Polymarket 13%"
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
  current_price: 0.13
  volume_24h_usd: 374561.670466
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Pete Hegseth leaving as Secretary of Defense by December 31 sits at 13%."
  - "House Republicans successfully tabled the impeachment articles; the failed vote is consistent with the 13% price staying elevated but below 50%."
  - "The market is not pricing removal as likely, but the double-digit probability reflects residual risk from ongoing political pressure."
  - "Resolves via UMA oracle; departure could occur via resignation, firing, Senate removal, or any other mechanism before December 31, 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "House Republicans blocked a Democratic effort to impeach Defense Secretary Pete Hegseth, with the Pentagon declaring a total victory."
    publisher: "0 NBC News NBC News"
    published_at: "2026-11-09T12:20:19.000Z"
    source_url: "https://www.nbcnews.com/politics/trump-administration/live-blog/trump-2026-midterm-elections-senate-house-supreme-court-live-updates-rcna608235"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "0 NBC News NBC News"
        source_url: "https://www.nbcnews.com/politics/trump-administration/live-blog/trump-2026-midterm-elections-senate-house-supreme-court-live-updates-rcna608235"
        retrieved_at: "2026-11-11T07:47:31+00:00"
  - type: "pm_response"
    notes: "Polymarket prices Hegseth's departure at 13%, a persistent non-trivial tail despite the blocked House vote."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "0 NBC News NBC News: Trump administration live updates: Congress returns with government fu"
    url: "https://www.nbcnews.com/politics/trump-administration/live-blog/trump-2026-midterm-elections-senate-house-supreme-court-live-updates-rcna608235"
    published_at: "2026-11-09T12:20:19.000Z"
    retrieved_at: "2026-11-11T07:47:31+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
