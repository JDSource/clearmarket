---
signal_id: "CMSIG2026070902"
signal_slug: "fed-funds-above-3-50-post-meeting-kalshi-91-2026-07-09"
headline: "Fed funds above 3.50% post-meeting: Kalshi 91%"
semantic_title: "Rate hold consensus wavers above 3.75 percent floor"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-09T19:48:36.374Z"
event_id: "CM-EVT-6BS28TS762"
event_slug: "kxfed-26oct"
event_question: "Fed funds upper bound (post-meeting, second ladder)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26OCT-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Oct 28, 2026 meeting?"
  current_price: 0.2
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-11-04T18:05:00Z"
bullets:
  - "This Kalshi ladder prices 91% above 3.50% but collapses to 20% above 3.75% and 23% above 4.00%, showing a bifurcated distribution."
  - "The task force launch signals institutional uncertainty about the policy framework, yet the market assigns only 20-23% odds to any level above 3.75%."
  - "The 3-percentage-point spread between the 4.00% and 3.75% strikes (23% vs. 20%) is unusually flat, suggesting some residual ambiguity about the tail."
  - "Compare to the CM-EVT-PHWX2H6DM5 ladder: both anchor the mode at 3.50-3.75%, but this ladder shows a fatter right tail, implying slightly more uncertainty about a hike scenario."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Federal Reserve announced five new task forces led by outside economists to reassess how it conducts policy on data, jobs, and inflation."
    publisher: "Neil Pierson, HousingWire Automation"
    published_at: "2026-07-09T19:48:36.374Z"
    source_url: "https://www.housingwire.com/articles/fed-task-forces-monetary-policy-communications-balance-sheet-inflation-2026/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Neil Pierson, HousingWire Automation"
        source_url: "https://www.housingwire.com/articles/fed-task-forces-monetary-policy-communications-balance-sheet-inflation-2026/"
        retrieved_at: "2026-07-10T10:49:37+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder; the 91%-to-20% collapse between the 3.50% and 3.75% strikes is the key read on hike probability."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Neil Pierson, HousingWire Automation: Fed launches task forces on data, jobs and inflation - Housing Wire"
    url: "https://www.housingwire.com/articles/fed-task-forces-monetary-policy-communications-balance-sheet-inflation-2026/"
    published_at: "2026-07-09T19:48:36.374Z"
    retrieved_at: "2026-07-10T10:49:37+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
