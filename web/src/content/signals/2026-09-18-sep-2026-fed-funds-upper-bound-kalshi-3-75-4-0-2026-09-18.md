---
signal_id: "CMSIG2026091802"
signal_slug: "sep-2026-fed-funds-upper-bound-kalshi-3-75-4-0-2026-09-18"
headline: "Sep 2026 Fed funds upper bound: Kalshi 3.75-4.0%"
semantic_title: "Fed funds upper bound seen in 3.75-4.0 percent range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-18T00:00:00.000Z"
event_id: "CM-EVT-6BS28TS762"
event_slug: "kxfed-26oct"
event_question: "September 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26OCT-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Oct 28, 2026 meeting?"
  current_price: 0.44
  volume_24h_usd: 4082.34
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-11-04T18:05:00Z"
bullets:
  - "The Kalshi ladder prices 98% above 3.75% but only 44% above 4.0%, implying the market centers the upper bound squarely at 4.0%."
  - "The confirmed hike to 3.75%-4% matches the ladder's 98% mass at or above 3.75%, with near-zero probability above 4.25%."
  - "The 44% at-or-above 4.0% likely reflects residual uncertainty around whether this meeting's decision lands exactly at 4.00% versus 4.25%."
  - "The 1% pricing above 4.25% effectively rules out any surprise 50 bps hike scenario in this cycle."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Fed raised rates to 3.75%-4% at its September 2026 meeting and signaled one additional hike this year."
    publisher: "Zachary B. Wolf"
    published_at: "2026-09-18T00:00:00.000Z"
    source_url: "https://www.cnn.com/2026/09/18/politics/fed-rate-increase-trump-midterms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Zachary B. Wolf"
        source_url: "https://www.cnn.com/2026/09/18/politics/fed-rate-increase-trump-midterms"
        retrieved_at: "2026-09-18T12:38:42+00:00"
  - type: "pm_response"
    notes: "The Kalshi ladder distribution is now resolving with the confirmed 4.0% upper bound, leaving the 44% at-or-above-4.0% tranche as the operative settlement question."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Zachary B. Wolf: How the Fed’s rate decisions could hurt GOP chances in the midterms |"
    url: "https://www.cnn.com/2026/09/18/politics/fed-rate-increase-trump-midterms"
    published_at: "2026-09-18T00:00:00.000Z"
    retrieved_at: "2026-09-18T12:38:42+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
