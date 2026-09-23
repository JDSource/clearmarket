---
signal_id: "CMSIG2026092202"
signal_slug: "fed-funds-upper-bound-kalshi-ladder-holds-4-0-4-25-range-2026-09-22"
headline: "Fed funds upper bound: Kalshi ladder holds 4.0-4.25% range"
semantic_title: "Markets back further hikes but cap expectations near 4.25%"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-22T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds rate upper bound (post-September)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.42
  volume_24h_usd: 2423.8
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder sees 86% odds the federal funds upper bound clears 4.0%, but only 42% above 4.25%, pinning the implied range at 4.0-4.25%."
  - "Barkin's 'Why Hike' speech reinforces the hawkish Fed communication wave; pricing is consistent with another hike but not a sustained multi-step campaign."
  - "Volume on the ladder rose 517x day over day, as noted in the Musalem wire, confirming aggregate hawkish Fed commentary is drawing concentrated market activity."
  - "The Kalshi distribution assigns only 10% to 4.5% and above, meaning the market is fading the most aggressive hike scenarios despite uniform Fed hawkishness."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Richmond Fed President Tom Barkin published a speech titled 'Why Hike,' defending the Fed's dual mandate rationale for continued tightening."
    publisher: "pubt.io"
    published_at: "2026-09-22T00:00:00.000Z"
    source_url: "https://www.pubt.io/view/B2182954E31289984E4C4AE83A98215F1E02FAFD"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "pubt.io"
        source_url: "https://www.pubt.io/view/B2182954E31289984E4C4AE83A98215F1E02FAFD"
        retrieved_at: "2026-09-23T13:17:11+00:00"
  - type: "pm_response"
    notes: "Same Kalshi ladder as Story 0; volume surge reflects cumulative hawkish Fed signal from multiple officials across the week."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "pubt.io: Federal Reserve Bank of Richmond (via Public) / Why Hike"
    url: "https://www.pubt.io/view/B2182954E31289984E4C4AE83A98215F1E02FAFD"
    published_at: "2026-09-22T00:00:00.000Z"
    retrieved_at: "2026-09-23T13:17:11+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
