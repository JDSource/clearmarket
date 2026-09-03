---
signal_id: "CMSIG2026090304"
signal_slug: "hormuz-normal-by-dec-31-polymarket-27-2026-09-03"
headline: "Hormuz normal by Dec 31: Polymarket 27%"
semantic_title: "Strait of Hormuz normal traffic by year-end stays below 30%"
telemetry: "Polymarket 27%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-03T01:45:32.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.27
  volume_24h_usd: 169722.21541899996
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Strait of Hormuz traffic returning to normal by December 31 sits at 27%, reflecting the market's skepticism about near-term de-escalation."
  - "Active US-Iran military exchanges, including Iranian attacks on US bases in Kuwait, are consistent with the market's sub-30% probability on restored waterway traffic."
  - "Trump's claim that the US controls the Strait of Hormuz stands in tension with Iran's continued ability to strike regional targets, which the 27% price reflects."
  - "Resolution depends on an independently verified return to normal Strait of Hormuz transit volumes by December 31, 2026, with no named resolution source specified."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump threatened further strikes on Iran and US forces conducted a second round of attacks in three days on radar and mine-laying systems, while Iran struck US bases in Kuwait with drones and missiles."
    publisher: "Ali Mustafa"
    published_at: "2026-09-03T01:45:32.000Z"
    source_url: "https://www.aljazeera.com/news/2026/9/3/trump-threatens-more-strikes-as-death-toll-in-iran-rises-to-19"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Ali Mustafa"
        source_url: "https://www.aljazeera.com/news/2026/9/3/trump-threatens-more-strikes-as-death-toll-in-iran-rises-to-19"
        retrieved_at: "2026-09-03T12:30:58+00:00"
  - type: "pm_response"
    notes: "The Polymarket contract at 27% is the only priced candidate across multiple Iran-Hormuz stories; all related contracts lack disclosed prices."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Ali Mustafa: Trump threatens more strikes as death toll in Iran rises to 18 | News"
    url: "https://www.aljazeera.com/news/2026/9/3/trump-threatens-more-strikes-as-death-toll-in-iran-rises-to-19"
    published_at: "2026-09-03T01:45:32.000Z"
    retrieved_at: "2026-09-03T12:30:58+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
