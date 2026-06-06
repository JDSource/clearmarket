---
signal_id: "CMSIG2026060605"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-76-2026-06-06"
headline: "Hormuz traffic normal by Dec 31: Polymarket 76%"
semantic_title: "Strait of Hormuz traffic normalization by year-end holds majority pricing"
telemetry: "Polymarket 76%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-06T02:14:28.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will traffic through the Strait of Hormuz return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.76
  volume_24h_usd: 24270.863375000004
  arbitration_model: "uma_oracle"
  resolution_source: "portwatch.imf.org"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 76% on Strait of Hormuz traffic returning to normal by December 31, treating full-year normalization as the base case despite fresh escalation."
  - "The drone intercept is consistent with continued disruption in the near term, but the market is pricing in resolution well before year-end."
  - "The June 30 normalization contract sits at only 20% and the July 31 contract at 39%, revealing a steep near-term discount that flattens by December."
  - "Polymarket contract resolves via PortWatch IMF shipping-traffic data; normalization requires measured vessel traffic to recover to pre-conflict baselines."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US forces intercepted and shot down four Iranian drones launched toward the Strait of Hormuz, which CENTCOM said posed an immediate threat to regional maritime traffic."
    publisher: "aa.com.tr"
    published_at: "2026-06-06T02:14:28.000Z"
    source_url: "https://www.aa.com.tr/en/us-israel-iran-war/us-forces-intercept-drones-launched-by-iran-toward-strait-of-hormuz-centcom/3958146"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "aa.com.tr"
        source_url: "https://www.aa.com.tr/en/us-israel-iran-war/us-forces-intercept-drones-launched-by-iran-toward-strait-of-hormuz-centcom/3958146"
        retrieved_at: "2026-06-06T10:00:26+00:00"
  - type: "pm_response"
    notes: "Polymarket resolves via portwatch.imf.org shipping data; the gap between 20% by June 30 and 76% by December 31 reflects the market's expectation of a protracted but ultimately resolved disruption."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "aa.com.tr: US forces intercept drones launched by Iran toward Strait of Hormuz: C"
    url: "https://www.aa.com.tr/en/us-israel-iran-war/us-forces-intercept-drones-launched-by-iran-toward-strait-of-hormuz-centcom/3958146"
    published_at: "2026-06-06T02:14:28.000Z"
    retrieved_at: "2026-06-06T10:00:26+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
