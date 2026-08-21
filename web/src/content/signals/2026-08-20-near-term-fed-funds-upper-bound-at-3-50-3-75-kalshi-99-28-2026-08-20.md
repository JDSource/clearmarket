---
signal_id: "CMSIG2026082002"
signal_slug: "near-term-fed-funds-upper-bound-at-3-50-3-75-kalshi-99-28-2026-08-20"
headline: "Near-term Fed funds upper bound at 3.50-3.75%: Kalshi 99%/28%"
semantic_title: "Fed funds near-term upper bound stays near 3.5 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-20T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Federal funds rate upper bound (near-term meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.28
  volume_24h_usd: 461.89
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder shows 99% above 3.50% but only 28% above 3.75%, firmly anchoring the implied upper bound in the 3.50-3.75% range."
  - "Three dissenters at July FOMC pushed for an immediate hike, yet the Kalshi distribution treats a move above 3.75% as a low-probability outcome."
  - "The market is broadly consistent with a hold at 3.50% as the modal outcome, with the hawkish minutes not shifting the implied range higher."
  - "Kalshi prices a large-cut scenario (CM-EVT-RWRZ1R3SD6) at only 6%, reinforcing that both tails are heavily discounted."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed minutes revealed three officials favored an immediate 25-basis-point hike, with many others flagging the need to act if inflation persists."
    publisher: "ANI"
    published_at: "2026-08-20T00:00:00.000Z"
    source_url: "https://www.thehindubusinessline.com/news/world/us-fed-minutes-signal-rate-hike-debate-as-inflation-risks-persist-3-officials-favoured-25-bps-increase/article71368240.ece"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ANI"
        source_url: "https://www.thehindubusinessline.com/news/world/us-fed-minutes-signal-rate-hike-debate-as-inflation-risks-persist-3-officials-favoured-25-bps-increase/article71368240.ece"
        retrieved_at: "2026-08-21T08:35:01+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves against the published federal funds rate upper bound following the relevant FOMC decision."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ANI: US Fed Minutes signal rate hike debate as inflation risks persist; 3 o"
    url: "https://www.thehindubusinessline.com/news/world/us-fed-minutes-signal-rate-hike-debate-as-inflation-risks-persist-3-officials-favoured-25-bps-increase/article71368240.ece"
    published_at: "2026-08-20T00:00:00.000Z"
    retrieved_at: "2026-08-21T08:35:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
