---
signal_id: "CMSIG2026081806"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-34-2026-08-18"
headline: "Hormuz traffic normal by Dec 31: Polymarket 34%"
semantic_title: "Hormuz traffic back to normal by year-end stays below 50%"
telemetry: "Polymarket 34%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-18T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.34
  volume_24h_usd: 82969.801367
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 34% on Strait of Hormuz traffic returning to normal by December 31, a long-shot reading."
  - "Trump's statement that no talks are planned and the expired 60-day peace deadline are consistent with below-50% odds on normalization."
  - "The absence of active diplomacy reinforces the Polymarket market's skeptical stance, news and pricing are aligned."
  - "Resolution via UMA oracle requires observable normalization of transit traffic, a high bar given ongoing ship attacks and no talks on the calendar."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump said no Iran talks are planned while Hormuz tensions persist following a lapsed ceasefire deadline and ship attacks."
    publisher: "Al Jazeera Staff"
    published_at: "2026-08-18T00:00:00.000Z"
    source_url: "https://www.aljazeera.com/news/2026/8/18/no-talks-with-iran-says-trump-as-us-president-stews-over-hormuz-deal"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Al Jazeera Staff"
        source_url: "https://www.aljazeera.com/news/2026/8/18/no-talks-with-iran-says-trump-as-us-president-stews-over-hormuz-deal"
        retrieved_at: "2026-08-20T08:32:51+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 34% resolves via UMA oracle; no diplomatic pathway currently visible makes the December deadline increasingly tight."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Al Jazeera Staff: Trump says no talks planned with Iran amid anger over Iran-Oman Hormuz"
    url: "https://www.aljazeera.com/news/2026/8/18/no-talks-with-iran-says-trump-as-us-president-stews-over-hormuz-deal"
    published_at: "2026-08-18T00:00:00.000Z"
    retrieved_at: "2026-08-20T08:32:51+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
