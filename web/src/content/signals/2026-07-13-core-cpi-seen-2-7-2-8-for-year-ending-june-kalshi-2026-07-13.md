---
signal_id: "CMSIG2026071302"
signal_slug: "core-cpi-seen-2-7-2-8-for-year-ending-june-kalshi-2026-07-13"
headline: "Core CPI seen 2.7-2.8% for year ending June: Kalshi"
semantic_title: "Core CPI pricing anchors near 2.7-2.8 percent ahead of hot print"
telemetry: "Kalshi ladder"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-07-13T02:15:46.000Z"
event_id: "CM-EVT-B5KCGZG8C0"
event_slug: "kxcpicoreyoy-26jun"
event_question: "Core CPI year-over-year rate, year ending June 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPICOREYOY-26JUN-T2.8"
  question_raw: "Will the rate of core CPI inflation be above 2.8% for the year ending in June 2026?"
  current_price: 0.33
  volume_24h_usd: 599.5
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-07-21T14:00:00Z"
bullets:
  - "Kalshi prices core CPI for the year ending June 2026 in the 2.7-2.8% range: 85% above 2.7% but only 33% above 2.8%, a tight distribution around a modest level."
  - "The 4.2% headline CPI print through May reflects tariff and energy pass-through; the market's core reading of roughly 2.75% suggests tariff effects are seen as transitory in core."
  - "The gap between a 4.2% headline and a sub-3% core implied by this ladder is the crux of the Fed policy debate, and the market is not pricing a core breakout."
  - "Resolves via Bureau of Labor Statistics CPI release; any core print at or above 2.9% would sharply compress the current 3% tail, now priced at just 3%."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Headline CPI hit 4.2% year-over-year through May 2026, the hottest in three years, with the June CPI report releasing today seen as a potential catalyst for a Fed rate hike."
    publisher: "Warren Cohen"
    published_at: "2026-07-13T02:15:46.000Z"
    source_url: "https://thefinancialwire.com/the-may-inflation-reading-hit-4-2-the-hottest-in-three-years-and-a-july-14-report-could-sway-the-fed/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Warren Cohen"
        source_url: "https://thefinancialwire.com/the-may-inflation-reading-hit-4-2-the-hottest-in-three-years-and-a-july-14-report-could-sway-the-fed/"
        retrieved_at: "2026-07-14T09:54:27+00:00"
  - type: "pm_response"
    notes: "Kalshi's core CPI ladder is concentrated well below the 4.2% headline, reflecting a market read that strips out tariff-driven components."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Warren Cohen: The May inflation reading hit 4.2%, the hottest in three years, and a"
    url: "https://thefinancialwire.com/the-may-inflation-reading-hit-4-2-the-hottest-in-three-years-and-a-july-14-report-could-sway-the-fed/"
    published_at: "2026-07-13T02:15:46.000Z"
    retrieved_at: "2026-07-14T09:54:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
