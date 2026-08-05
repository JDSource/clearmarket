---
signal_id: "CMSIG2026080402"
signal_slug: "fed-funds-upper-bound-at-3-75-4-0-ladder-implied-2026-08-04"
headline: "Fed funds upper bound at 3.75-4.0%: ladder-implied"
semantic_title: "Fed funds upper bound stays near 3.75 percent on rate hike bets"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-04T16:29:46.733Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Federal funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.01
  volume_24h_usd: 34.81
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "The ladder prices the federal funds upper bound in the 3.75-4.00% range: 98% above 3.50%, 52% above 3.75%, but only 1% above 4.00%."
  - "A four-year high ISM reading and elevated input prices align with the pricing of a hike to 3.75-4.00%, but the market assigns near-zero probability to a hike beyond 4.00%."
  - "Trading volume on this ladder is up 575x day over day, a strong signal of fresh attention drawn by the ISM print and the Fed rate-hike narrative."
  - "The companion Polymarket contract (CM-EVT-87QV1G78C4) prices a 2026 rate hike at 62%, consistent with the ladder implying the most likely terminal level is 3.75-4.00%, not higher."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "ISM Manufacturing PMI hit 55.6, a four-year high, with elevated input prices, prompting analysis that the Fed could raise rates in 2026."
    publisher: "Rich Duprey"
    published_at: "2026-08-04T16:29:46.733Z"
    source_url: "https://247wallst.com/investing/2026/08/04/this-indicator-hasnt-been-this-high-in-4-years-it-means-the-fed-could-raise-rates-in-2026/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Rich Duprey"
        source_url: "https://247wallst.com/investing/2026/08/04/this-indicator-hasnt-been-this-high-in-4-years-it-means-the-fed-could-raise-rates-in-2026/"
        retrieved_at: "2026-08-05T10:30:51+00:00"
  - type: "pm_response"
    notes: "Ladder volume surge of 575x day over day is the standout signal; no single binary price is available for this event, read the distribution."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Rich Duprey: This Indicator Hasn't Been This High in 4 Years. It Means the Fed Coul"
    url: "https://247wallst.com/investing/2026/08/04/this-indicator-hasnt-been-this-high-in-4-years-it-means-the-fed-could-raise-rates-in-2026/"
    published_at: "2026-08-04T16:29:46.733Z"
    retrieved_at: "2026-08-05T10:30:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
