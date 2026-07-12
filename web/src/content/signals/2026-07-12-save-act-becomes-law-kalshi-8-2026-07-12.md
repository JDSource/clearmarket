---
signal_id: "CMSIG2026071205"
signal_slug: "save-act-becomes-law-kalshi-8-2026-07-12"
headline: "SAVE Act becomes law: Kalshi 8%"
semantic_title: "SAVE Act passage pricing collapses as Trump withholds housing bill"
telemetry: "Kalshi 8%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-12T01:26:45.000Z"
event_id: "CM-EVT-QFC5QGJS96"
event_slug: "kxsaveact-27"
event_question: "Will the SAVE Act become law?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSAVEACT-27-JAN04"
  question_raw: "Will \"SAVE Act\" (H.R. 22) becomes law before Jan 4, 2027?"
  current_price: 0.079
  volume_24h_usd: 3278.87
  arbitration_model: "kalshi_staff"
  resolution_source: "White House"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices only an 8% probability that the SAVE Act becomes law, via White House resolution."
  - "Trump's public pressure tactic linking the housing bill to SAVE Act passage has not moved Kalshi's implied probability meaningfully off its low base."
  - "The market is treating Trump's leverage play as unlikely to succeed legislatively, consistent with Senate resistance to the SAVE Act."
  - "Resolves via White House confirmation of presidential signature; the housing bill auto-enacting without signature does not resolve this contract."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "President Trump refused to sign the bipartisan 21st Century ROAD to Housing Act, using it as leverage to pressure the Senate into passing the SAVE America Act voter ID legislation."
    publisher: "by"
    published_at: "2026-07-12T01:26:45.000Z"
    source_url: "https://latimesnow.com/2026/07/12/trump-wont-sign-housing-bill-in-save-america-act-protest/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "by"
        source_url: "https://latimesnow.com/2026/07/12/trump-wont-sign-housing-bill-in-save-america-act-protest/"
        retrieved_at: "2026-07-12T09:47:51+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via White House; Trump's stated refusal to sign the housing bill is the stated mechanism of pressure, but market assigns low odds to the endgame."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "by: Trump won't sign housing bill, in SAVE America Act protest - LA Times"
    url: "https://latimesnow.com/2026/07/12/trump-wont-sign-housing-bill-in-save-america-act-protest/"
    published_at: "2026-07-12T01:26:45.000Z"
    retrieved_at: "2026-07-12T09:47:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
