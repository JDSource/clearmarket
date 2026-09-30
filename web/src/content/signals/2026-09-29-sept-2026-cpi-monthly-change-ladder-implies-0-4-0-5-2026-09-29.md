---
signal_id: "CMSIG2026092902"
signal_slug: "sept-2026-cpi-monthly-change-ladder-implies-0-4-0-5-2026-09-29"
headline: "Sept 2026 CPI monthly change: ladder implies +0.4-+0.5%"
semantic_title: "September CPI monthly change stays near 50-50 at 0.5 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-29T00:00:00.000Z"
event_id: "CM-EVT-F9NPW9F1V9"
event_slug: "kxcpi-26sep"
event_question: "September 2026 CPI monthly change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26SEP-T0.6"
  question_raw: "Will CPI rise more than 0.6% in September 2026?"
  current_price: 0.14
  volume_24h_usd: 93.6
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-01-13T13:56:00Z"
bullets:
  - "Prediction market ladder puts 89% on CPI above +0.4% but only 54% on above +0.5%, pinning the implied central estimate near +0.4 to +0.5% for September 2026."
  - "The sharp drop in consumer confidence to a 12-year low is broadly consistent with demand softening, yet the ladder shows the market still assigns meaningful odds to a firm monthly print."
  - "The steep drop from 54% to 14% between the +0.5% and +0.6% strikes suggests the market sees little chance of a hot surprise."
  - "Resolves via BLS CPI release; any energy or shelter component surprise could shift the distribution sharply given the narrow spread at the median strike."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Consumer confidence dropped to its lowest level in over a decade, falling 6.7 points to 81.9 in September per the Conference Board."
    publisher: "thehill.com"
    published_at: "2026-09-29T00:00:00.000Z"
    source_url: "https://thehill.com/business/6118506-consumer-confidence-reaches-dozen-year-low/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "thehill.com"
        source_url: "https://thehill.com/business/6118506-consumer-confidence-reaches-dozen-year-low/"
        retrieved_at: "2026-09-30T07:47:19+00:00"
  - type: "pm_response"
    notes: "Ladder pricing implies a modest but still-positive September CPI print, with the market not yet pricing in demand destruction from collapsing consumer confidence."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "thehill.com: Consumer confidence falls to a dozen-year low in September"
    url: "https://thehill.com/business/6118506-consumer-confidence-reaches-dozen-year-low/"
    published_at: "2026-09-29T00:00:00.000Z"
    retrieved_at: "2026-09-30T07:47:19+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
