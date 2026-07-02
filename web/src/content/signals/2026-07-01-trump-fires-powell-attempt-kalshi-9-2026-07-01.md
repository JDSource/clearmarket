---
signal_id: "CMSIG2026070102"
signal_slug: "trump-fires-powell-attempt-kalshi-9-2026-07-01"
headline: "Trump fires Powell attempt: Kalshi 9%"
semantic_title: "Market absorbs Warsh independence stance, Trump-fires-Powell risk stays low"
telemetry: "Kalshi 9%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-01T16:20:16.000Z"
event_id: "CM-EVT-TMHG8WLK69"
event_slug: "kxtryfirepowell-26may12"
event_question: "Will Trump attempt to fire Powell as Federal Reserve Chair or Governor?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRYFIREPOWELL-26MAY12-GOV2"
  question_raw: "Will the President try to fire the Jerome Powell as either Chair of the Board of Governors of the Federal Reserve System or Member of the Board of Governors of the Federal Reserve System before Jan 1, 2027?"
  current_price: 0.093
  volume_24h_usd: 4.84
  arbitration_model: "kalshi_staff"
  resolution_source: "ABC"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prediction market prices only 9% on Trump attempting to fire Powell as Fed Chair or Governor."
  - "Warsh's independence language is consistent with the low probability, the market is not pricing a near-term constitutional confrontation at the Fed."
  - "A companion Kalshi contract puts just 7% on a Fed cut exceeding 25 basis points in a single meeting, suggesting markets also read Warsh's inflation focus as credibly hawkish."
  - "Resolves via ABC News confirmation of a formal Trump attempt to remove Powell; the legal question of whether such removal is permissible is separate from the trigger event."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "New Fed Chair Kevin Warsh publicly stressed the Federal Reserve's political independence and signaled a sustained focus on bringing inflation down."
    publisher: "pbs.org"
    published_at: "2026-07-01T16:20:16.000Z"
    source_url: "https://www.pbs.org/newshour/economy/federal-reserve-chair-warsh-emphasizes-political-independence-signals-focus-on-inflation"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "pbs.org"
        source_url: "https://www.pbs.org/newshour/economy/federal-reserve-chair-warsh-emphasizes-political-independence-signals-focus-on-inflation"
        retrieved_at: "2026-07-02T10:34:14+00:00"
  - type: "pm_response"
    notes: "Kalshi's 9% on a Trump-Powell firing attempt reflects markets treating Warsh's independence posture as a stabilizing signal rather than a provocation."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "pbs.org: Federal Reserve Chair Warsh emphasizes political independence, signals"
    url: "https://www.pbs.org/newshour/economy/federal-reserve-chair-warsh-emphasizes-political-independence-signals-focus-on-inflation"
    published_at: "2026-07-01T16:20:16.000Z"
    retrieved_at: "2026-07-02T10:34:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
