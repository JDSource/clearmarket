---
signal_id: "CMSIG2026062101"
signal_slug: "us-iran-deal-by-june-30-polymarket-51-2026-06-21"
headline: "US-Iran deal by June 30: Polymarket 51%"
semantic_title: "June 30 US-Iran nuclear deal pricing splits at even odds"
telemetry: "Polymarket 51%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-21T04:46:43.000Z"
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
  - "The Polymarket contract sits at 51% on a US-Iran nuclear deal by June 30, essentially a coin-flip with nine days to resolution."
  - "Vance's arrival in Switzerland and the launch of formal talks are consistent with a near-even probability, talks are happening but no framework is confirmed."
  - "The longer-horizon Polymarket contract on a deal before 2027 prices at 71%, indicating markets see the timeline as the main risk, not the deal itself."
  - "Resolution via UMA oracle; the June 30 deadline is hard, and Vance signaled he expects to stay only 'a day or two,' leaving little room for negotiation delays."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US Vice President JD Vance arrived in Switzerland on June 21 to formally launch nuclear negotiations with Iranian officials, seeking to build on a fragile interim ceasefire deal."
    publisher: "ABC News"
    published_at: "2026-06-21T04:46:43.000Z"
    source_url: "https://abcnews.com/US/wireStory/us-vice-president-jd-vance-arrives-switzerland-launch-134069217"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ABC News"
        source_url: "https://abcnews.com/US/wireStory/us-vice-president-jd-vance-arrives-switzerland-launch-134069217"
        retrieved_at: "2026-06-21T11:13:58+00:00"
  - type: "pm_response"
    notes: "Polymarket prices the June 30 deadline at 51% versus 71% for the broader 2027 horizon, a 20-point spread that captures pure deadline risk on these talks."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ABC News: US Vice President JD Vance arrives in Switzerland to launch talks with"
    url: "https://abcnews.com/US/wireStory/us-vice-president-jd-vance-arrives-switzerland-launch-134069217"
    published_at: "2026-06-21T04:46:43.000Z"
    retrieved_at: "2026-06-21T11:13:58+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
