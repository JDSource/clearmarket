---
signal_id: "CMSIG2026060804"
signal_slug: "fed-cut-over-25bps-in-single-move-kalshi-10-2026-06-08"
headline: "Fed cut over 25bps in single move: Kalshi 10%"
semantic_title: "Jumbo Fed cut pricing collapses to 10 percent"
telemetry: "Kalshi 10%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-08T02:41:03.000Z"
event_id: "CM-EVT-RWRZ1R3SD6"
event_slug: "kxlargecut-26"
event_question: "Will the Federal Reserve cut interest rates by more than 25 basis points in a single action this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLARGECUT-26"
  question_raw: "Will the Fed cut rates more than 25 bps in 2026?"
  current_price: 0.104
  volume_24h_usd: 26.64
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only a 10% chance the Fed cuts by more than 25 basis points in any single meeting."
  - "May's blowout payroll print is consistent with this low probability; no macro catalyst supports jumbo-cut pricing."
  - "Combined with the 19% on any cut before 2027, the market is pricing out both the timing and magnitude of near-term easing."
  - "Resolves via the Federal Reserve's official policy statement; a 50bp or larger single-meeting cut is required for YES resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Kevin Warsh faces his first policy test as the May jobs surge reinforces the case against early or aggressive monetary easing."
    publisher: "Martin Thomas"
    published_at: "2026-06-08T02:41:03.000Z"
    source_url: "https://www.prof-fx.com/p/us-jobs-surge-reinforces-hawkish-fed-bias-as-kevin-warsh-faces-first-policy-test/17204/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Martin Thomas"
        source_url: "https://www.prof-fx.com/p/us-jobs-surge-reinforces-hawkish-fed-bias-as-kevin-warsh-faces-first-policy-test/17204/"
        retrieved_at: "2026-06-09T10:57:53+00:00"
  - type: "pm_response"
    notes: "Kalshi's 10% on a jumbo cut and 19% on any cut form a coherent, hawkish term structure consistent with current jobs data."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Martin Thomas: US Jobs Surge Reinforces Hawkish Fed Bias as Kevin Warsh Faces First P"
    url: "https://www.prof-fx.com/p/us-jobs-surge-reinforces-hawkish-fed-bias-as-kevin-warsh-faces-first-policy-test/17204/"
    published_at: "2026-06-08T02:41:03.000Z"
    retrieved_at: "2026-06-09T10:57:53+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
