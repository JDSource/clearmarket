---
signal_id: "CMSIG2026091404"
signal_slug: "clarity-act-signed-into-law-by-2026-polymarket-21-2026-09-14"
headline: "Clarity Act signed into law by 2026: Polymarket 21%"
semantic_title: "Clarity Act passage by year-end holds below 25%"
telemetry: "Polymarket 21%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-14T00:00:00.000Z"
event_id: "CM-EVT-ZXN47LV744"
event_slug: "clarity-act-signed-into-law-in-2026"
event_question: "Will the Clarity Act (H.R. 3633) be signed into law by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9cb23d04b2ded06147482076688b69b487a8d982c63ebdda2ab3678cf27cf390"
  question_raw: "Clarity Act (H.R.3633) signed into law in 2026?"
  current_price: 0.21
  volume_24h_usd: 1220556.2788880006
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "Polymarket prices the Clarity Act being signed into law by 2026 at 21%, resolving via UMA oracle."
  - "Despite a make-or-break Senate cloture vote Tuesday and Trump backing the bill with new ethics concessions, Polymarket still puts better than 3-in-4 odds against passage this year."
  - "Bitcoin trading near $77,000-$80,000 (Story 30, 32) is a correlated signal, crypto asset prices are rallying on legislative hope even as the prediction market stays skeptical on actual enactment."
  - "Passage requires Senate cloture, floor vote, House concurrence, and presidential signature all before December 31, 2026, a tight sequential path that explains the discount."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The Senate is set to hold a crucial procedural cloture vote Tuesday on the Clarity Act, which would establish a new regulatory framework for crypto assets."
    publisher: "Garrett Downs"
    published_at: "2026-09-14T00:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/09/14/clarity-act-senate-vote-crypto-regulation.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Garrett Downs"
        source_url: "https://www.cnbc.com/2026/09/14/clarity-act-senate-vote-crypto-regulation.html"
        retrieved_at: "2026-09-15T13:05:57+00:00"
  - type: "pm_response"
    notes: "Polymarket's 21% is a meaningful long-shot pricing: the market acknowledges real momentum but assigns high probability to the bill failing one of its remaining legislative hurdles."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Garrett Downs: Clarity Act faces crucial Senate vote Tuesday in big moment for crypto"
    url: "https://www.cnbc.com/2026/09/14/clarity-act-senate-vote-crypto-regulation.html"
    published_at: "2026-09-14T00:00:00.000Z"
    retrieved_at: "2026-09-15T13:05:57+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
