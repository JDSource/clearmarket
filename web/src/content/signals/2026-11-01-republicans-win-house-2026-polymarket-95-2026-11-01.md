---
signal_id: "CMSIG2026110105"
signal_slug: "republicans-win-house-2026-polymarket-95-2026-11-01"
headline: "Republicans win House 2026: Polymarket 95%"
semantic_title: "Republicans heavily favored to hold the House in 2026"
telemetry: "Polymarket 95%"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-11-01T00:00:00.000Z"
event_id: "CM-EVT-2N6T7M0T15"
event_slug: "which-party-will-win-the-house-in-2026"
event_question: "Will the Republican Party win control of the House of Representatives in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd5d9fc47718bd553592d126b1fa5e87183d27f3936975b0c04cc0f2dec1f1bb4"
  question_raw: "Will the Democratic Party control the House after the 2026 Midterm elections?"
  current_price: 0.95
  volume_24h_usd: 1661663.6458480004
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "The Polymarket contract on Republicans winning House control in 2026 sits at 95%, making Democratic hopes of a House flip a long shot."
  - "Widespread media coverage of Democratic optimism is at odds with prediction-market pricing, which strongly favors a Republican House hold."
  - "The companion Kalshi contract (CM-EVT-T5VXKJT451) at 71% for Republicans controlling at least one chamber is a weaker read, consistent with Senate uncertainty dampening the overall-chamber probability."
  - "The Polymarket Senate control contract (CM-EVT-M9WJY06T90) at 73% for one party reveals the House-Senate spread: the House is seen as far more settled than the Senate race outcome."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "With midterm elections on Tuesday, Democrats hope to take control of Congress and derail President Donald Trump's second-term agenda."
    publisher: "Alexei Koseff"
    published_at: "2026-11-01T00:00:00.000Z"
    source_url: "https://www.washingtonpost.com/politics/2026/11/01/whats-stake-tuesdays-midterm-elections/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Alexei Koseff"
        source_url: "https://www.washingtonpost.com/politics/2026/11/01/whats-stake-tuesdays-midterm-elections/"
        retrieved_at: "2026-11-02T07:48:26+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via uma_oracle; the 95% House probability reflects a strong market consensus that runs counter to Democratic campaign optimism in media coverage."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Alexei Koseff: What’s at stake in Tuesday’s midterm elections? - The Washington Post"
    url: "https://www.washingtonpost.com/politics/2026/11/01/whats-stake-tuesdays-midterm-elections/"
    published_at: "2026-11-01T00:00:00.000Z"
    retrieved_at: "2026-11-02T07:48:26+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
