---
signal_id: "CMSIG2026061408"
signal_slug: "save-act-becomes-law-kalshi-9-2026-06-14"
headline: "SAVE Act becomes law: Kalshi 9%"
semantic_title: "SAVE Act becoming law priced at deep discount despite White House push"
telemetry: "Kalshi 9%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-14T20:01:04.000Z"
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
  - "Kalshi prices only a 9% probability the SAVE Act becomes law, despite Trump tying it to FISA renewal as leverage."
  - "Markets are treating Trump's FISA linkage as a negotiating posture rather than a credible path to enactment, given the 9% read."
  - "The White House separately eyes July 4 passage for the CLARITY Act crypto bill; Congress is managing multiple legislative deadlines simultaneously."
  - "Resolves via the White House official record of enactment; the bar is presidential signature into law, not passage of either chamber alone."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "President Trump is conditioning his support for FISA renewal on Congress attaching the SAVE America Act voter ID bill."
    publisher: "Andrew Pantazi"
    published_at: "2026-06-14T20:01:04.000Z"
    source_url: "https://www.axios.com/2026/06/14/trump-fisa-renewal-save-america-act"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Andrew Pantazi"
        source_url: "https://www.axios.com/2026/06/14/trump-fisa-renewal-save-america-act"
        retrieved_at: "2026-06-16T12:50:14+00:00"
  - type: "pm_response"
    notes: "Kalshi's 9% read signals prediction markets regard the FISA-SAVE Act linkage as unlikely to convert into actual law, regardless of executive pressure."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Andrew Pantazi: Trump won't back FISA renewal without SAVE America Act voting bill"
    url: "https://www.axios.com/2026/06/14/trump-fisa-renewal-save-america-act"
    published_at: "2026-06-14T20:01:04.000Z"
    retrieved_at: "2026-06-16T12:50:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
