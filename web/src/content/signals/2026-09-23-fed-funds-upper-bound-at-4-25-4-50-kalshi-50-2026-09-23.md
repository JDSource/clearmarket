---
signal_id: "CMSIG2026092302"
signal_slug: "fed-funds-upper-bound-at-4-25-4-50-kalshi-50-2026-09-23"
headline: "Fed funds upper bound at 4.25-4.50%: Kalshi 50%"
semantic_title: "Fed funds peak near 4.25 percent stays the consensus view"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-23T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound (multi-meeting ladder)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.50"
  question_raw: "Will the upper bound of the federal funds rate be above 4.50% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.07
  volume_24h_usd: 55.5
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder shows 90% probability above 4.00%, 50% above 4.25%, and only 7% above 4.50%, centering the market-implied peak at 4.25-4.50%."
  - "Richmond Fed President Tom Barkin's public case for hiking is consistent with market pricing of one more move, but the 7% above 4.50% shows the market is not pricing an aggressive sequence."
  - "Boston Fed President Susan Collins (Story 6) also backed a hike with possible further increase; the ladder absorbs both hawkish signals without shifting the tail materially."
  - "Resolution will reference the official FOMC rate decision; the named source is unspecified, but outcome is observable via the Federal Reserve's published target range."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Richmond Fed President Tom Barkin's 'WHY HIKE?' address to CFA Society Baltimore argued the FOMC's dual mandate justifies further tightening."
    publisher: "insurancenewsnet.com"
    published_at: "2026-09-23T00:00:00.000Z"
    source_url: "https://insurancenewsnet.com/oarticle/why-hike"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "insurancenewsnet.com"
        source_url: "https://insurancenewsnet.com/oarticle/why-hike"
        retrieved_at: "2026-09-24T07:47:37+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder; multiple Fed officials' hawkish signals are consistent with current pricing, which remains anchored below 4.50% with high confidence."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "insurancenewsnet.com: WHY HIKE? - Insurance News | InsuranceNewsNet"
    url: "https://insurancenewsnet.com/oarticle/why-hike"
    published_at: "2026-09-23T00:00:00.000Z"
    retrieved_at: "2026-09-24T07:47:37+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
