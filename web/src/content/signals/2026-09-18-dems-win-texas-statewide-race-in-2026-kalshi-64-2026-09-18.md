---
signal_id: "CMSIG2026091804"
signal_slug: "dems-win-texas-statewide-race-in-2026-kalshi-64-2026-09-18"
headline: "Dems win Texas statewide race in 2026: Kalshi 64%"
semantic_title: "Democrats winning Texas statewide in 2026 holds near 64%"
telemetry: "Kalshi 64%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-18T07:46:14.460Z"
event_id: "CM-EVT-NQQNC9S0P9"
event_slug: "kxanydemwintexas-26nov03"
event_question: "Will Democrats win any statewide election in Texas in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXANYDEMWINTEXAS-26NOV03"
  question_raw: "Will the number of Democrats who win a statewide election in Texas in 2026 be above 0?"
  current_price: 0.64
  volume_24h_usd: 3.2
  arbitration_model: "kalshi_staff"
  resolution_source: "The Source Agencies are"
  resolves_at: "2027-11-02T14:00:00Z"
bullets:
  - "Kalshi puts 64% odds on Democrats winning at least one statewide election in Texas in 2026, a historically rare outcome."
  - "Reporting describes Talarico consistently leading Paxton in polls two months out, with national forecasters calling Texas competitive, consistent with the above-50% pricing."
  - "A 64% read suggests the market sees Talarico's lead as real but not dominant, reflecting Texas's long Republican lean and the race's remaining uncertainty."
  - "Resolves via Texas state government certification; the question requires at least one Democratic statewide win, so a single Senate upset is sufficient."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Democrat James Talarico is consistently polling ahead of Ken Paxton in Texas, with national forecasters calling the race a toss-up or leaning Democratic."
    publisher: "Eleanor Klibanoff"
    published_at: "2026-09-18T07:46:14.460Z"
    source_url: "https://www.texastribune.org/2026/09/17/democrats-texas-james-talarico-november-midterms/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Eleanor Klibanoff"
        source_url: "https://www.texastribune.org/2026/09/17/democrats-texas-james-talarico-november-midterms/"
        retrieved_at: "2026-09-20T07:47:17+00:00"
  - type: "pm_response"
    notes: "Kalshi at 64% reflects an unusual competitive positioning for Texas statewide races, consistent with polling cited in the news but not a lock."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Eleanor Klibanoff: “Uncharted territory”: Two months from Election Day, Democrats in Texa"
    url: "https://www.texastribune.org/2026/09/17/democrats-texas-james-talarico-november-midterms/"
    published_at: "2026-09-18T07:46:14.460Z"
    retrieved_at: "2026-09-20T07:47:17+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
