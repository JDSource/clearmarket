---
signal_id: "CMSIG2026060808"
signal_slug: "dems-win-house-in-2026-midterms-kalshi-78-2026-06-08"
headline: "Dems win House in 2026 midterms: Kalshi 78%"
semantic_title: "Democrats favored to retake the House at 78 percent"
telemetry: "Kalshi 78%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-08T11:29:39.000Z"
event_id: "CM-EVT-FV8MR86S63"
event_slug: "controlh-2026"
event_question: "Will the Democratic Party or the Republican Party win control of the U.S. House of Representatives in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "CONTROLH-2026-D"
  question_raw: "Will Democrats win the House in 2026?"
  current_price: 0.78
  volume_24h_usd: 13639.57
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices a 78% chance Democrats win control of the US House of Representatives after the 2026 midterms."
  - "Republican urgency on a pre-recess legislative package reflects awareness of the hostile electoral environment the market is pricing."
  - "The companion Kalshi contract on Republicans controlling at least one chamber sits at only 23%, a structurally consistent read."
  - "Resolves via Library of Congress official certification of House composition following the November 2026 election."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "House Republicans are racing to pass a third party-line legislative package before August recess, seeking to cement Trump's agenda ahead of midterms amid growing intra-party friction."
    publisher: "Sudiksha Kochi"
    published_at: "2026-06-08T11:29:39.000Z"
    source_url: "https://www.newsnationnow.com/politics/republican-third-reconciliation-bill-midterm-elections/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Sudiksha Kochi"
        source_url: "https://www.newsnationnow.com/politics/republican-third-reconciliation-bill-midterm-elections/"
        retrieved_at: "2026-06-09T10:57:53+00:00"
  - type: "pm_response"
    notes: "Kalshi's 78% Democratic House probability is consistent with the 23% Republican chamber-control figure, forming a coherent midterm pricing structure."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Sudiksha Kochi: House Republicans push for third party-line package ahead of midterms"
    url: "https://www.newsnationnow.com/politics/republican-third-reconciliation-bill-midterm-elections/"
    published_at: "2026-06-08T11:29:39.000Z"
    retrieved_at: "2026-06-09T10:57:53+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
