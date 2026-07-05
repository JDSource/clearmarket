---
signal_id: "CMSIG2026070406"
signal_slug: "june-cpi-monthly-change-seen-at-0-3-to-0-2-kalshi-2026-07-04"
headline: "June CPI monthly change seen at -0.3% to -0.2%: Kalshi"
semantic_title: "June CPI monthly change consensus anchors near negative territory"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-04T18:07:17.000Z"
event_id: "CM-EVT-KJ2LGV0M57"
event_slug: "kxcpi-26jun"
event_question: "June 2026 CPI monthly change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26JUN-T-0.2"
  question_raw: "Will CPI rise more than -0.2% in June 2026?"
  current_price: 0.36
  volume_24h_usd: 211.6
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-07-14T13:56:00Z"
bullets:
  - "Kalshi ladder implies the June 2026 CPI monthly change in the -0.3% to -0.2% range: 80% above -0.3% but only 36% above -0.2%, with sharp dropoff above zero."
  - "Trading volume on this Kalshi ladder surged 14,950% day over day, with the weak jobs print and Bitcoin rally both drawing fresh CPI positioning."
  - "A deflationary monthly CPI print would combine with the soft labor market to reinforce the case for Fed cuts priced in the companion rate ladder (CM-EVT-PHWX2H6DM5)."
  - "A separate Kalshi ladder for August 2026 CPI (CM-EVT-D057W6W251) implies a return to positive territory near 0.1-0.2%, suggesting the market treats June deflation as a one-month dip, not a trend."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin rebounded above $63,000 on July 4 as weak US payrolls data boosted rate-cut hopes, lifting risk assets broadly."
    publisher: "coindesk.com"
    published_at: "2026-07-04T18:07:17.000Z"
    source_url: "https://www.coindesk.com/markets/2026/07/04/bitcoin-jumps-above-usd63-000-reversing-end-june-losses"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "coindesk.com"
        source_url: "https://www.coindesk.com/markets/2026/07/04/bitcoin-jumps-above-usd63-000-reversing-end-june-losses"
        retrieved_at: "2026-07-05T10:07:52+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder contract; extraordinary volume spike confirms the June jobs miss catalyzed intense fresh CPI positioning across multiple strikes."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "coindesk.com: BTC price news: Bitcoin retakes $63,000, reversing end-June losses"
    url: "https://www.coindesk.com/markets/2026/07/04/bitcoin-jumps-above-usd63-000-reversing-end-june-losses"
    published_at: "2026-07-04T18:07:17.000Z"
    retrieved_at: "2026-07-05T10:07:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
