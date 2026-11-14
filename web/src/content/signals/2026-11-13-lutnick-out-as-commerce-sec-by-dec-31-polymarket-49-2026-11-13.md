---
signal_id: "CMSIG2026111304"
signal_slug: "lutnick-out-as-commerce-sec-by-dec-31-polymarket-49-2026-11-13"
headline: "Lutnick out as Commerce Sec by Dec 31: Polymarket 49%"
semantic_title: "Lutnick departure by year-end holds near 50 percent on Polymarket"
telemetry: "Polymarket 49%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-13T10:00:26.000Z"
event_id: "CM-EVT-H31QLM4JT3"
event_slug: "howard-lutnick-out-as-secretary-of-commerce-by-december-31"
event_question: "Will Howard Lutnick be out as Secretary of Commerce by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x7978663d03b5c053dcea87b39e06fad5bcdd036b0c7febfa4309502c02f70c2c"
  question_raw: "Howard Lutnick out as Secretary of Commerce by December 31?"
  current_price: 0.49
  volume_24h_usd: 100012.461437
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Lutnick leaving as Commerce Secretary by December 31 sits at 49%, essentially a coin flip."
  - "Bessent's on-record criticism of Lutnick's Commerce Department over the Nvidia chip China leakage is a concrete escalation that is consistent with the near-50% market reading."
  - "Lutnick separately agreed to testify before the Senate Banking Committee next month, adding a formal accountability layer that keeps removal odds elevated."
  - "Resolves via UMA oracle; departure must be confirmed by December 31 for a yes settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Treasury Secretary Scott Bessent publicly blamed Commerce Secretary Howard Lutnick's department for Nvidia chip leakage to China, intensifying cabinet tension."
    publisher: "Kevin Breuninger, Lim Hui Jie"
    published_at: "2026-11-13T10:00:26.000Z"
    source_url: "https://www.cnbc.com/2026/11/13/us-inflation-outlook-federal-reserve-rate-hike.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Kevin Breuninger, Lim Hui Jie"
        source_url: "https://www.cnbc.com/2026/11/13/us-inflation-outlook-federal-reserve-rate-hike.html"
        retrieved_at: "2026-11-14T07:47:51+00:00"
  - type: "pm_response"
    notes: "Polymarket at 49% signals genuine two-way uncertainty; the companion unspecified contract (CM-EVT-3BCV214BT2) has no live price to compare."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Kevin Breuninger, Lim Hui Jie: U.S. inflation outlook puts Federal Reserve rate hike in focus"
    url: "https://www.cnbc.com/2026/11/13/us-inflation-outlook-federal-reserve-rate-hike.html"
    published_at: "2026-11-13T10:00:26.000Z"
    retrieved_at: "2026-11-14T07:47:51+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
