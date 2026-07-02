---
signal_id: "CMSIG2026070103"
signal_slug: "fed-funds-upper-bound-seen-at-3-50-3-75-kalshi-ladder-2026-07-01"
headline: "Fed funds upper bound seen at 3.50-3.75%: Kalshi ladder"
semantic_title: "Fed funds upper bound consensus hardens well above 3.75 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-01T19:21:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Fed funds rate upper bound following next FOMC decision"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.29
  volume_24h_usd: 435.58
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-16T18:05:00Z"
bullets:
  - "Kalshi ladder prices 89% above 3.50%, but collapses to 29% above 3.75%, placing the market-implied upper bound squarely in the 3.50-3.75% range."
  - "Warsh's 'inflation risks diminishing' language is partly consistent with this pricing, markets are not pricing an imminent cut to below 3.50%."
  - "The 22% Kalshi probability on any Fed rate cut before 2027 suggests traders still see the current hold as durable despite the softer inflation rhetoric."
  - "Resolves via Federal Reserve official policy announcement; the settlement level is the upper bound of the federal funds target range after the next FOMC decision."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Chair Kevin Warsh said inflation risks are declining and predicted artificial intelligence will be a net job creator, delivering a cautiously optimistic macro read."
    publisher: "NBCNews"
    published_at: "2026-07-01T19:21:00.000Z"
    source_url: "https://us.headtopics.com/news/fed-chairman-says-inflation-risks-are-declining-predicts-85121373"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "NBCNews"
        source_url: "https://us.headtopics.com/news/fed-chairman-says-inflation-risks-are-declining-predicts-85121373"
        retrieved_at: "2026-07-02T10:34:14+00:00"
  - type: "pm_response"
    notes: "Kalshi's ladder distribution on the fed funds upper bound is the clearest market signal on how Warsh's comments are being digested by rate traders."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "NBCNews: Fed chairman says inflation risks are declining, predicts AI will crea"
    url: "https://us.headtopics.com/news/fed-chairman-says-inflation-risks-are-declining-predicts-85121373"
    published_at: "2026-07-01T19:21:00.000Z"
    retrieved_at: "2026-07-02T10:34:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
