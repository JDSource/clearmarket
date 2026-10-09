---
signal_id: "CMSIG2026100905"
signal_slug: "ukraine-russia-peace-deal-by-2027-polymarket-9-2026-10-09"
headline: "Ukraine-Russia peace deal by 2027: Polymarket 9%"
semantic_title: "Ukraine-Russia peace deal before 2027 stays a long shot"
telemetry: "Polymarket 9%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-09T11:23:33.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.09
  volume_24h_usd: 3221.6011120000003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Ukraine signing a peace deal with Russia before 2027 sits at 9%, resolving via UMA oracle."
  - "Active US-led talks in Miami mark a concrete diplomatic step, but the Polymarket price shows the market is far from pricing a signed deal, the news has not moved the probability near any meaningful threshold."
  - "A related Polymarket contract on Ukraine agreeing to cede territory to Russia by 2026 holds at 5%, suggesting the market sees both deal likelihood and territorial concession as remote."
  - "The Polymarket contract on Trump, Putin, and Zelensky being seen together before 2027 sits at 5%, reinforcing a broad scepticism that talks will reach head-of-state summit level."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Kushner and Witkoff are set to discuss a new peace plan with the Ukrainian delegation in Miami, as Ukrainian and European officials converge on US-led talks."
    publisher: "Yuliya Talmazan"
    published_at: "2026-10-09T11:23:33.000Z"
    source_url: "https://www.nbcnews.com/world/ukraine/russia-war-kushner-witkoff-discuss-new-peace-plan-rcna602463"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Yuliya Talmazan"
        source_url: "https://www.nbcnews.com/world/ukraine/russia-war-kushner-witkoff-discuss-new-peace-plan-rcna602463"
        retrieved_at: "2026-10-09T14:55:32+00:00"
  - type: "pm_response"
    notes: "Polymarket prices a full Ukraine-Russia peace deal before 2027 at 9%, with territorial-cession and trilateral-summit contracts both at 5%, forming a consistent low-probability cluster."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Yuliya Talmazan: Kushner and Witkoff to discuss ‘new’ peace plan with Ukrainian delegat"
    url: "https://www.nbcnews.com/world/ukraine/russia-war-kushner-witkoff-discuss-new-peace-plan-rcna602463"
    published_at: "2026-10-09T11:23:33.000Z"
    retrieved_at: "2026-10-09T14:55:32+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
