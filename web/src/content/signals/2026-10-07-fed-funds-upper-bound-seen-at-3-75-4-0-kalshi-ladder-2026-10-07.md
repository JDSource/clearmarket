---
signal_id: "CMSIG2026100701"
signal_slug: "fed-funds-upper-bound-seen-at-3-75-4-0-kalshi-ladder-2026-10-07"
headline: "Fed funds upper bound seen at 3.75-4.0%: Kalshi ladder"
semantic_title: "Fed funds peak near 4 percent as October hike bets slip"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-07T00:00:00.000Z"
event_id: "CM-EVT-6BS28TS762"
event_slug: "kxfed-26oct"
event_question: "Federal funds upper bound following next Fed decision"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26OCT-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Oct 28, 2026 meeting?"
  current_price: 0.18
  volume_24h_usd: 3119.29
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-11-04T18:05:00Z"
bullets:
  - "Kalshi ladder pins the federal funds upper bound in the 3.75-4.0% range: 99% above 3.75%, only 18% above 4.0%."
  - "The weak 29K September payroll print aligns with this pricing, markets are consistent with an October hold, not a hike."
  - "Trading volume on this contract surged 84.5x day-over-day, signaling this ladder is drawing intense fresh attention post-NFP."
  - "A companion Kalshi ladder (CM-EVT-MR57HVWJT3) implies a slightly higher terminal of 4.0-4.25%, putting the inter-contract spread at roughly one quarter-point, the market's best guess at a December hike premium."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "September payrolls rose just 29,000, well below expectations, reducing bets on a Fed October rate hike."
    publisher: "nexusstocksdaily.com"
    published_at: "2026-10-07T00:00:00.000Z"
    source_url: "https://nexusstocksdaily.com/us-jobs-report-payrolls-rise-just-29000-fed-october-hike-bets-fade-2/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "nexusstocksdaily.com"
        source_url: "https://nexusstocksdaily.com/us-jobs-report-payrolls-rise-just-29000-fed-october-hike-bets-fade-2/"
        retrieved_at: "2026-10-08T07:48:09+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder; 84.5x volume spike confirms the September NFP report is the dominant repricing catalyst."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "nexusstocksdaily.com: US jobs report: Payrolls rise just 29,000; Fed October hike bets fade"
    url: "https://nexusstocksdaily.com/us-jobs-report-payrolls-rise-just-29000-fed-october-hike-bets-fade-2/"
    published_at: "2026-10-07T00:00:00.000Z"
    retrieved_at: "2026-10-08T07:48:09+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
