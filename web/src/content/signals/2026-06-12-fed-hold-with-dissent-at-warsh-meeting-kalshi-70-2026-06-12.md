---
signal_id: "CMSIG2026061202"
signal_slug: "fed-hold-with-dissent-at-warsh-meeting-kalshi-70-2026-06-12"
headline: "Fed hold with dissent at Warsh meeting: Kalshi 70%"
semantic_title: "Fed hold with dissent at Warsh first meeting solidifies at 70 percent"
telemetry: "Kalshi 70%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-12T00:00:00.000Z"
event_id: "CM-EVT-MZGHWX20T0"
event_slug: "kxfedcombo-26jun"
event_question: "Will the Federal Reserve hold rates at 4.25%-4.50% with at least one dissent at its June 2026 meeting?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDCOMBO-26JUN-0-0"
  question_raw: "Will Federal Funds Rate Decision be No change AND Dissents be 0 for Jun 2026?"
  current_price: 0.7
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-06-17T19:00:00Z"
bullets:
  - "Kalshi puts 70% odds on the Fed holding rates at 4.25%-4.50% with at least one dissent at the upcoming June meeting."
  - "Surging CPI and PPI data are consistent with a hold, but the dissent premium reflects genuine uncertainty over whether Warsh signals a hawkish pivot or patient posture."
  - "The 70% hold-with-dissent probability implies a meaningful 30% chance of either a cut without dissent, a hike, or a clean unanimous hold, all live scenarios given the energy shock backdrop."
  - "Resolves via Bureau of Labor Statistics data combined with the official Fed statement; a dissent requires at least one FOMC voter to register a formal objection in the published minutes."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Inflationary pressures are rising as new Fed Chair Kevin Warsh prepares to lead his first monetary policy meeting amid surging energy-driven CPI and PPI."
    publisher: "aa.com.tr"
    published_at: "2026-06-12T00:00:00.000Z"
    source_url: "https://www.aa.com.tr/en/features/inflationary-pressures-rise-in-us-as-new-fed-chair-prepares-for-1st-meeting/3964939"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "aa.com.tr"
        source_url: "https://www.aa.com.tr/en/features/inflationary-pressures-rise-in-us-as-new-fed-chair-prepares-for-1st-meeting/3964939"
        retrieved_at: "2026-06-12T11:42:07+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via the official FOMC statement and BLS data; the 70% price reflects genuine two-way risk around Warsh's debut meeting posture."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "aa.com.tr: Inflationary pressures rise in US as new Fed chair prepares for 1st me"
    url: "https://www.aa.com.tr/en/features/inflationary-pressures-rise-in-us-as-new-fed-chair-prepares-for-1st-meeting/3964939"
    published_at: "2026-06-12T00:00:00.000Z"
    retrieved_at: "2026-06-12T11:42:07+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
