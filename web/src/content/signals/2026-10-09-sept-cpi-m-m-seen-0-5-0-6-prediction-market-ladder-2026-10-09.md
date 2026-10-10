---
signal_id: "CMSIG2026100903"
signal_slug: "sept-cpi-m-m-seen-0-5-0-6-prediction-market-ladder-2026-10-09"
headline: "Sept CPI m/m seen 0.5-0.6%: prediction market ladder"
semantic_title: "September CPI monthly gain priced near 0.5 percent"
telemetry: "Kalshi ladder"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-10-09T00:00:00.000Z"
event_id: "CM-EVT-F9NPW9F1V9"
event_slug: "kxcpi-26sep"
event_question: "September 2026 CPI month-over-month change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26SEP-T0.6"
  question_raw: "Will CPI rise more than 0.6% in September 2026?"
  current_price: 0.21
  volume_24h_usd: 7002.53
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-01-13T13:56:00Z"
bullets:
  - "The prediction market ladder implies a September CPI monthly gain in the 0.5-0.6% range: 59% above 0.5%, but only 21% above 0.6%."
  - "August PCE cooling more than expected has not pulled the ladder's implied CPI print lower; the market still prices a firm monthly gain consistent with above-target inflation."
  - "October 14 CPI is the next live catalyst; the 59%-to-21% drop between the 0.5% and 0.6% strikes marks the distribution's sharp upper tail."
  - "Resolution is via the official CPI release; the named resolution source is not further specified, but the standard resolver is the Bureau of Labor Statistics CPI report."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Fed's preferred inflation gauge cooled more than expected in August but remained well above target, keeping price-pressure concerns alive ahead of October 14 CPI."
    publisher: "Press Room"
    published_at: "2026-10-09T00:00:00.000Z"
    source_url: "https://fundingconceptpros.com/feds-favored-inflation-gauge-cooled-in-august-but-remained-elevated/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Press Room"
        source_url: "https://fundingconceptpros.com/feds-favored-inflation-gauge-cooled-in-august-but-remained-elevated/"
        retrieved_at: "2026-10-10T07:47:51+00:00"
  - type: "pm_response"
    notes: "Ladder distribution provided; market-implied range read from strike probabilities at 0.5% and 0.6% thresholds."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Press Room: Fed's favored inflation gauge cooled in August but remained elevated |"
    url: "https://fundingconceptpros.com/feds-favored-inflation-gauge-cooled-in-august-but-remained-elevated/"
    published_at: "2026-10-09T00:00:00.000Z"
    retrieved_at: "2026-10-10T07:47:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
