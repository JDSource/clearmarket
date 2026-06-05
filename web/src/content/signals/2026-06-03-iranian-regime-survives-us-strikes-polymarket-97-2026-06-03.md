---
signal_id: "CMSIG2026060305"
signal_slug: "iranian-regime-survives-us-strikes-polymarket-97-2026-06-03"
headline: "Iranian regime survives US strikes: Polymarket 97%"
semantic_title: "Iranian regime survival after US strikes commands near-certain pricing"
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
  - "Polymarket prices a 97% chance the Iranian regime survives any U.S. military strikes."
  - "Despite confirmed U.S. strikes on Qeshm Island and Iranian missile attacks on Gulf neighbors, the market treats regime survival as near-certain."
  - "A companion Polymarket contract on a U.S. invasion of Iran before 2027 sits at just 17%, consistent with the regime survival pricing."
  - "Resolves via Polymarket's UMA oracle; criteria for regime 'fall' would need to be met, not merely territorial strikes or leadership changes."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran fired missiles at Kuwait and Bahrain while the U.S. launched strikes on Iran's Qeshm Island, escalating Gulf hostilities."
    publisher: "Al Jazeera Staff"
    published_at: "2026-06-03T11:42:59.000Z"
    source_url: "https://www.aljazeera.com/news/2026/6/3/iran-kuwait-bahrain-hit-is-the-war-in-the-gulf-escalating-again"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Al Jazeera Staff"
        source_url: "https://www.aljazeera.com/news/2026/6/3/iran-kuwait-bahrain-hit-is-the-war-in-the-gulf-escalating-again"
        retrieved_at: "2026-06-05T12:03:19+00:00"
  - type: "pm_response"
    notes: "Polymarket's 97% survival price holds firm against active strike escalation, with the invasion contract at 17% providing a corroborating signal."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Al Jazeera Staff: Iran, Kuwait, Bahrain hit: Is the war in the Gulf escalating again? |"
    url: "https://www.aljazeera.com/news/2026/6/3/iran-kuwait-bahrain-hit-is-the-war-in-the-gulf-escalating-again"
    published_at: "2026-06-03T11:42:59.000Z"
    retrieved_at: "2026-06-05T12:03:19+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
