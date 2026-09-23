---
signal_id: "CMSIG2026092305"
signal_slug: "xi-visits-us-before-2027-polymarket-100-2026-09-23"
headline: "Xi visits US before 2027: Polymarket 100%"
semantic_title: "Xi US visit nears full pricing on Polymarket"
telemetry: "Polymarket 100%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-09-23T00:00:00.000Z"
event_id: "CM-EVT-LKD4XHGN64"
event_slug: "will-xi-jinping-visit-us-before-2027"
event_question: "Will Xi Jinping visit the US before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd7e906eaec2c7f66697447785aa1d4fdaa82f536ca533a2bc0d3535b04e832ec"
  question_raw: "Will Xi Jinping visit US before 2027?"
  current_price: 0.998
  volume_24h_usd: 83819.882309
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Xi Jinping visiting the US before 2027 prices at 100%, effectively fully resolved."
  - "The Xi visit is confirmed and underway, so the contract price reflects a completed event rather than forward-looking uncertainty."
  - "The Kalshi contract on Xi visiting the United States also sits at 99%, consistent with the event being treated as a done fact across venues."
  - "Resolves via uma_oracle on Polymarket; with the visit actively occurring, resolution is a formality."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US President Donald Trump is hosting Chinese leader Xi Jinping in Washington this week to discuss AI, trade, and Taiwan."
    publisher: "bbc.com"
    published_at: "2026-09-23T00:00:00.000Z"
    source_url: "https://www.bbc.com/news/articles/c6n9w410v3vzo"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "bbc.com"
        source_url: "https://www.bbc.com/news/articles/c6n9w410v3vzo"
        retrieved_at: "2026-09-23T07:47:29+00:00"
  - type: "pm_response"
    notes: "Both Polymarket at 100% and Kalshi at 99% treat the Xi US visit as a resolved event, with the news confirming what markets had already fully priced."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "bbc.com: White House to roll out the red carpet for historic Xi Jinping visit"
    url: "https://www.bbc.com/news/articles/c6n9w410v3vzo"
    published_at: "2026-09-23T00:00:00.000Z"
    retrieved_at: "2026-09-23T07:47:29+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
