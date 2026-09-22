---
signal_id: "CMSIG2026092202"
signal_slug: "dems-senate-control-2026-polymarket-65-2026-09-22"
headline: "Dems Senate control 2026: Polymarket 65%"
semantic_title: "Democrats stay favored to win Senate control in 2026"
telemetry: "Polymarket 65%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-22T00:00:00.000Z"
event_id: "CM-EVT-M9WJY06T90"
event_slug: "which-party-will-win-the-senate-in-2026"
event_question: "Which party will win control of the U.S. Senate in the 2026 election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x307a1ed89d60b61002dd5bbf00e1408c5ed2ab3fcdb056191ca7ef9bc34d38f3"
  question_raw: "Will the Democratic Party control the Senate after the 2026 Midterm elections?"
  current_price: 0.65
  volume_24h_usd: 110406.73484299993
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket puts Democrats winning Senate control at 65%, a clear but not dominant majority."
  - "The 8.6-point Democratic polling lead in Quantus Insights data is directionally consistent with Polymarket's 65% Democrat-favored read."
  - "Companion Kalshi contract on Republicans controlling at least one chamber sits at 60%, implying markets see a split-Congress outcome as plausible."
  - "Resolution via uma oracle on Polymarket ties to certified election results; any prolonged count or runoff could delay settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Democrats opened their widest polling lead of the 2026 election cycle, up 8.6 points over Republicans in Quantus Insights' congressional survey."
    publisher: "newsweek.com"
    published_at: "2026-09-22T00:00:00.000Z"
    source_url: "https://www.newsweek.com/democrats-lead-republicans-midterms-poll-12470910"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "newsweek.com"
        source_url: "https://www.newsweek.com/democrats-lead-republicans-midterms-poll-12470910"
        retrieved_at: "2026-09-22T13:03:08+00:00"
  - type: "pm_response"
    notes: "Polymarket at 65% Democrats versus Kalshi at 60% Republicans holding one chamber reflect a genuine split-control scenario being priced in across venues."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "newsweek.com: Democrats Open Up Widest Lead Just Weeks Before Midterms - Newsweek"
    url: "https://www.newsweek.com/democrats-lead-republicans-midterms-poll-12470910"
    published_at: "2026-09-22T00:00:00.000Z"
    retrieved_at: "2026-09-22T13:03:08+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
