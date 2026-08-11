---
signal_id: "CMSIG2026081103"
signal_slug: "july-2026-cpi-monthly-change-seen-0-0-to-0-1-ladder-2026-08-11"
headline: "July 2026 CPI monthly change seen 0.0% to +0.1%: ladder"
semantic_title: "July CPI monthly change priced near flat to slightly negative"
telemetry: "Kalshi ladder"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-08-11T08:47:04.772Z"
event_id: "CM-EVT-HVKDYMRT39"
event_slug: "kxcpi-26jul"
event_question: "July 2026 CPI monthly change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26JUL-T0.1"
  question_raw: "Will CPI rise more than 0.1% in July 2026?"
  current_price: 0.17
  volume_24h_usd: 3829.12
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-11-11T13:56:00Z"
bullets:
  - "The prediction market ladder prices the July 2026 CPI monthly change in the 0.0% to +0.1% range: 60% above 0.0%, only 17% above +0.1%."
  - "June CPI (333.95) was actually lower than May (335.12), consistent with the ladder's tilt toward a flat or marginally positive July print."
  - "A near-zero monthly CPI would reinforce the weak-jobs narrative driving the S&P record and keep Fed hike bets capped near 60%."
  - "Resolution depends on the Bureau of Labor Statistics CPI release; any upside surprise above +0.2% is priced at only 7% probability."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "CPI data showing stagnant consumer prices in recent months sets the stage for the July inflation report now in focus."
    publisher: "exa.ai"
    published_at: "2026-08-11T08:47:04.772Z"
    source_url: "https://exa.ai/library/markets/economy/inflation?date=2026-08-11"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "exa.ai"
        source_url: "https://exa.ai/library/markets/economy/inflation?date=2026-08-11"
        retrieved_at: "2026-08-11T08:49:29+00:00"
  - type: "pm_response"
    notes: "Ladder distribution; resolution source unspecified but tracks BLS CPI release; sharp drop from 60% at 0.0% to 17% at +0.1% marks the consensus ceiling."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "exa.ai: U.S. Inflation, Consumer Price Index for all Urban Consumers: 333.95"
    url: "https://exa.ai/library/markets/economy/inflation?date=2026-08-11"
    published_at: "2026-08-11T08:47:04.772Z"
    retrieved_at: "2026-08-11T08:49:29+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
