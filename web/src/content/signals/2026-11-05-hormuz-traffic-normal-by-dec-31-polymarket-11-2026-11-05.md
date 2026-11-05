---
signal_id: "CMSIG2026110505"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-11-2026-11-05"
headline: "Hormuz traffic normal by Dec 31: Polymarket 11%"
semantic_title: "Strait of Hormuz traffic returning to normal by year-end stays a long shot"
telemetry: "Polymarket 11%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-05T04:27:05.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.11
  volume_24h_usd: 277334.547406
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract puts only 11% odds on Strait of Hormuz traffic returning to normal by December 31."
  - "Active IRGC operations in the strait, including tanker fires reported today, are consistent with the market's low-probability read on near-term normalization."
  - "The separate Polymarket contract on the Iranian regime falling before 2027 sits at just 3%, suggesting the market sees neither a quick end to the conflict nor a regime collapse as likely."
  - "Resolves via Polymarket's UMA oracle; definition of 'normal traffic' is the key settlement edge case given disputed reporting on transit volumes."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran's IRGC claimed two tankers and a tugboat caught fire in the Strait of Hormuz amid the ongoing U.S.-Iran war, with oil prices below $95 a barrel."
    publisher: "The National"
    published_at: "2026-11-05T04:27:05.000Z"
    source_url: "https://www.thenationalnews.com/news/mena/2026/11/05/live-iran-war-irgc-strait-of-hormuz/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "The National"
        source_url: "https://www.thenationalnews.com/news/mena/2026/11/05/live-iran-war-irgc-strait-of-hormuz/"
        retrieved_at: "2026-11-05T07:48:08+00:00"
  - type: "pm_response"
    notes: "Polymarket prices Hormuz normalization by year-end at just 11%, consistent with continued active conflict and no sign of ceasefire talks bearing fruit."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "The National: Iran war latest: IRGC claims two tankers and tugboat caught fire in St"
    url: "https://www.thenationalnews.com/news/mena/2026/11/05/live-iran-war-irgc-strait-of-hormuz/"
    published_at: "2026-11-05T04:27:05.000Z"
    retrieved_at: "2026-11-05T07:48:08+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
