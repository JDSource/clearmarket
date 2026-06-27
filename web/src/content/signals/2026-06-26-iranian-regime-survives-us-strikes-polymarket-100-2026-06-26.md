---
signal_id: "CMSIG2026062604"
signal_slug: "iranian-regime-survives-us-strikes-polymarket-100-2026-06-26"
headline: "Iranian regime survives US strikes: Polymarket 100%"
semantic_title: "Iranian regime survival after US strikes near full pricing"
telemetry: "Polymarket 100%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-26T23:11:35.000Z"
event_id: "CM-EVT-XYC4HDKBW3"
event_slug: "will-the-iranian-regime-survive-us-military-strikes-741"
event_question: "Will the Iranian regime survive any U.S. military strikes?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xefc69f5f48827e331957acbcc2339eb3b15e27e32453b8e6f29b5de67474c986"
  question_raw: "Will the Iranian regime survive U.S. military strikes?"
  current_price: 0.998
  volume_24h_usd: 52896.28724900001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices Iranian regime survival at 100% despite the US-Iran military exchange, reflecting no credible near-term collapse scenario."
  - "The tit-for-tat strike exchange, with Iran targeting US military positions in response, is consistent with escalation remaining below regime-threatening intensity."
  - "Companion Kalshi contract (CM-EVT-SM21RS13V3) puts only 3% on Iran becoming a democracy by end of 2026, reinforcing the regime-continuity consensus."
  - "Resolves via Polymarket's uma_oracle; regime survival means the Islamic Republic government remains in power, not absence of military strikes."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US struck Iran in response to an alleged Iranian attack on a commercial vessel; Iran's IRGC said it targeted US military positions in the region in response."
    publisher: "CGTN"
    published_at: "2026-06-26T23:11:35.000Z"
    source_url: "https://news.cgtn.com/news/2026-06-27/news-1Oj6GyJY1oY/p.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "CGTN"
        source_url: "https://news.cgtn.com/news/2026-06-27/news-1Oj6GyJY1oY/p.html"
        retrieved_at: "2026-06-27T01:35:43+00:00"
  - type: "pm_response"
    notes: "Polymarket's 100% pricing signals the prediction market treats this exchange as a contained military episode, not an existential threat to the regime."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "CGTN: US strikes Iran over alleged attack on commercial vessel; Iran says it"
    url: "https://news.cgtn.com/news/2026-06-27/news-1Oj6GyJY1oY/p.html"
    published_at: "2026-06-26T23:11:35.000Z"
    retrieved_at: "2026-06-27T01:35:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
