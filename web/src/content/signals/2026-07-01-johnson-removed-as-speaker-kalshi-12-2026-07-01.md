---
signal_id: "CMSIG2026070105"
signal_slug: "johnson-removed-as-speaker-kalshi-12-2026-07-01"
headline: "Johnson removed as Speaker: Kalshi 12%"
semantic_title: "Johnson Speaker removal risk stays muted despite GOP revolt"
telemetry: "Kalshi 12%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-01T10:00:02.000Z"
event_id: "CM-EVT-YSH7DQ1TV1"
event_slug: "kxsothleave-26"
event_question: "Will Mike Johnson be removed as Speaker of the House?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSOTHLEAVE-26-NOV"
  question_raw: "Will Mike Johnson no longer be Speaker of the House before 2026?"
  current_price: 0.12
  volume_24h_usd: 11.9
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi prediction market prices 12% on Speaker Mike Johnson being removed from his position."
  - "The House deadlock is consistent with elevated but not decisive removal risk, markets are not treating a holiday-week revolt as a tipping-point event."
  - "A prior precedent where Kevin McCarthy was removed after a similar series of revolts provides the real-world reference that Kalshi bettors appear to be discounting."
  - "Resolves via New York Times confirmation of Johnson's removal as Speaker; the trigger is removal, not a failed procedural vote."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "House Republican leadership abruptly canceled votes and sent lawmakers home early as a GOP member revolt again paralyzed the chamber ahead of the holiday recess."
    publisher: "Chad de Guzman"
    published_at: "2026-07-01T10:00:02.000Z"
    source_url: "https://time.com/article/2026/07/01/gop-republican-house-defense-save-america-act/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Chad de Guzman"
        source_url: "https://time.com/article/2026/07/01/gop-republican-house-defense-save-america-act/"
        retrieved_at: "2026-07-02T10:34:14+00:00"
  - type: "pm_response"
    notes: "Kalshi at 12% is treating the GOP revolt as a recurring friction pattern rather than a credible near-term speaker change."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Chad de Guzman: House Starts Recess Early After GOP Members Rebel"
    url: "https://time.com/article/2026/07/01/gop-republican-house-defense-save-america-act/"
    published_at: "2026-07-01T10:00:02.000Z"
    retrieved_at: "2026-07-02T10:34:14+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
