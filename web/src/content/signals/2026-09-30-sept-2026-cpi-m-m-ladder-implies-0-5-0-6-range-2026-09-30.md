---
signal_id: "CMSIG2026093004"
signal_slug: "sept-2026-cpi-m-m-ladder-implies-0-5-0-6-range-2026-09-30"
headline: "Sept 2026 CPI m/m: ladder implies 0.5%-0.6% range"
semantic_title: "September CPI seen in the 0.5 percent range by markets"
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
  current_price: 0.2
  volume_24h_usd: 144.66
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-01-13T13:56:00Z"
bullets:
  - "The CPI ladder for September 2026 implies a monthly gain in the 0.5%-0.6% range: 91% above 0.4%, 59% above 0.5%, but only 20% above 0.6%."
  - "August PCE core held at 3.0% versus a 3.3% consensus expectation, a cooler-than-feared print; yet the September CPI ladder still prices meaningful inflation, not a collapse."
  - "The sharp drop from 59% to 20% between the 0.5% and 0.6% strikes marks the market's conviction line, above 0.6% is a tail outcome."
  - "Minneapolis Fed President Neel Kashkari said inflation remains 'too high' even after the softer PCE print, consistent with the ladder's pricing of continued positive monthly CPI gains."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "August PCE inflation came in below expectations at 3.0% core year-over-year, with the Fed's preferred gauge rising less than forecast."
    publisher: "Eric Revell"
    published_at: "2026-09-30T00:00:00.000Z"
    source_url: "https://www.foxbusiness.com/economy/august-2026-pce-inflation"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Eric Revell"
        source_url: "https://www.foxbusiness.com/economy/august-2026-pce-inflation"
        retrieved_at: "2026-10-02T14:25:25+00:00"
  - type: "pm_response"
    notes: "The ladder is sourced from prediction market strikes; no single-venue binary price is available for September CPI month-over-month."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Eric Revell: August PCE: Fed's favored inflation gauge rose less than expected | Fo"
    url: "https://www.foxbusiness.com/economy/august-2026-pce-inflation"
    published_at: "2026-09-30T00:00:00.000Z"
    retrieved_at: "2026-10-02T14:25:25+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
