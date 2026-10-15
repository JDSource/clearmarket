---
signal_id: "CMSIG2026101505"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-12-2026-10-15"
headline: "Hormuz traffic normal by Dec 31: Polymarket 12%"
semantic_title: "Strait of Hormuz returning to normal by year-end stays a long shot"
telemetry: "Polymarket 12%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-15T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.12
  volume_24h_usd: 92671.57654499997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Strait of Hormuz traffic returning to normal by December 31 at just 12%, a strong long-shot read."
  - "Two ships sunk in 24 hours and record daily attack levels are fully consistent with this deeply discounted resolution probability."
  - "The 88% implied probability of continued disruption through year-end represents a significant geopolitical risk premium priced into energy transit markets."
  - "The Kalshi ladder on gas prices (CM-EVT-3H5LTWXVM6) showing 50% odds above $4.25 is a correlated cross-market signal that supply disruptions are baked in."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Attacks in the Strait of Hormuz hit their highest daily level since the US-Iran war began, with two ships sunk in 24 hours."
    publisher: "abc.net.au"
    published_at: "2026-10-15T00:00:00.000Z"
    source_url: "https://www.abc.net.au/news/2026-10-15/attacks-in-strait-of-hormuz-reach-highest-daily-level/107269360"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "abc.net.au"
        source_url: "https://www.abc.net.au/news/2026-10-15/attacks-in-strait-of-hormuz-reach-highest-daily-level/107269360"
        retrieved_at: "2026-10-15T13:02:56+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolving via UMA oracle; record attack frequency makes near-term normalization deeply unlikely per current market pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "abc.net.au: Attacks in Strait of Hormuz reach highest daily level since US-Iran wa"
    url: "https://www.abc.net.au/news/2026-10-15/attacks-in-strait-of-hormuz-reach-highest-daily-level/107269360"
    published_at: "2026-10-15T00:00:00.000Z"
    retrieved_at: "2026-10-15T13:02:56+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
