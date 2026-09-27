---
signal_id: "CMSIG2026092706"
signal_slug: "ukraine-russia-peace-deal-before-2027-polymarket-9-2026-09-27"
headline: "Ukraine-Russia peace deal before 2027: Polymarket 9%"
semantic_title: "Ukraine peace deal before 2027 stays a long shot"
telemetry: "Polymarket 9%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-27T00:00:00.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.09
  volume_24h_usd: 108.609781
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only a 9% chance Ukraine signs a peace deal with Russia before 2027."
  - "Escalating air strikes on both sides while Trump calls for peace are consistent with this low probability, the market sees the rhetoric not matching battlefield reality."
  - "A companion Polymarket contract puts just 8% on Trump, Putin, and Zelensky being seen together before 2027, reinforcing how far off a summit appears."
  - "Polymarket also prices Vladimir Putin leaving the Russian presidency by end-2026 at just 4%, anchoring the negotiating landscape as effectively static."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Russia and Ukraine intensified air attacks killing 10 people despite Trump's renewed push for a peace deal."
    publisher: "newswav.com"
    published_at: "2026-09-27T00:00:00.000Z"
    source_url: "https://newswav.com/article/ukraine-russia-war-latest-air-attacks-intensify-killing-10-people-despite-t-A2609_PSDEv5"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "newswav.com"
        source_url: "https://newswav.com/article/ukraine-russia-war-latest-air-attacks-intensify-killing-10-people-despite-t-A2609_PSDEv5"
        retrieved_at: "2026-09-27T07:47:06+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via uma_oracle; continued military escalation with no ceasefire mechanism keeps this contract firmly in single digits."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "newswav.com: Ukraine-Russia war latest: Air attacks intensify, killing 10 people, d"
    url: "https://newswav.com/article/ukraine-russia-war-latest-air-attacks-intensify-killing-10-people-despite-t-A2609_PSDEv5"
    published_at: "2026-09-27T00:00:00.000Z"
    retrieved_at: "2026-09-27T07:47:06+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
