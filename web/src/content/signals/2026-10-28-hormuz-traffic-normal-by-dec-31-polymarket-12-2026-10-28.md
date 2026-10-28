---
signal_id: "CMSIG2026102804"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-12-2026-10-28"
headline: "Hormuz traffic normal by Dec 31: Polymarket 12%"
semantic_title: "Strait of Hormuz return to normal by year-end stays a long shot"
telemetry: "Polymarket 12%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-28T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.12
  volume_24h_usd: 38113.847034
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Hormuz traffic returning to normal by December 31 sits at 12%, resolving via uma_oracle."
  - "The Guardian reports Iran wants firm sanctions relief guarantees before reopening the strait; the 12% probability reflects the market treating a year-end resolution as unlikely."
  - "Despite active Gulf-state diplomacy, Polymarket is not pricing in a near-term breakthrough, keeping the contract deep in long-shot territory."
  - "The Kalshi contract on the US reopening its embassy in Iran (CM-EVT-CM-EVT-34SYT4T2T1) is at 2%, signaling the market sees no comprehensive normalization in sight either."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Gulf states are working on a multipart peace deal with Iran, which is seeking sanctions relief in exchange for reopening the Strait of Hormuz."
    publisher: "Patrick Wintour"
    published_at: "2026-10-28T00:00:00.000Z"
    source_url: "https://www.theguardian.com/world/2026/oct/28/gulf-states-multipart-peace-deal-avert-renewal-us-iran-war"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Patrick Wintour"
        source_url: "https://www.theguardian.com/world/2026/oct/28/gulf-states-multipart-peace-deal-avert-renewal-us-iran-war"
        retrieved_at: "2026-10-28T14:49:33+00:00"
  - type: "pm_response"
    notes: "Polymarket at 12% on Hormuz normalization by year-end reflects skepticism that ongoing Gulf-state mediation will produce a binding deal within the 2026 calendar year."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Patrick Wintour: Gulf states working on multipart peace deal to avert renewal of US-Ira"
    url: "https://www.theguardian.com/world/2026/oct/28/gulf-states-multipart-peace-deal-avert-renewal-us-iran-war"
    published_at: "2026-10-28T00:00:00.000Z"
    retrieved_at: "2026-10-28T14:49:33+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
