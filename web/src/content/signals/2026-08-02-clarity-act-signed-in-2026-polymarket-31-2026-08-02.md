---
signal_id: "CMSIG2026080206"
signal_slug: "clarity-act-signed-in-2026-polymarket-31-2026-08-02"
headline: "CLARITY Act signed in 2026: Polymarket 31%"
semantic_title: "CLARITY Act signed into law in 2026 stays a long shot"
telemetry: "Polymarket 31%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-02T00:00:00.000Z"
event_id: "CM-EVT-ZXN47LV744"
event_slug: "clarity-act-signed-into-law-in-2026"
event_question: "Will the Clarity Act be signed into law in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9cb23d04b2ded06147482076688b69b487a8d982c63ebdda2ab3678cf27cf390"
  question_raw: "Clarity Act signed into law in 2026?"
  current_price: 0.31
  volume_24h_usd: 109623.90994699995
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "The Polymarket contract puts 31% odds on the CLARITY Act being signed into law in 2026."
  - "The coordinated White House and SEC push on the Senate is a meaningful escalation, but the market at 31% reflects skepticism that legislative timing will align before year-end."
  - "The STS Digital CEO's warning of delayed US crypto regulation as a headwind is broadly consistent with the market staying well below 50%."
  - "The Kalshi contract on Republicans controlling at least one chamber after the midterms sits at 46%, meaning post-midterm legislative dynamics add further uncertainty to the 2026 window."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The Trump administration and crypto industry launched a multi-agency pressure campaign on the Senate to pass the CLARITY Act this week."
    publisher: "bitrss.com"
    published_at: "2026-08-02T00:00:00.000Z"
    source_url: "https://bitrss.com/clarity-act-faces-white-house-blitz-as-treasury-and-sec-flood-senate-with-coordinated-pressure-this-week-200070"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "bitrss.com"
        source_url: "https://bitrss.com/clarity-act-faces-white-house-blitz-as-treasury-and-sec-flood-senate-with-coordinated-pressure-this-week-200070"
        retrieved_at: "2026-08-02T09:52:49+00:00"
  - type: "pm_response"
    notes: "Polymarket at 31% resolves via UMA oracle; the market prices the lobbying blitz as a nudge, not a near-certain catalyst for passage."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "bitrss.com: CLARITY Act faces White House blitz as Treasury and SEC flood Senate w"
    url: "https://bitrss.com/clarity-act-faces-white-house-blitz-as-treasury-and-sec-flood-senate-with-coordinated-pressure-this-week-200070"
    published_at: "2026-08-02T00:00:00.000Z"
    retrieved_at: "2026-08-02T09:52:49+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
