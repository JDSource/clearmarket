---
signal_id: "CMSIG2026081904"
signal_slug: "fed-cut-greater-than-25bp-in-2026-kalshi-6-2026-08-19"
headline: "Fed cut greater than 25bp in 2026: Kalshi 6%"
semantic_title: "Odds on a large Fed rate cut this year remain a long shot"
telemetry: "Kalshi 6%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-19T00:00:00.000Z"
event_id: "CM-EVT-RWRZ1R3SD6"
event_slug: "kxlargecut-26"
event_question: "Will the Federal Reserve do a rate cut greater than 25 basis points this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLARGECUT-26"
  question_raw: "Will the Fed cut rates more than 25 bps in 2026?"
  current_price: 0.06
  volume_24h_usd: 12.21
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi contract puts only 6% probability on the Fed cutting by more than 25 basis points at any 2026 meeting."
  - "With the July FOMC minutes flagging potential hikes and debt crossing $40 trillion adding fiscal complexity, the Kalshi pricing treats any large cut as a remote tail."
  - "This is directionally consistent with the Kalshi near-term funds rate ladder implying a hold-to-hike bias, not an easing cycle."
  - "Resolves via Federal Reserve official rate decision; a cut greater than 25bp would require a sharp pivot from the current committee posture."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US debt crossed $40 trillion, adding fiscal pressure context as Fed minutes simultaneously showed officials leaning toward hikes rather than cuts."
    publisher: "David Lawder"
    published_at: "2026-08-19T00:00:00.000Z"
    source_url: "https://www.reuters.com/world/us-debt-crosses-40-trillion-threshold-after-doubling-under-trump-biden-2026-08-19/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "David Lawder"
        source_url: "https://www.reuters.com/world/us-debt-crosses-40-trillion-threshold-after-doubling-under-trump-biden-2026-08-19/"
        retrieved_at: "2026-08-21T08:35:01+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via the Federal Reserve; the 6% price reflects strong cross-market coherence with hawkish FOMC signaling."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "David Lawder: US debt crosses $40 trillion threshold after doubling under Trump and"
    url: "https://www.reuters.com/world/us-debt-crosses-40-trillion-threshold-after-doubling-under-trump-biden-2026-08-19/"
    published_at: "2026-08-19T00:00:00.000Z"
    retrieved_at: "2026-08-21T08:35:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
