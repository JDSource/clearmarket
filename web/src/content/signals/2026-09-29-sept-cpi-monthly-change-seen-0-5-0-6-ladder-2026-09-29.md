---
signal_id: "CMSIG2026092904"
signal_slug: "sept-cpi-monthly-change-seen-0-5-0-6-ladder-2026-09-29"
headline: "Sept CPI monthly change seen 0.5-0.6%: ladder"
semantic_title: "September CPI monthly change seen between 0.5 and 0.6 percent"
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
  current_price: 0.17
  volume_24h_usd: 150.29
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-01-13T13:56:00Z"
bullets:
  - "The ladder pins September CPI monthly change in the 0.5-0.6% range: 54% above 0.5% but only 17% above 0.6%, a relatively tight distribution."
  - "Collapsing consumer confidence to a 12-year low is not yet reflected as downward pressure on the CPI ladder, which still prices a moderate monthly gain."
  - "August core PCE came in at 3.0% year-over-year, softer than expected; if that disinflationary impulse carries into September CPI, the 0.6%-plus tail could erode further."
  - "Resolution source is unspecified; the BLS typically releases the following month's CPI mid-month, making this an October data event."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Conference Board's consumer confidence index fell to 81.9 in September, its lowest level in over a decade, as consumers grow more pessimistic."
    publisher: "thehill.com"
    published_at: "2026-09-29T00:00:00.000Z"
    source_url: "https://thehill.com/business/6118506-consumer-confidence-reaches-dozen-year-low/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "thehill.com"
        source_url: "https://thehill.com/business/6118506-consumer-confidence-reaches-dozen-year-low/"
        retrieved_at: "2026-09-30T14:32:59+00:00"
  - type: "pm_response"
    notes: "Ladder event carries no named venue; resolution mechanics and source are unspecified in the provided data."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "thehill.com: Consumer confidence falls to a dozen-year low in September"
    url: "https://thehill.com/business/6118506-consumer-confidence-reaches-dozen-year-low/"
    published_at: "2026-09-29T00:00:00.000Z"
    retrieved_at: "2026-09-30T14:32:59+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
