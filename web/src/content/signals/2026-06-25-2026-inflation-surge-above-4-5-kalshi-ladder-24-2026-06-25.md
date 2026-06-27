---
signal_id: "CMSIG2026062501"
signal_slug: "2026-inflation-surge-above-4-5-kalshi-ladder-24-2026-06-25"
headline: "2026 inflation surge above 4.5%: Kalshi ladder 24%"
semantic_title: "Inflation surge above 4.5 percent consensus wavers at low odds"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-25T10:01:18.953Z"
event_id: "CM-EVT-H50NT0MZ04"
event_slug: "kxlcpimaxyoy-27"
event_question: "2026 annual US inflation peak level"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLCPIMAXYOY-27-P4.5"
  question_raw: "Inflation surge in 2026?"
  current_price: 0.243
  volume_24h_usd: 69.52
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-14T15:00:00Z"
bullets:
  - "Kalshi ladder prices only 24% chance inflation exceeds 4.5%, implying the market sees the 3-year high as a ceiling, not a floor."
  - "PCE hitting a 3-year high at 4.1% is consistent with the ladder's implied range below 4.5%, as the market does not anticipate a further surge."
  - "The distribution collapses sharply above 5.0% (21%) and 5.5% (11%), signaling the market sees only a thin tail of runaway inflation scenarios."
  - "Resolves via the named inflation data series; the market-implied peak sits just below 4.5%, with sharp drop-off above 5.0%."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Fed's preferred inflation gauge, PCE, hit a 3-year high in May 2026, with consumer prices rising 4.1% year-over-year, driven by fuel costs."
    publisher: "finance.yahoo.com"
    published_at: "2026-06-25T10:01:18.953Z"
    source_url: "https://finance.yahoo.com/economy/policy/article/pce-report-feds-preferred-inflation-measure-hits-3-year-high-keeping-talk-of-possible-rate-hike-in-play-124158491.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "finance.yahoo.com"
        source_url: "https://finance.yahoo.com/economy/policy/article/pce-report-feds-preferred-inflation-measure-hits-3-year-high-keeping-talk-of-possible-rate-hike-in-play-124158491.html"
        retrieved_at: "2026-06-27T10:02:20+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder contract on 2026 inflation peak; current distribution implies the market is absorbing the PCE surprise without pricing a sustained breakout above 4.5%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "finance.yahoo.com: PCE report: Fed's preferred inflation measure hits 3-year high ..."
    url: "https://finance.yahoo.com/economy/policy/article/pce-report-feds-preferred-inflation-measure-hits-3-year-high-keeping-talk-of-possible-rate-hike-in-play-124158491.html"
    published_at: "2026-06-25T10:01:18.953Z"
    retrieved_at: "2026-06-27T10:02:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
