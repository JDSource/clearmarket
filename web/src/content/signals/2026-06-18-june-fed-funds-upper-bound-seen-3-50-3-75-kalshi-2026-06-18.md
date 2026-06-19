---
signal_id: "CMSIG2026061801"
signal_slug: "june-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-06-18"
headline: "June Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Fed funds upper bound consensus anchors at 3.5-3.75 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-18T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Fed funds upper bound post-June 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.36
  volume_24h_usd: 3.96
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-16T18:05:00Z"
bullets:
  - "Kalshi pins the June 2026 Fed funds upper bound in the 3.50-3.75% range, pricing 95% above 3.50% but only 36% above 3.75%."
  - "Xinhua confirmed the Fed held at 3.50-3.75%; the prediction market distribution is fully consistent with that reported hold."
  - "The 36% probability above 3.75% reflects policymaker signals of one hike later this year, not full consensus for a move."
  - "The Kalshi large-cut contract (CM-EVT-RWRZ1R3SD6) prices only 7% on a cut exceeding 25 bps, confirming the hawkish lean from the dot-plot shift."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Fed held the federal funds rate at 3.50-3.75% at Chair Kevin Warsh's first FOMC meeting, with policymakers signaling support for a future hike."
    publisher: "english.news.cn"
    published_at: "2026-06-18T00:00:00.000Z"
    source_url: "https://english.news.cn/20260618/77b4170f2c984fb6a11ae4f89c677c87/c.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "english.news.cn"
        source_url: "https://english.news.cn/20260618/77b4170f2c984fb6a11ae4f89c677c87/c.html"
        retrieved_at: "2026-06-19T12:03:18+00:00"
  - type: "pm_response"
    notes: "Kalshi's rate ladder resolves via Fed policy statement and matches the reported 3.50-3.75% hold with a modest hike tail priced in."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "english.news.cn: U.S. Fed holds interest rate steady-Xinhua"
    url: "https://english.news.cn/20260618/77b4170f2c984fb6a11ae4f89c677c87/c.html"
    published_at: "2026-06-18T00:00:00.000Z"
    retrieved_at: "2026-06-19T12:03:18+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
