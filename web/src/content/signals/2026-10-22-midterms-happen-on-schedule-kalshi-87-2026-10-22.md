---
signal_id: "CMSIG2026102203"
signal_slug: "midterms-happen-on-schedule-kalshi-87-2026-10-22"
headline: "Midterms happen on schedule: Kalshi 87%"
semantic_title: "Midterm elections running on schedule stays heavily favored"
telemetry: "Kalshi 87%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-22T00:00:00.000Z"
event_id: "CM-EVT-HT9T7KMRT5"
event_slug: "kxmidtermhappen-2026"
event_question: "Will the midterm elections happen on schedule?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMIDTERMHAPPEN-2026-T50"
  question_raw: "Will at least 50 states conduct 2026 U.S. House midterms on time?"
  current_price: 0.87
  volume_24h_usd: 10753.78
  arbitration_model: "kalshi_staff"
  resolution_source: "The Washington Post"
  resolves_at: "2026-11-10T15:00:00Z"
bullets:
  - "Kalshi prices an 87% probability that the midterm elections proceed on their scheduled date."
  - "Diverse voter issue salience, including corruption as the top concern per a CNBC survey, has not shifted the scheduling probability."
  - "The 13% residual reflects general uncertainty around election disruption, not any specific announced threat."
  - "Resolution source is The Washington Post; any postponement or cancellation announcement would trigger settlement mechanics."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A Washington Post analysis identifies corruption, health care, and AI as rising voter concerns alongside cost of living heading into the November midterms."
    publisher: "Amber Phillips"
    published_at: "2026-10-22T00:00:00.000Z"
    source_url: "https://www.washingtonpost.com/politics/2026/10/22/top-issues-midterms/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Amber Phillips"
        source_url: "https://www.washingtonpost.com/politics/2026/10/22/top-issues-midterms/"
        retrieved_at: "2026-10-25T12:56:07+00:00"
  - type: "pm_response"
    notes: "Kalshi holds a firm 87% on schedule adherence, with the market treating disruption risk as a tail scenario despite a charged political environment."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Amber Phillips: The top issues in the midterms  - The Washington Post"
    url: "https://www.washingtonpost.com/politics/2026/10/22/top-issues-midterms/"
    published_at: "2026-10-22T00:00:00.000Z"
    retrieved_at: "2026-10-25T12:56:07+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
