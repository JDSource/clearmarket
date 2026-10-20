---
signal_id: "CMSIG2026101908"
signal_slug: "strait-of-hormuz-traffic-normal-by-dec-31-polymarket-12-2026-10-19"
headline: "Strait of Hormuz traffic normal by Dec 31: Polymarket 12%"
semantic_title: "Strait of Hormuz traffic returning to normal by year-end stays near 12 percent"
telemetry: "Polymarket 12%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-19T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.12
  volume_24h_usd: 205045.87494
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket prediction market prices only 12% odds on Strait of Hormuz traffic returning to normal by December 31, 2026."
  - "The Houthi escalation story is consistent with the market's skeptical pricing: a normal-traffic outcome by year-end is treated as a long shot."
  - "Story 22 reported Iran saying the Strait is reopening, yet a 12% Polymarket probability shows the market is not treating that statement as credible or durable."
  - "Resolution via UMA oracle; the 88% probability of continued disruption through year-end carries direct implications for oil price and shipping cost markets."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "A Dhaka Tribune analysis warns that Houthi escalation is exposing the limits of Saudi military power and raising security risks across shipping lanes in the Middle East."
    publisher: "Nasir Uddin Ahmed"
    published_at: "2026-10-19T00:00:00.000Z"
    source_url: "https://www.thedailystar.net/slow-reads/geopolitical-insights/news/the-houthis-wont-back-down-what-does-it-mean-bangladesh-4301851"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Nasir Uddin Ahmed"
        source_url: "https://www.thedailystar.net/slow-reads/geopolitical-insights/news/the-houthis-wont-back-down-what-does-it-mean-bangladesh-4301851"
        retrieved_at: "2026-10-20T07:47:27+00:00"
  - type: "pm_response"
    notes: "Polymarket binary at 12%; the gap between Iran's reopening claim (Story 22) and the market's 12% recovery odds is the sharpest news-versus-price divergence in this data set."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Nasir Uddin Ahmed: The Houthis won't back down, but what does it mean for Bangladesh?"
    url: "https://www.thedailystar.net/slow-reads/geopolitical-insights/news/the-houthis-wont-back-down-what-does-it-mean-bangladesh-4301851"
    published_at: "2026-10-19T00:00:00.000Z"
    retrieved_at: "2026-10-20T07:47:27+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
