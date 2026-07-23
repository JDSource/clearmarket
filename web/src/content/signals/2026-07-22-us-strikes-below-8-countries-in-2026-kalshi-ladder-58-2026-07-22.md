---
signal_id: "CMSIG2026072203"
signal_slug: "us-strikes-below-8-countries-in-2026-kalshi-ladder-58-2026-07-22"
headline: "US strikes below 8 countries in 2026: Kalshi ladder 58%"
semantic_title: "US strikes fewer than 8 countries in 2026 stays favored"
telemetry: "Polymarket ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-22T00:00:00.000Z"
event_id: "CM-EVT-5855JBL478"
event_slug: "how-many-different-countries-will-the-us-strike-in-2026"
event_question: "Number of countries struck by US in 2026"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x713ab27f31c1d8080ea3b9c21c8a021609f8fcb7aad13a87b8b069265e7fdfda"
  question_raw: "Will the US strike 8 countries in 2026?"
  current_price: 0.419
  volume_24h_usd: 189.606267
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Kalshi ladder prices 42% that the US strikes 8 or more countries in 2026, with volume up 9,312% day over day, the highest activity signal in today's data set."
  - "Ongoing US strikes on Iran plus Houthi-linked Red Sea activity are driving fresh attention to this contract, reflected in the extraordinary volume surge."
  - "The sharp drop-off above 8 countries (42%) versus above 9 countries (30%) shows the market concentrating risk at exactly the 8-country threshold."
  - "Resolves via the named person or source; the counting methodology, what constitutes a distinct 'country struck', is the decisive settlement edge."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US and Iranian attacks continued as tensions mounted on the Red Sea, with the conflict expanding to involve Houthi attacks on Saudi vessels."
    publisher: "kpbs.org"
    published_at: "2026-07-22T00:00:00.000Z"
    source_url: "https://www.kpbs.org/news/international/2026/07/22/u-s-and-iranian-attacks-continue-as-tensions-mount-on-a-key-waterway-in-the-red-sea"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "kpbs.org"
        source_url: "https://www.kpbs.org/news/international/2026/07/22/u-s-and-iranian-attacks-continue-as-tensions-mount-on-a-key-waterway-in-the-red-sea"
        retrieved_at: "2026-07-23T10:16:46+00:00"
  - type: "pm_response"
    notes: "The 9,312% volume surge on the Kalshi 'countries struck' ladder is the strongest day-over-day activity signal in today's data, flagging live market attention to escalation scope."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "kpbs.org: U.S. and Iranian attacks continue as tensions mount on a key waterway"
    url: "https://www.kpbs.org/news/international/2026/07/22/u-s-and-iranian-attacks-continue-as-tensions-mount-on-a-key-waterway-in-the-red-sea"
    published_at: "2026-07-22T00:00:00.000Z"
    retrieved_at: "2026-07-23T10:16:46+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
