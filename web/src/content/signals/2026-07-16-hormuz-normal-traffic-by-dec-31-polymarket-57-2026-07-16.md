---
signal_id: "CMSIG2026071601"
signal_slug: "hormuz-normal-traffic-by-dec-31-polymarket-57-2026-07-16"
headline: "Hormuz normal traffic by Dec 31: Polymarket 57%"
semantic_title: "Strait of Hormuz reopening by year-end wavers amid escalation"
telemetry: "Polymarket 57%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-16T07:06:38.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.57
  volume_24h_usd: 38960.414496
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 57% chance Strait of Hormuz traffic returns to normal by December 31, 2026."
  - "Active US-Iran military exchange, including US naval blockade enforcement and Iranian missile retaliation, is directly consistent with a near-coin-flip on Hormuz normalization."
  - "Iran explicitly naming the Strait a 'red line' raises the stakes for the December resolution window."
  - "A separate Polymarket contract prices only 24% on a full US invasion of Iran, suggesting markets see escalation as bounded, not regime-ending."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US and Iran exchanged escalating military strikes, with Iran calling the Strait of Hormuz a 'red line' as US forces hit targets further north and disabled a blockade-running ship."
    publisher: "bbc.com"
    published_at: "2026-07-16T07:06:38.000Z"
    source_url: "https://www.bbc.com/news/articles/c2lq1ed28jxo"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "bbc.com"
        source_url: "https://www.bbc.com/news/articles/c2lq1ed28jxo"
        retrieved_at: "2026-07-16T17:20:43+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; normalization language and who certifies traffic levels are key settlement edge cases."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "bbc.com: Iran targets military bases as US launches wave of strikes"
    url: "https://www.bbc.com/news/articles/c2lq1ed28jxo"
    published_at: "2026-07-16T07:06:38.000Z"
    retrieved_at: "2026-07-16T17:20:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
