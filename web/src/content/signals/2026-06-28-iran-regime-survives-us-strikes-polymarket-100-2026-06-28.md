---
signal_id: "CMSIG2026062802"
signal_slug: "iran-regime-survives-us-strikes-polymarket-100-2026-06-28"
headline: "Iran regime survives US strikes: Polymarket 100%"
semantic_title: "Iranian regime survival after US strikes commands full pricing"
telemetry: "Polymarket 100%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-28T21:58:00.000Z"
event_id: "CM-EVT-XYC4HDKBW3"
event_slug: "will-the-iranian-regime-survive-us-military-strikes-741"
event_question: "Will the Iranian regime survive any U.S. military strikes?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xefc69f5f48827e331957acbcc2339eb3b15e27e32453b8e6f29b5de67474c986"
  question_raw: "Will the Iranian regime survive U.S. military strikes?"
  current_price: 0.999
  volume_24h_usd: 42846.664555
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices the Iranian regime surviving US military strikes at 100%, resolving via uma_oracle."
  - "Mutual strike-and-halt sequence, with both sides accusing ceasefire violations, is fully consistent with the market's certainty of regime survival."
  - "A companion Polymarket contract prices Iran ending uranium enrichment by June 30 at just 1%, and by December 31 at 28%, signaling regime continuity without disarmament."
  - "Polymarket's 'US invades Iran before 2027' contract sits at 14%, suggesting markets treat the current conflict as contained below full-invasion threshold."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US and Iran agreed to halt attacks after counter-strikes, with Qatar set to host Hormuz talks, but the Iranian regime remained intact throughout the exchange."
    publisher: "TOI World Desk  / TIMESOFINDIA.COM /   Jun 29, 2026, 03:28 IST"
    published_at: "2026-06-28T21:58:00.000Z"
    source_url: "https://timesofindia.indiatimes.com/world/us/us-iran-agree-to-halt-attacks-after-counter-strikes-qatar-to-host-hormuz-talks-on-tuesday/articleshow/132058740.cms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "TOI World Desk  / TIMESOFINDIA.COM /   Jun 29, 2026, 03:28 IST"
        source_url: "https://timesofindia.indiatimes.com/world/us/us-iran-agree-to-halt-attacks-after-counter-strikes-qatar-to-host-hormuz-talks-on-tuesday/articleshow/132058740.cms"
        retrieved_at: "2026-06-29T01:46:24+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via uma_oracle; 100% pricing reflects no credible path to regime collapse within the current conflict arc."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "TOI World Desk  / TIMESOFINDIA.COM /   Jun 29, 2026, 03:28 IST: US, Iran agree to halt attacks after counter-strikes; Qatar to host Ho"
    url: "https://timesofindia.indiatimes.com/world/us/us-iran-agree-to-halt-attacks-after-counter-strikes-qatar-to-host-hormuz-talks-on-tuesday/articleshow/132058740.cms"
    published_at: "2026-06-28T21:58:00.000Z"
    retrieved_at: "2026-06-29T01:46:24+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
