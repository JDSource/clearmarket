---
signal_id: "CMSIG2026071704"
signal_slug: "proof-of-citizenship-for-federal-voter-reg-kalshi-15-2026-07-17"
headline: "Proof of citizenship for federal voter reg: Kalshi 15%"
semantic_title: "Proof-of-citizenship voting rule wavers at slim 15 percent"
telemetry: "Kalshi 15%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-17T00:00:00.000Z"
event_id: "CM-EVT-G8CYMWNWC6"
event_slug: "kxelectionbill"
event_question: "Will proof of citizenship be required for federal voter registration?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXELECTIONBILL-27JAN01"
  question_raw: "Will legislation that requires proof of U.S. citizenship as a condition of registering to vote in federal elections become law before Jan 1, 2027?"
  current_price: 0.15
  volume_24h_usd: 845.59
  arbitration_model: "kalshi_staff"
  resolution_source: "White House"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi puts only 15% probability on proof of citizenship becoming a federal voter registration requirement."
  - "The SAVE Act's legislative stall, stuck between House and Senate despite GOP majorities, is consistent with the market's skeptical pricing."
  - "At 15%, the market is treating passage as a low-probability tail event, not a near-term policy shift."
  - "Resolves via White House confirmation of whether the requirement is signed into law."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump's SAVE America Act, which would require proof of citizenship for federal voter registration, remains stuck in Congress despite Republican control of both chambers."
    publisher: "SoRelle Wyckoff Gaynor"
    published_at: "2026-07-17T00:00:00.000Z"
    source_url: "https://theconversation.com/republicans-control-congress-so-why-is-trumps-save-america-act-stuck-287156"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "SoRelle Wyckoff Gaynor"
        source_url: "https://theconversation.com/republicans-control-congress-so-why-is-trumps-save-america-act-stuck-287156"
        retrieved_at: "2026-07-18T09:20:01+00:00"
  - type: "pm_response"
    notes: "Kalshi at 15% reflects legislative gridlock; the market is not pricing the SAVE Act as a near-term certainty despite administration rhetoric."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "SoRelle Wyckoff Gaynor: Republicans control Congress, so why is Trump’s SAVE America Act stuck"
    url: "https://theconversation.com/republicans-control-congress-so-why-is-trumps-save-america-act-stuck-287156"
    published_at: "2026-07-17T00:00:00.000Z"
    retrieved_at: "2026-07-18T09:20:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
