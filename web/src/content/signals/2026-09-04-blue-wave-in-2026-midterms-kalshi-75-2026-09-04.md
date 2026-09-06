---
signal_id: "CMSIG2026090405"
signal_slug: "blue-wave-in-2026-midterms-kalshi-75-2026-09-04"
headline: "Blue wave in 2026 midterms: Kalshi 75%"
semantic_title: "Blue wave in 2026 holds near 75% as Democrats gain edge"
telemetry: "Kalshi 75%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-04T11:53:10.540Z"
event_id: "CM-EVT-QK0HJYVMX2"
event_slug: "kxbluewavecombo-27feb"
event_question: "Will there be a blue wave in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBLUEWAVECOMBO-27FEB"
  question_raw: "Will Democrats hold 218 or more seats in the House after the 2026 midterms AND hold 49 or more seats in the Senate after the 2026 midterms?"
  current_price: 0.75
  volume_24h_usd: 2292.23
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices 75% on a blue wave materializing in the 2026 midterms, resolving via Bureau of Labor Statistics."
  - "The Cornell academic forecast aligns with the market's strong Democratic lean, not at odds with it."
  - "Companion Kalshi contract (CM-EVT-6CY3Y4C610) puts only 41% on a blue tsunami, a meaningful gap suggesting markets see a substantial but not dominant Democratic sweep."
  - "Republican control of at least one chamber (CM-EVT-T5VXKJT451) sits at 48%, broadly consistent with 75% blue wave odds if the Senate outcome remains contested."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A Cornell University midterm forecast strongly favors Democrats to win the House majority in 2026, consistent with Gallup data showing Democrats holding a party identification advantage."
    publisher: "Credit:  Ryan Young/Cornell University"
    published_at: "2026-09-04T11:53:10.540Z"
    source_url: "https://news.cornell.edu/stories/2026/09/midterm-forecast-strongly-favors-democrats-win-house-majority"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Credit:  Ryan Young/Cornell University"
        source_url: "https://news.cornell.edu/stories/2026/09/midterm-forecast-strongly-favors-democrats-win-house-majority"
        retrieved_at: "2026-09-06T11:54:11+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via Bureau of Labor Statistics; resolution source appears anomalous for an electoral question and may introduce settlement uncertainty."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Credit:  Ryan Young/Cornell University: Midterm forecast strongly favors Democrats to win House majority"
    url: "https://news.cornell.edu/stories/2026/09/midterm-forecast-strongly-favors-democrats-win-house-majority"
    published_at: "2026-09-04T11:53:10.540Z"
    retrieved_at: "2026-09-06T11:54:11+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
