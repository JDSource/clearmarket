---
signal_id: "CMSIG2026111407"
signal_slug: "ukraine-russia-peace-deal-before-2027-polymarket-7-2026-11-14"
headline: "Ukraine-Russia peace deal before 2027: Polymarket 7%"
semantic_title: "Ukraine-Russia peace deal before 2027 stays a long shot at 7 percent"
telemetry: "Polymarket 7%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-14T00:48:52.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.07
  volume_24h_usd: 2703.496955
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Ukraine signing a peace deal with Russia before 2027 sits at 7%, a long shot despite diplomatic momentum."
  - "Kushner's statement on European inclusion in talks is a constructive signal, but Polymarket is not pricing it as a near-term breakthrough."
  - "The companion Polymarket contract on Trump, Putin, and Zelensky being seen together before 2027 is at 4%, consistent with the 7% peace deal reading; both markets see resolution as unlikely this year."
  - "Resolves via UMA oracle; requires a formally signed peace agreement before January 1, 2027."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US envoy Jared Kushner said Putin would give European participation in Ukraine peace talks 'a try,' with the next round of talks set to include European representatives."
    publisher: "english.news.cn"
    published_at: "2026-11-14T00:48:52.000Z"
    source_url: "https://english.news.cn/20261114/29ab40daef2043c084f16bc7766e2c36/c.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "english.news.cn"
        source_url: "https://english.news.cn/20261114/29ab40daef2043c084f16bc7766e2c36/c.html"
        retrieved_at: "2026-11-14T07:47:51+00:00"
  - type: "pm_response"
    notes: "Polymarket at 7% with a companion contract at 4% for a joint Trump-Putin-Zelensky appearance creates a coherent, mutually consistent set of low-probability diplomatic outcomes."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "english.news.cn: Daily World Briefing, Nov. 14-Xinhua"
    url: "https://english.news.cn/20261114/29ab40daef2043c084f16bc7766e2c36/c.html"
    published_at: "2026-11-14T00:48:52.000Z"
    retrieved_at: "2026-11-14T07:47:51+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
