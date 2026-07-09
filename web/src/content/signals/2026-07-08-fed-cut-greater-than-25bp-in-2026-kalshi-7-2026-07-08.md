---
signal_id: "CMSIG2026070804"
signal_slug: "fed-cut-greater-than-25bp-in-2026-kalshi-7-2026-07-08"
headline: "Fed cut greater than 25bp in 2026: Kalshi 7%"
semantic_title: "Jumbo cut pricing wavers near historic lows despite weak data"
telemetry: "Kalshi 7%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-08T18:00:33.000Z"
event_id: "CM-EVT-RWRZ1R3SD6"
event_slug: "kxlargecut-26"
event_question: "Will the Federal Reserve do a rate cut greater than 25 basis points this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLARGECUT-26"
  question_raw: "Will the Fed cut rates more than 25 bps in 2026?"
  current_price: 0.073
  volume_24h_usd: 783.29
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only 7% on the Fed cutting by more than 25 basis points at any 2026 meeting, signaling near-consensus against a jumbo cut."
  - "Despite 57,000 June payrolls and divided Fed minutes, the market is not pricing emergency-style easing; the 7% reflects institutional resistance to large cuts."
  - "A companion Kalshi contract (CM-EVT-5Z1MKFCSL8) prices only 10% on an emergency Fed meeting in 2026, consistent with the low jumbo-cut probability."
  - "Resolves via Federal Reserve official rate announcement; a jumbo cut would require either a sharp deterioration in labor markets or a financial stability event beyond current pricing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Thursday's data slate includes jobless claims and Fed official remarks that could shape near-term rate-path expectations following weak June payrolls."
    publisher: "tradevae.com"
    published_at: "2026-07-08T18:00:33.000Z"
    source_url: "https://tradevae.com/news/stock-markets/thursdays-data-slate-centers-on-jobless-claims-existing-home-sales-and-fed-remarks/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "tradevae.com"
        source_url: "https://tradevae.com/news/stock-markets/thursdays-data-slate-centers-on-jobless-claims-existing-home-sales-and-fed-remarks/"
        retrieved_at: "2026-07-09T10:56:21+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolving via Federal Reserve; 7% on jumbo cut implies markets see standard 25bp increments as the dominant easing path."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "tradevae.com: Thursday’s data slate centers on jobless claims, existing home sales a"
    url: "https://tradevae.com/news/stock-markets/thursdays-data-slate-centers-on-jobless-claims-existing-home-sales-and-fed-remarks/"
    published_at: "2026-07-08T18:00:33.000Z"
    retrieved_at: "2026-07-09T10:56:21+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
