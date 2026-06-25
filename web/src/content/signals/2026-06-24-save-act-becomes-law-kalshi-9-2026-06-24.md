---
signal_id: "CMSIG2026062406"
signal_slug: "save-act-becomes-law-kalshi-9-2026-06-24"
headline: "SAVE Act becomes law: Kalshi 9%"
semantic_title: "SAVE Act becoming law holds at deep discount despite Trump leverage"
telemetry: "Kalshi 9%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-24T13:58:00.000Z"
event_id: "CM-EVT-QFC5QGJS96"
event_slug: "kxsaveact-27"
event_question: "Will the SAVE Act become law?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSAVEACT-27-JAN04"
  question_raw: "Will \"SAVE Act\" (H.R. 22) becomes law before Jan 4, 2027?"
  current_price: 0.091
  volume_24h_usd: 1388.98
  arbitration_model: "kalshi_staff"
  resolution_source: "White House"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices only a 9% probability the SAVE Act becomes law, unchanged despite Trump's public pressure campaign."
  - "Trump's housing bill hostage-taking adds political leverage, but the market treats Senate passage of SAVE Act as still highly unlikely."
  - "The separate Kalshi contract on at least one reconciliation bill passing in 2026 sits at 90%, showing broader legislative optimism excludes the SAVE Act."
  - "Resolves via White House confirmation of presidential signature; Senate floor vote is the primary bottleneck per the resolution mechanic."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "President Trump cancelled the signing of a bipartisan housing affordability bill, conditioning it on congressional passage of the SAVE Act voter ID measure."
    publisher: "cbsnews.com"
    published_at: "2026-06-24T13:58:00.000Z"
    source_url: "https://www.cbsnews.com/news/trump-signs-housing-bill-capitol/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cbsnews.com"
        source_url: "https://www.cbsnews.com/news/trump-signs-housing-bill-capitol/"
        retrieved_at: "2026-06-25T10:38:54+00:00"
  - type: "pm_response"
    notes: "Kalshi holds SAVE Act odds at 9%, treating Trump's leverage play as insufficient to overcome Senate resistance to the voter ID bill."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cbsnews.com: Trump cancels bipartisan housing bill signing, reiterates demand for S"
    url: "https://www.cbsnews.com/news/trump-signs-housing-bill-capitol/"
    published_at: "2026-06-24T13:58:00.000Z"
    retrieved_at: "2026-06-25T10:38:54+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
