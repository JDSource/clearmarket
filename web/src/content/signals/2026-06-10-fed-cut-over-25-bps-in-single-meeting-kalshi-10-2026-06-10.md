---
signal_id: "CMSIG2026061002"
signal_slug: "fed-cut-over-25-bps-in-single-meeting-kalshi-10-2026-06-10"
headline: "Fed cut over 25 bps in single meeting: Kalshi 10%"
semantic_title: "Fed jumbo cut consensus fractures under hot CPI pressure"
telemetry: "Kalshi 10%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-10T15:59:33.000Z"
event_id: "CM-EVT-RWRZ1R3SD6"
event_slug: "kxlargecut-26"
event_question: "Will the Federal Reserve cut interest rates by more than 25 basis points in a single action this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLARGECUT-26"
  question_raw: "Will the Fed cut rates more than 25 bps in 2026?"
  current_price: 0.104
  volume_24h_usd: 26.64
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi puts only 10% on the Federal Reserve cutting rates by more than 25 basis points in a single meeting."
  - "May CPI at 4.2%, driven by a 23.5% annual energy surge, is consistent with the market pricing out any aggressive easing; the hot print reinforces the 90% probability against a jumbo cut."
  - "The 10% residual likely reflects a tail scenario where energy shocks reverse sharply and growth deteriorates faster than expected, forcing Fed hand."
  - "Resolution via the Federal Reserve's official rate decision; any intra-meeting emergency cut or split decision would settle the contract immediately outside the regular calendar."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "May CPI hit 4.2% with energy prices up 23.5% annually, but analysts note the Fed typically looks past energy-driven spikes, leaving rate-hike probability low and large cuts even lower."
    publisher: "Rich Duprey"
    published_at: "2026-06-10T15:59:33.000Z"
    source_url: "https://247wallst.com/investing/2026/06/10/may-cpi-surges-to-4-2-but-the-fed-may-not-be-ready-to-raise-rates/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Rich Duprey"
        source_url: "https://247wallst.com/investing/2026/06/10/may-cpi-surges-to-4-2-but-the-fed-may-not-be-ready-to-raise-rates/"
        retrieved_at: "2026-06-11T12:08:11+00:00"
  - type: "pm_response"
    notes: "Kalshi contract prices only a 10% chance of a Fed cut exceeding 25 bps in one meeting, consistent with the current hot inflation print keeping the central bank sidelined on aggressive easing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Rich Duprey: May CPI Surges to 4.2%, but the Fed May Not Be Ready to Raise Rates -"
    url: "https://247wallst.com/investing/2026/06/10/may-cpi-surges-to-4-2-but-the-fed-may-not-be-ready-to-raise-rates/"
    published_at: "2026-06-10T15:59:33.000Z"
    retrieved_at: "2026-06-11T12:08:11+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
