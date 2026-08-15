---
signal_id: "CMSIG2026081307"
signal_slug: "us-recession-by-end-2026-polymarket-8-2026-08-13"
headline: "US recession by end-2026: Polymarket 8%"
semantic_title: "US recession by end of 2026 stays a long shot at 8%"
telemetry: "Polymarket 8%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-13T00:00:00.000Z"
event_id: "CM-EVT-943Z5Y3NP4"
event_slug: "us-recession-by-end-of-2026"
event_question: "Will the United States enter a recession by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xfdc73f10edf0266756686f35b5712cffa828b0940fc015e0426c76c934c2105d"
  question_raw: "US recession by end of 2026?"
  current_price: 0.08
  volume_24h_usd: 49.84
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-31T00:00:00Z"
bullets:
  - "The Polymarket contract on a US recession by end-2026 sits at 8%, a firmly low reading despite active naval operations near the Strait of Hormuz."
  - "Hegseth's indefinite-blockade signal is a meaningful supply-side risk, yet the market is not pricing a recession as a likely outcome for 2026."
  - "Companion Kalshi contract CM-EVT-L7017DJDX1 also prices the recession probability at 6%, with both venues aligned in dismissing near-term recession risk."
  - "Resolves via Bureau of Economic Analysis on Polymarket; settlement requires an official BEA determination of two consecutive quarters of negative GDP growth within the 2026 window."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US Defense Secretary Pete Hegseth said the US naval blockade of Iran could be maintained indefinitely, raising economic risk from prolonged Strait of Hormuz disruption."
    publisher: "Thomson Reuters    ·  Posted: Aug 13, 2026 6:42 PM EDT | Last Updated: August 14"
    published_at: "2026-08-13T00:00:00.000Z"
    source_url: "https://www.cbc.ca/news/world/hegseth-us-blockade-iran-9.7306636"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Thomson Reuters    ·  Posted: Aug 13, 2026 6:42 PM EDT | Last Updated: August 14"
        source_url: "https://www.cbc.ca/news/world/hegseth-us-blockade-iran-9.7306636"
        retrieved_at: "2026-08-15T08:21:50+00:00"
  - type: "pm_response"
    notes: "Polymarket and Kalshi are tightly aligned at 8% and 6% respectively, offering a cross-venue confirmation that recession risk is being discounted despite geopolitical escalation."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Thomson Reuters    ·  Posted: Aug 13, 2026 6:42 PM EDT | Last Updated: August 14: U.S. can maintain 'indefinite' naval blockade of Iran if needed, Hegse"
    url: "https://www.cbc.ca/news/world/hegseth-us-blockade-iran-9.7306636"
    published_at: "2026-08-13T00:00:00.000Z"
    retrieved_at: "2026-08-15T08:21:50+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
