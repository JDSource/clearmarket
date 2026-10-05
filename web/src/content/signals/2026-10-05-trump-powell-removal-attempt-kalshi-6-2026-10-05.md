---
signal_id: "CMSIG2026100503"
signal_slug: "trump-powell-removal-attempt-kalshi-6-2026-10-05"
headline: "Trump Powell removal attempt: Kalshi 6%"
semantic_title: "Trump removing Powell stays near long-shot odds"
telemetry: "Kalshi 6%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-05T00:00:00.000Z"
event_id: "CM-EVT-TMHG8WLK69"
event_slug: "kxtryfirepowell-26may12"
event_question: "Will Trump attempt to remove Powell as Federal Reserve Chair or Governor?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRYFIREPOWELL-26MAY12-GOV2"
  question_raw: "Will the President try to fire the Jerome Powell as either Chair of the Board of Governors of the Federal Reserve System or Member of the Board of Governors of the Federal Reserve System before Jan 1, 2027?"
  current_price: 0.058
  volume_24h_usd: 23.45
  arbitration_model: "kalshi_staff"
  resolution_source: "ABC"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices a Trump attempt to remove Powell at just 6%, keeping it a heavy long shot despite the adviser's public call."
  - "The news is a notable escalation in rhetoric, but the Kalshi contract at 6% suggests the market is not treating the adviser's comments as a credible near-term action signal."
  - "Trading volume on this contract is up 4,778% day over day, indicating a sharp surge in fresh attention to the removal question after the adviser's remarks."
  - "Resolution via ABC as the named source; the contract requires an actual removal attempt, not a statement, setting a high bar."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump's chief economic adviser called for former Federal Reserve Chair Jerome Powell to leave the Fed board, reigniting debate over central bank independence."
    publisher: "Rony Roy"
    published_at: "2026-10-05T00:00:00.000Z"
    source_url: "https://crypto.news/trump-adviser-calls-for-powell-exit-could-bitcoin-benefit/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Rony Roy"
        source_url: "https://crypto.news/trump-adviser-calls-for-powell-exit-could-bitcoin-benefit/"
        retrieved_at: "2026-10-05T16:44:30+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 6% with volume up 48.8x day over day; the volume spike is the key signal, not the price level."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Rony Roy: Trump adviser calls for Powell exit, could Bitcoin benefit?"
    url: "https://crypto.news/trump-adviser-calls-for-powell-exit-could-bitcoin-benefit/"
    published_at: "2026-10-05T00:00:00.000Z"
    retrieved_at: "2026-10-05T16:44:30+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
