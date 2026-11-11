---
signal_id: "CMSIG2026111005"
signal_slug: "ukraine-cedes-donbas-before-2027-polymarket-4-2026-11-10"
headline: "Ukraine cedes Donbas before 2027: Polymarket 4%"
semantic_title: "Ukraine giving up rest of Donbas stays a long shot at 4%"
telemetry: "Polymarket 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-10T07:09:12.000Z"
event_id: "CM-EVT-CP6V946J32"
event_slug: "will-ukraine-agree-to-give-up-the-rest-of-donbas-before-2027"
event_question: "Will Ukraine agree to give up the rest of Donbas before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xbac2d74fbb7ab5f72b557605538376485d1a093bd9a526584b33153a83a74d97"
  question_raw: "Will Ukraine agree to give up the rest of Donbas before 2027?"
  current_price: 0.039
  volume_24h_usd: 279.406977
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Ukraine agreeing to give up the rest of Donbas before 2027 sits at 4%, a strong long-shot read."
  - "Trading volume on this contract surged 5,488x day over day, the largest volume signal among Ukraine peace-related markets, reflecting fresh attention on the Abu Dhabi talks."
  - "Despite the talks being described as constructive, Rubio admitted much work remains; the 4% price is consistent with no breakthrough pricing."
  - "Resolves via UMA oracle; a formal Ukrainian agreement to cede Donbas territory must be publicly announced before January 1, 2027."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Russia, Ukraine, and the US held a second day of trilateral peace talks in Abu Dhabi, described as constructive but with no ceasefire in sight."
    publisher: "Elizabeth Schumacher, Timothy Jones"
    published_at: "2026-11-10T07:09:12.000Z"
    source_url: "https://www.dw.com/en/us-russia-and-ukraine-kick-off-second-day-of-abu-dhabi-talks/live-79906232"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Elizabeth Schumacher, Timothy Jones"
        source_url: "https://www.dw.com/en/us-russia-and-ukraine-kick-off-second-day-of-abu-dhabi-talks/live-79906232"
        retrieved_at: "2026-11-11T07:47:31+00:00"
  - type: "pm_response"
    notes: "Polymarket holds at 4% with a 55.9x volume surge, confirming the talks are drawing trader attention without shifting the consensus toward a deal."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Elizabeth Schumacher, Timothy Jones: US, Russia and Ukraine start second day of Abu Dhabi talks"
    url: "https://www.dw.com/en/us-russia-and-ukraine-kick-off-second-day-of-abu-dhabi-talks/live-79906232"
    published_at: "2026-11-10T07:09:12.000Z"
    retrieved_at: "2026-11-11T07:47:31+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
