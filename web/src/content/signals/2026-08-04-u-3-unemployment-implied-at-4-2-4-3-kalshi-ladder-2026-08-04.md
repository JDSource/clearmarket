---
signal_id: "CMSIG2026080403"
signal_slug: "u-3-unemployment-implied-at-4-2-4-3-kalshi-ladder-2026-08-04"
headline: "U-3 unemployment implied at 4.2-4.3%: Kalshi ladder"
semantic_title: "Unemployment rate seen near 4.2-4.3% despite resilient labor data"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-04T00:00:00.000Z"
event_id: "CM-EVT-CN1M891289"
event_slug: "kxu3-26aug"
event_question: "U-3 unemployment rate (August 2026)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26AUG-T4.3"
  question_raw: "Will the unemployment rate (U-3) be above 4.3% in August?"
  current_price: 0.39
  volume_24h_usd: 39.39
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-12-04T14:00:00Z"
bullets:
  - "Kalshi ladder implies U-3 unemployment in the 4.2-4.3% range: 61% above 4.2%, but only 39% above 4.3%, and just 12% above 4.4%."
  - "Falling labor force participation, per St. Louis Fed research, can hold the headline unemployment rate down even as underlying labor conditions soften, consistent with market pricing near 4.2-4.3%."
  - "A companion October ladder (CM-EVT-2X91TW50H2) also centers at 4.2-4.3%, suggesting the market sees no significant near-term deterioration in the unemployment trajectory."
  - "Both ladders resolve via Bureau of Labor Statistics Employment Situation releases; participation-rate distortions could shift the realized rate above or below the implied range."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The St. Louis Fed published research noting a sharp drop in labor force participation in 2026, which can mask underlying labor market weakness even as headline job metrics hold firm."
    publisher: "stlouisfed.org"
    published_at: "2026-08-04T00:00:00.000Z"
    source_url: "https://www.stlouisfed.org/on-the-economy/2026/aug/what-is-behind-sharp-drop-labor-force-participation"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "stlouisfed.org"
        source_url: "https://www.stlouisfed.org/on-the-economy/2026/aug/what-is-behind-sharp-drop-labor-force-participation"
        retrieved_at: "2026-08-06T10:35:15+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via BLS; the August and October distributions are tightly aligned, both centering at 4.2-4.3% U-3."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "stlouisfed.org: What’s Behind the Sharp Drop in Labor Force Participation? | St. Louis"
    url: "https://www.stlouisfed.org/on-the-economy/2026/aug/what-is-behind-sharp-drop-labor-force-participation"
    published_at: "2026-08-04T00:00:00.000Z"
    retrieved_at: "2026-08-06T10:35:15+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
