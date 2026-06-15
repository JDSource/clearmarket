---
signal_id: "CMSIG2026061501"
signal_slug: "us-iran-nuclear-deal-by-june-30-polymarket-51-2026-06-15"
headline: "US-Iran nuclear deal by June 30: Polymarket 51%"
semantic_title: "US-Iran nuclear deal by June 30 holds at coin-flip pricing"
telemetry: "Polymarket 51%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-15T08:23:00.000Z"
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
  - "Polymarket prices the US-Iran nuclear deal by June 30 at 51%, a near-even split despite deal announcement headlines."
  - "Pakistan announced a breakthrough ceasefire with Hormuz reopening June 19, yet the Polymarket contract barely clears 50%, signaling the market distinguishes a ceasefire from a formal nuclear deal."
  - "The July 31 companion Polymarket contract sits at 59%, suggesting markets see the nuclear terms resolving later than the ceasefire, not by month-end."
  - "Resolution is via UMA oracle; whether a ceasefire agreement qualifies as a nuclear deal under contract terms is the key settlement question."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Pakistan brokered a US-Iran agreement announcing immediate permanent cessation of military operations and reopening of the Strait of Hormuz by June 19."
    publisher: "geo.tv"
    published_at: "2026-06-15T08:23:00.000Z"
    source_url: "https://www.geo.tv/latest/668790-iran-us-agree-to-halt-war-and-reopen-hormuz-sending-oil-prices-tumbling"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "geo.tv"
        source_url: "https://www.geo.tv/latest/668790-iran-us-agree-to-halt-war-and-reopen-hormuz-sending-oil-prices-tumbling"
        retrieved_at: "2026-06-15T13:51:44+00:00"
  - type: "pm_response"
    notes: "Polymarket at 51% shows the market is treating the ceasefire and nuclear deal as distinct events, consistent with contract wording that likely requires formal nuclear terms."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "geo.tv: Pakistan-mediated breakthrough: US, Iran agree to halt war, reopen Hor"
    url: "https://www.geo.tv/latest/668790-iran-us-agree-to-halt-war-and-reopen-hormuz-sending-oil-prices-tumbling"
    published_at: "2026-06-15T08:23:00.000Z"
    retrieved_at: "2026-06-15T13:51:44+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
