---
signal_id: "CMSIG2026101004"
signal_slug: "blue-wave-in-2026-midterms-kalshi-81-2026-10-10"
headline: "Blue wave in 2026 midterms: Kalshi 81%"
semantic_title: "Blue wave in 2026 midterms stays the favored outcome"
telemetry: "Kalshi 81%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-10T00:00:00.000Z"
event_id: "CM-EVT-QK0HJYVMX2"
event_slug: "kxbluewavecombo-27feb"
event_question: "Will there be a blue wave in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBLUEWAVECOMBO-27FEB"
  question_raw: "Will Democrats hold 218 or more seats in the House after the 2026 midterms AND hold 49 or more seats in the Senate after the 2026 midterms?"
  current_price: 0.81
  volume_24h_usd: 36225.02
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices a blue wave in the 2026 midterms at 81%, a strong majority outcome."
  - "The policy analysis citing favorable Democratic fundamentals is consistent with the Kalshi contract's heavy lean toward a Democratic wave result."
  - "A related Kalshi contract puts a blue tsunami, a larger Democratic sweep, at 44%, suggesting the market sees a significant but not historically dominant wave as most likely."
  - "Resolves via official electoral commission results; the gap between 81% wave and 44% tsunami pricing implies the market expects a meaningful but bounded Democratic gain."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A midterm analysis published October 10 finds Democrats holding structural advantages in both the House and Senate with less than a month until Election Day on November 3."
    publisher: "Kevin Nealer"
    published_at: "2026-10-10T00:00:00.000Z"
    source_url: "https://www.policymagazine.ca/letter-from-washington-the-state-of-the-midterms/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Kevin Nealer"
        source_url: "https://www.policymagazine.ca/letter-from-washington-the-state-of-the-midterms/"
        retrieved_at: "2026-10-13T07:48:09+00:00"
  - type: "pm_response"
    notes: "Kalshi prices a blue wave at 81% and a blue tsunami at 44%, with the spread indicating the market favors a solid but not historic Democratic midterm performance."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Kevin Nealer: Letter from Washington: The State of the Midterms - Policy Magazine"
    url: "https://www.policymagazine.ca/letter-from-washington-the-state-of-the-midterms/"
    published_at: "2026-10-10T00:00:00.000Z"
    retrieved_at: "2026-10-13T07:48:09+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
