---
signal_id: "CMSIG2026062305"
signal_slug: "fed-cut-over-25bp-in-single-meeting-kalshi-7-2026-06-23"
headline: "Fed cut over 25bp in single meeting: Kalshi 7%"
semantic_title: "Big Fed cut consensus fractures as PCE inflation peaks near 4 percent"
telemetry: "Kalshi 7%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-23T05:36:57.000Z"
event_id: "CM-EVT-RWRZ1R3SD6"
event_slug: "kxlargecut-26"
event_question: "Will the Federal Reserve cut interest rates by more than 25 basis points in a single action this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLARGECUT-26"
  question_raw: "Will the Fed cut rates more than 25 bps in 2026?"
  current_price: 0.07
  volume_24h_usd: 9.4
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only a 7% chance the Federal Reserve cuts rates by more than 25 basis points in a single meeting."
  - "A 4.1% PCE forecast is consistent with the market's near-total rejection of aggressive easing; the news and the price align."
  - "Economists projecting May as the inflation peak suggest potential for eventual cuts, but the market sees no urgency for outsized action."
  - "Resolves via Federal Reserve policy announcement; a jumbo cut would require a dramatic and rapid inflation reversal not currently priced."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "May PCE inflation is forecast at 4.1% annually by FactSet, its highest level since April 2023, with economists expecting May to mark the year's inflation peak."
    publisher: "morningstar.com"
    published_at: "2026-06-23T05:36:57.000Z"
    source_url: "https://www.morningstar.com/economy/may-pce-expected-show-rising-inflation"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "morningstar.com"
        source_url: "https://www.morningstar.com/economy/may-pce-expected-show-rising-inflation"
        retrieved_at: "2026-06-25T10:38:54+00:00"
  - type: "pm_response"
    notes: "Kalshi at 7% is firmly consistent with a rising-inflation environment and Warsh's stated price-stability mandate."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "morningstar.com: May PCE Expected to Show Rising Inflation | Morningstar"
    url: "https://www.morningstar.com/economy/may-pce-expected-show-rising-inflation"
    published_at: "2026-06-23T05:36:57.000Z"
    retrieved_at: "2026-06-25T10:38:54+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
