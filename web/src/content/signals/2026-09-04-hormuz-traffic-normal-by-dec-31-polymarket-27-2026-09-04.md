---
signal_id: "CMSIG2026090406"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-27-2026-09-04"
headline: "Hormuz traffic normal by Dec 31: Polymarket 27%"
semantic_title: "Strait of Hormuz traffic back to normal by year-end below 50%"
telemetry: "Polymarket 27%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-04T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.27
  volume_24h_usd: 36353.626658
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts only 27% on Strait of Hormuz traffic returning to normal by December 31, 2026, a strong long-shot read."
  - "Active Iran-US military exchanges and VP Vance's ultimatum framing suggest further disruption, consistent with the below-30% pricing."
  - "Iran's strikes on US bases in Kuwait and the UAE, alongside Hormuz attack warnings, make near-term normalization of shipping traffic appear unlikely to the market."
  - "Polymarket contract resolves via UMA oracle; 'normal' traffic likely benchmarked to pre-conflict transit levels, making the resolution bar concrete but potentially disputed."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran struck US military targets in Kuwait and the UAE in retaliation for a deadly wedding strike it blamed on Washington, while US Vice President JD Vance called on Tehran to stop attacks on commercial shipping through the Strait of Hormuz."
    publisher: "nation.com.pk"
    published_at: "2026-09-04T00:00:00.000Z"
    source_url: "https://www.nation.com.pk/04-Sep-2026/iran-targets-kuwait-us-vp-advises-tehran-stop-hormuz-attacks"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "nation.com.pk"
        source_url: "https://www.nation.com.pk/04-Sep-2026/iran-targets-kuwait-us-vp-advises-tehran-stop-hormuz-attacks"
        retrieved_at: "2026-09-04T12:28:22+00:00"
  - type: "pm_response"
    notes: "Polymarket hosts this Hormuz normalization contract; at 27%, the market is pricing continued disruption as the dominant scenario through year-end."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "nation.com.pk: Iran targets Kuwait as US VP advises Tehran to stop Hormuz attacks"
    url: "https://www.nation.com.pk/04-Sep-2026/iran-targets-kuwait-us-vp-advises-tehran-stop-hormuz-attacks"
    published_at: "2026-09-04T00:00:00.000Z"
    retrieved_at: "2026-09-04T12:28:22+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
