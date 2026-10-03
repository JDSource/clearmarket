---
signal_id: "CMSIG2026093003"
signal_slug: "sept-cpi-mom-implied-0-5-0-6-kalshi-ladder-2026-09-30"
headline: "Sept CPI MoM implied 0.5-0.6%: Kalshi ladder"
semantic_title: "September CPI month-over-month implied near 0.5 percent"
telemetry: "Kalshi ladder"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-09-30T00:00:00.000Z"
event_id: "CM-EVT-F9NPW9F1V9"
event_slug: "kxcpi-26sep"
event_question: "September 2026 CPI month-over-month change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26SEP-T0.6"
  question_raw: "Will CPI rise more than 0.6% in September 2026?"
  current_price: 0.18
  volume_24h_usd: 335.44
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-01-13T13:56:00Z"
bullets:
  - "Kalshi ladder implies September CPI MoM near 0.5-0.6%, with 60% above 0.5% but only 18% above 0.6%."
  - "August core PCE printing at 3.0% versus 3.3% expected suggests some disinflationary momentum, but the ladder still prices a firm monthly gain."
  - "Rising oil prices cited in the Fox Business story could anchor the 0.5%+ range; the ladder's 91% above 0.4% reflects that floor."
  - "Resolution depends on BLS CPI release; gasoline and shelter components are the key swing variables given the oil price backdrop."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "August PCE inflation came in below the 3.3% expected, with core PCE at 3.0%, reinforcing a softer inflation narrative heading into the September CPI print."
    publisher: "Eric Revell"
    published_at: "2026-09-30T00:00:00.000Z"
    source_url: "https://www.foxbusiness.com/economy/august-2026-pce-inflation"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Eric Revell"
        source_url: "https://www.foxbusiness.com/economy/august-2026-pce-inflation"
        retrieved_at: "2026-10-03T07:47:35+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder distribution shows a tight consensus around 0.5%, with the soft PCE print not yet sufficient to push the implied level meaningfully lower."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Eric Revell: August PCE: Fed's favored inflation gauge rose less than expected | Fo"
    url: "https://www.foxbusiness.com/economy/august-2026-pce-inflation"
    published_at: "2026-09-30T00:00:00.000Z"
    retrieved_at: "2026-10-03T07:47:35+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
