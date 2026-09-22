---
signal_id: "CMSIG2026092205"
signal_slug: "xi-visits-us-before-2027-polymarket-100-2026-09-22"
headline: "Xi visits US before 2027: Polymarket 100%"
semantic_title: "Xi Jinping US visit before 2027 fully priced in at 100 percent"
telemetry: "Polymarket 100%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-09-22T04:32:52.000Z"
event_id: "CM-EVT-LKD4XHGN64"
event_slug: "will-xi-jinping-visit-us-before-2027"
event_question: "Will Xi Jinping visit the US before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd7e906eaec2c7f66697447785aa1d4fdaa82f536ca533a2bc0d3535b04e832ec"
  question_raw: "Will Xi Jinping visit US before 2027?"
  current_price: 0.998
  volume_24h_usd: 66966.72035500001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket prediction market prices Xi Jinping visiting the US before 2027 at 100%, indicating the event is treated as already confirmed."
  - "ABC News reporting on a Trump-Xi meeting is consistent with and effectively confirms the Polymarket contract at full pricing."
  - "The companion Kalshi contract on Xi visiting the United States also sits at 98%, showing cross-venue alignment with near-certain consensus."
  - "Resolves via Polymarket's uma_oracle upon documented confirmation of Xi's US presence."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump and Chinese President Xi Jinping met amid tensions over AI, trade, and the Iran war but both sides sought stability."
    publisher: "ABC News"
    published_at: "2026-09-22T04:32:52.000Z"
    source_url: "https://abcnews.com/Business/wireStory/trump-xi-tensions-flare-ai-trade-iran-seek-136640292"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ABC News"
        source_url: "https://abcnews.com/Business/wireStory/trump-xi-tensions-flare-ai-trade-iran-seek-136640292"
        retrieved_at: "2026-09-22T07:47:31+00:00"
  - type: "pm_response"
    notes: "Both Polymarket at 100% and Kalshi at 98% reflect full or near-full pricing ahead of the ABC News confirmation of the meeting."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ABC News: Trump and Xi see tensions flare over AI, trade and Iran but still seek"
    url: "https://abcnews.com/Business/wireStory/trump-xi-tensions-flare-ai-trade-iran-seek-136640292"
    published_at: "2026-09-22T04:32:52.000Z"
    retrieved_at: "2026-09-22T07:47:31+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
