---
signal_id: "CMSIG2026071208"
signal_slug: "save-act-becomes-law-kalshi-8-2026-07-12"
headline: "SAVE Act becomes law: Kalshi 8%"
semantic_title: "SAVE Act becoming law prices as a deep long-shot on Kalshi"
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
  current_price: 0.077
  volume_24h_usd: 3870.68
  arbitration_model: "kalshi_staff"
  resolution_source: "White House"
  resolves_at: "2027-01-04T15:00:00Z"
bullets:
  - "Kalshi prices only 8% on the SAVE Act becoming law, resolving via White House confirmation."
  - "Trump's refusal to sign the housing bill as a protest against the SAVE Act suggests active presidential opposition; the 8% is consistent with that stance."
  - "No companion market available with a price to benchmark the SAVE Act probability against a broader legislative timeline."
  - "Resolves via White House; the automatic-law mechanism for the housing bill does not apply to the SAVE Act, which requires affirmative action."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "President Trump declined to sign the bipartisan housing bill passed in June, allowing it to become law automatically, while withholding his signature as a protest over the SAVE America Act."
    publisher: "by"
    published_at: "2026-07-12T01:26:45.000Z"
    source_url: "https://latimesnow.com/2026/07/12/trump-wont-sign-housing-bill-in-save-america-act-protest/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "by"
        source_url: "https://latimesnow.com/2026/07/12/trump-wont-sign-housing-bill-in-save-america-act-protest/"
        retrieved_at: "2026-07-13T10:56:18+00:00"
  - type: "pm_response"
    notes: "Kalshi at 8% prices the SAVE Act as a near-dead legislative priority, consistent with Trump's active protest posture described in the news."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "by: Trump won't sign housing bill, in SAVE America Act protest - LA Times"
    url: "https://latimesnow.com/2026/07/12/trump-wont-sign-housing-bill-in-save-america-act-protest/"
    published_at: "2026-07-12T01:26:45.000Z"
    retrieved_at: "2026-07-13T10:56:18+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
