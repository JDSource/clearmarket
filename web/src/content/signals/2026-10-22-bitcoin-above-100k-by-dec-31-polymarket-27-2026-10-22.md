---
signal_id: "CMSIG2026102208"
signal_slug: "bitcoin-above-100k-by-dec-31-polymarket-27-2026-10-22"
headline: "Bitcoin above $100K by Dec 31: Polymarket 27%"
semantic_title: "Bitcoin above $100K by year-end stays below 25 percent odds"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-22T09:54:26.000Z"
event_id: "CM-EVT-0MWN62PNG9"
event_slug: "kxbtcmaxy-26dec31"
event_question: "Bitcoin price above $100K by Dec 31 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXY-26DEC31-99999.99"
  question_raw: "Will Bitcoin be above $99,999.99 by Dec 31, 2026 at 11:59 PM ET?"
  current_price: 0.27
  volume_24h_usd: 206.85
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T04:59:00Z"
bullets:
  - "Polymarket ladder prices 27% on Bitcoin exceeding $100K by December 31, 2026, falling to 10% above $110K and 5% above $120K."
  - "Bitcoin's drop below $82,000 amid a risk-off AI selloff and oil surge puts the current spot price roughly 20% below the $100K strike, consistent with sub-30% odds."
  - "The Kalshi contract on a National Bitcoin Reserve in 2026 sits at 5%, removing a key potential policy catalyst from the near-term bull case."
  - "JPMorgan Asset Management's first long-term Bitcoin forecast projects 10% annual returns, a gradual-appreciation view that does not support a near-term $100K print."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin slumped below $82,000 as markets moved risk-off on an AI selloff and oil price surge tied to Middle East tensions."
    publisher: "Shaurya Malwa, James Van Straten, Omkar Godbole"
    published_at: "2026-10-22T09:54:26.000Z"
    source_url: "https://www.coindesk.com/business/2026/10/22/live-updates-bitcoin-s-round-trip-to-usd85-000-burns-traders-on-both-sides"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Shaurya Malwa, James Van Straten, Omkar Godbole"
        source_url: "https://www.coindesk.com/business/2026/10/22/live-updates-bitcoin-s-round-trip-to-usd85-000-burns-traders-on-both-sides"
        retrieved_at: "2026-10-22T13:24:33+00:00"
  - type: "pm_response"
    notes: "Polymarket ladder resolves via uma_oracle; the distribution shows rapidly thinning probability above $110K, implying the market treats $100K as a meaningful ceiling near term."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Shaurya Malwa, James Van Straten, Omkar Godbole: Live updates: Bitcoin slumps below $82,000 as markets go risk off on A"
    url: "https://www.coindesk.com/business/2026/10/22/live-updates-bitcoin-s-round-trip-to-usd85-000-burns-traders-on-both-sides"
    published_at: "2026-10-22T09:54:26.000Z"
    retrieved_at: "2026-10-22T13:24:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
