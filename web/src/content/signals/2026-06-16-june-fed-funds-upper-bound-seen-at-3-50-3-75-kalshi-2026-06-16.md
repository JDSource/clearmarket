---
signal_id: "CMSIG2026061602"
signal_slug: "june-fed-funds-upper-bound-seen-at-3-50-3-75-kalshi-2026-06-16"
headline: "June Fed funds upper bound seen at 3.50-3.75%: Kalshi"
semantic_title: "June Fed funds upper bound pricing clusters at 3.50 to 3.75 percent"
telemetry: "Kalshi ladder"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-06-16T04:03:15.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "June 2026 Fed funds upper bound"
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
  - "Kalshi ladder pins the June 2026 Fed funds upper bound in the 3.50-3.75% range: 95% above 3.50% but only 36% above 3.75%."
  - "Current Fed funds target is 4.25-4.50%; the ladder implies markets price in significant cuts by the end of this rate cycle, well below Warsh's debut level."
  - "PGIM separately argues the market-implied rate path is underpriced, suggesting the current ladder distribution may be too dovish."
  - "A companion ladder (CM-EVT-PHWX2H6DM5) shows nearly identical distribution, corroborating the 3.50-3.75% implied range with high cross-market consistency."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Kevin Warsh chairs his first Fed meeting Wednesday with markets watching for rate-path signals amid elevated inflation."
    publisher: "CHRISTOPHER RUGABER — AP Economics Writer"
    published_at: "2026-06-16T04:03:15.000Z"
    source_url: "https://www.wral.com/news/ap/9a65c-all-eyes-turn-to-fed-chair-kevin-warsh-and-his-first-moves-on-interest-rates/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "CHRISTOPHER RUGABER — AP Economics Writer"
        source_url: "https://www.wral.com/news/ap/9a65c-all-eyes-turn-to-fed-chair-kevin-warsh-and-his-first-moves-on-interest-rates/"
        retrieved_at: "2026-06-16T12:50:14+00:00"
  - type: "pm_response"
    notes: "Two Kalshi ladders converge on the same 3.50-3.75% implied endpoint, reinforcing the distribution read without contradicting the June hold contract."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "CHRISTOPHER RUGABER, AP Economics Writer: All eyes turn to Fed chair Kevin Warsh and his first moves on interest"
    url: "https://www.wral.com/news/ap/9a65c-all-eyes-turn-to-fed-chair-kevin-warsh-and-his-first-moves-on-interest-rates/"
    published_at: "2026-06-16T04:03:15.000Z"
    retrieved_at: "2026-06-16T12:50:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
