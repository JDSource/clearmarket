---
signal_id: "CMSIG2026092303"
signal_slug: "democrats-win-or-3-house-seat-kalshi-93-2026-09-23"
headline: "Democrats win OR-3 House seat: Kalshi 93%"
semantic_title: "Democrats heavily favored in Oregon 3rd District House race"
telemetry: "Kalshi 93%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-23T13:06:58.311Z"
event_id: "CM-EVT-98TTCLWRD8"
event_slug: "kxmidtermmov-or03d"
event_question: "Will the margin of victory for Democrats in the Oregon's 3rd District House election be at least 38 percentage points?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMIDTERMMOV-OR03D-P38"
  question_raw: "Will the margin of victory for Democrats in the Oregon's 3rd District House election be at least 38 percentage points?"
  current_price: 0.93
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "official election authority responsible for certifying results in <geography>"
  resolves_at: "2027-11-03T15:00:00Z"
bullets:
  - "Kalshi prices Democratic victory in Oregon's 3rd District House race at 93%, a heavy favorite reading."
  - "The PBS poll showing Democrats with a large national lead among independents is consistent with the lopsided Kalshi contract on this safely Democratic seat."
  - "Companion Kalshi contract on Republicans holding more governorships than Democrats after the midterms sits at 71%, pointing to a split picture: Democrats strong in blue districts, Republicans still favored on governors."
  - "Resolves via the official election authority responsible for certifying the Oregon 3rd District result."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A new PBS poll shows Democratic congressional candidates holding a significant lead over Republicans nationally, with independents breaking sharply against President Trump heading into the midterms."
    publisher: "PBS"
    published_at: "2026-09-23T13:06:58.311Z"
    source_url: "https://www.pbs.org/newshour/politics/democrats-lead-in-new-poll-as-trump-looms-over-midterms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "PBS"
        source_url: "https://www.pbs.org/newshour/politics/democrats-lead-in-new-poll-as-trump-looms-over-midterms"
        retrieved_at: "2026-09-24T13:07:56+00:00"
  - type: "pm_response"
    notes: "Kalshi's 93% on OR-3 reflects a safe Democratic district; the more contested midterm picture is captured in the 62% Republicans-hold-one-chamber contract (CM-EVT-T5VXKJT451)."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "PBS: Democrats hold midterm lead with independents breaking sharply against"
    url: "https://www.pbs.org/newshour/politics/democrats-lead-in-new-poll-as-trump-looms-over-midterms"
    published_at: "2026-09-23T13:06:58.311Z"
    retrieved_at: "2026-09-24T13:07:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
