---
signal_id: "CMSIG2026102805"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-12-2026-10-28"
headline: "Hormuz traffic normal by Dec 31: Polymarket 12%"
semantic_title: "Strait of Hormuz returning to normal by year-end stays a long shot"
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
  volume_24h_usd: 38113.84703399999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract puts only 12% odds on Strait of Hormuz traffic returning to normal by December 31, 2026."
  - "News of active Gulf mediation efforts has not moved the market above a long-shot read, the Polymarket price implies skepticism that diplomacy can close in weeks."
  - "Iran's rejection of Qatar's seven-day peace plan (Story 25) reinforces the market's low probability; the two data points are directionally consistent."
  - "Companion Polymarket contract CM-EVT-V6DP4NW6X0 puts just 4% on Israel reopening its embassy in Iran by 2026, suggesting the market sees no near-term normalization on any Iran-related track."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Gulf states are working on a multipart peace deal to avert renewed US-Iran conflict, with Iran seeking sanctions relief in exchange for reopening the Strait of Hormuz."
    publisher: "Patrick Wintour"
    published_at: "2026-10-28T00:00:00.000Z"
    source_url: "https://www.theguardian.com/world/2026/oct/28/gulf-states-multipart-peace-deal-avert-renewal-us-iran-war"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Patrick Wintour"
        source_url: "https://www.theguardian.com/world/2026/oct/28/gulf-states-multipart-peace-deal-avert-renewal-us-iran-war"
        retrieved_at: "2026-10-28T15:33:55+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; at 12%, the market is fading the optimism implied by Gulf mediation headlines."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Patrick Wintour: Gulf states working on multipart peace deal to avert renewal of US-Ira"
    url: "https://www.theguardian.com/world/2026/oct/28/gulf-states-multipart-peace-deal-avert-renewal-us-iran-war"
    published_at: "2026-10-28T00:00:00.000Z"
    retrieved_at: "2026-10-28T15:33:55+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
