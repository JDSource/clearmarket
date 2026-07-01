---
signal_id: "CMSIG2026063006"
signal_slug: "scotus-hears-tariff-case-by-end-2026-kalshi-22-2026-06-30"
headline: "SCOTUS hears tariff case by end 2026: Kalshi 22%"
semantic_title: "SCOTUS tariff case by year-end holds at low conviction"
telemetry: "Kalshi 22%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-30T14:35:43.000Z"
event_id: "CM-EVT-RJRTFQZDJ0"
event_slug: "kxtrumptariffhear-27jan"
event_question: "Will the Supreme Court hear a case on Trump's tariffs by the end of 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPTARIFFHEAR-27JAN-X"
  question_raw: "What cases will the Supreme Court agree to hear before Jan 2027?"
  current_price: 0.22
  volume_24h_usd: 4.17
  arbitration_model: "kalshi_staff"
  resolution_source: "Supreme Court"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prediction market prices only 22% on the Supreme Court agreeing to hear a case on Trump's tariffs before end of 2026."
  - "The Court's willingness to rule against Trump on birthright citizenship shows judicial independence, but a tariff case requires a circuit split or emergency application the market views as unlikely this year."
  - "The birthright ruling itself does not directly bear on tariff litigation timelines, making this a weaker cross-market read."
  - "Resolves via Supreme Court docket; the Court must formally grant certiorari or agree to an expedited review before December 31, 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Supreme Court struck down Trump's birthright citizenship executive order 6-3, delivering a major legal defeat on a core immigration policy."
    publisher: "AOL"
    published_at: "2026-06-30T14:35:43.000Z"
    source_url: "https://www.aol.com/articles/supreme-court-rejects-trumps-birthright-143543000.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "AOL"
        source_url: "https://www.aol.com/articles/supreme-court-rejects-trumps-birthright-143543000.html"
        retrieved_at: "2026-07-01T11:20:57+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 22% on Supreme Court resolution; low base rate reflects the Court's discretionary docket control."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "AOL: Supreme Court rejects Trump's birthright citizenship order in major bl"
    url: "https://www.aol.com/articles/supreme-court-rejects-trumps-birthright-143543000.html"
    published_at: "2026-06-30T14:35:43.000Z"
    retrieved_at: "2026-07-01T11:20:57+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
