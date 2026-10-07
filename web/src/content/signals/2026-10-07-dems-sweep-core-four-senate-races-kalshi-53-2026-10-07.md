---
signal_id: "CMSIG2026100704"
signal_slug: "dems-sweep-core-four-senate-races-kalshi-53-2026-10-07"
headline: "Dems sweep core four Senate races: Kalshi 53%"
semantic_title: "Democrats sweep four core Senate races holds near 50 percent"
telemetry: "Kalshi 53%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-07T00:00:00.000Z"
event_id: "CM-EVT-QH62PP4D92"
event_slug: "kxdemcorefoursenatesweep-26nov03"
event_question: "Will Democrats sweep the core four Senate races by 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXDEMCOREFOURSENATESWEEP-26NOV03"
  question_raw: "Will Democrats win the 2026 senate elections in Georgia, Michigan, North Carolina, AND Maine?"
  current_price: 0.53
  volume_24h_usd: 154.79
  arbitration_model: "kalshi_staff"
  resolution_source: "Bloomberg"
  resolves_at: "2026-11-10T15:00:00Z"
bullets:
  - "Kalshi puts 53% on Democrats sweeping all four core Senate races, nearly a coin-flip heading into the debate cycle."
  - "The Maine race between Collins and Jackson is a linchpin; a Collins loss is required for a Democratic sweep."
  - "Polymarket (CM-EVT-P54SDG6NP7) puts 49% on Democrats winning all four core races, nearly matching Kalshi and confirming the near-even split across venues."
  - "Resolves via Bloomberg's official call of all four race outcomes after Election Day."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Susan Collins and challenger Troy Jackson clashed in Maine's first Senate debate over Trump alignment and seniority in a key battleground race."
    publisher: "nbcnews.com"
    published_at: "2026-10-07T00:00:00.000Z"
    source_url: "https://www.nbcnews.com/politics/2026-election/susan-collins-troy-jackson-clash-trump-seniority-maines-first-senate-d-rcna601346"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "nbcnews.com"
        source_url: "https://www.nbcnews.com/politics/2026-election/susan-collins-troy-jackson-clash-trump-seniority-maines-first-senate-d-rcna601346"
        retrieved_at: "2026-10-07T07:47:51+00:00"
  - type: "pm_response"
    notes: "Kalshi at 53% and Polymarket at 49% are tightly aligned, with no material cross-venue gap."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "nbcnews.com: Susan Collins and Troy Jackson clash over Trump and seniority in Maine"
    url: "https://www.nbcnews.com/politics/2026-election/susan-collins-troy-jackson-clash-trump-seniority-maines-first-senate-d-rcna601346"
    published_at: "2026-10-07T00:00:00.000Z"
    retrieved_at: "2026-10-07T07:47:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
