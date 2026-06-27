---
signal_id: "CMSIG2026062605"
signal_slug: "hormuz-traffic-back-to-normal-by-june-30-polymarket-5-2026-06-26"
headline: "Hormuz traffic back to normal by June 30: Polymarket 5%"
semantic_title: "Hormuz traffic normalization by June 30 fades to near zero"
telemetry: "Polymarket 5%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-26T11:18:00.000Z"
event_id: "CM-EVT-YPW93GCTK6"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-end-of-june"
event_question: "Will traffic through the Strait of Hormuz return to normal by the end of June?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x348cd9adf4f6855f58bd9c6dbf9ff251c4142ef77233a5dc95c65b4b61cd2187"
  question_raw: "Strait of Hormuz traffic returns to normal by end of June?"
  current_price: 0.052
  volume_24h_usd: 1341796.083945
  arbitration_model: "uma_oracle"
  resolution_source: "portwatch.imf.org"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices only 5% odds on Strait of Hormuz traffic returning to normal by June 30, reflecting near-certainty of continued disruption."
  - "Iran's explicit claim of Hormuz control rights, combined with the US-Iran military exchange, is consistent with the market pricing out near-term normalization."
  - "The market is pricing this as a durable disruption: the resolution deadline of June 30 is just days away, making the 5% a nearly expired tail."
  - "Resolves via portwatch.imf.org shipping traffic data; 'normal' requires restoration of pre-disruption transit volumes by the deadline."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran asserted its right to control shipping in the Strait of Hormuz after a vessel was hit near Oman, as the US conducted strikes on Iran."
    publisher: "channelnewsasia.com"
    published_at: "2026-06-26T11:18:00.000Z"
    source_url: "https://www.channelnewsasia.com/world/iran-strait-hormuz-control-ship-hit-oman-us-6213036"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "channelnewsasia.com"
        source_url: "https://www.channelnewsasia.com/world/iran-strait-hormuz-control-ship-hit-oman-us-6213036"
        retrieved_at: "2026-06-27T01:35:43+00:00"
  - type: "pm_response"
    notes: "Polymarket at 5% with a June 30 deadline is effectively a countdown to a NO resolution, with the Iran-US exchange removing any remaining optionality."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "channelnewsasia.com: Iran insists on right to control shipping in Strait of Hormuz after sh"
    url: "https://www.channelnewsasia.com/world/iran-strait-hormuz-control-ship-hit-oman-us-6213036"
    published_at: "2026-06-26T11:18:00.000Z"
    retrieved_at: "2026-06-27T01:35:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
