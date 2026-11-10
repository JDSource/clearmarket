---
signal_id: "CMSIG2026111006"
signal_slug: "ukraine-russia-peace-deal-before-2027-polymarket-7-2026-11-10"
headline: "Ukraine-Russia peace deal before 2027: Polymarket 7%"
semantic_title: "Ukraine peace deal before 2027 stays a long shot at 7%"
telemetry: "Polymarket 7%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-10T05:06:13.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.07
  volume_24h_usd: 4268.935605000001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts just 7% odds on Ukraine signing a peace deal with Russia before 2027, resolving via UMA oracle."
  - "Talks resuming in Abu Dhabi after a months-long pause are consistent with diplomatic progress, but the market treats a completed deal this year as a remote outcome."
  - "Two companion Polymarket contracts, Ukraine ceding territory by 2026 at 4% and Ukraine giving up the rest of Donbas before 2027 at 4%, confirm the market sees territorial concessions as even less likely than a deal itself."
  - "Resolution requires a signed peace agreement confirmed by UMA oracle before January 1, 2027; resumption of talks does not trigger resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US-brokered three-way talks between Russia, Ukraine, and the United States began Tuesday in Abu Dhabi, the first such meeting since February."
    publisher: "apnews.com"
    published_at: "2026-11-10T05:06:13.000Z"
    source_url: "https://apnews.com/article/russia-ukraine-war-putin-zelenskyy-uae-3d878a3e56d5df5bd198a6d20c824d18"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/russia-ukraine-war-putin-zelenskyy-uae-3d878a3e56d5df5bd198a6d20c824d18"
        retrieved_at: "2026-11-10T07:47:48+00:00"
  - type: "pm_response"
    notes: "Polymarket binary contract at 7%; companion territorial-concession contracts at 4% each reinforce the consensus that talks are unlikely to produce a signed deal in 2026."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: US-brokered talks are set to start in Abu Dhabi to discuss Ukraine-Rus"
    url: "https://apnews.com/article/russia-ukraine-war-putin-zelenskyy-uae-3d878a3e56d5df5bd198a6d20c824d18"
    published_at: "2026-11-10T05:06:13.000Z"
    retrieved_at: "2026-11-10T07:47:48+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
