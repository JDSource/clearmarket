---
signal_id: "CMSIG2026072607"
signal_slug: "democrats-win-us-house-next-election-kalshi-84-2026-07-26"
headline: "Democrats win US House next election: Kalshi 84%"
semantic_title: "Democrats winning the US House stays heavily favored at 84 percent"
telemetry: "Kalshi 84%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-26T00:00:00.000Z"
event_id: "CM-EVT-FV8MR86S63"
event_slug: "controlh-2026"
event_question: "Will the Democratic Party win the U.S. House in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "CONTROLH-2026-D"
  question_raw: "Will Democrats win the House in 2026?"
  current_price: 0.84
  volume_24h_usd: 8376.12
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "The Kalshi contract prices an 84% chance Democrats win the US House in the next election, resolving via Library of Congress."
  - "Democratic polling leads and a focused affordability message from Jeffries are consistent with the strong odds, but the market prices in that structural advantages matter."
  - "Companion Kalshi event CM-EVT-T5VXKJT451 puts only 43% on Republicans controlling at least one chamber after midterms, showing Democrats are favored in the House but the Senate remains contested."
  - "Redistricting gains for Republicans cited in news are already in the market; the 84% hold suggests traders view them as insufficient to overcome the Democratic polling advantage."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "House Democratic leader Hakeem Jeffries launched a 100-day sprint to midterms with an affordability agenda from battleground Pennsylvania, as Democrats lead in polls but face redistricting headwinds."
    publisher: "apnews.com"
    published_at: "2026-07-26T00:00:00.000Z"
    source_url: "https://apnews.com/article/house-midterms-election-affordability-trump-d1d9d0cd0c3ed3b53a7f812a6bd2e7a6"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/house-midterms-election-affordability-trump-d1d9d0cd0c3ed3b53a7f812a6bd2e7a6"
        retrieved_at: "2026-07-27T11:15:45+00:00"
  - type: "pm_response"
    notes: "Kalshi at 84% resolves via Library of Congress and represents the composite House control question, distinct from individual district markets also in this story group."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: Jeffries kicks off sprint to midterms with Democrats' affordability ag"
    url: "https://apnews.com/article/house-midterms-election-affordability-trump-d1d9d0cd0c3ed3b53a7f812a6bd2e7a6"
    published_at: "2026-07-26T00:00:00.000Z"
    retrieved_at: "2026-07-27T11:15:45+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
