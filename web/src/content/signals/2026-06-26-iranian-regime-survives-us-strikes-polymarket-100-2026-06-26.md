---
signal_id: "CMSIG2026062601"
signal_slug: "iranian-regime-survives-us-strikes-polymarket-100-2026-06-26"
headline: "Iranian regime survives US strikes: Polymarket 100%"
semantic_title: "Iranian regime survival after US strikes anchors at certainty"
telemetry: "Polymarket 100%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-26T20:54:00.000Z"
event_id: "CM-EVT-XYC4HDKBW3"
event_slug: "will-the-iranian-regime-survive-us-military-strikes-741"
event_question: "Will the Iranian regime survive any U.S. military strikes?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xefc69f5f48827e331957acbcc2339eb3b15e27e32453b8e6f29b5de67474c986"
  question_raw: "Will the Iranian regime survive U.S. military strikes?"
  current_price: 0.999
  volume_24h_usd: 42252.994555000005
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices Iranian regime survival at 100%, treating regime collapse from US strikes as fully off the table."
  - "US strikes followed Iran's drone attack on a cargo ship; the market reads the exchange as below the threshold for existential threat to Tehran."
  - "Separately, the Polymarket contract on a US invasion of Iran before 2027 sits at only 15%, consistent with a tit-for-tat read rather than full escalation."
  - "Resolves via Polymarket UMA oracle; contract tests whether the Islamic Republic government structure survives any US military engagement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US military struck Iranian targets after Iran's drone attack on a commercial vessel in the Strait of Hormuz, challenging a fragile ceasefire."
    publisher: "cbsnews.com"
    published_at: "2026-06-26T20:54:00.000Z"
    source_url: "https://www.cbsnews.com/news/us-strikes-iran-drone-attack-cargo-ship-challenge-ceasefire-trump/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cbsnews.com"
        source_url: "https://www.cbsnews.com/news/us-strikes-iran-drone-attack-cargo-ship-challenge-ceasefire-trump/"
        retrieved_at: "2026-06-28T10:24:59+00:00"
  - type: "pm_response"
    notes: "Polymarket at 100% reflects consensus that US strikes remain punitive and limited, not regime-threatening."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cbsnews.com: U.S. strikes targets in Iran after Iranian drone attack on cargo ship,"
    url: "https://www.cbsnews.com/news/us-strikes-iran-drone-attack-cargo-ship-challenge-ceasefire-trump/"
    published_at: "2026-06-26T20:54:00.000Z"
    retrieved_at: "2026-06-28T10:24:59+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
