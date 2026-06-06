---
signal_id: "CMSIG2026060501"
signal_slug: "fed-cut-25bps-in-single-meeting-kalshi-10-2026-06-05"
headline: "Fed cut >25bps in single meeting: Kalshi 10%"
semantic_title: "Fed jumbo cut consensus breaks away after hot jobs data"
telemetry: "Kalshi 10%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-05T17:44:14.000Z"
event_id: "CM-EVT-RWRZ1R3SD6"
event_slug: "kxlargecut-26"
event_question: "Will the Federal Reserve cut interest rates by more than 25 basis points in a single action this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLARGECUT-26"
  question_raw: "Will the Fed cut rates more than 25 bps in 2026?"
  current_price: 0.104
  volume_24h_usd: 26.64
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi puts only 10% on the Fed cutting more than 25 basis points in a single meeting, reflecting deeply suppressed easing expectations."
  - "May's blowout jobs print is consistent with this low probability, reinforcing that aggressive cuts are off the table for now."
  - "New Fed Chair Kevin Warsh inherits an economy with inflation above 2% for five straight years, complicating any dovish pivot."
  - "Companion Kalshi contract on any Fed cut before 2027 sits at just 19%, underscoring the market's view that even modest easing is unlikely this year."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "May payrolls surged 172,000, beating forecasts and pushing Fed rate-cut expectations further out as new Chair Kevin Warsh faces a stagflationary policy dilemma."
    publisher: "Jeff Cox"
    published_at: "2026-06-05T17:44:14.000Z"
    source_url: "https://www.cnbc.com/2026/06/05/hot-jobs-report-puts-fed-cuts-further-out-of-reach-as-chair-warsh-faces-policy-tests.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jeff Cox"
        source_url: "https://www.cnbc.com/2026/06/05/hot-jobs-report-puts-fed-cuts-further-out-of-reach-as-chair-warsh-faces-policy-tests.html"
        retrieved_at: "2026-06-06T10:00:26+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via Federal Reserve official rate decision; a 50bps-or-larger cut in any single meeting would be required for resolution."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jeff Cox: Hot jobs report puts Fed cuts further out of reach as Chair Warsh face"
    url: "https://www.cnbc.com/2026/06/05/hot-jobs-report-puts-fed-cuts-further-out-of-reach-as-chair-warsh-faces-policy-tests.html"
    published_at: "2026-06-05T17:44:14.000Z"
    retrieved_at: "2026-06-06T10:00:26+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
