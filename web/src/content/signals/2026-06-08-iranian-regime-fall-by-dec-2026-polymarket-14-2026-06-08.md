---
signal_id: "CMSIG2026060804"
signal_slug: "iranian-regime-fall-by-dec-2026-polymarket-14-2026-06-08"
headline: "Iranian regime fall by Dec 2026: Polymarket 14%"
semantic_title: "Iranian regime survival consensus holds despite fresh strikes"
telemetry: "Polymarket 14%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-08T10:14:18.000Z"
event_id: "CM-EVT-QNQ4VPVP80"
event_slug: "will-the-iranian-regime-fall-by-the-end-of-2026"
event_question: "Will the Iranian regime fall by December 31, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xbb4d51e6364066d92eb6f9b8413dd7193de70966736044463b205834805a1f3b"
  question_raw: "Will the Iranian regime fall before 2027?"
  current_price: 0.14
  volume_24h_usd: 41794.567678
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 14% on the Iranian regime falling by December 31, 2026, despite active Israel-Iran exchange of strikes."
  - "The ceasefire breakdown and fresh airstrikes are not moving the regime-survival consensus, 86% of capital-weighted probability backs continuity."
  - "A companion Polymarket contract on a US invasion of Iran (CM-EVT-WD982793G1) sits at 17%, suggesting markets see escalation as limited, not existential for Tehran."
  - "Resolves via UMA oracle based on recognized governmental change in Iran; the low probability reflects that past rounds of strikes have not destabilized the regime."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran and Israel exchanged strikes on June 8, breaking the US-backed ceasefire and fueling dollar and oil market moves."
    publisher: "investing.com"
    published_at: "2026-06-08T10:14:18.000Z"
    source_url: "https://www.investing.com/analysis/dollar-rallies-stocks-tumble-as-nfp-report-fuels-fed-hike-bets-200681708"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "investing.com"
        source_url: "https://www.investing.com/analysis/dollar-rallies-stocks-tumble-as-nfp-report-fuels-fed-hike-bets-200681708"
        retrieved_at: "2026-06-08T12:25:51+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; current pricing is broadly consistent across the June 30 (3%) and December 31 (14%) horizon contracts."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "investing.com: Dollar Rallies, Stocks Tumble as NFP Report Fuels Fed Hike Bets | Inve"
    url: "https://www.investing.com/analysis/dollar-rallies-stocks-tumble-as-nfp-report-fuels-fed-hike-bets-200681708"
    published_at: "2026-06-08T10:14:18.000Z"
    retrieved_at: "2026-06-08T12:25:51+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
