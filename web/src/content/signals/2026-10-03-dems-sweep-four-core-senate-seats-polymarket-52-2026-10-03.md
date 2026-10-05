---
signal_id: "CMSIG2026100306"
signal_slug: "dems-sweep-four-core-senate-seats-polymarket-52-2026-10-03"
headline: "Dems sweep four core Senate seats: Polymarket 52%"
semantic_title: "Democrats winning all four core Senate races stays near 50%"
telemetry: "Polymarket 52%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-03T00:00:00.000Z"
event_id: "CM-EVT-P54SDG6NP7"
event_slug: "will-democrats-win-all-core-four-senate-races"
event_question: "Will Democrats win all four core Senate races?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x096f26b2abcfde3ee7863e7916ca17682522715f7631debd4878a43ee6c797a9"
  question_raw: "Will Democrats win all \"core four\" senate races?"
  current_price: 0.52
  volume_24h_usd: 232.68154300000003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket puts 52% on Democrats winning all four core Senate races, essentially a coin-flip."
  - "Polling showing Democratic gains in Republican territory is consistent with the near-even pricing; the market is not discounting the Democratic momentum."
  - "The Kalshi companion contract on the same sweep stands at 51%, with near-zero cross-venue spread, indicating high consensus at the toss-up level."
  - "Both contracts resolve on certified results from the four named Senate races; a single Republican hold in any of the four flips the contract to NO."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "New midterm polling showed Democrats making inroads in Republican-leaning strongholds, raising prospects for a Democratic Senate sweep of the four most contested races."
    publisher: "Muskan Singh"
    published_at: "2026-10-03T00:00:00.000Z"
    source_url: "https://economictimes.indiatimes.com/news/international/us/u-s-midterm-elections-2026-are-democrats-finally-making-a-comeback-in-republican-strongholds-heres-what-a-new-midterm-poll-shows/articleshow/134664760.cms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Muskan Singh"
        source_url: "https://economictimes.indiatimes.com/news/international/us/u-s-midterm-elections-2026-are-democrats-finally-making-a-comeback-in-republican-strongholds-heres-what-a-new-midterm-poll-shows/articleshow/134664760.cms"
        retrieved_at: "2026-10-05T07:47:16+00:00"
  - type: "pm_response"
    notes: "Polymarket 52%, Kalshi 51% -- tightest cross-venue alignment in today's midterm slate; market reads the four-race sweep as a genuine toss-up."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Muskan Singh: Midterm polls: U.S. midterm elections 2026: Are Democrats finally maki"
    url: "https://economictimes.indiatimes.com/news/international/us/u-s-midterm-elections-2026-are-democrats-finally-making-a-comeback-in-republican-strongholds-heres-what-a-new-midterm-poll-shows/articleshow/134664760.cms"
    published_at: "2026-10-03T00:00:00.000Z"
    retrieved_at: "2026-10-05T07:47:16+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
