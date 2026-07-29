---
signal_id: "CMSIG2026072901"
signal_slug: "fed-hike-by-settlement-date-polymarket-22-2026-07-29"
headline: "Fed hike by settlement date: Polymarket 22%"
semantic_title: "Fed rate hike by settlement stays a long shot at 22%"
telemetry: "Polymarket 22%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-29T00:00:00.000Z"
event_id: "CM-EVT-VZKJ3PV470"
event_slug: "fed-rate-hike-by"
event_question: "Will the Federal Reserve raise its benchmark interest rate by the settlement date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xac550c316d635e7f2dc810de6d6afd531e254b3c9c7d56d32d14337e7c3979e4"
  question_raw: "Fed Rate Hike by July 2026 Meeting?"
  current_price: 0.216
  volume_24h_usd: 32862.914967
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-09T00:00:00Z"
bullets:
  - "Polymarket puts only 22% on the Fed raising its benchmark rate by the settlement date."
  - "Citadel Securities publicly called for a July hike, but the Polymarket contract at 22% shows markets are unconvinced by that argument."
  - "The broader 2026 Polymarket contract on any Fed hike this year sits at 76%, indicating markets see a hike as likely eventually, just not now."
  - "Resolution via UMA oracle; the near-term 22% vs. full-year 76% gap reflects a debate over timing, not destination."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Citadel Securities argues Fed Chair Kevin Warsh should surprise markets with a July hike, while 104 economists and bitcoin analysts expect a hold."
    publisher: "coindesk.com"
    published_at: "2026-07-29T00:00:00.000Z"
    source_url: "https://www.coindesk.com/markets/2026/07/29/citadel-bets-on-a-fed-rate-hike-wednesday-as-bitcoin-analysts-call-a-hold-someone-will-be-wrong"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "coindesk.com"
        source_url: "https://www.coindesk.com/markets/2026/07/29/citadel-bets-on-a-fed-rate-hike-wednesday-as-bitcoin-analysts-call-a-hold-someone-will-be-wrong"
        retrieved_at: "2026-07-29T10:35:12+00:00"
  - type: "pm_response"
    notes: "Polymarket covers both the near-term settlement event at 22% and a full-year 2026 hike event at 76%, revealing a sharp timing wedge."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "coindesk.com: FOMC preview: Citadel bets on a Fed rate hike Wednesday as bitcoin (BT"
    url: "https://www.coindesk.com/markets/2026/07/29/citadel-bets-on-a-fed-rate-hike-wednesday-as-bitcoin-analysts-call-a-hold-someone-will-be-wrong"
    published_at: "2026-07-29T00:00:00.000Z"
    retrieved_at: "2026-07-29T10:35:12+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
