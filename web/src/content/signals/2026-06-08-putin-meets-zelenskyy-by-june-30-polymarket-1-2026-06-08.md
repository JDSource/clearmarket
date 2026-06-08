---
signal_id: "CMSIG2026060806"
signal_slug: "putin-meets-zelenskyy-by-june-30-polymarket-1-2026-06-08"
headline: "Putin meets Zelenskyy by June 30: Polymarket 1%"
semantic_title: "Putin-Zelenskyy June 30 meeting nears zero pricing"
telemetry: "Polymarket 1%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-08T00:00:00.000Z"
event_id: "CM-EVT-2DR1P4YZ13"
event_slug: "will-putin-meet-with-zelenskyy-by-june-30-2026"
event_question: "Will Putin meet with Zelenskyy by June 30, 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xc5ab3fb332af0bebf7ed6df1b1d5e1cc32a91e960c57d7602a5224830cf0084b"
  question_raw: "Will Putin meet with Zelenskyy by June 30, 2026?"
  current_price: 0.011
  volume_24h_usd: 535.846363
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices just 1% on Putin meeting Zelenskyy before June 30, near-zero despite E3 diplomatic backing."
  - "Western leaders' endorsement of the call for talks has not shifted prediction market pricing; markets price the meeting as essentially impossible this month."
  - "A longer-horizon ceasefire contract (CM-EVT-LVRHCH4653) sits at 49% for a Russia-Ukraine ceasefire by December 31, 2026, showing markets are open to a deal but not on a June timeline."
  - "Resolves via UMA oracle on a confirmed in-person bilateral meeting between the two heads of state before June 30."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "UK, France, and Germany backed Zelenskyy's call for direct talks with Putin after a meeting in London on June 7."
    publisher: "Euractiv"
    published_at: "2026-06-08T00:00:00.000Z"
    source_url: "https://www.euractiv.com/news/uk-france-germany-back-zelenskyys-call-for-putin-meeting/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Euractiv"
        source_url: "https://www.euractiv.com/news/uk-france-germany-back-zelenskyys-call-for-putin-meeting/"
        retrieved_at: "2026-06-08T12:25:51+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; the 1% near-June-30 print versus 49% end-of-year ceasefire probability reveals the market prices a longer diplomatic runway."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Euractiv: UK, France, Germany back Zelenskyy's call for Putin meeting | Euractiv"
    url: "https://www.euractiv.com/news/uk-france-germany-back-zelenskyys-call-for-putin-meeting/"
    published_at: "2026-06-08T00:00:00.000Z"
    retrieved_at: "2026-06-08T12:25:51+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
