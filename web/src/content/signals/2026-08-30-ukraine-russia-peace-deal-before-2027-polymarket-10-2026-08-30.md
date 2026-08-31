---
signal_id: "CMSIG2026083006"
signal_slug: "ukraine-russia-peace-deal-before-2027-polymarket-10-2026-08-30"
headline: "Ukraine-Russia peace deal before 2027: Polymarket 10%"
semantic_title: "Ukraine peace deal with Russia before 2027 remains a long shot"
telemetry: "Polymarket 10%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-30T00:00:00.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.1
  volume_24h_usd: 11239.91838
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts only 10% odds on Ukraine signing a peace deal with Russia before 2027, a firmly long-shot read."
  - "Russia's escalating strikes on civilian infrastructure and Ukrainian energy sites are consistent with the market's near-dismissal of a near-term settlement."
  - "A companion Polymarket contract (CM-EVT-T1H8NR4G99) puts just 8% on the U.S. recognizing Russian sovereignty over Ukraine before 2027, suggesting neither diplomatic pathway is seen as likely."
  - "The Polymarket contract resolves via UMA oracle on a formal signed peace deal; ceasefires or framework agreements short of a signed treaty would not trigger resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Russia threatened mass strikes on Ukrainian energy infrastructure as the death toll from a strike on a Kyiv arms depot climbed to 38, marking the deadliest Russian attack on Ukraine in 2026."
    publisher: "euronews.com"
    published_at: "2026-08-30T00:00:00.000Z"
    source_url: "https://www.euronews.com/my-europe/2026/08/30/russia-threatens-mass-strikes-on-ukraine-energy-sites-as-kyiv-depot-death-toll-hits-38"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "euronews.com"
        source_url: "https://www.euronews.com/my-europe/2026/08/30/russia-threatens-mass-strikes-on-ukraine-energy-sites-as-kyiv-depot-death-toll-hits-38"
        retrieved_at: "2026-08-31T15:47:21+00:00"
  - type: "pm_response"
    notes: "Polymarket's 10% peace-deal probability and 8% U.S.-recognition probability form a mutually reinforcing pair confirming markets see no near-term diplomatic exit from the conflict."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "euronews.com: Russia threatens mass strikes on Ukraine energy sites as Kyiv depot de"
    url: "https://www.euronews.com/my-europe/2026/08/30/russia-threatens-mass-strikes-on-ukraine-energy-sites-as-kyiv-depot-death-toll-hits-38"
    published_at: "2026-08-30T00:00:00.000Z"
    retrieved_at: "2026-08-31T15:47:21+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
