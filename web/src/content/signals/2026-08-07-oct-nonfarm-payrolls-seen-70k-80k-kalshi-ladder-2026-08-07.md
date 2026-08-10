---
signal_id: "CMSIG2026080701"
signal_slug: "oct-nonfarm-payrolls-seen-70k-80k-kalshi-ladder-2026-08-07"
headline: "Oct nonfarm payrolls seen 70K-80K: Kalshi ladder"
semantic_title: "October payrolls market holds near 70K-80K range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-07T00:00:00.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "October 2026 nonfarm payrolls"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T80000"
  question_raw: "Will above 80000 jobs be added in October 2026?"
  current_price: 0.45
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "Kalshi ladder prices October payrolls in the 70K-80K range: 85% above -25K, 50% above 70K, 45% above 80K."
  - "July's -23,000 print is a sharp miss, but the Kalshi distribution still implies positive October payrolls, suggesting markets treat July as a one-month anomaly."
  - "The 54% probability above 50K and sharp drop to 24% above 100K shows a compressed, cautious range rather than a recessionary signal."
  - "Resolution via the Bureau of Labor Statistics October nonfarm payrolls release; government-sector job losses, cited as the July driver, remain a wild card."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The US economy unexpectedly shed 23,000 jobs in July, well below the consensus forecast of +83,000, with June also revised downward."
    publisher: "usatoday.com"
    published_at: "2026-08-07T00:00:00.000Z"
    source_url: "https://www.usatoday.com/story/business/2026/08/07/nonfarm-payrolls-down-in-july-unemployment-rate-eases-to-4-1/91211328007/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "usatoday.com"
        source_url: "https://www.usatoday.com/story/business/2026/08/07/nonfarm-payrolls-down-in-july-unemployment-rate-eases-to-4-1/91211328007/"
        retrieved_at: "2026-08-10T09:14:34+00:00"
  - type: "pm_response"
    notes: "Kalshi's October payrolls ladder reflects a market still pricing modest recovery, not extrapolating July's shock into sustained contraction."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "usatoday.com: Nonfarm payrolls down in July; unemployment rate eases to 4.1%"
    url: "https://www.usatoday.com/story/business/2026/08/07/nonfarm-payrolls-down-in-july-unemployment-rate-eases-to-4-1/91211328007/"
    published_at: "2026-08-07T00:00:00.000Z"
    retrieved_at: "2026-08-10T09:14:34+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
