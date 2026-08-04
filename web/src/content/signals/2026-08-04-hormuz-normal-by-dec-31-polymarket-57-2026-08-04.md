---
signal_id: "CMSIG2026080406"
signal_slug: "hormuz-normal-by-dec-31-polymarket-57-2026-08-04"
headline: "Hormuz normal by Dec 31: Polymarket 57%"
semantic_title: "Hormuz back to normal by year-end holds near 50-50"
telemetry: "Polymarket 57%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-04T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.57
  volume_24h_usd: 101843.33134399998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket contract prices Strait of Hormuz traffic returning to normal by December 31 at 57%."
  - "Contradictory US-Iran accounts on talks and a fresh cargo ship strike are consistent with the market holding near 50-50 rather than pricing a clean resolution."
  - "The market is not deeply discounting the year-end normalization scenario despite the striking divergence in official narratives."
  - "Resolution: Polymarket UMA oracle settles based on whether Strait of Hormuz traffic objectively returns to pre-conflict normal levels by December 31."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US-Iran talks remain uncertain after a cargo ship was struck in the Strait of Hormuz and Tehran denied accounts given by Washington about ongoing negotiations."
    publisher: "al-monitor.com"
    published_at: "2026-08-04T00:00:00.000Z"
    source_url: "https://www.al-monitor.com/originals/2026/08/status-us-iran-talks-uncertain-ship-struck-hormuz"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "al-monitor.com"
        source_url: "https://www.al-monitor.com/originals/2026/08/status-us-iran-talks-uncertain-ship-struck-hormuz"
        retrieved_at: "2026-08-04T10:33:12+00:00"
  - type: "pm_response"
    notes: "Polymarket sits at 57%, barely above even odds, reflecting genuine strategic uncertainty on the Hormuz standoff timeline."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "al-monitor.com: Status of US-Iran talks uncertain as ship struck in Hormuz - AL-MONITO"
    url: "https://www.al-monitor.com/originals/2026/08/status-us-iran-talks-uncertain-ship-struck-hormuz"
    published_at: "2026-08-04T00:00:00.000Z"
    retrieved_at: "2026-08-04T10:33:12+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
