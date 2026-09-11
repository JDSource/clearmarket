---
signal_id: "CMSIG2026091105"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-18-2026-09-11"
headline: "Hormuz traffic normal by Dec 31: Polymarket 18%"
semantic_title: "Strait of Hormuz return to normal by year-end stays unlikely"
telemetry: "Polymarket 18%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-11T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.18
  volume_24h_usd: 197591.96454000002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 18% on Strait of Hormuz traffic returning to normal by December 31, 2026."
  - "Houthi seizure of the Bab al-Mandab is a distinct chokepoint from Hormuz, but the combined shipping disruption signals deepening regional instability that is consistent with the low 18% pricing."
  - "Iran hitting a US drone in the Hormuz Strait (Story 27) and 96 vessels diverted adds further evidence the market's skeptical stance reflects current ground truth."
  - "Resolves via UMA oracle; settlement requires documented evidence of normal commercial shipping transit volumes through the Strait of Hormuz."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Houthi forces have completed a takeover of the Bab al-Mandab strait area, seizing a key Red Sea island and threatening Saudi oil export routes."
    publisher: "france24.com"
    published_at: "2026-09-11T00:00:00.000Z"
    source_url: "https://www.france24.com/en/live-news/20260911-yemen-s-houthis-complete-takeover-of-bab-al-mandab-area-govt-official-to-afp"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "france24.com"
        source_url: "https://www.france24.com/en/live-news/20260911-yemen-s-houthis-complete-takeover-of-bab-al-mandab-area-govt-official-to-afp"
        retrieved_at: "2026-09-11T12:32:20+00:00"
  - type: "pm_response"
    notes: "Polymarket at 18% on Hormuz normalization; no intraday price move data available, but the news flow is directionally consistent with the low probability."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "france24.com: Yemen's Houthis complete takeover of Bab al-Mandab area: govt official"
    url: "https://www.france24.com/en/live-news/20260911-yemen-s-houthis-complete-takeover-of-bab-al-mandab-area-govt-official-to-afp"
    published_at: "2026-09-11T00:00:00.000Z"
    retrieved_at: "2026-09-11T12:32:20+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
