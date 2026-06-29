---
signal_id: "CMSIG2026062901"
signal_slug: "iranian-regime-survival-after-us-strikes-polymarket-100-2026-06-29"
headline: "Iranian regime survival after US strikes: Polymarket 100%"
semantic_title: "Iranian regime survival consensus holds at full pricing"
telemetry: "Polymarket 100%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-29T04:52:17.000Z"
event_id: "CM-EVT-XYC4HDKBW3"
event_slug: "will-the-iranian-regime-survive-us-military-strikes-741"
event_question: "Will the Iranian regime survive any U.S. military strikes?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xefc69f5f48827e331957acbcc2339eb3b15e27e32453b8e6f29b5de67474c986"
  question_raw: "Will the Iranian regime survive U.S. military strikes?"
  current_price: 0.999
  volume_24h_usd: 5710.0
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices the Iranian regime surviving US military strikes at 100%, a near-certainty read."
  - "US-Iran mutual stand-down announcement is fully consistent with this pricing; no regime collapse implied by either side."
  - "Companion Polymarket contract on US invasion of Iran before 2027 sits at just 14%, reinforcing a limited-strikes, not regime-change, scenario."
  - "Resolves via UMA oracle; key edge case is definition of 'survive' -- regime continuity, not territorial or leadership changes."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US announced a mutual stand-down with Iran after exchanges of strikes, with talks set for Doha over the Strait of Hormuz."
    publisher: "bbc.co.uk"
    published_at: "2026-06-29T04:52:17.000Z"
    source_url: "https://www.bbc.co.uk/news/articles/c872rjw17qpo"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "bbc.co.uk"
        source_url: "https://www.bbc.co.uk/news/articles/c872rjw17qpo"
        retrieved_at: "2026-06-29T12:28:56+00:00"
  - type: "pm_response"
    notes: "Polymarket at 100% on regime survival is in lockstep with the stand-down news; the 14% invasion contract frames the ceiling on escalation consensus."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "bbc.co.uk: US says it has agreed to 'stand down' after exchange of strikes with I"
    url: "https://www.bbc.co.uk/news/articles/c872rjw17qpo"
    published_at: "2026-06-29T04:52:17.000Z"
    retrieved_at: "2026-06-29T12:28:56+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
