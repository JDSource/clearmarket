---
signal_id: "CMSIG2026082404"
signal_slug: "dems-win-u-s-house-in-next-election-kalshi-85-2026-08-24"
headline: "Dems win U.S. House in next election: Kalshi 85%"
semantic_title: "Democrats heavily favored to win the House in November"
telemetry: "Kalshi 85%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-24T00:00:00.000Z"
event_id: "CM-EVT-FV8MR86S63"
event_slug: "controlh-2026"
event_question: "Will the Democratic Party win the U.S. House in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "CONTROLH-2026-D"
  question_raw: "Will Democrats win the House in 2026?"
  current_price: 0.85
  volume_24h_usd: 48789.03
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices Democrats winning the U.S. House at 85%, a strong favorite position heading into the November midterms."
  - "The Kushner-Jeffries meeting underscores Republican concern about House control, consistent with the market's heavily Democratic lean."
  - "A companion Kalshi contract (CM-EVT-T5VXKJT451) puts Republicans controlling at least one chamber at 47%, implying the Senate is the GOP's more viable path."
  - "Resolves via Library of Congress official chamber composition record after the 2026 election."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Jared Kushner's private meeting with House Democratic leader Hakeem Jeffries, confirmed by CBS News, signals cross-aisle maneuvering less than three months before the midterms."
    publisher: "cbsnews.com"
    published_at: "2026-08-24T00:00:00.000Z"
    source_url: "https://www.cbsnews.com/news/jared-kushner-hakeem-jeffries-meeting-2026-midterm-elections/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cbsnews.com"
        source_url: "https://www.cbsnews.com/news/jared-kushner-hakeem-jeffries-meeting-2026-midterm-elections/"
        retrieved_at: "2026-08-25T08:36:45+00:00"
  - type: "pm_response"
    notes: "Kalshi hosts both contracts; the 85% Democratic House probability versus 47% Republican single-chamber odds suggests markets see a split Congress as the most likely outcome."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cbsnews.com: Jared Kushner and Democratic House leader Hakeem Jeffries met as midte"
    url: "https://www.cbsnews.com/news/jared-kushner-hakeem-jeffries-meeting-2026-midterm-elections/"
    published_at: "2026-08-24T00:00:00.000Z"
    retrieved_at: "2026-08-25T08:36:45+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
