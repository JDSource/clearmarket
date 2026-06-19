---
signal_id: "CMSIG2026061904"
signal_slug: "us-iran-nuclear-deal-by-jun-30-polymarket-51-2026-06-19"
headline: "US-Iran nuclear deal by Jun 30: Polymarket 51%"
semantic_title: "US-Iran nuclear deal by June 30 pricing wavers at midpoint"
telemetry: "Polymarket 51%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-19T01:36:00.000Z"
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
  - "Polymarket prices the US-Iran nuclear deal at 51% by June 30, a near-coin-flip despite a framework deal being signed."
  - "The Switzerland talks cancellation is consistent with the market's refusal to price a done deal; 49% still prices failure by month-end."
  - "The longer-horizon contract (CM-EVT-VP51KKLQH2) prices 71% for a deal before 2027, showing the market sees eventual resolution but doubts the June 30 deadline."
  - "Uranium enrichment end by July 31 (CM-EVT-8SWDJJDJM0) sits at 29%, revealing deep skepticism about the hardest verification commitments even with a framework in place."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "A US-Iran peace deal was signed June 18, but follow-on Switzerland talks were canceled June 19 as Iran protested Israeli ceasefire violations in Lebanon."
    publisher: "economictimes.indiatimes.com"
    published_at: "2026-06-19T01:36:00.000Z"
    source_url: "https://economictimes.indiatimes.com/news/defence/high-wire-diplomacy-delivered-us-iran-deal-but-hardest-stage-lies-ahead-sources-say/articleshow/131844430.cms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "economictimes.indiatimes.com"
        source_url: "https://economictimes.indiatimes.com/news/defence/high-wire-diplomacy-delivered-us-iran-deal-but-hardest-stage-lies-ahead-sources-say/articleshow/131844430.cms"
        retrieved_at: "2026-06-19T12:03:18+00:00"
  - type: "pm_response"
    notes: "Polymarket resolves via UMA oracle; the 51% price reflects acute deadline risk given the Switzerland cancellation announced June 19."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "economictimes.indiatimes.com: High-wire diplomacy delivered US-Iran deal but hardest stage lies ahea"
    url: "https://economictimes.indiatimes.com/news/defence/high-wire-diplomacy-delivered-us-iran-deal-but-hardest-stage-lies-ahead-sources-say/articleshow/131844430.cms"
    published_at: "2026-06-19T01:36:00.000Z"
    retrieved_at: "2026-06-19T12:03:18+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
