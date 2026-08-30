---
signal_id: "CMSIG2026083008"
signal_slug: "venezuela-crude-output-above-1-2m-bpd-in-2026-kalshi-style-l-2026-08-30"
headline: "Venezuela crude output above 1.2M bpd in 2026: Kalshi-style ladder 77%"
semantic_title: "Venezuelan crude output reaching 1.2 million barrels a day stays favored"
telemetry: "Polymarket ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-30T00:00:00.000Z"
event_id: "CM-EVT-WL6DTZN086"
event_slug: "will-venezuelan-crude-oil-production-reach-barrels-per-day-in-2026"
event_question: "Venezuelan crude oil production 2026 (barrels per day)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x59bb2cc4b116c5137e858222c867638bcd78b236db7656adf93114fcdf62b902"
  question_raw: "Will Venezuelan crude oil production reach 1.3m barrels per day in 2026?"
  current_price: 0.13
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolution_source: "opec.org"
  resolves_at: "2027-02-28T00:00:00Z"
bullets:
  - "The ladder market prices a 77% probability that Venezuelan crude oil production reaches 1.2 million barrels per day in 2026, with only 13% above 1.3 million bpd."
  - "The US-Venezuela oil deal is broadly consistent with the high probability at the 1.2M bpd threshold, as US operational involvement could accelerate output; the market sees limited probability of production surging much further in the near term."
  - "The sharp drop from 77% at 1.2M bpd to 13% at 1.3M bpd signals the market views infrastructure and execution risk as real constraints on rapid production scaling."
  - "Resolution depends on an official Venezuelan or internationally recognized crude production data release for 2026; sovereignty disputes and data transparency could create settlement uncertainty."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US and Venezuela announced a major oil deal giving the US significant access to Venezuelan oil reserves, with Venezuela's interim government asserting retained sovereignty."
    publisher: "Al Jazeera Staff"
    published_at: "2026-08-30T00:00:00.000Z"
    source_url: "https://www.aljazeera.com/news/2026/8/30/venezuela-says-it-retains-sovereignty-following-us-oil-deal"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Al Jazeera Staff"
        source_url: "https://www.aljazeera.com/news/2026/8/30/venezuela-says-it-retains-sovereignty-following-us-oil-deal"
        retrieved_at: "2026-08-30T13:30:27+00:00"
  - type: "pm_response"
    notes: "Ladder pricing concentrates strongly at the 1.2M bpd threshold; the deal announcement is consistent with elevated production probability but the market prices limited upside beyond that level."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Al Jazeera Staff: Venezuela says it retains ‘sovereignty’ following US oil deal | News |"
    url: "https://www.aljazeera.com/news/2026/8/30/venezuela-says-it-retains-sovereignty-following-us-oil-deal"
    published_at: "2026-08-30T00:00:00.000Z"
    retrieved_at: "2026-08-30T13:30:27+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
