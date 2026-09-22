---
signal_id: "CMSIG2026092101"
signal_slug: "sept-fed-funds-upper-bound-seen-at-4-0-4-25-kalshi-ladder-2026-09-21"
headline: "Sept Fed funds upper bound seen at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound stays near 4.0-4.25 percent range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-21T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound after September 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.38
  volume_24h_usd: 177.94
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the September 2026 Fed funds upper bound in the 4.0-4.25% range: 85% above 4.0%, only 38% above 4.25%."
  - "St. Louis Fed President Alberto Musalem's call for more hikes is broadly consistent with the ladder's 4.0-4.25% modal range."
  - "The sharp drop from 85% to 38% between the 4.0% and 4.25% strikes signals the market sees a hike as likely but not a certainty of overshooting to 4.25%."
  - "Only 5% probability sits at 4.5% or above, suggesting the Kalshi ladder is fading the most aggressive end of Musalem's hawkish language."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "St. Louis Fed President Alberto Musalem said more rate hikes are likely needed to quell inflation, reinforcing a hawkish Fed posture."
    publisher: "Howard Schneider"
    published_at: "2026-09-21T00:00:00.000Z"
    source_url: "https://www.reuters.com/business/feds-musalem-says-more-rate-hikes-likely-needed-quell-inflation-2026-09-21/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Howard Schneider"
        source_url: "https://www.reuters.com/business/feds-musalem-says-more-rate-hikes-likely-needed-quell-inflation-2026-09-21/"
        retrieved_at: "2026-09-22T13:03:08+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder provides full strike distribution; modal range 4.0-4.25% is the actionable read, with tail probability above 4.25% modest at 38%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Howard Schneider: EXCLUSIVE: Fed's Musalem says more rate hikes likely needed to quell i"
    url: "https://www.reuters.com/business/feds-musalem-says-more-rate-hikes-likely-needed-quell-inflation-2026-09-21/"
    published_at: "2026-09-21T00:00:00.000Z"
    retrieved_at: "2026-09-22T13:03:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
