---
signal_id: "CMSIG2026091308"
signal_slug: "strait-of-hormuz-normal-by-dec-31-polymarket-16-2026-09-13"
headline: "Strait of Hormuz normal by Dec 31: Polymarket 16%"
semantic_title: "Hormuz traffic back to normal by year-end stays a long shot"
telemetry: "Polymarket 16%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-13T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.16
  volume_24h_usd: 105650.38211800001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts 16% on Strait of Hormuz traffic returning to normal by December 31, 2026, resolving via UMA oracle."
  - "The breakdown of the Oman-brokered Gulf-Iran talks is consistent with the market's heavy skepticism on normalization within the year."
  - "An Iranian cargo vessel was struck near Qeshm Island on the same day talks collapsed, adding fresh operational risk the market was already pricing."
  - "At 16%, the contract signals the market sees normalization as unlikely absent a major diplomatic breakthrough not yet in sight."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Diplomatic talks on a Hormuz transit framework collapsed after Saudi Arabia called off a high-level Oman-brokered meeting with Iran amid escalating Houthi and militia threats."
    publisher: "Mohammed Ghobari"
    published_at: "2026-09-13T00:00:00.000Z"
    source_url: "https://www.reuters.com/business/energy/diplomacy-stumbles-with-postponement-meeting-strait-hormuz-proposal-2026-09-13/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Mohammed Ghobari"
        source_url: "https://www.reuters.com/business/energy/diplomacy-stumbles-with-postponement-meeting-strait-hormuz-proposal-2026-09-13/"
        retrieved_at: "2026-09-14T14:41:02+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle on whether Hormuz transit volumes return to pre-disruption normal levels before January 1, 2027."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Mohammed Ghobari: Diplomacy stumbles with postponement of meeting on Strait of Hormuz pr"
    url: "https://www.reuters.com/business/energy/diplomacy-stumbles-with-postponement-meeting-strait-hormuz-proposal-2026-09-13/"
    published_at: "2026-09-13T00:00:00.000Z"
    retrieved_at: "2026-09-14T14:41:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
