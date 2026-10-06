---
signal_id: "CMSIG2026100304"
signal_slug: "dems-sweep-four-core-senate-seats-kalshi-51-2026-10-03"
headline: "Dems sweep four core Senate seats: Kalshi 51%"
semantic_title: "Democrat Senate sweep sits near 50 percent on Kalshi"
telemetry: "Kalshi 51%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-03T00:00:00.000Z"
event_id: "CM-EVT-QH62PP4D92"
event_slug: "kxdemcorefoursenatesweep-26nov03"
event_question: "Will Democrats sweep the core four Senate races by 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXDEMCOREFOURSENATESWEEP-26NOV03"
  question_raw: "Will Democrats win the 2026 senate elections in Georgia, Michigan, North Carolina, AND Maine?"
  current_price: 0.51
  volume_24h_usd: 1945.83
  arbitration_model: "kalshi_staff"
  resolution_source: "Bloomberg"
  resolves_at: "2026-11-10T15:00:00Z"
bullets:
  - "The Kalshi contract on Democrats sweeping the four core Senate races sits at 51%, essentially a coin flip."
  - "A companion Polymarket contract (CM-EVT-P54SDG6NP7) prices the same outcome at 49%, producing near-perfect cross-venue agreement and no exploitable gap."
  - "The near-50% pricing on both venues is consistent with new polling showing Democratic gains in Republican-leaning districts, neither side is favored."
  - "Resolves via Bloomberg per the Kalshi contract terms; individual race calls will drive settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "New polling showed Democrats making inroads in traditionally Republican strongholds ahead of the 2026 midterm elections."
    publisher: "Muskan Singh"
    published_at: "2026-10-03T00:00:00.000Z"
    source_url: "https://economictimes.indiatimes.com/news/international/us/u-s-midterm-elections-2026-are-democrats-finally-making-a-comeback-in-republican-strongholds-heres-what-a-new-midterm-poll-shows/articleshow/134664760.cms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Muskan Singh"
        source_url: "https://economictimes.indiatimes.com/news/international/us/u-s-midterm-elections-2026-are-democrats-finally-making-a-comeback-in-republican-strongholds-heres-what-a-new-midterm-poll-shows/articleshow/134664760.cms"
        retrieved_at: "2026-10-06T07:48:15+00:00"
  - type: "pm_response"
    notes: "Kalshi at 51% and Polymarket at 49% for the identical Democrat-sweep outcome reflect genuine toss-up conditions with essentially no cross-venue arbitrage."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Muskan Singh: Midterm polls: U.S. midterm elections 2026: Are Democrats finally maki"
    url: "https://economictimes.indiatimes.com/news/international/us/u-s-midterm-elections-2026-are-democrats-finally-making-a-comeback-in-republican-strongholds-heres-what-a-new-midterm-poll-shows/articleshow/134664760.cms"
    published_at: "2026-10-03T00:00:00.000Z"
    retrieved_at: "2026-10-06T07:48:15+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
