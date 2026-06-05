---
signal_id: "CMSIG2026060307"
signal_slug: "iranian-regime-survives-us-strikes-polymarket-97-2026-06-03"
headline: "Iranian regime survives US strikes: Polymarket 97%"
semantic_title: "Iranian regime survival after US strikes nears full pricing"
telemetry: "Polymarket 97%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-03T11:42:59.000Z"
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
  - "Polymarket prices 97% odds the Iranian regime survives any US military strikes, resolving via UMA oracle."
  - "US strikes on Qeshm Island and Iranian missile attacks on Kuwait and Bahrain represent continued escalation, yet the survival probability barely moves from near-certainty."
  - "A companion Polymarket contract (CM-EVT-QNQ4VPVP80) puts only 14% on the Iranian regime falling by December 31, 2026, consistent with the near-certain survival read."
  - "Strait of Hormuz traffic normalization by year-end sits at 76% on Polymarket (CM-EVT-LCPV825X09), suggesting markets expect the conflict to persist but not escalate to regime collapse."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran fired missiles at Kuwait and Bahrain while the US launched strikes on Iran's Qeshm Island, escalating Gulf hostilities with diplomacy showing little progress."
    publisher: "Al Jazeera Staff"
    published_at: "2026-06-03T11:42:59.000Z"
    source_url: "https://www.aljazeera.com/news/2026/6/3/iran-kuwait-bahrain-hit-is-the-war-in-the-gulf-escalating-again"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Al Jazeera Staff"
        source_url: "https://www.aljazeera.com/news/2026/6/3/iran-kuwait-bahrain-hit-is-the-war-in-the-gulf-escalating-again"
        retrieved_at: "2026-06-05T11:24:05+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; 'survive' likely requires the Islamic Republic to remain the governing authority, not merely that leadership individuals persist."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Al Jazeera Staff: Iran, Kuwait, Bahrain hit: Is the war in the Gulf escalating again? |"
    url: "https://www.aljazeera.com/news/2026/6/3/iran-kuwait-bahrain-hit-is-the-war-in-the-gulf-escalating-again"
    published_at: "2026-06-03T11:42:59.000Z"
    retrieved_at: "2026-06-05T11:24:05+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
