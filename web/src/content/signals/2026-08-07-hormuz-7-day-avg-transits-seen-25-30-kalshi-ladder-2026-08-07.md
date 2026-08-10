---
signal_id: "CMSIG2026080707"
signal_slug: "hormuz-7-day-avg-transits-seen-25-30-kalshi-ladder-2026-08-07"
headline: "Hormuz 7-day avg transits seen 25-30: Kalshi ladder"
semantic_title: "Hormuz daily transits implied near 25-30 calls"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-07T00:00:00.000Z"
event_id: "CM-EVT-L5QXXGC9M4"
event_slug: "kxhormuzweekly-26aug09"
event_question: "Strait of Hormuz daily transit calls"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHORMUZWEEKLY-26AUG09-T30"
  question_raw: "Will there be more than 30 transit calls through the Strait of Hormuz from Aug 3, 2026 to Aug 9, 2026?"
  current_price: 0.4
  volume_24h_usd: 927.72
  arbitration_model: "kalshi_staff"
  resolution_source: "IMF PortWatch"
  resolves_at: "2026-11-09T14:00:00Z"
bullets:
  - "Kalshi ladder implies Hormuz 7-day average transits in the 25-30 range: 68% above 25 calls, 40% above 30, falling sharply to 15% above 40."
  - "Houthi attacks on ADNOC vessels and Iran's conditions for reopening are consistent with the market pricing well below pre-conflict transit levels."
  - "A companion Kalshi ladder on the 7-day moving average (CM-EVT-JR1WTQ5JH0) shows 53% above 40, a sharper distribution implying uncertainty about which week the data captures."
  - "Resolution depends on the specific measurement date and transit counting methodology; the named source is unspecified, creating settlement edge-case risk."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Houthi attacks on vessels in the region are stoking fears of a wider conflict that could further restrict Strait of Hormuz shipping."
    publisher: "apnews.com"
    published_at: "2026-08-07T00:00:00.000Z"
    source_url: "https://apnews.com/article/yemen-houthis-attacks-iran-us-explainer-6d79ab62dc697281ba5be0352e95b2c5"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/yemen-houthis-attacks-iran-us-explainer-6d79ab62dc697281ba5be0352e95b2c5"
        retrieved_at: "2026-08-10T09:14:34+00:00"
  - type: "pm_response"
    notes: "Kalshi's transit ladder prices a deeply disrupted but not fully closed strait, with Houthi escalation news consistent with the lower end of the implied range."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: Houthis' claims of deadly attacks stoke fears of a wider regional conf"
    url: "https://apnews.com/article/yemen-houthis-attacks-iran-us-explainer-6d79ab62dc697281ba5be0352e95b2c5"
    published_at: "2026-08-07T00:00:00.000Z"
    retrieved_at: "2026-08-10T09:14:34+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
