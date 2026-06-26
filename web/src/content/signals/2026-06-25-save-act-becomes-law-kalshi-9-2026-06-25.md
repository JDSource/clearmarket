---
signal_id: "CMSIG2026062504"
signal_slug: "save-act-becomes-law-kalshi-9-2026-06-25"
headline: "SAVE Act becomes law: Kalshi 9%"
semantic_title: "SAVE Act becoming law wavers near long-shot pricing"
telemetry: "Kalshi 9%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-25T19:17:00.000Z"
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
  - "Kalshi prices only 9% on the SAVE Act becoming law, treating passage as a long-shot despite Trump's high-profile pressure campaign."
  - "Trump's leverage play, blocking a popular housing bill to force the SAVE Act, has not moved the Kalshi contract toward meaningful probability."
  - "The market is pricing the Senate Republican resistance as a significant obstacle; the standoff narrative is consistent with, not contradicted by, the 9% quote."
  - "Resolves via White House confirmation of enactment; the housing bill's veto-proof margins in both chambers are not captured by this contract but illustrate the legislative cross-pressure."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump conditioned his signature on a bipartisan housing bill on Senate passage of the SAVE America Act voter-eligibility measure, driving a congressional standoff."
    publisher: "cbsnews.com"
    published_at: "2026-06-25T19:17:00.000Z"
    source_url: "https://www.cbsnews.com/news/trump-save-america-act-house-senate-standoff/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cbsnews.com"
        source_url: "https://www.cbsnews.com/news/trump-save-america-act-house-senate-standoff/"
        retrieved_at: "2026-06-26T10:48:01+00:00"
  - type: "pm_response"
    notes: "Kalshi's 9% implies the market views Trump's gambit as unlikely to succeed within the resolution window, despite public pressure."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cbsnews.com: Trump's obsession with SAVE America Act drives Congress into a standof"
    url: "https://www.cbsnews.com/news/trump-save-america-act-house-senate-standoff/"
    published_at: "2026-06-25T19:17:00.000Z"
    retrieved_at: "2026-06-26T10:48:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
