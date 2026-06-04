---
signal_id: "CMSIG2026060406"
signal_slug: "israel-lebanon-ceasefire-extension-by-june-7-polymarket-20-2026-06-04"
headline: "Israel-Lebanon ceasefire extension by June 7: Polymarket 20%"
semantic_title: "Israel-Lebanon ceasefire extension by June 7 a long shot"
telemetry: "Polymarket 20%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-04T06:47:34.000Z"
event_id: "CM-EVT-KFM6RVW5P7"
event_slug: "israel-announces-lebanon-ceasefire-extension-by"
event_question: "Israel announces Lebanon ceasefire extension by June 7?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x42973552f8bcfc9269fba8492766f2c20a22243cbba154cf695acaff88ec96c7"
  question_raw: "Israel announces Lebanon ceasefire extension by June 7?"
  current_price: 0.2
  volume_24h_usd: 44425.682103000014
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-07T00:00:00Z"
bullets:
  - "Polymarket prices 20% on Israel announcing a Lebanon ceasefire extension by June 7."
  - "A ceasefire renewal has been announced but Israel simultaneously declared continued operations in south Lebanon, creating ambiguity over whether the contract resolves yes."
  - "A companion Polymarket contract at 98% on an Israel-Lebanon diplomatic meeting by June 7 confirms talks are priced as near-certain; the extension itself remains uncertain."
  - "Resolves via uma_oracle; whether Israel's conditional ceasefire qualifies as a formal extension is the key settlement question."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Israel and Lebanon agreed to renew a ceasefire banning Hezbollah from pilot security zones in a US-brokered deal."
    publisher: "Press Association"
    published_at: "2026-06-04T06:47:34.000Z"
    source_url: "https://www.thejournal.ie/israel-and-lebanon-agree-to-renew-ceasefire-7059979-Jun2026/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Press Association"
        source_url: "https://www.thejournal.ie/israel-and-lebanon-agree-to-renew-ceasefire-7059979-Jun2026/"
        retrieved_at: "2026-06-04T11:14:54+00:00"
  - type: "pm_response"
    notes: "Polymarket resolves via uma_oracle; the gap between 98% for a meeting and 20% for a ceasefire extension captures the market's doubt about durability."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Press Association: Israel and Lebanon agree to renew ceasefire, with Hezbollah banned fro"
    url: "https://www.thejournal.ie/israel-and-lebanon-agree-to-renew-ceasefire-7059979-Jun2026/"
    published_at: "2026-06-04T06:47:34.000Z"
    retrieved_at: "2026-06-04T11:14:54+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
