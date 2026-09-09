---
signal_id: "CMSIG2026090704"
signal_slug: "peak-unemployment-below-4-5-before-2027-kalshi-84-2026-09-07"
headline: "Peak unemployment below 4.5% before 2027: Kalshi 84%"
semantic_title: "Unemployment staying below 4.5 percent remains the consensus"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-07T00:00:00.000Z"
event_id: "CM-EVT-RBY62SKLC0"
event_slug: "kxu3max-27"
event_question: "Peak US unemployment rate before 2027"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3MAX-27-4.5"
  question_raw: "How high will unemployment get before 2027?"
  current_price: 0.16
  volume_24h_usd: 0.8
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-03-09T15:00:00Z"
bullets:
  - "Kalshi ladder implies peak unemployment before 2027 stays below 4.5%: only 16% probability at the 4.5% strike, with higher strikes pricing 7% or less."
  - "The blowout jobs report is consistent with this low-peak pricing; the market is not treating the strong payroll print as a precursor to labor market deterioration."
  - "Above 5.0% unemployment before 2027 prices at just 2%, reflecting near-full market dismissal of a recession-level labor shock this cycle."
  - "Resolution via Kalshi; the contract tracks the highest monthly unemployment rate reported by the Bureau of Labor Statistics before January 2027."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "August payrolls of 162,000 beat forecasts by roughly three times, reinforcing a resilient labor market picture as the Fed debates rate hikes."
    publisher: "gryphonfp.com"
    published_at: "2026-09-07T00:00:00.000Z"
    source_url: "https://gryphonfp.com/blog/162000-jobs-a-smaller-labor-force-and-a-fed-that-is-arguing-about-hikes/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "gryphonfp.com"
        source_url: "https://gryphonfp.com/blog/162000-jobs-a-smaller-labor-force-and-a-fed-that-is-arguing-about-hikes/"
        retrieved_at: "2026-09-09T12:40:02+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder prices unemployment risk as heavily left-tailed; sub-4.5% peak is the strong consensus consistent with the current jobs resilience narrative."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "gryphonfp.com: 162,000 Jobs, a Smaller Labor Force, and a Fed That Is Arguing About H"
    url: "https://gryphonfp.com/blog/162000-jobs-a-smaller-labor-force-and-a-fed-that-is-arguing-about-hikes/"
    published_at: "2026-09-07T00:00:00.000Z"
    retrieved_at: "2026-09-09T12:40:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
