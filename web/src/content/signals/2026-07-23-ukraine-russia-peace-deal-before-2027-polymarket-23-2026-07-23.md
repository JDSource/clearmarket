---
signal_id: "CMSIG2026072308"
signal_slug: "ukraine-russia-peace-deal-before-2027-polymarket-23-2026-07-23"
headline: "Ukraine-Russia peace deal before 2027: Polymarket 23%"
semantic_title: "Ukraine peace deal before 2027 stays under 25%"
telemetry: "Polymarket 23%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-23T05:32:01.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.23
  volume_24h_usd: 12674.418237999998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 23% probability of Ukraine signing a peace deal with Russia before 2027, keeping the outcome firmly in long-shot territory."
  - "Zelensky's claim of Kremlin inner-circle dysfunction is a diplomatic narrative, but the market assigns it little weight, the probability remains below 25%."
  - "The companion Polymarket contract on Putin leaving office by December 31 sits at 9%, suggesting markets do not read the isolation claims as an imminent power shift."
  - "Resolves via UMA oracle; a formally signed peace agreement, not a ceasefire or framework, is the presumed settlement bar."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Ukrainian President Volodymyr Zelensky claimed that aides to Vladimir Putin signaled the Russian president is isolated in his inner circle, describing a toxic atmosphere around the Kremlin leader."
    publisher: "the-independent.com"
    published_at: "2026-07-23T05:32:01.000Z"
    source_url: "https://www.the-independent.com/news/world/europe/ukraine-russia-war-live-putin-zelensky-drone-raids-wildberries-b3019965.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "the-independent.com"
        source_url: "https://www.the-independent.com/news/world/europe/ukraine-russia-war-live-putin-zelensky-drone-raids-wildberries-b3019965.html"
        retrieved_at: "2026-07-23T10:16:46+00:00"
  - type: "pm_response"
    notes: "Polymarket's 23% on a peace deal and 9% on Putin departure together suggest markets are pricing diplomatic noise, not structural change, from the Zelensky claims."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "the-independent.com: Ukraine war live: Zelensky claims ‘toxic’ atmosphere in Putin’s inner"
    url: "https://www.the-independent.com/news/world/europe/ukraine-russia-war-live-putin-zelensky-drone-raids-wildberries-b3019965.html"
    published_at: "2026-07-23T05:32:01.000Z"
    retrieved_at: "2026-07-23T10:16:46+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
