---
signal_id: "CMSIG2026060202"
signal_slug: "fed-holds-with-dissent-at-june-fomc-kalshi-66-2026-06-02"
headline: "Fed holds with dissent at June FOMC: Kalshi 66%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-02T16:41:44.000Z"
event_id: "CM-EVT-MZGHWX20T0"
event_slug: "kxfedcombo-26jun"
event_question: "Will the Federal Reserve hold rates at 4.25%-4.50% with at least one dissent at its June 2026 meeting?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDCOMBO-26JUN-0-0"
  question_raw: "Will Federal Funds Rate Decision be No change AND Dissents be 0 for Jun 2026?"
  current_price: 0.66
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-06-17T19:00:00Z"
bullets:
  - "Kalshi puts 66% odds on the Fed holding rates at 4.25%-4.50% with at least one dissent at the June FOMC meeting."
  - "Hammack's public hike warning and her April dissent make the dissent component of this contract highly plausible; the hold component aligns with Kalshi rate ladders pricing below 3.75%."
  - "April CPI at 3.8% and core at 2.8% are the cited inflation triggers; energy costs up 17.9% annually add upward pressure."
  - "Resolves via Bureau of Labor Statistics official FOMC statement; contract requires both a hold decision AND a named dissenting vote."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Cleveland Fed President Beth Hammack warned rate hikes may be needed after April CPI printed 3.8% year-over-year with core at 2.8%."
    publisher: "PomiNews"
    published_at: "2026-06-02T16:41:44.000Z"
    source_url: "https://pomegra.io/news/feds-hammack-rate-hikes-back-on-table"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "PomiNews"
        source_url: "https://pomegra.io/news/feds-hammack-rate-hikes-back-on-table"
        retrieved_at: "2026-06-03T01:50:17+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 66% reflects a market split: hold is expected, but the dissent condition adds meaningful uncertainty beyond a simple rate decision."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "PomiNews: Fed's Hammack: Rate Hikes Back on Table - Pomegra News"
    url: "https://pomegra.io/news/feds-hammack-rate-hikes-back-on-table"
    published_at: "2026-06-02T16:41:44.000Z"
    retrieved_at: "2026-06-03T01:50:17+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
