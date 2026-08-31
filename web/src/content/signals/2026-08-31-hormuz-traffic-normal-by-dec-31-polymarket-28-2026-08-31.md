---
signal_id: "CMSIG2026083105"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-28-2026-08-31"
headline: "Hormuz traffic normal by Dec 31: Polymarket 28%"
semantic_title: "Strait of Hormuz traffic back to normal by year-end stays a long shot"
telemetry: "Polymarket 28%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-31T09:19:40.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.28
  volume_24h_usd: 80267.83761499997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts just 28% odds on Strait of Hormuz traffic returning to normal by December 31, reflecting persistent disruption risk."
  - "Fresh U.S. strikes on Iranian launchers in the strait and Iranian retaliatory missile fire at U.S. bases in Jordan are consistent with the market's skeptical pricing on a near-term resolution."
  - "The 72% probability of continued disruption through year-end implies markets see the conflict as likely to drag well beyond the current exchange of strikes."
  - "Resolution via UMA oracle requires a verifiable return to normal transit volumes; active hostilities make that threshold extremely difficult to satisfy within four months."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran attacked Jordan and UAE after U.S. forces bombed Larak Island in the Strait of Hormuz, escalating the US-Iran military confrontation."
    publisher: "Al Jazeera Staff"
    published_at: "2026-08-31T09:19:40.000Z"
    source_url: "https://www.aljazeera.com/news/2026/8/31/iran-attacks-jordan-uae-after-us-bombs-larak-island-whats-the-latest"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Al Jazeera Staff"
        source_url: "https://www.aljazeera.com/news/2026/8/31/iran-attacks-jordan-uae-after-us-bombs-larak-island-whats-the-latest"
        retrieved_at: "2026-08-31T15:47:21+00:00"
  - type: "pm_response"
    notes: "Polymarket at 28% is the only priced contract on Hormuz normalization; with active combat reported today, that figure represents the clearest real-money read on the conflict's trajectory."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Al Jazeera Staff: Iran attacks Jordan, UAE after US bombs Larak Island: What’s the lates"
    url: "https://www.aljazeera.com/news/2026/8/31/iran-attacks-jordan-uae-after-us-bombs-larak-island-whats-the-latest"
    published_at: "2026-08-31T09:19:40.000Z"
    retrieved_at: "2026-08-31T15:47:21+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
