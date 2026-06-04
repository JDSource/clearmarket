---
signal_id: "CMSIG2026060305"
signal_slug: "iran-oman-hormuz-deal-by-june-15-polymarket-6-2026-06-03"
headline: "Iran-Oman Hormuz deal by June 15: Polymarket 6%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-03T19:00:00.000Z"
event_id: "CM-EVT-974T1626Q2"
event_slug: "iran-x-oman-strait-of-hormuz-agreement-by-june-15"
event_question: "Will Iran and Oman reach an agreement regarding the Strait of Hormuz by June 15?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x27a7a60a3605b0cc0f41f0f243e6be5f2a6144b0adf59fad803fbc1ca6eeb928"
  question_raw: "Iran x Oman Strait of Hormuz agreement by June 15?"
  current_price: 0.06
  volume_24h_usd: 428.79064000000005
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-15T00:00:00Z"
bullets:
  - "Polymarket prices only 6% on an Iran-Oman Strait of Hormuz agreement by June 15."
  - "Escalating strikes near Hormuz are consistent with the very low near-term deal probability on Polymarket."
  - "A companion Polymarket contract prices 13% on unrestricted Iran shipping through Hormuz by June 30, confirming the market sees no quick resolution."
  - "Resolves via uma_oracle based on confirmed public agreement between Iran and Oman by June 15."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran struck Kuwait and the US conducted strikes near the Strait of Hormuz as Middle East conflict intensified."
    publisher: "thenews.pk"
    published_at: "2026-06-03T19:00:00.000Z"
    source_url: "https://www.thenews.pk/print/1418823-me-conflict-surges-as-iran-hits-kuwait-us-strikes-near-hormuz"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "thenews.pk"
        source_url: "https://www.thenews.pk/print/1418823-me-conflict-surges-as-iran-hits-kuwait-us-strikes-near-hormuz"
        retrieved_at: "2026-06-04T11:14:54+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via uma_oracle; the June 15 deadline makes this an extremely short-dated binary."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "thenews.pk: ME conflict surges as Iran hits Kuwait, US strikes near Hormuz"
    url: "https://www.thenews.pk/print/1418823-me-conflict-surges-as-iran-hits-kuwait-us-strikes-near-hormuz"
    published_at: "2026-06-03T19:00:00.000Z"
    retrieved_at: "2026-06-04T11:14:54+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
