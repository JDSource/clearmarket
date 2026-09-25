---
signal_id: "CMSIG2026092403"
signal_slug: "republicans-hold-governorship-edge-post-midterms-kalshi-70-2026-09-24"
headline: "Republicans hold governorship edge post-midterms: Kalshi 70%"
semantic_title: "Republicans holding more governorships after midterms stays near 75%"
telemetry: "Kalshi 70%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-24T07:46:42.584Z"
event_id: "CM-EVT-4DFCBXLZN6"
event_slug: "kxgovwins-27jan01"
event_question: "Will Republicans hold more governorships than Democrats after the midterms?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVWINS-27JAN01-R-50"
  question_raw: "Will the difference between the number of Republican governors and the number of Democratic governors be between -50 and -1 governors after the 2026 midterms?"
  current_price: 0.7
  volume_24h_usd: 80.12
  arbitration_model: "kalshi_staff"
  resolution_source: "the Statistical Review of World Energy"
  resolves_at: "2027-04-01T15:00:00Z"
bullets:
  - "Kalshi prices a 70% chance Republicans hold more governorships than Democrats after the 2026 midterms."
  - "The Democratic polling lead in congressional races has not shifted the governorship market, governors and House seats move on different electoral maps."
  - "Senate rejection of the Iran war powers resolution (Story 15) and the pre-election rate hike backdrop may compound Republican headwinds, but the governorship market holds above two-thirds."
  - "Resolves via the Statistical Review of World Energy as named resolution source, an unusual resolver; traders should confirm the resolution criteria carefully."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A new poll shows Democratic congressional candidates holding a significant lead over Republicans, with independents breaking sharply against President Trump ahead of the midterms."
    publisher: "PBS"
    published_at: "2026-09-24T07:46:42.584Z"
    source_url: "https://www.pbs.org/newshour/politics/democrats-lead-in-new-poll-as-trump-looms-over-midterms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "PBS"
        source_url: "https://www.pbs.org/newshour/politics/democrats-lead-in-new-poll-as-trump-looms-over-midterms"
        retrieved_at: "2026-09-25T07:47:46+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 70%; resolution source listed as the Statistical Review of World Energy, which warrants scrutiny for a US gubernatorial outcome."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "PBS: Democrats hold midterm lead with independents breaking sharply against"
    url: "https://www.pbs.org/newshour/politics/democrats-lead-in-new-poll-as-trump-looms-over-midterms"
    published_at: "2026-09-24T07:46:42.584Z"
    retrieved_at: "2026-09-25T07:47:46+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
