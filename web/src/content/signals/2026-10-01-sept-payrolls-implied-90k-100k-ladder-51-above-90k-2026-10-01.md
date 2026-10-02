---
signal_id: "CMSIG2026100101"
signal_slug: "sept-payrolls-implied-90k-100k-ladder-51-above-90k-2026-10-01"
headline: "Sept payrolls implied 90K-100K: ladder 51% above 90K"
semantic_title: "September payrolls seen landing near 90K to 100K"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-01T00:00:00.000Z"
event_id: "CM-EVT-MZQH465PC3"
event_slug: "kxpayrolls-26sep"
event_question: "September 2026 nonfarm payrolls added"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26SEP-T100000"
  question_raw: "Will above 100000 jobs be added in September 2026?"
  current_price: 0.45
  volume_24h_usd: 7567.48
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "Ladder pins September payrolls in the 90K-100K range: 51% above 90K, only 45% above 100K, 28% above 125K."
  - "ADP's 90K private-sector print and Wall Street's 84K consensus both sit squarely in the ladder's modal band, markets broadly consistent with incoming data."
  - "Trading volume on this ladder surged roughly 9,950x day over day, signaling intense fresh attention ahead of the Friday BLS print."
  - "The sharp drop from 65% above 80K to 51% above 90K shows the market sees meaningful downside tail risk around the consensus estimate."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Wall Street forecasts 84,000 September nonfarm payrolls ahead of Friday's BLS release, with ADP printing 90,000 private-sector jobs."
    publisher: "Jeff Cox"
    published_at: "2026-10-01T00:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/10/01/the-september-jobs-report-will-be-released-friday-heres-what-to-expect.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jeff Cox"
        source_url: "https://www.cnbc.com/2026/10/01/the-september-jobs-report-will-be-released-friday-heres-what-to-expect.html"
        retrieved_at: "2026-10-02T07:47:52+00:00"
  - type: "pm_response"
    notes: "Ladder resolves via BLS Employment Situation; volume spike confirms high event sensitivity heading into the release."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jeff Cox: The September jobs report will be released Friday. Here's what to expe"
    url: "https://www.cnbc.com/2026/10/01/the-september-jobs-report-will-be-released-friday-heres-what-to-expect.html"
    published_at: "2026-10-01T00:00:00.000Z"
    retrieved_at: "2026-10-02T07:47:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
