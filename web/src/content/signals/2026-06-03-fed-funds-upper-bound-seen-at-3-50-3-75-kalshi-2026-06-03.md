---
signal_id: "CMSIG2026060305"
signal_slug: "fed-funds-upper-bound-seen-at-3-50-3-75-kalshi-2026-06-03"
headline: "Fed funds upper bound seen at 3.50-3.75%: Kalshi"
semantic_title: "Funds rate staying at 3.50-3.75 percent commands pricing"
telemetry: "Kalshi 34%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-03T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Fed funds upper bound (next decision)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.34
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-16T18:05:00Z"
bullets:
  - "Kalshi pins the Fed funds upper bound in the 3.50-3.75% range: 91% above 3.50% but only 34% above 3.75%."
  - "Hammack's hike signal is consistent with the hawkish end of the distribution, but markets still put only 15% on 4.00% or higher."
  - "Beige Book flagging Middle East energy-driven inflation and labor stagnation adds upside risk but markets are not yet pricing a full move above 3.75%."
  - "Companion Kalshi ladder (CM-EVT-85LZKDJL71) prices 97% above 3.50% but only 1% above 3.75%, showing the near-term EFFR distribution is even more tightly capped."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Cleveland Fed President Beth Hammack signaled a rate hike may be needed soon as inflation risks intensify."
    publisher: "Anupam Nagar"
    published_at: "2026-06-03T00:00:00.000Z"
    source_url: "https://economictimes.indiatimes.com/markets/us-stocks/news/feds-hammack-signals-rate-hike-may-be-needed-soon-as-inflation-risks-intensify/articleshow/131476088.cms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Anupam Nagar"
        source_url: "https://economictimes.indiatimes.com/markets/us-stocks/news/feds-hammack-signals-rate-hike-may-be-needed-soon-as-inflation-risks-intensify/articleshow/131476088.cms"
        retrieved_at: "2026-06-04T03:24:20+00:00"
  - type: "pm_response"
    notes: "Kalshi's distribution places peak probability at 3.50-3.75%, fading Hammack's hike rhetoric at higher levels."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Anupam Nagar: Fed's Hammack signals rate hike may be needed soon as inflation risks"
    url: "https://economictimes.indiatimes.com/markets/us-stocks/news/feds-hammack-signals-rate-hike-may-be-needed-soon-as-inflation-risks-intensify/articleshow/131476088.cms"
    published_at: "2026-06-03T00:00:00.000Z"
    retrieved_at: "2026-06-04T03:24:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
