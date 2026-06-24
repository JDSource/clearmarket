---
signal_id: "CMSIG2026062406"
signal_slug: "progressives-sweep-dem-senate-primaries-kalshi-56-2026-06-24"
headline: "Progressives sweep Dem Senate primaries: Kalshi 56%"
semantic_title: "Progressive Senate primary sweep consensus wavers at majority odds"
telemetry: "Kalshi 56%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-24T00:00:00.000Z"
event_id: "CM-EVT-GTBT00NHW6"
event_slug: "kxdemprogressivesenatesweep-26nov03"
event_question: "Will progressives sweep the Democratic Senate primaries?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXDEMPROGRESSIVESENATESWEEP-26NOV03"
  question_raw: "Will the listed Democratic Senate candidates all win their primary elections?"
  current_price: 0.56
  volume_24h_usd: 61.6
  arbitration_model: "kalshi_staff"
  resolution_source: "Bloomberg"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi prices a progressive sweep of Democratic Senate primaries at 56%, a slim majority reflecting real uncertainty."
  - "Mamdani's slate winning New York congressional primaries is the most prominent data point in favor of a broader progressive sweep narrative."
  - "The companion contract (CM-EVT-QH62PP4D92) puts only 49% on Democrats winning all four core Senate races, showing the party's path remains contested."
  - "Resolves via Bloomberg; the sweep definition likely requires progressives to win a defined set of Senate primary contests, not just House races."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "New York City Mayor Zohran Mamdani's progressive slate swept Democratic congressional primaries in New York, ousting two incumbent congressmembers."
    publisher: "Al Jazeera Staff"
    published_at: "2026-06-24T00:00:00.000Z"
    source_url: "https://www.aljazeera.com/news/2026/6/24/mamdani-backed-candidates-sweep-new-york-city-democratic-primaries"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Al Jazeera Staff"
        source_url: "https://www.aljazeera.com/news/2026/6/24/mamdani-backed-candidates-sweep-new-york-city-democratic-primaries"
        retrieved_at: "2026-06-24T10:45:49+00:00"
  - type: "pm_response"
    notes: "Kalshi's 56% on a progressive Senate primary sweep is a thin edge, with the New York results the clearest confirming catalyst so far in the cycle."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Al Jazeera Staff: Mamdani-backed candidates sweep New York City Democratic primaries | E"
    url: "https://www.aljazeera.com/news/2026/6/24/mamdani-backed-candidates-sweep-new-york-city-democratic-primaries"
    published_at: "2026-06-24T00:00:00.000Z"
    retrieved_at: "2026-06-24T10:45:49+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
