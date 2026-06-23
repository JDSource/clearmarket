---
signal_id: "CMSIG2026062301"
signal_slug: "us-iran-nuclear-deal-by-june-30-polymarket-51-2026-06-23"
headline: "US-Iran nuclear deal by June 30: Polymarket 51%"
semantic_title: "US-Iran nuclear deal by June 30 sits near coin-flip pricing"
telemetry: "Polymarket 51%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-23T02:58:29.000Z"
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
  - "Polymarket prices a US-Iran nuclear deal by June 30 at 51%, essentially a coin flip."
  - "Vance's 'good foundation' language and US sanctions waiver are consistent with the near-even odds, but Iran's denial of enrichment concessions keeps the market from pricing higher."
  - "The companion Polymarket contract on a deal before 2027 sits at 71%, showing the market assigns strong odds eventually but doubts the June 30 deadline specifically."
  - "Resolves via UMA oracle; any ambiguity over what constitutes a 'nuclear deal' versus a framework MoU could be a settlement edge case."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US Vice President JD Vance said Switzerland talks laid a 'good foundation' for a final deal as the US waived Iran sanctions, though Iran denied halting uranium enrichment."
    publisher: "cnbctv18.com"
    published_at: "2026-06-23T02:58:29.000Z"
    source_url: "https://www.cnbctv18.com/world/us-waives-iran-sanctions-after-talks-lebanon-fighting-abates-19930304.htm"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cnbctv18.com"
        source_url: "https://www.cnbctv18.com/world/us-waives-iran-sanctions-after-talks-lebanon-fighting-abates-19930304.htm"
        retrieved_at: "2026-06-23T10:59:18+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 51% reflects near-term deadline uncertainty despite diplomatic progress, with the longer 2027 horizon priced at 71%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cnbctv18.com: US waives Iran sanctions after talks; Lebanon fighting abates - CNBC T"
    url: "https://www.cnbctv18.com/world/us-waives-iran-sanctions-after-talks-lebanon-fighting-abates-19930304.htm"
    published_at: "2026-06-23T02:58:29.000Z"
    retrieved_at: "2026-06-23T10:59:18+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
