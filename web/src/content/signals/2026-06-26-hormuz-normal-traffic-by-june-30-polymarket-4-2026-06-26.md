---
signal_id: "CMSIG2026062604"
signal_slug: "hormuz-normal-traffic-by-june-30-polymarket-4-2026-06-26"
headline: "Hormuz normal traffic by June 30: Polymarket 4%"
semantic_title: "Strait of Hormuz normal traffic by June 30 breaks away as near-zero"
telemetry: "Polymarket 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-26T09:09:34.000Z"
event_id: "CM-EVT-YPW93GCTK6"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-end-of-june"
event_question: "Will traffic through the Strait of Hormuz return to normal by the end of June?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x348cd9adf4f6855f58bd9c6dbf9ff251c4142ef77233a5dc95c65b4b61cd2187"
  question_raw: "Strait of Hormuz traffic returns to normal by end of June?"
  current_price: 0.045
  volume_24h_usd: 911002.8343429996
  arbitration_model: "uma_oracle"
  resolution_source: "portwatch.imf.org"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices only 4% on normal Strait of Hormuz traffic returning by end of June, resolving via portwatch.imf.org shipping data."
  - "Iran's strike on an Evergreen vessel and its assertion of control rights are consistent with the near-zero market probability for a rapid normalization."
  - "The market is not fading the disruption headlines; 4% implies the market sees essentially no path to normalization within days."
  - "Resolves via portwatch.imf.org transit data by June 30; with only days remaining and active IRGC interdiction, resolution as 'no' appears near-certain."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran struck a vessel in the Strait of Hormuz on June 26, threatening further shipping disruptions as the IRGC asserts control over the waterway."
    publisher: "dnyuz.com"
    published_at: "2026-06-26T09:09:34.000Z"
    source_url: "https://dnyuz.com/2026/06/26/iran-strikes-vessel-in-strait-of-hormuz-threatening-more-shipping-disruptions/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "dnyuz.com"
        source_url: "https://dnyuz.com/2026/06/26/iran-strikes-vessel-in-strait-of-hormuz-threatening-more-shipping-disruptions/"
        retrieved_at: "2026-06-27T10:02:20+00:00"
  - type: "pm_response"
    notes: "Polymarket contract on Hormuz normalization by June 30; at 4%, the market is fully aligned with ongoing Iranian interdiction activity reported this week."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "dnyuz.com: Iran Strikes Vessel in Strait of Hormuz, Threatening More Shipping Dis"
    url: "https://dnyuz.com/2026/06/26/iran-strikes-vessel-in-strait-of-hormuz-threatening-more-shipping-disruptions/"
    published_at: "2026-06-26T09:09:34.000Z"
    retrieved_at: "2026-06-27T10:02:20+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
