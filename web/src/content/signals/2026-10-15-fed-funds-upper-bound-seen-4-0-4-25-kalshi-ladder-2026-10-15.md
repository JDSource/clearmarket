---
signal_id: "CMSIG2026101501"
signal_slug: "fed-funds-upper-bound-seen-4-0-4-25-kalshi-ladder-2026-10-15"
headline: "Fed funds upper bound seen 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds above 4.25% stays a long shot after Warsh silence"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-15T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound (post-meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.15
  volume_24h_usd: 68.39
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the fed funds upper bound in the 4.0-4.25% range: 91% above 4.0% but only 15% above 4.25%."
  - "Warsh gave no rate guidance, and the market is consistent with that ambiguity, a hike to 4.25% or above remains a distinct minority view despite hot CPI and PPI."
  - "The sharp probability cliff between 4.0% (91%) and 4.25% (15%) signals the market treats one more hike as the base but rules out an aggressive step higher."
  - "A companion Kalshi ladder (CM-EVT-6BS28TS762) prices the same upper-bound question even more conservatively, collapsing to 13% above 4.0%, suggesting some resolution-date disagreement across contracts."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Chair Kevin Warsh declined to signal the next rate hike direction despite two hot inflation prints this week raising expectations of an earlier move."
    publisher: "Steve Kopack"
    published_at: "2026-10-15T00:00:00.000Z"
    source_url: "https://www.nbcnews.com/business/economy/will-fed-raise-interest-rates-kevin-warsh-offer-clues-rcna603661"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Steve Kopack"
        source_url: "https://www.nbcnews.com/business/economy/will-fed-raise-interest-rates-kevin-warsh-offer-clues-rcna603661"
        retrieved_at: "2026-10-16T12:59:00+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder; the 76-percentage-point gap between 4.0% and 4.25% is the sharpest cliff in the distribution and is the key market read on Warsh's silence."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Steve Kopack: Will the Fed raise interest rates? Kevin Warsh gives no clues"
    url: "https://www.nbcnews.com/business/economy/will-fed-raise-interest-rates-kevin-warsh-offer-clues-rcna603661"
    published_at: "2026-10-15T00:00:00.000Z"
    retrieved_at: "2026-10-16T12:59:00+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
