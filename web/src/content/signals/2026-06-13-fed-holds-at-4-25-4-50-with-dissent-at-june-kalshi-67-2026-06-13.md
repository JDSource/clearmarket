---
signal_id: "CMSIG2026061305"
signal_slug: "fed-holds-at-4-25-4-50-with-dissent-at-june-kalshi-67-2026-06-13"
headline: "Fed holds at 4.25-4.50% with dissent at June: Kalshi 67%"
semantic_title: "Fed June hold with dissent wavers near two-thirds odds"
telemetry: "Kalshi 67%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-13T00:42:13.000Z"
event_id: "CM-EVT-MZGHWX20T0"
event_slug: "kxfedcombo-26jun"
event_question: "Will the Federal Reserve hold rates at 4.25%-4.50% with at least one dissent at its June 2026 meeting?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDCOMBO-26JUN-0-0"
  question_raw: "Will Federal Funds Rate Decision be No change AND Dissents be 0 for Jun 2026?"
  current_price: 0.67
  volume_24h_usd: 238.04
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-06-17T19:00:00Z"
bullets:
  - "Kalshi prices a Fed hold at 4.25-4.50% with at least one dissent at 67% ahead of the June FOMC meeting."
  - "The hot May CPI print and collapse of rate-cut calls are consistent with a hold, but the 67% level reflects uncertainty about whether dissent materializes."
  - "Bitcoin's 14.3% drop is attributed in part to the hawkish macro backdrop, though the Kalshi contract reflects current pricing only."
  - "Resolves via the Bureau of Labor Statistics; the dissent condition requires at least one FOMC member to formally register opposition to the hold decision."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin dropped 14.3% amid ETF outflows and hawkish Fed expectations following the hot CPI print."
    publisher: "interactivecrypto.com"
    published_at: "2026-06-13T00:42:13.000Z"
    source_url: "https://www.interactivecrypto.com/bitcoin-s-14-3-drop-2-97-billion-etf-outflows-and-hawkish-fed-drive-downtrend-jun-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "interactivecrypto.com"
        source_url: "https://www.interactivecrypto.com/bitcoin-s-14-3-drop-2-97-billion-etf-outflows-and-hawkish-fed-drive-downtrend-jun-2026"
        retrieved_at: "2026-06-13T10:25:37+00:00"
  - type: "pm_response"
    notes: "Kalshi prices a hold as the base case at 67%, with the dissent clause adding meaningful uncertainty to resolution."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "interactivecrypto.com: Bitcoin's 14.3% Drop: $2.97 Billion ETF Outflows and Hawkish Fed Drive"
    url: "https://www.interactivecrypto.com/bitcoin-s-14-3-drop-2-97-billion-etf-outflows-and-hawkish-fed-drive-downtrend-jun-2026"
    published_at: "2026-06-13T00:42:13.000Z"
    retrieved_at: "2026-06-13T10:25:37+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
