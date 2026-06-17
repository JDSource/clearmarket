---
signal_id: "CMSIG2026061702"
signal_slug: "fed-hold-with-dissent-at-june-fomc-kalshi-67-2026-06-17"
headline: "Fed hold with dissent at June FOMC: Kalshi 67%"
semantic_title: "Dissent at Warsh debut FOMC anchors at two-thirds odds"
telemetry: "Kalshi 67%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-17T00:00:00.000Z"
event_id: "CM-EVT-MZGHWX20T0"
event_slug: "kxfedcombo-26jun"
event_question: "Will the Federal Reserve hold rates at 4.25%-4.50% with at least one dissent at its June 2026 meeting?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDCOMBO-26JUN-0-0"
  question_raw: "Will Federal Funds Rate Decision be No change AND Dissents be 0 for Jun 2026?"
  current_price: 0.67
  volume_24h_usd: 238.04
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-06-17T19:00:00Z"
bullets:
  - "Kalshi prediction market prices a 67% chance the Fed holds at 4.25%-4.50% with at least one dissent at the June FOMC."
  - "Note: the Kalshi dissent contract references a 4.25%-4.50% target range, which conflicts with the Kalshi ladder showing current upper bound at 3.50-3.75%; treat this contract's rate-level framing as potentially misaligned with the live rate level."
  - "Reuters sourcing that some members may lean hawkish is consistent with elevated dissent odds; the 67% price reflects genuine uncertainty about internal Fed dynamics under Warsh."
  - "Resolves via Bureau of Labor Statistics; resolution source appears atypical for a Fed decision outcome, monitor for contract-specific settlement rules."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Reuters reports some FOMC members may pencil in a rate hike, while Chair Kevin Warsh's own dot remains uncertain heading into the June meeting."
    publisher: "investing.com"
    published_at: "2026-06-17T00:00:00.000Z"
    source_url: "https://www.investing.com/analysis/fomc-meeting-preview-will-warsh-kill-the-rate-cut-trade-for-good-200682293"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "investing.com"
        source_url: "https://www.investing.com/analysis/fomc-meeting-preview-will-warsh-kill-the-rate-cut-trade-for-good-200682293"
        retrieved_at: "2026-06-17T12:13:58+00:00"
  - type: "pm_response"
    notes: "Kalshi prices this at 67%; the BLS resolution source is unusual for a Fed-meeting contract and warrants attention on settlement mechanics."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "investing.com: FOMC Meeting Preview: Will Warsh Kill the Rate Cut Trade for Good?"
    url: "https://www.investing.com/analysis/fomc-meeting-preview-will-warsh-kill-the-rate-cut-trade-for-good-200682293"
    published_at: "2026-06-17T00:00:00.000Z"
    retrieved_at: "2026-06-17T12:13:58+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
