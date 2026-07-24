---
signal_id: "CMSIG2026072308"
signal_slug: "trump-calls-for-thune-ouster-kalshi-39-2026-07-23"
headline: "Trump calls for Thune ouster: Kalshi 39%"
semantic_title: "Trump publicly calling out Thune stays below 40%"
telemetry: "Kalshi 39%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-23T00:00:00.000Z"
event_id: "CM-EVT-57VMK4QRS7"
event_slug: "kxtrumpthuneout-27jan01"
event_question: "Will Trump publicly call for John Thune to step down as Senate Majority Leader?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPTHUNEOUT-27JAN01"
  question_raw: "Will Donald Trump issue a statement about explicitly calling for John Thune to resign, step down, be replaced, or be removed from his position as Senate Majority Leader before Jan 1, 2027?"
  current_price: 0.39
  volume_24h_usd: 327.31
  arbitration_model: "kalshi_staff"
  resolution_source: "The Washington Post"
  resolves_at: "2027-01-08T15:00:00Z"
bullets:
  - "Kalshi prices a 39% chance Trump publicly calls for John Thune to step down as Senate Majority Leader."
  - "The White House warning that Trump's patience is running out is an escalation signal, yet Kalshi keeps the probability below 40%, the market is not pricing an imminent public break as the base case."
  - "The Trump-Thune rift is also entangled with the stalled election bill and the crypto CLARITY Act impasse, providing multiple pressure vectors that could move this probability higher."
  - "Kalshi resolves via The Washington Post reporting a public call by Trump; the distinction between private pressure and a public demand is the key resolution edge case."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Tension between President Trump and Senate Majority Leader John Thune intensified after the White House said Trump's patience on the stalled election bill is running out."
    publisher: "dnyuz.com"
    published_at: "2026-07-23T00:00:00.000Z"
    source_url: "https://dnyuz.com/2026/07/23/trump-thune-rift-intensifies-over-stalled-election-bill/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "dnyuz.com"
        source_url: "https://dnyuz.com/2026/07/23/trump-thune-rift-intensifies-over-stalled-election-bill/"
        retrieved_at: "2026-07-24T10:13:15+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 39% resolves via The Washington Post; the rift news is concurrent with the current price, not a post-event lagging read."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "dnyuz.com: Trump-Thune Rift Intensifies Over Stalled Election Bill, DNYUZ"
    url: "https://dnyuz.com/2026/07/23/trump-thune-rift-intensifies-over-stalled-election-bill/"
    published_at: "2026-07-23T00:00:00.000Z"
    retrieved_at: "2026-07-24T10:13:15+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
