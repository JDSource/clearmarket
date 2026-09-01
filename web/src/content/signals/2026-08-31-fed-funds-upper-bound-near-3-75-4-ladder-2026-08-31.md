---
signal_id: "CMSIG2026083102"
signal_slug: "fed-funds-upper-bound-near-3-75-4-ladder-2026-08-31"
headline: "Fed funds upper bound near 3.75-4%: ladder"
semantic_title: "Fed funds upper bound seen near 3.75 to 4 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-31T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds rate upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.34
  volume_24h_usd: 0.34
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "The prediction market ladder pins the fed funds upper bound in the 3.75-4.0% range: 76% above 3.75% but only 34% above 4.0%."
  - "Warsh's hawkish tone is consistent with the market leaning toward 3.75-4.0%, but the 34% at 4.0% reflects lingering skepticism about a full hike cycle."
  - "The near-term ladder (CM-EVT-4ZQLQPNH91) shows only 59% above 3.75% and just 1% above 4.0%, suggesting markets are split on whether hikes materialize before a closer horizon."
  - "The spread between the two ladders reveals genuine timeline uncertainty: the market agrees on the destination range but not the timing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Markets debated whether Fed Chairman Kevin Warsh's Jackson Hole speech signals a September rate hike, with some participants skeptical given limited data."
    publisher: "Jeff Cox"
    published_at: "2026-08-31T00:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/08/31/markets-see-warsh-endorsing-a-rate-hike-in-september-not-everyone-is-convinced.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jeff Cox"
        source_url: "https://www.cnbc.com/2026/08/31/markets-see-warsh-endorsing-a-rate-hike-in-september-not-everyone-is-convinced.html"
        retrieved_at: "2026-09-01T13:00:06+00:00"
  - type: "pm_response"
    notes: "Two separate ladder markets diverge sharply at the 4.0% strike, highlighting timing uncertainty in the Warsh hike narrative."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jeff Cox: Markets see Warsh endorsing a rate hike in September. Not everyone is"
    url: "https://www.cnbc.com/2026/08/31/markets-see-warsh-endorsing-a-rate-hike-in-september-not-everyone-is-convinced.html"
    published_at: "2026-08-31T00:00:00.000Z"
    retrieved_at: "2026-09-01T13:00:06+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
