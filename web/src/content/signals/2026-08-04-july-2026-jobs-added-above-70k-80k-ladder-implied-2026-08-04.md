---
signal_id: "CMSIG2026080405"
signal_slug: "july-2026-jobs-added-above-70k-80k-ladder-implied-2026-08-04"
headline: "July 2026 jobs added above 70K-80K: ladder-implied"
semantic_title: "July payroll growth seen in the 70K-80K range by prediction markets"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-04T00:00:00.000Z"
event_id: "CM-EVT-K086YCMND2"
event_slug: "kxpayrolls-26jul"
event_question: "July 2026 nonfarm payroll change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26JUL-T80000"
  question_raw: "Will above 80000 jobs be added in July 2026?"
  current_price: 0.43
  volume_24h_usd: 1234.26
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2026-11-06T14:00:00Z"
bullets:
  - "The July payroll ladder implies a modal outcome near 70K-80K: 58% above 70K, 43% above 80K, and 95% above zero."
  - "Soft job openings data is consistent with below-consensus payroll expectations, but the market assigns near-zero chance of outright job losses."
  - "The ADP employment ladder (CM-EVT-5NXN7ZTR53) implies a similar 50K-75K range for July private payrolls, providing corroborating cross-market support."
  - "Resolves on the BLS nonfarm payrolls release; the wide spread between 70K and 80K reflects genuine uncertainty ahead of the print."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US job openings slid below 7.4 million in June as healthcare vacancies posted their largest drop in 11 months, with layoffs steady and voluntary quits rising."
    publisher: "theepochtimes.com"
    published_at: "2026-08-04T00:00:00.000Z"
    source_url: "https://www.theepochtimes.com/us/us-job-openings-slide-below-7-4-million-in-june-6071054"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "theepochtimes.com"
        source_url: "https://www.theepochtimes.com/us/us-job-openings-slide-below-7-4-million-in-june-6071054"
        retrieved_at: "2026-08-05T10:30:51+00:00"
  - type: "pm_response"
    notes: "Ladder distribution is the key read here; no single binary price exists for this event."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "theepochtimes.com: US Job Openings Slide Below 7.4 Million in June | The Epoch Times"
    url: "https://www.theepochtimes.com/us/us-job-openings-slide-below-7-4-million-in-june-6071054"
    published_at: "2026-08-04T00:00:00.000Z"
    retrieved_at: "2026-08-05T10:30:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
