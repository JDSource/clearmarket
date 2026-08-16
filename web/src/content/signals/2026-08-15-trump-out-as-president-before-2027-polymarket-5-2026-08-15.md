---
signal_id: "CMSIG2026081508"
signal_slug: "trump-out-as-president-before-2027-polymarket-5-2026-08-15"
headline: "Trump out as president before 2027: Polymarket 5%"
semantic_title: "Trump ceasing to be president before 2027 stays a long shot at 5%"
telemetry: "Polymarket 5%"
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
  current_price: 0.05
  volume_24h_usd: 6968.095517
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices the probability of Trump ceasing to be president before 2027 at 5%, a strong long-shot read despite mounting intra-party Iran war pressure."
  - "Republican pressure over the Iran war is notable, but the 5% price shows the market assigns negligible probability to that pressure translating into removal or resignation before year-end."
  - "The Kalshi contract on whether 2026 will be a bad year for Trump sits at 5% as well, while a separate Kalshi contract on a successful year also sits at just 3%, both near-null readings suggest the market sees the Iran war as an ongoing drag, not a decisive break either way."
  - "Resolves via Polymarket's UMA oracle based on Trump's official presidential status before January 1, 2027."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "A growing number of prominent MAGA figures are urging President Trump to find an exit from the Iran war ahead of the 2026 midterms, warning of dire political consequences."
    publisher: "usatoday.com"
    published_at: "2026-08-15T00:00:00.000Z"
    source_url: "https://www.usatoday.com/story/news/politics/2026/08/15/trump-iran-war-republicans-midterm-elections/91277119007/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "usatoday.com"
        source_url: "https://www.usatoday.com/story/news/politics/2026/08/15/trump-iran-war-republicans-midterm-elections/91277119007/"
        retrieved_at: "2026-08-16T08:23:09+00:00"
  - type: "pm_response"
    notes: "Polymarket's 5% on Trump leaving office before 2027 reflects a market treating intra-party Iran war dissent as politically manageable rather than existential."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "usatoday.com: Republicans push Trump to find path out of Iran war as midterms near"
    url: "https://www.usatoday.com/story/news/politics/2026/08/15/trump-iran-war-republicans-midterm-elections/91277119007/"
    published_at: "2026-08-15T00:00:00.000Z"
    retrieved_at: "2026-08-16T08:23:09+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
