---
signal_id: "CMSIG2026060406"
signal_slug: "trump-national-bitcoin-reserve-by-dec-31-kalshi-23-2026-06-04"
headline: "Trump National Bitcoin Reserve by Dec 31: Kalshi 23%"
semantic_title: "National Bitcoin Reserve by year-end wavers at low consensus"
telemetry: "Kalshi 23%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-04T08:57:56.000Z"
event_id: "CM-EVT-JQRXSG4ZX9"
event_slug: "kxbtcreserve-27"
event_question: "Will Trump create a National Bitcoin Reserve by December 31, 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCRESERVE-27-JAN01"
  question_raw: "Will Trump create a National Bitcoin Reserve before Jan 1, 2027?"
  current_price: 0.23
  volume_24h_usd: 115.83
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only 23% odds that Trump formally creates a National Bitcoin Reserve by December 31, 2026, resolving via The New York Times."
  - "Bessent's 'deliberate speed' framing is consistent with below-50% pricing: rhetoric signals intent but market assigns low probability to full execution this year."
  - "Legislative dependency on the CLARITY Act passing the Senate adds a second hurdle, compressing the timeline probability further."
  - "Bitcoin spot near $62K-$63K (per concurrent selloff news) provides a market-price backdrop suggesting macro and geopolitical pressures may delay institutional crypto policy action."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Treasury Secretary Scott Bessent told the Senate Finance Committee the Strategic Bitcoin Reserve is advancing at 'deliberate speed' and pushed for the CLARITY Act to pass this summer."
    publisher: "Aakash Girimath"
    published_at: "2026-06-04T08:57:56.000Z"
    source_url: "https://unchainedcrypto.com/bessent-pushes-senate-to-pass-clarity-act-this-summer-as-strategic-bitcoin-reserve-advances-at-deliberate-speed/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Aakash Girimath"
        source_url: "https://unchainedcrypto.com/bessent-pushes-senate-to-pass-clarity-act-this-summer-as-strategic-bitcoin-reserve-advances-at-deliberate-speed/"
        retrieved_at: "2026-06-05T11:24:05+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via New York Times confirmation of a formal National Bitcoin Reserve creation; executive order alone may or may not satisfy resolution criteria."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Aakash Girimath: Bessent Pushes Senate to Pass CLARITY Act This Summer as Strategic Bit"
    url: "https://unchainedcrypto.com/bessent-pushes-senate-to-pass-clarity-act-this-summer-as-strategic-bitcoin-reserve-advances-at-deliberate-speed/"
    published_at: "2026-06-04T08:57:56.000Z"
    retrieved_at: "2026-06-05T11:24:05+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
