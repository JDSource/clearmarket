---
signal_id: "CMSIG2026100302"
signal_slug: "dems-sweep-four-core-senate-races-polymarket-55-2026-10-03"
headline: "Dems sweep four core Senate races: Polymarket 55%"
semantic_title: "Democrats sweep four core Senate races stays near 50%"
telemetry: "Polymarket 55%"
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
  current_price: 0.55
  volume_24h_usd: 145.39999999999998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices 55% on Democrats winning all four core Senate races, a slim majority-leaning read with no decisive lean."
  - "Poll data showing Democratic momentum in Republican-leaning districts is broadly consistent with the near-50% pricing, not a clear market mismatch."
  - "Kalshi's companion contract on the same sweep question sits at 53%, showing tight cross-venue alignment and little arbitrage gap."
  - "Resolution requires Democrats to win all four races; a single loss collapses the contract to zero, which explains the discount from a straight single-race favorite read."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "A new midterm poll suggests Democrats may be making inroads in traditional Republican strongholds ahead of the November 3 elections."
    publisher: "Muskan Singh"
    published_at: "2026-10-03T00:00:00.000Z"
    source_url: "https://economictimes.indiatimes.com/news/international/us/u-s-midterm-elections-2026-are-democrats-finally-making-a-comeback-in-republican-strongholds-heres-what-a-new-midterm-poll-shows/articleshow/134664760.cms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Muskan Singh"
        source_url: "https://economictimes.indiatimes.com/news/international/us/u-s-midterm-elections-2026-are-democrats-finally-making-a-comeback-in-republican-strongholds-heres-what-a-new-midterm-poll-shows/articleshow/134664760.cms"
        retrieved_at: "2026-10-04T07:47:36+00:00"
  - type: "pm_response"
    notes: "Polymarket at 55% and Kalshi at 53% are in close agreement, reflecting genuine uncertainty rather than a consensus directional call on the Senate sweep."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Muskan Singh: Midterm polls: U.S. midterm elections 2026: Are Democrats finally maki"
    url: "https://economictimes.indiatimes.com/news/international/us/u-s-midterm-elections-2026-are-democrats-finally-making-a-comeback-in-republican-strongholds-heres-what-a-new-midterm-poll-shows/articleshow/134664760.cms"
    published_at: "2026-10-03T00:00:00.000Z"
    retrieved_at: "2026-10-04T07:47:36+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
