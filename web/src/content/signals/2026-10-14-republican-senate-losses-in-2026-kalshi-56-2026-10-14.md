---
signal_id: "CMSIG2026101405"
signal_slug: "republican-senate-losses-in-2026-kalshi-56-2026-10-14"
headline: "Republican Senate losses in 2026: Kalshi 56%"
semantic_title: "Republican Senate incumbent losses in 2026 near 50%"
telemetry: "Kalshi 56%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-14T00:00:00.000Z"
event_id: "CM-EVT-39Y2BB24Y8"
event_slug: "kxlosereelectionrsen-2026"
event_question: "How many Republican senators will lose reelection in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLOSEREELECTIONRSEN-2026-5"
  question_raw: "Will at least 5 the Senate Republicans lose re-election in 2026?"
  current_price: 0.56
  volume_24h_usd: 8.73
  arbitration_model: "kalshi_staff"
  resolution_source: "the Senate Parliamentarian"
  resolves_at: "2026-12-31T15:00:00Z"
bullets:
  - "The Kalshi prediction market prices a 56% chance that at least one Republican senator loses reelection in 2026, close to a coin flip."
  - "Trading volume on this contract rose 204.6x day-over-day, the largest volume surge in today's dataset, signaling intense new positioning ahead of November 3."
  - "The companion Kalshi contract on Kansas Senate (CM-EVT-S6Y29BSL46) sits at 63% for the Republican candidate, suggesting at least one seat is genuinely contested."
  - "Resolves via the Senate Parliamentarian's official certification of 2026 election results; any runoff or recount scenario would delay settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Politico reported two Senate Republicans urging the Supreme Court to review John Eastman's disbarment, amid broader congressional activity three weeks before midterms."
    publisher: "Erin Doherty, Chris Marquette, Jasper Goodman, Brian Faler, Calen Razor"
    published_at: "2026-10-14T00:00:00.000Z"
    source_url: "https://www.politico.com/live-updates/2026/10/14/congress"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Erin Doherty, Chris Marquette, Jasper Goodman, Brian Faler, Calen Razor"
        source_url: "https://www.politico.com/live-updates/2026/10/14/congress"
        retrieved_at: "2026-10-15T07:47:47+00:00"
  - type: "pm_response"
    notes: "Kalshi contract on Republican Senate losses drew 204.6x normal daily volume, the sharpest activity spike in today's batch, as midterm uncertainty peaks."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Erin Doherty, Chris Marquette, Jasper Goodman, Brian Faler, Calen Razor: Inside Congress Live - Live Updates - POLITICO"
    url: "https://www.politico.com/live-updates/2026/10/14/congress"
    published_at: "2026-10-14T00:00:00.000Z"
    retrieved_at: "2026-10-15T07:47:47+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
