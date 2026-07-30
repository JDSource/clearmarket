---
signal_id: "CMSIG2026073002"
signal_slug: "fed-funds-upper-bound-seen-at-3-5-3-75-kalshi-ladder-2026-07-30"
headline: "Fed funds upper bound seen at 3.5-3.75%: Kalshi ladder"
semantic_title: "Fed funds upper bound holds near 3.5 percent post-meeting"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-30T00:00:00.000Z"
event_id: "CM-EVT-5P6C5JFKT9"
event_slug: "kxfed-27jan"
event_question: "Post-July-meeting Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-27JAN-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Jan 27, 2027 meeting?"
  current_price: 0.32
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2027-02-03T19:05:00Z"
bullets:
  - "Kalshi ladder pins the post-meeting Fed funds upper bound in the 3.5-3.75% range, with 83% above 3.0% but only 32% above 3.75%."
  - "Warsh's anti-inflation stance and the 9-3 hold are fully consistent with the ladder's sharp probability cliff above 3.75%."
  - "The 35% reading at the 4.0% strike reflects three dissenting votes but markets clearly assign minority odds to an imminent hike."
  - "Cross-referencing the Kalshi contract on a rate cut greater than 25 basis points this year at 9% confirms the market sees a narrow path in both directions."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Federal Reserve Chair Kevin Warsh vowed not to waver on inflation as the Fed held rates unchanged at 3.5%-3.75% with three dissents favoring a hike."
    publisher: "No Author"
    published_at: "2026-07-30T00:00:00.000Z"
    source_url: "https://www.japantimes.co.jp/business/2026/07/30/markets/warsh-inflation-fed-rates/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "No Author"
        source_url: "https://www.japantimes.co.jp/business/2026/07/30/markets/warsh-inflation-fed-rates/"
        retrieved_at: "2026-07-30T10:20:48+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via Federal Reserve official policy statements; the 3.5%-3.75% hold band is the current market consensus with a shallow hike tail."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "No Author: Warsh vows not to ‘waver’ on inflation as divided Fed leaves rates unc"
    url: "https://www.japantimes.co.jp/business/2026/07/30/markets/warsh-inflation-fed-rates/"
    published_at: "2026-07-30T00:00:00.000Z"
    retrieved_at: "2026-07-30T10:20:48+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
