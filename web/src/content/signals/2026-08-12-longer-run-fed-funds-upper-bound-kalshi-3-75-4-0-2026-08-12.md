---
signal_id: "CMSIG2026081203"
signal_slug: "longer-run-fed-funds-upper-bound-kalshi-3-75-4-0-2026-08-12"
headline: "Longer-run Fed funds upper bound: Kalshi 3.75-4.0%"
semantic_title: "Longer-run Fed funds rate seen settling near 3.75-4.0%"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-12T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Longer-run Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.22
  volume_24h_usd: 22.22
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder for a later Fed funds horizon implies a 3.75-4.0% upper bound: 81% above 3.50%, 51% above 3.75%, only 22% above 4.0%."
  - "Mild July CPI is consistent with a hold, but the ladder shows meaningful probability mass above the current 3.50-3.75% near-term range, reflecting lingering hike risk further out."
  - "The spread between this ladder and the post-September ladder (CM-EVT-4ZQLQPNH91, implied 3.50-3.75%) implies the market sees rates drifting slightly higher over a longer horizon."
  - "Resolves via Federal Reserve official rate decisions; the named source is the Federal Reserve itself."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US CPI rose just 0.1% in July, in line with expectations, easing pressure on the Federal Reserve ahead of September."
    publisher: "semafor.com"
    published_at: "2026-08-12T00:00:00.000Z"
    source_url: "https://www.semafor.com/article/08/12/2026/mild-us-inflation-eases-fed-pressure"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "semafor.com"
        source_url: "https://www.semafor.com/article/08/12/2026/mild-us-inflation-eases-fed-pressure"
        retrieved_at: "2026-08-15T08:21:50+00:00"
  - type: "pm_response"
    notes: "Kalshi's longer-horizon ladder sits about one quarter-point higher than the near-term ladder, capturing residual hike risk the September pause narrative does not fully eliminate."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "semafor.com: US inflation rises 0.1% in July, easing pressure on Fed | Semafor"
    url: "https://www.semafor.com/article/08/12/2026/mild-us-inflation-eases-fed-pressure"
    published_at: "2026-08-12T00:00:00.000Z"
    retrieved_at: "2026-08-15T08:21:50+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
