---
signal_id: "CMSIG2026061603"
signal_slug: "us-iran-nuclear-deal-by-june-30-polymarket-51-2026-06-16"
headline: "US-Iran nuclear deal by June 30: Polymarket 51%"
semantic_title: "US-Iran nuclear deal by June 30 wavers at even odds"
telemetry: "Polymarket 51%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-16T06:36:41.000Z"
event_id: "CM-EVT-LG47Z78CF2"
event_slug: "us-iran-nuclear-deal-by-june-30"
event_question: "Will the US and Iran reach a nuclear deal by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa70fc3695a65833b91b45df6db6015096f3e1471b70352ca411b4209010e7633"
  question_raw: "US-Iran nuclear deal by June 30?"
  current_price: 0.51
  volume_24h_usd: 1088905.717404001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices the US-Iran nuclear deal by June 30 at 51%, essentially a coin flip despite deal momentum headlines."
  - "News of a tentative memorandum of understanding is consistent with the near-50% pricing; markets are treating signing and full implementation as genuinely uncertain."
  - "The July 31 deadline contract on Polymarket sits at 59%, showing markets give meaningful extra probability to an 8-week slippage in formalization."
  - "Resolves via UMA oracle; the June 30 contract has only 13 days of runway, a tight window that explains why even positive headlines cannot push probability above 51%."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Al-Monitor reports a US-Iran deal promising an end to the war has emerged but implementation details remain murky ahead of a signing ceremony."
    publisher: "al-monitor.com"
    published_at: "2026-06-16T06:36:41.000Z"
    source_url: "https://www.al-monitor.com/originals/2026/06/us-iran-deal-promises-end-war-how-it-will-work-remains-unclear"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "al-monitor.com"
        source_url: "https://www.al-monitor.com/originals/2026/06/us-iran-deal-promises-end-war-how-it-will-work-remains-unclear"
        retrieved_at: "2026-06-17T12:13:58+00:00"
  - type: "pm_response"
    notes: "Polymarket's 51% on June 30 versus 59% on July 31 reveals a clear term-structure discount for near-term signing risk."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "al-monitor.com: US-Iran deal promises end to war but how it will work remains unclear"
    url: "https://www.al-monitor.com/originals/2026/06/us-iran-deal-promises-end-war-how-it-will-work-remains-unclear"
    published_at: "2026-06-16T06:36:41.000Z"
    retrieved_at: "2026-06-17T12:13:58+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
