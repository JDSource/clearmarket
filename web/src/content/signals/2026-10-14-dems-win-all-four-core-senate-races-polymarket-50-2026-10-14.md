---
signal_id: "CMSIG2026101405"
signal_slug: "dems-win-all-four-core-senate-races-polymarket-50-2026-10-14"
headline: "Dems win all four core Senate races: Polymarket 50%"
semantic_title: "Democrats sweeping all four core Senate races sits near 50 percent"
telemetry: "Polymarket 50%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-14T00:00:00.000Z"
event_id: "CM-EVT-P54SDG6NP7"
event_slug: "will-democrats-win-all-core-four-senate-races"
event_question: "Will Democrats win all four core Senate races?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x096f26b2abcfde3ee7863e7916ca17682522715f7631debd4878a43ee6c797a9"
  question_raw: "Will Democrats win all \"core four\" senate races?"
  current_price: 0.5
  volume_24h_usd: 4.0
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "The Polymarket contract on Democrats winning all four core Senate races prices at exactly 50%, reflecting maximum uncertainty."
  - "GOP distancing from Trump on the economy and Iran (Story 15) is consistent with a competitive Senate map, matching the even-odds pricing."
  - "The Kalshi contract on Republicans holding at least one chamber at 60% (Story 11) implies markets expect partial GOP retention even if Democrats sweep key Senate contests."
  - "Resolves via UMA oracle; the 50% price signals no directional consensus ahead of election night."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "President Donald Trump is personalizing the midterm elections as a referendum on his agenda while some Republicans distance themselves on the economy and immigration."
    publisher: "Jihan Abdalla"
    published_at: "2026-10-14T00:00:00.000Z"
    source_url: "https://www.thenationalnews.com/news/us/2026/10/14/trump-midterms-republicans-toxic/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jihan Abdalla"
        source_url: "https://www.thenationalnews.com/news/us/2026/10/14/trump-midterms-republicans-toxic/"
        retrieved_at: "2026-10-14T07:47:32+00:00"
  - type: "pm_response"
    notes: "Polymarket contract via UMA oracle; 50% pricing means the contract offers no directional edge and reflects genuine market uncertainty about Senate control."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jihan Abdalla: Toxic Trump? President makes midterms all about him but some Republica"
    url: "https://www.thenationalnews.com/news/us/2026/10/14/trump-midterms-republicans-toxic/"
    published_at: "2026-10-14T00:00:00.000Z"
    retrieved_at: "2026-10-14T07:47:32+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
