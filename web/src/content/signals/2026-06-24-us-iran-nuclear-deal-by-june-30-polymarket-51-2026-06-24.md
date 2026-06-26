---
signal_id: "CMSIG2026062407"
signal_slug: "us-iran-nuclear-deal-by-june-30-polymarket-51-2026-06-24"
headline: "US-Iran nuclear deal by June 30: Polymarket 51%"
semantic_title: "US-Iran nuclear deal by June 30 sits at near coin-flip"
telemetry: "Polymarket 51%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-24T12:32:00.000Z"
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
  - "Polymarket prices 51% on a US-Iran nuclear deal by June 30, effectively a coin-flip with four days left in the window."
  - "IAEA inspections being confirmed is consistent with deal momentum, but the Hormuz drone strike the same day introduces conflicting signals the market has not resolved."
  - "The companion contract on Iran agreeing to end uranium enrichment by June 30 prices at just 24%, showing the market sees process progress but not a full commitment yet."
  - "Resolves via UMA oracle; the enrichment-end-by-July-31 contract at 29% and by-December-31 at 46% indicate the market expects a deal structure, if any, to take months to finalize."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The IAEA chief confirmed nuclear inspectors will visit Iranian sites under a preliminary US-Iran peace agreement."
    publisher: "bbc.co.uk"
    published_at: "2026-06-24T12:32:00.000Z"
    source_url: "https://www.bbc.co.uk/news/articles/cpd395zv81vo"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "bbc.co.uk"
        source_url: "https://www.bbc.co.uk/news/articles/cpd395zv81vo"
        retrieved_at: "2026-06-26T10:48:01+00:00"
  - type: "pm_response"
    notes: "Polymarket's 51% on a June 30 deal sits in tension with the 24% on enrichment cessation, signaling the market prices a partial or framework deal rather than a complete agreement."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "bbc.co.uk: UN nuclear chief says inspectors will visit Iran sites as part of war"
    url: "https://www.bbc.co.uk/news/articles/cpd395zv81vo"
    published_at: "2026-06-24T12:32:00.000Z"
    retrieved_at: "2026-06-26T10:48:01+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
