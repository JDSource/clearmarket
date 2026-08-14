---
signal_id: "CMSIG2026081201"
signal_slug: "sept-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-08-12"
headline: "Sept Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Fed funds upper bound stays near 3.5-3.75% after CPI"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-12T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Fed funds upper bound after next FOMC meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.29
  volume_24h_usd: 4246.17
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder pins the Fed funds upper bound in the 3.50-3.75% range: 98% above 3.50% but only 29% above 3.75%."
  - "July CPI at 0.1% month-over-month met expectations, consistent with the market pricing in a hold near current levels."
  - "A companion Kalshi ladder (CM-EVT-MR57HVWJT3) for a later meeting prices 53% above 3.75%, showing markets see cuts eventually but not soon."
  - "Resolution via Federal Reserve policy announcement; any surprise in upcoming jobs or PPI data could shift the distribution sharply."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US CPI rose 0.1% in July, in line with expectations, easing pressure on the Federal Reserve to act."
    publisher: "semafor.com"
    published_at: "2026-08-12T00:00:00.000Z"
    source_url: "https://www.semafor.com/article/08/12/2026/mild-us-inflation-eases-fed-pressure"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "semafor.com"
        source_url: "https://www.semafor.com/article/08/12/2026/mild-us-inflation-eases-fed-pressure"
        retrieved_at: "2026-08-14T09:03:59+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder pricing is consistent with a Fed hold scenario described by the soft CPI print, with the implied mode firmly in the 3.50-3.75% band."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "semafor.com: US inflation rises 0.1% in July, easing pressure on Fed | Semafor"
    url: "https://www.semafor.com/article/08/12/2026/mild-us-inflation-eases-fed-pressure"
    published_at: "2026-08-12T00:00:00.000Z"
    retrieved_at: "2026-08-14T09:03:59+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
