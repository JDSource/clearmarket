---
signal_id: "CMSIG2026062501"
signal_slug: "fed-cut-above-25bp-in-single-move-kalshi-7-2026-06-25"
headline: "Fed cut above 25bp in single move: Kalshi 7%"
semantic_title: "Fed outsized cut consensus collapses on inflation surge"
telemetry: "Kalshi 7%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-25T19:02:56.000Z"
event_id: "CM-EVT-RWRZ1R3SD6"
event_slug: "kxlargecut-26"
event_question: "Will the Federal Reserve cut interest rates by more than 25 basis points in a single action this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLARGECUT-26"
  question_raw: "Will the Fed cut rates more than 25 bps in 2026?"
  current_price: 0.074
  volume_24h_usd: 199.61
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi puts only 7% odds on the Fed cutting by more than 25 basis points in any single meeting."
  - "May PCE hitting 4.1% year-over-year, a 3-year high, is consistent with the market pricing out aggressive easing."
  - "At 7%, the Kalshi contract signals traders see no credible path to a jumbo cut while inflation runs this hot."
  - "Resolves via Federal Reserve official rate decision; any single-meeting cut larger than 25bp triggers YES."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "PCE, the Fed's preferred inflation gauge, rose to a 3-year high of 4.1% in May, driven by gas prices, raising political and monetary policy stakes."
    publisher: "newsnationnow.com"
    published_at: "2026-06-25T19:02:56.000Z"
    source_url: "https://www.newsnationnow.com/business/ap-business/ap-key-inflation-gauge-jumps-to-3-year-high-in-latest-sign-of-affordability-challenges/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "newsnationnow.com"
        source_url: "https://www.newsnationnow.com/business/ap-business/ap-key-inflation-gauge-jumps-to-3-year-high-in-latest-sign-of-affordability-challenges/"
        retrieved_at: "2026-06-27T01:35:43+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 7% reflects the market absorbing the PCE print as a durable hold-or-hike signal, not a cut catalyst."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "newsnationnow.com: Key inflation gauge jumps to 3-year high in latest sign of affordabili"
    url: "https://www.newsnationnow.com/business/ap-business/ap-key-inflation-gauge-jumps-to-3-year-high-in-latest-sign-of-affordability-challenges/"
    published_at: "2026-06-25T19:02:56.000Z"
    retrieved_at: "2026-06-27T01:35:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
