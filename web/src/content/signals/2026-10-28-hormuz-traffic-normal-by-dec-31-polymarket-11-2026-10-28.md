---
signal_id: "CMSIG2026102806"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-11-2026-10-28"
headline: "Hormuz traffic normal by Dec 31: Polymarket 11%"
semantic_title: "Strait of Hormuz returning to normal by year-end stays a long shot"
telemetry: "Polymarket 11%"
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
  current_price: 0.11
  volume_24h_usd: 33233.236623
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 11% on Strait of Hormuz traffic returning to normal by December 31, 2026."
  - "Guardian reporting of active Gulf-state peace diplomacy is a positive signal, but the market remains deeply skeptical of a resolution within the year-end horizon."
  - "A companion Kalshi contract (CM-EVT-34SYT4T2T1) prices only 2% on the US reopening its embassy in Iran, suggesting broader normalization is priced as even more remote."
  - "Resolves via UMA oracle; normal traffic definition and the pace of sanctions-relief talks are the key settlement variables."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Gulf states are working on a multipart peace deal as Iran seeks sanctions relief in exchange for reopening the Strait of Hormuz."
    publisher: "Patrick Wintour"
    published_at: "2026-10-28T00:00:00.000Z"
    source_url: "https://www.theguardian.com/world/2026/oct/28/gulf-states-multipart-peace-deal-avert-renewal-us-iran-war"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Patrick Wintour"
        source_url: "https://www.theguardian.com/world/2026/oct/28/gulf-states-multipart-peace-deal-avert-renewal-us-iran-war"
        retrieved_at: "2026-10-28T07:49:08+00:00"
  - type: "pm_response"
    notes: "Polymarket at 11% is consistent with active but early-stage diplomacy; the market discounts a fast resolution despite Gulf-state mediation efforts."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Patrick Wintour: Gulf states working on multipart peace deal to avert renewal of US-Ira"
    url: "https://www.theguardian.com/world/2026/oct/28/gulf-states-multipart-peace-deal-avert-renewal-us-iran-war"
    published_at: "2026-10-28T00:00:00.000Z"
    retrieved_at: "2026-10-28T07:49:08+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
