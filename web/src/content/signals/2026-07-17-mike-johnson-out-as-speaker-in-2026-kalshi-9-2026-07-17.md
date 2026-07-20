---
signal_id: "CMSIG2026071706"
signal_slug: "mike-johnson-out-as-speaker-in-2026-kalshi-9-2026-07-17"
headline: "Mike Johnson out as Speaker in 2026: Kalshi 9%"
semantic_title: "Johnson speaker exit in 2026 holds at low probability"
telemetry: "Kalshi 9%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-17T00:00:00.000Z"
event_id: "CM-EVT-YSH7DQ1TV1"
event_slug: "kxsothleave-26"
event_question: "Will Mike Johnson be out as Speaker of the House in 2026? (multi-deadline series)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSOTHLEAVE-26-NOV"
  question_raw: "Will Mike Johnson no longer be Speaker of the House before 2026?"
  current_price: 0.093
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi prices only 9% on Mike Johnson losing the Speaker role in 2026."
  - "Trump's speech upending House Republican plans is a real pressure point, but the market sees it as unlikely to cost Johnson the speakership."
  - "The low 9% is consistent with Johnson retaining Trump's backing; the lobbying effort itself signals a working relationship rather than a rupture."
  - "Resolves via The New York Times confirmation; a speakership vote or Johnson resignation before year-end would settle the Kalshi contract YES."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "House Speaker Mike Johnson is privately lobbying President Trump after Trump's election speech scrambled Republican legislative strategy heading into SAVE America Act negotiations."
    publisher: "Eren Waris"
    published_at: "2026-07-17T00:00:00.000Z"
    source_url: "https://news.meaww.com/what-mike-johnson-is-privately-asking-trump-to-do-after-his-speech-scrambled-gop-plans"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Eren Waris"
        source_url: "https://news.meaww.com/what-mike-johnson-is-privately-asking-trump-to-do-after-his-speech-scrambled-gop-plans"
        retrieved_at: "2026-07-20T10:47:34+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolved by The New York Times; current pricing reflects that intra-party tension rarely translates to a speaker removal."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Eren Waris: What Mike Johnson is privately asking Trump to do after his speech scr"
    url: "https://news.meaww.com/what-mike-johnson-is-privately-asking-trump-to-do-after-his-speech-scrambled-gop-plans"
    published_at: "2026-07-17T00:00:00.000Z"
    retrieved_at: "2026-07-20T10:47:34+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
