---
signal_id: "CMSIG2026092001"
signal_slug: "fed-funds-upper-bound-seen-4-0-4-25-kalshi-ladder-2026-09-20"
headline: "Fed funds upper bound seen 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound priced in the 4 to 4.25 percent range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-20T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound post-September 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.35
  volume_24h_usd: 107.22
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the federal funds upper bound in the 4.0-4.25% range: 85% above 4.0%, but only 35% above 4.25%."
  - "Multiple news sources confirm the Fed hiked rates at the September 16 meeting; the ladder distribution is consistent with a single 25bp hike landing the upper bound at 4.25%."
  - "The sharp drop from 85% to 35% between the 4.0% and 4.25% strikes signals genuine uncertainty over whether the hike brought the bound to exactly 4.25% or stayed at 4.0%."
  - "Strikes above 4.5% price at 1-2%, suggesting markets see the current cycle as near its terminal rate despite ongoing inflation concerns flagged across this week's news cycle."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US spot Bitcoin ETFs drew $433M in net inflows Friday, rebounding from midweek outflows triggered by the Federal Reserve's rate hike, as markets digest the tightening cycle's pace."
    publisher: "woofun.ai"
    published_at: "2026-09-20T00:00:00.000Z"
    source_url: "https://www.woofun.ai/en/news/detail/108467"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "woofun.ai"
        source_url: "https://www.woofun.ai/en/news/detail/108467"
        retrieved_at: "2026-09-20T12:50:04+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via the Federal Reserve's official September 2026 meeting statement; the sharp cliff between the 4.0% and 4.25% strikes is the key distribution feature."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "woofun.ai: Fidelity's $310M Inflow Anchors Bitcoin ETF Rebound Amid Fed Hike | Wo"
    url: "https://www.woofun.ai/en/news/detail/108467"
    published_at: "2026-09-20T00:00:00.000Z"
    retrieved_at: "2026-09-20T12:50:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
