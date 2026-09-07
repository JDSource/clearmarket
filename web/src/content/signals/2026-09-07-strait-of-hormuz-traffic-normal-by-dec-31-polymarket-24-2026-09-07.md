---
signal_id: "CMSIG2026090707"
signal_slug: "strait-of-hormuz-traffic-normal-by-dec-31-polymarket-24-2026-09-07"
headline: "Strait of Hormuz traffic normal by Dec 31: Polymarket 24%"
semantic_title: "Hormuz traffic returning to normal by year-end stays below 25%"
telemetry: "Polymarket 24%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-07T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.24
  volume_24h_usd: 80563.411292
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Strait of Hormuz traffic returning to normal by December 31 at 24%, a long shot."
  - "Iran's announcement of an expanded exclusion zone is directionally consistent with the low normalization probability, the market is not pricing a quick resolution."
  - "A companion ladder (CM-EVT-JR1WTQ5JH0) shows only 25% probability of the 7-day moving average of Hormuz transit calls reaching 40 or above, with volume up 34,298% day-over-day, flagging surging attention to this contract."
  - "Polymarket resolves via UMA oracle; the December 31 deadline leaves limited runway given Iran's stated intention to formalize the restricted zone in coming days."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran announced plans to establish a new restricted zone near the Strait of Hormuz and said passage route maps would be approved imminently, escalating maritime tension with the US."
    publisher: "channelnewsasia.com"
    published_at: "2026-09-07T00:00:00.000Z"
    source_url: "https://www.channelnewsasia.com/world/iran-us-gulf-new-restricted-zone-hormuz-6366526"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "channelnewsasia.com"
        source_url: "https://www.channelnewsasia.com/world/iran-us-gulf-new-restricted-zone-hormuz-6366526"
        retrieved_at: "2026-09-07T13:54:18+00:00"
  - type: "pm_response"
    notes: "The Polymarket 24% normalization contract and the transit-volume ladder both reflect the same hawkish Hormuz read; the 34,298% volume surge in the ladder is the standout activity signal today."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "channelnewsasia.com: Iran says to announce new restricted zone in the Gulf in the coming da"
    url: "https://www.channelnewsasia.com/world/iran-us-gulf-new-restricted-zone-hormuz-6366526"
    published_at: "2026-09-07T00:00:00.000Z"
    retrieved_at: "2026-09-07T13:54:18+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
