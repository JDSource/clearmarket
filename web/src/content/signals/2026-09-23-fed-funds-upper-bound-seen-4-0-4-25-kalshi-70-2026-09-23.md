---
signal_id: "CMSIG2026092301"
signal_slug: "fed-funds-upper-bound-seen-4-0-4-25-kalshi-70-2026-09-23"
headline: "Fed funds upper bound seen 4.0-4.25%: Kalshi 70%"
semantic_title: "Fed funds above 4 percent prices in amid hike talk"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-23T00:00:00.000Z"
event_id: "CM-EVT-6BS28TS762"
event_slug: "kxfed-26oct"
event_question: "Federal funds upper bound (multi-meeting ladder)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26OCT-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Oct 28, 2026 meeting?"
  current_price: 0.02
  volume_24h_usd: 66.71
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-11-04T18:05:00Z"
bullets:
  - "Kalshi ladder puts ~70% on the federal funds upper bound clearing 4.00%, but collapses to 2% above 4.25%, pinning the implied range at 4.00-4.25%."
  - "Reuters reports Fed officials view inflation and a strengthening economy as grounds for further tightening; the Kalshi distribution is broadly consistent with one more hike, not two."
  - "Trading volume on this Kalshi ladder surged 327x day-over-day, signaling fresh capital flowing into the rate-path bet as the news cycle intensified."
  - "A companion Kalshi ladder (CM-EVT-MR57HVWJT3) implies a similar 4.25-4.50% peak, with only 7% above 4.50%, confirming the market sees limited probability of aggressive multi-hike follow-through."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Multiple Fed officials and mounting inflation data are pushing the Federal Reserve toward additional rate hikes ahead of midterm elections."
    publisher: "Thomson Reuters"
    published_at: "2026-09-23T00:00:00.000Z"
    source_url: "https://my957.com/2026/09/23/feds-barr-says-further-rate-hikes-will-likely-be-needed/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Thomson Reuters"
        source_url: "https://my957.com/2026/09/23/feds-barr-says-further-rate-hikes-will-likely-be-needed/"
        retrieved_at: "2026-09-24T07:47:37+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder; the 327x volume surge is a clear signal of elevated market attention, though current pricing stops well short of pricing in a sustained tightening cycle."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Thomson Reuters: Inflation pressures raise prospect of Fed rate hike on eve of election"
    url: "https://my957.com/2026/09/23/feds-barr-says-further-rate-hikes-will-likely-be-needed/"
    published_at: "2026-09-23T00:00:00.000Z"
    retrieved_at: "2026-09-24T07:47:37+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
