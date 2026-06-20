---
signal_id: "CMSIG2026061806"
signal_slug: "strait-of-hormuz-traffic-normal-by-dec-31-polymarket-78-2026-06-18"
headline: "Strait of Hormuz traffic normal by Dec 31: Polymarket 78%"
semantic_title: "Hormuz traffic back to normal by year-end hardens above three quarters"
telemetry: "Polymarket 78%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-18T19:20:57.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will traffic through the Strait of Hormuz return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.78
  volume_24h_usd: 289674.7514719999
  arbitration_model: "uma_oracle"
  resolution_source: "portwatch.imf.org"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 78% on Strait of Hormuz traffic returning to normal by December 31, reflecting confidence the blockade removal is durable over a multi-month horizon."
  - "The US military ending the port blockade and the Hormuz reopening are the direct catalysts; the market is broadly consistent with these developments."
  - "The near-term contract on Hormuz returning to normal by end of June (CM-EVT-YPW93GCTK6) is at only 18%, revealing the market sees the physical restoration of full traffic as a weeks-long process despite the political breakthrough."
  - "Resolves via portwatch.imf.org traffic data; measured shipping flow through the Strait, not political announcements, determines settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US lifted its blockade of Iran and the Iranian supreme leader endorsed direct talks with American officials following the June 18 US-Iran peace deal signing."
    publisher: "pbs.org"
    published_at: "2026-06-18T19:20:57.000Z"
    source_url: "https://www.pbs.org/newshour/world/u-s-lifts-blockade-of-iran-and-iranian-supreme-leader-endorses-direct-talks-with-american-officials"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "pbs.org"
        source_url: "https://www.pbs.org/newshour/world/u-s-lifts-blockade-of-iran-and-iranian-supreme-leader-endorses-direct-talks-with-american-officials"
        retrieved_at: "2026-06-20T10:30:38+00:00"
  - type: "pm_response"
    notes: "The 78% year-end versus 18% end-of-June spread is the key term structure signal: political opening is priced, operational normalization is not yet."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "pbs.org: U.S. lifts blockade of Iran and Iranian supreme leader endorses direct"
    url: "https://www.pbs.org/newshour/world/u-s-lifts-blockade-of-iran-and-iranian-supreme-leader-endorses-direct-talks-with-american-officials"
    published_at: "2026-06-18T19:20:57.000Z"
    retrieved_at: "2026-06-20T10:30:38+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
