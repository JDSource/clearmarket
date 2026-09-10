---
signal_id: "CMSIG2026090703"
signal_slug: "fed-rate-hike-in-2026-polymarket-72-after-blowout-jobs-print-2026-09-07"
headline: "Fed rate hike in 2026: Polymarket 72% after blowout jobs print"
semantic_title: "Odds on a Fed hike in 2026 hold near 75 percent"
telemetry: "Polymarket 72%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-07T00:00:00.000Z"
event_id: "CM-EVT-87QV1G78C4"
event_slug: "fed-rate-hike-in-2026"
event_question: "Will the Federal Reserve raise its benchmark interest rate in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x80b3af88cb991980e8da1ce86b9794a0957f96ec98c29319dd7ba65e9744d82b"
  question_raw: "Fed rate hike in 2026?"
  current_price: 0.72
  volume_24h_usd: 43459.19598099999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-09T00:00:00Z"
bullets:
  - "The Polymarket contract on the Fed raising its benchmark rate in 2026 sits at 72%, resolving via UMA oracle."
  - "Siegel's argument that a hike is economically warranted is broadly consistent with the 72% pricing, though the contract is not at near-certainty, reflecting genuine uncertainty about the political timing he cited."
  - "August payrolls came in at 162,000, roughly triple the 53,000 consensus, adding fuel to the hawkish case but the market has not moved to price near-certainty of a hike."
  - "A companion Kalshi contract on the multi-deadline hike series also sits at 76%, a tight cross-venue read suggesting little divergence in the base-case probability."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Wharton's Professor Jeremy Siegel argued that only midterm-election political constraints are stopping the Federal Reserve from hiking rates after August's blowout 162,000 jobs report."
    publisher: "pbs.org"
    published_at: "2026-09-07T00:00:00.000Z"
    source_url: "https://www.pbs.org/newshour/politics/trump-keeps-heralding-an-economic-boom-but-even-a-solid-jobs-report-is-causing-problems-for-him"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "pbs.org"
        source_url: "https://www.pbs.org/newshour/politics/trump-keeps-heralding-an-economic-boom-but-even-a-solid-jobs-report-is-causing-problems-for-him"
        retrieved_at: "2026-09-10T12:39:52+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle on whether the Fed raises its benchmark rate at any point in 2026; the 72% read is consistent across both Polymarket and Kalshi."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "pbs.org: Trump keeps heralding an economic boom, but even a solid jobs report i"
    url: "https://www.pbs.org/newshour/politics/trump-keeps-heralding-an-economic-boom-but-even-a-solid-jobs-report-is-causing-problems-for-him"
    published_at: "2026-09-07T00:00:00.000Z"
    retrieved_at: "2026-09-10T12:39:52+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
