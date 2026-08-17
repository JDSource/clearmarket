---
signal_id: "CMSIG2026081507"
signal_slug: "trump-ceases-to-be-president-before-2027-polymarket-6-2026-08-15"
headline: "Trump ceases to be president before 2027: Polymarket 6%"
semantic_title: "Trump leaving presidency before 2027 remains a long shot"
telemetry: "Polymarket 6%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-15T00:00:00.000Z"
event_id: "CM-EVT-ZW6ZK09DB1"
event_slug: "trump-out-as-president-before-2027"
event_question: "Will Donald Trump cease to be President before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x48b0b0bca515f68fccf95af4793dbd0edbfec1f8ec6e8df2c0f69ba74f8c4722"
  question_raw: "Trump out as President before 2027?"
  current_price: 0.06
  volume_24h_usd: 74251.078032
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts only 6% probability on Donald Trump ceasing to be president before 2027, resolving via UMA oracle."
  - "Republican pressure over the Iran war and midterm fears is a notable political stress signal, but the market is not pricing meaningful removal or resignation risk."
  - "The 6% price suggests markets view the Iran war backlash as an electoral problem for Republicans rather than an existential threat to the Trump presidency."
  - "Resolution via UMA oracle on any departure from office; the low probability holds regardless of the Iran conflict trajectory."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Growing MAGA pressure on Trump to exit the Iran war amid warnings of severe midterm political consequences."
    publisher: "usatoday.com"
    published_at: "2026-08-15T00:00:00.000Z"
    source_url: "https://www.usatoday.com/story/news/politics/2026/08/15/trump-iran-war-republicans-midterm-elections/91277119007/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "usatoday.com"
        source_url: "https://www.usatoday.com/story/news/politics/2026/08/15/trump-iran-war-republicans-midterm-elections/91277119007/"
        retrieved_at: "2026-08-17T08:37:49+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; at 6%, the market strongly dismisses near-term presidential succession scenarios despite political friction."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "usatoday.com: Republicans push Trump to find path out of Iran war as midterms near"
    url: "https://www.usatoday.com/story/news/politics/2026/08/15/trump-iran-war-republicans-midterm-elections/91277119007/"
    published_at: "2026-08-15T00:00:00.000Z"
    retrieved_at: "2026-08-17T08:37:49+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
