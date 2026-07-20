---
signal_id: "CMSIG2026071902"
signal_slug: "fed-funds-above-3-75-after-june-kalshi-7-2026-07-19"
headline: "Fed funds above 3.75% after June: Kalshi 7%"
semantic_title: "Rate hike consensus wavers despite fresh Fed inflation warnings"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-19T00:00:00.000Z"
event_id: "CM-EVT-PHWX2H6DM5"
event_slug: "kxfed-26jul"
event_question: "June 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26JUL-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Jul 29, 2026 meeting?"
  current_price: 0.07
  volume_24h_usd: 530.94
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-08-05T18:05:00Z"
bullets:
  - "Kalshi prices only 7% odds the June 2026 Fed funds upper bound exceeds 3.75%, despite the Fed's hawkish framing."
  - "The market is at odds with the hawkish posture: officials warn of persistent inflation, yet the pricing implies near-certain hold at 3.50-3.75%."
  - "Import prices surging 7.1% year-over-year in June add a concrete upside risk the 7% above-3.75% tail may be underpricing."
  - "Companion binary CM-EVT-RJ6SMJGK50 on the June meeting upper bound carries no price data; the ladder is the only live signal available."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Fed flagged fresh inflation threats after June CPI printed at 3.5% year-over-year, with core prices still elevated and officials warning relief may not last."
    publisher: "Matthew Benjamin"
    published_at: "2026-07-19T00:00:00.000Z"
    source_url: "https://www.fool.com/investing/2026/07/19/fed-flags-inflation-threat-could-rattle-market/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Matthew Benjamin"
        source_url: "https://www.fool.com/investing/2026/07/19/fed-flags-inflation-threat-could-rattle-market/"
        retrieved_at: "2026-07-20T10:47:34+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder; hawkish Fed commentary is being absorbed rather than amplified in current strike distribution."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Matthew Benjamin: Fed Flags a Fresh Inflation Threat That Could Rattle Markets | The Mot"
    url: "https://www.fool.com/investing/2026/07/19/fed-flags-inflation-threat-could-rattle-market/"
    published_at: "2026-07-19T00:00:00.000Z"
    retrieved_at: "2026-07-20T10:47:34+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
