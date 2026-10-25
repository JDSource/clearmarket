---
signal_id: "CMSIG2026102502"
signal_slug: "fed-funds-upper-bound-above-4-0-kalshi-80-2026-10-25"
headline: "Fed funds upper bound above 4.0%: Kalshi 80%"
semantic_title: "Fed funds above 4 percent stays near consensus into October meeting"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-25T02:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds rate upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.1
  volume_24h_usd: 0.8
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder puts 80% odds on the federal funds upper bound staying above 4.0%, but only 10% above 4.25%, pinning the implied level in the 4.0-4.25% range."
  - "News reports that the Fed is expected to hold rates at the October meeting are broadly consistent with the 4.0% anchor in the Kalshi distribution."
  - "The sharp drop from 80% above 4.0% to just 10% above 4.25% signals the market sees a hike as a clear tail risk, not a base case, despite hot September PCE data."
  - "A separate Kalshi ladder (CM-EVT-6BS28TS762) pins the implied rate even lower at 3.75-4.0%, with just 8% above 4.0%, the spread between the two ladders may reflect different meeting horizons."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The US Federal Reserve is widely expected to hold rates steady at its October meeting despite persistent inflation and pre-midterm political pressure."
    publisher: "Yashasvi Vasistha"
    published_at: "2026-10-25T02:00:00.000Z"
    source_url: "https://timesofindia.indiatimes.com/business/international-business/us-fed-expected-to-hold-rates-as-inflation-energy-costs-weigh-ahead-of-midterms/articleshow/135181691.cms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Yashasvi Vasistha"
        source_url: "https://timesofindia.indiatimes.com/business/international-business/us-fed-expected-to-hold-rates-as-inflation-energy-costs-weigh-ahead-of-midterms/articleshow/135181691.cms"
        retrieved_at: "2026-10-25T07:48:12+00:00"
  - type: "pm_response"
    notes: "Kalshi carries two federal funds rate ladder contracts with differing implied ranges, suggesting timeline or meeting-date differences between the two instruments."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Yashasvi Vasistha: US Fed expected to hold rates as inflation, energy costs weigh ahead o"
    url: "https://timesofindia.indiatimes.com/business/international-business/us-fed-expected-to-hold-rates-as-inflation-energy-costs-weigh-ahead-of-midterms/articleshow/135181691.cms"
    published_at: "2026-10-25T02:00:00.000Z"
    retrieved_at: "2026-10-25T07:48:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
