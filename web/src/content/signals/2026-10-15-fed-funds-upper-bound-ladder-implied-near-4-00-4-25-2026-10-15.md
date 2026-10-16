---
signal_id: "CMSIG2026101503"
signal_slug: "fed-funds-upper-bound-ladder-implied-near-4-00-4-25-2026-10-15"
headline: "Fed funds upper bound ladder: implied near 4.00-4.25%"
semantic_title: "Fed funds above 4.25% seen as a long shot after Warsh"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-15T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds rate upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.17
  volume_24h_usd: 63.57
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Ladder prices 90% on the upper bound exceeding 4.00% but only 17% above 4.25%, centering the implied range at 4.00-4.25%."
  - "Warsh's non-committal stance is consistent with the market sitting on the fence near 4.00-4.25%, not pricing a firm hike above 4.25%."
  - "The sharp drop from 90% at 4.00% to 17% at 4.25% shows markets see the next hike as likely but a move beyond it as improbable near-term."
  - "A companion ladder (CM-EVT-6BS28TS762) prices only 14% above 4.00% for a separate meeting, suggesting timeline uncertainty across the hiking path."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Chair Kevin Warsh signaled focus on inflation but gave no hint about the next rate hike, a day after Reuters reported the October decision is a closer call than expected."
    publisher: "Steve Kopack"
    published_at: "2026-10-15T00:00:00.000Z"
    source_url: "https://www.nbcnews.com/business/economy/will-fed-raise-interest-rates-kevin-warsh-offer-clues-rcna603661"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Steve Kopack"
        source_url: "https://www.nbcnews.com/business/economy/will-fed-raise-interest-rates-kevin-warsh-offer-clues-rcna603661"
        retrieved_at: "2026-10-16T07:47:56+00:00"
  - type: "pm_response"
    notes: "Ladder distribution consistent across two separate Fed meeting contracts; both anchor near the 4.00-4.25% zone with thin probability above 4.25%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Steve Kopack: Will the Fed raise interest rates? Kevin Warsh gives no clues"
    url: "https://www.nbcnews.com/business/economy/will-fed-raise-interest-rates-kevin-warsh-offer-clues-rcna603661"
    published_at: "2026-10-15T00:00:00.000Z"
    retrieved_at: "2026-10-16T07:47:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
