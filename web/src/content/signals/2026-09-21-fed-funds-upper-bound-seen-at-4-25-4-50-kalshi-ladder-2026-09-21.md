---
signal_id: "CMSIG2026092101"
signal_slug: "fed-funds-upper-bound-seen-at-4-25-4-50-kalshi-ladder-2026-09-21"
headline: "Fed funds upper bound seen at 4.25-4.50%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen near 4.25 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-21T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound following next meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.50"
  question_raw: "Will the upper bound of the federal funds rate be above 4.50% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.07
  volume_24h_usd: 55.29
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the fed funds upper bound at roughly 4.25-4.50%, with 91% above 4.00% but only 7% above 4.50%."
  - "Musalem's call for more hikes is consistent with the ladder's midpoint near 4.25-4.50%, but the market is not pricing a move above 4.50% as likely."
  - "Separately, the Kalshi contract on a rate cut greater than 25 basis points this year sits at just 3%, underscoring the market's firm rejection of any near-term easing."
  - "Resolution follows the Federal Reserve's official rate decision announcement, which settles the ladder strike by strike."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "St. Louis Fed President Alberto Musalem said more rate hikes are likely needed to quell inflation, reinforcing an already hawkish Fed posture."
    publisher: "Howard Schneider"
    published_at: "2026-09-21T00:00:00.000Z"
    source_url: "https://www.reuters.com/business/feds-musalem-says-more-rate-hikes-likely-needed-quell-inflation-2026-09-21/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Howard Schneider"
        source_url: "https://www.reuters.com/business/feds-musalem-says-more-rate-hikes-likely-needed-quell-inflation-2026-09-21/"
        retrieved_at: "2026-09-24T13:07:56+00:00"
  - type: "pm_response"
    notes: "Kalshi's rate-path ladder is the best-priced instrument available here; the 3% cut contract confirms the market is squarely in hike-or-hold territory."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Howard Schneider: EXCLUSIVE: Fed's Musalem says more rate hikes likely needed to quell i"
    url: "https://www.reuters.com/business/feds-musalem-says-more-rate-hikes-likely-needed-quell-inflation-2026-09-21/"
    published_at: "2026-09-21T00:00:00.000Z"
    retrieved_at: "2026-09-24T13:07:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
