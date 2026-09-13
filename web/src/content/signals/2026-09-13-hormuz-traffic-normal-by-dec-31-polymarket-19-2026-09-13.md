---
signal_id: "CMSIG2026091306"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-19-2026-09-13"
headline: "Hormuz traffic normal by Dec 31: Polymarket 19%"
semantic_title: "Strait of Hormuz traffic returning to normal by year-end stays unlikely"
telemetry: "Polymarket 19%"
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
  current_price: 0.19
  volume_24h_usd: 93595.924259
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract prices Strait of Hormuz traffic returning to normal by December 31 at 19%, resolving via UMA oracle."
  - "Fresh attack reports on Hormuz shipping are consistent with the market's heavily skeptical stance on near-term normalization."
  - "A parallel Saudi pipeline attack blamed on Iran-backed Iraqi militias (Story 29) adds further regional supply disruption context that reinforces the low normalization probability."
  - "Houthi advances in Yemen (Story 22) compound the threat picture; the market's 19% is pricing persistent, multi-front pressure on regional shipping lanes through year-end."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "New reports of attacks on Strait of Hormuz shipping are fanning fears about threats to global oil supplies."
    publisher: "al-monitor.com"
    published_at: "2026-09-13T00:00:00.000Z"
    source_url: "https://www.al-monitor.com/originals/2026/09/new-report-attack-strait-hormuz-shipping-fans-fears-threats-oil-supplies"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "al-monitor.com"
        source_url: "https://www.al-monitor.com/originals/2026/09/new-report-attack-strait-hormuz-shipping-fans-fears-threats-oil-supplies"
        retrieved_at: "2026-09-13T13:04:33+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; 'normal' traffic likely requires a verified return to pre-disruption transit volumes, a high bar given current multi-actor pressure."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "al-monitor.com: New report of attack on Strait of Hormuz shipping fans fears of threat"
    url: "https://www.al-monitor.com/originals/2026/09/new-report-attack-strait-hormuz-shipping-fans-fears-threats-oil-supplies"
    published_at: "2026-09-13T00:00:00.000Z"
    retrieved_at: "2026-09-13T13:04:33+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
