---
signal_id: "CMSIG2026061106"
signal_slug: "iranian-regime-survives-us-strikes-polymarket-97-2026-06-11"
headline: "Iranian regime survives US strikes: Polymarket 97%"
semantic_title: "Iranian regime survival through US strikes nears full pricing"
telemetry: "Polymarket 97%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-11T01:53:43.000Z"
event_id: "CM-EVT-XYC4HDKBW3"
event_slug: "will-the-iranian-regime-survive-us-military-strikes-741"
event_question: "Will the Iranian regime survive any U.S. military strikes?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xefc69f5f48827e331957acbcc2339eb3b15e27e32453b8e6f29b5de67474c986"
  question_raw: "Will the Iranian regime survive U.S. military strikes?"
  current_price: 0.971
  volume_24h_usd: 10685.813842000001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices 97% on the Iranian regime surviving any US military strikes."
  - "Second-day US strikes and Iranian IRGC ballistic missile retaliation are consistent with the market's near-certain pricing of regime survival, the exchange of fire implies neither side is pursuing regime-change outcomes."
  - "A companion Polymarket contract prices 14% on the Iranian regime falling by December 31, 2026, revealing the market treats military strikes and regime collapse as largely decoupled events."
  - "Resolves via uma_oracle assessment of regime continuity; the key settlement question is what constitutes 'regime survival' if Iran undergoes leadership transition under duress."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US military struck multiple targets in Iran for a second consecutive night, with Iran retaliating by firing 12 ballistic missiles at a US airbase in Jordan."
    publisher: "AP"
    published_at: "2026-06-11T01:53:43.000Z"
    source_url: "https://www.thehindu.com/news/international/us-military-strikes-multiple-targets-in-iran-in-second-day-of-renewed-fire/article71087454.ece"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "AP"
        source_url: "https://www.thehindu.com/news/international/us-military-strikes-multiple-targets-in-iran-in-second-day-of-renewed-fire/article71087454.ece"
        retrieved_at: "2026-06-11T12:08:11+00:00"
  - type: "pm_response"
    notes: "Polymarket's 97% on Iranian regime survival through US strikes is consistent across multiple Iran-conflict stories, with the 14% year-end regime-collapse contract confirming the market treats current strikes as contained rather than existential."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "AP: U.S. military strikes ‘multiple targets’ in Iran in second day of rene"
    url: "https://www.thehindu.com/news/international/us-military-strikes-multiple-targets-in-iran-in-second-day-of-renewed-fire/article71087454.ece"
    published_at: "2026-06-11T01:53:43.000Z"
    retrieved_at: "2026-06-11T12:08:11+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
