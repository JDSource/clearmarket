---
signal_id: "CMSIG2026091106"
signal_slug: "iran-npt-withdrawal-before-2027-polymarket-15-2026-09-11"
headline: "Iran NPT withdrawal before 2027: Polymarket 15%"
semantic_title: "Iran NPT withdrawal odds build on escalating tensions"
telemetry: "Polymarket 15%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-11T00:00:00.000Z"
event_id: "CM-EVT-BR5SMCCW00"
event_slug: "will-iran-withdraw-from-the-npt-before-2027"
event_question: "Will Iran withdraw from the NPT before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x3e0845c4736ae232c57b347d05f6145650416dfd3adb0fa5d7ddd335c64a84ca"
  question_raw: "Will Iran withdraw from the NPT before 2027?"
  current_price: 0.15
  volume_24h_usd: 37411.615104000004
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 15% on Iran withdrawing from the NPT before 2027, with trading volume up 14,861% day over day, a 149.6x surge signaling sharply elevated fresh attention."
  - "The volume spike coincides with reports of Iran-US military exchanges, Hormuz disruption, and now Pakistan-Iran de-escalation talks, drawing traders to the contract."
  - "A companion Polymarket contract on Israel-Saudi normalization (CM-EVT-4KV364R788) also shows a 4,201% volume surge, suggesting cross-market activity around the broader Gulf confrontation."
  - "Resolves via UMA oracle; YES requires Iran to formally notify the IAEA of NPT withdrawal before January 1, 2027."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Pakistan and Iran are discussing de-escalation amid Houthi attacks on Saudi Arabia, as regional tensions and the US-Iran confrontation intensify."
    publisher: "The National"
    published_at: "2026-09-11T00:00:00.000Z"
    source_url: "https://www.thenationalnews.com/news/mena/2026/09/11/pakistan-and-iran-discuss-de-escalation-and-houthi-attacks-on-saudi-arabia/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "The National"
        source_url: "https://www.thenationalnews.com/news/mena/2026/09/11/pakistan-and-iran-discuss-de-escalation-and-houthi-attacks-on-saudi-arabia/"
        retrieved_at: "2026-09-11T12:32:20+00:00"
  - type: "pm_response"
    notes: "Volume explosion on both Iran NPT and Israel-Saudi normalization contracts is the clearest real-time signal of market attention to the Gulf crisis narrative."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "The National: Pakistan and Iran discuss de-escalation and Houthi attacks on Saudi Ar"
    url: "https://www.thenationalnews.com/news/mena/2026/09/11/pakistan-and-iran-discuss-de-escalation-and-houthi-attacks-on-saudi-arabia/"
    published_at: "2026-09-11T00:00:00.000Z"
    retrieved_at: "2026-09-11T12:32:20+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
