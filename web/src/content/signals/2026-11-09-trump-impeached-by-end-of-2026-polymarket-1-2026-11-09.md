---
signal_id: "CMSIG2026110903"
signal_slug: "trump-impeached-by-end-of-2026-polymarket-1-2026-11-09"
headline: "Trump impeached by end of 2026: Polymarket 1%"
semantic_title: "Trump impeachment by end of 2026 stays a long shot"
telemetry: "Polymarket 1%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-09T06:56:00.000Z"
event_id: "CM-EVT-64KY3VMH10"
event_slug: "will-trump-be-impeached-by-december-31-2026"
event_question: "Will Trump be impeached by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4c8ceef9b9c0a27b6b4efa7c398ece4a5eeda76502f722de398c232abefe2ede"
  question_raw: "Will Trump be impeached by end of 2026?"
  current_price: 0.013
  volume_24h_usd: 2069.962935
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Trump being impeached by end of 2026 sits at 1%, an extreme long shot."
  - "Despite Democratic gains in the midterms and a Hegseth impeachment attempt, the news flow does not involve Trump impeachment proceedings directly."
  - "The 1% price is consistent with Republicans still holding enough Senate influence to block conviction; the market is not moved by the Hegseth episode."
  - "Resolves via UMA oracle; requires a full House vote to impeach Trump, not a cabinet member, before December 31, 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump stood by Defense Secretary Pete Hegseth and declared the Iran war militarily over as House Republicans faced an impeachment push against Hegseth."
    publisher: "Bridget Brown, Michael Warren, Luena Rodriguez-Feo Vileira, Jeff Mcmurray"
    published_at: "2026-11-09T06:56:00.000Z"
    source_url: "https://apnews.com/live/trump-politics-election-news-updates-11-09-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Bridget Brown, Michael Warren, Luena Rodriguez-Feo Vileira, Jeff Mcmurray"
        source_url: "https://apnews.com/live/trump-politics-election-news-updates-11-09-2026"
        retrieved_at: "2026-11-11T07:47:31+00:00"
  - type: "pm_response"
    notes: "Polymarket holds this at 1%, unchanged by the adjacent Hegseth political drama."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Bridget Brown, Michael Warren, Luena Rodriguez-Feo Vileira, Jeff Mcmurray: Trump says Iran war is militarily ‘effectively over’ and stands by Heg"
    url: "https://apnews.com/live/trump-politics-election-news-updates-11-09-2026"
    published_at: "2026-11-09T06:56:00.000Z"
    retrieved_at: "2026-11-11T07:47:31+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
