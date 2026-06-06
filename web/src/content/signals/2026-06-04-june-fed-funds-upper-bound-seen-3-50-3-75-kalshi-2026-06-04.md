---
signal_id: "CMSIG2026060402"
signal_slug: "june-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-06-04"
headline: "June Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Fed funds upper bound anchors in the 3.50-3.75 percent range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-04T00:34:37.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Federal funds rate upper bound (next Fed decision)"
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
  - "Kalshi prices the Fed funds upper bound in the 3.50-3.75% range: 91% above 3.50% but only 34% above 3.75%, with near-zero odds above 4.25%."
  - "Persistent inflation and a strong labor market are consistent with the market holding rates in this corridor, ruling out near-term cuts."
  - "The sharp drop from 91% to 34% between the 3.50% and 3.75% strikes pins the most likely upper bound at exactly 3.50-3.75%."
  - "The 10% Kalshi probability on a jumbo cut (CM-EVT-RWRZ1R3SD6) corroborates the rate-ladder distribution, with no easing signal at any strike above 3.75%."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "New Fed Chair Kevin Warsh faces persistent inflation above the 2% target, compounding the policy challenge from a strong labor market."
    publisher: "businesstimes.com.sg"
    published_at: "2026-06-04T00:34:37.000Z"
    source_url: "https://www.businesstimes.com.sg/international/global/us-feds-kevin-warsh-inherits-economy-increasingly-squeezed-inflation"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "businesstimes.com.sg"
        source_url: "https://www.businesstimes.com.sg/international/global/us-feds-kevin-warsh-inherits-economy-increasingly-squeezed-inflation"
        retrieved_at: "2026-06-06T10:00:26+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via Federal Reserve official rate announcement; each strike settles independently based on the published upper bound."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "businesstimes.com.sg: US Fed's Kevin Warsh inherits economy increasingly squeezed by inflati"
    url: "https://www.businesstimes.com.sg/international/global/us-feds-kevin-warsh-inherits-economy-increasingly-squeezed-inflation"
    published_at: "2026-06-04T00:34:37.000Z"
    retrieved_at: "2026-06-06T10:00:26+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
