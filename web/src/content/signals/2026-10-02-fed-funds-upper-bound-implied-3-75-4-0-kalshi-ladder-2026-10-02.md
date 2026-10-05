---
signal_id: "CMSIG2026100204"
signal_slug: "fed-funds-upper-bound-implied-3-75-4-0-kalshi-ladder-2026-10-02"
headline: "Fed funds upper bound implied 3.75-4.0%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen near 3.75 to 4 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-02T00:00:00.000Z"
event_id: "CM-EVT-6BS28TS762"
event_slug: "kxfed-26oct"
event_question: "Federal funds rate upper bound (post-next-meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26OCT-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Oct 28, 2026 meeting?"
  current_price: 0.24
  volume_24h_usd: 218.82
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-11-04T18:05:00Z"
bullets:
  - "Kalshi ladder prices the federal funds upper bound in the 3.75-4.0% range: 99% above 3.75%, only 24% above 4.0%."
  - "Jefferson's hawkish-leaning inflation commentary is broadly consistent with the market's implied ceiling near 4.0%, not a meaningful move higher."
  - "The 29,000 September payroll miss creates a dual-mandate tension but the ladder shows markets are not pricing a sharp dovish pivot below 3.75%."
  - "The distribution's sharp drop from 99% at 3.75% to 24% at 4.0% identifies 4.0% as the key resistance level the market assigns low probability to breaching."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Vice Chair Philip Jefferson flagged GDP growth of 2.4% in the first half of 2026 and said inflation remains 'too high for too long,' signaling caution on easing."
    publisher: "Econ Data Tools Editorial Team"
    published_at: "2026-10-02T00:00:00.000Z"
    source_url: "https://econdatatools.com/news/fed-vice-chair-jefferson-speech-october-1-2026-gdp-inflation-rates"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Econ Data Tools Editorial Team"
        source_url: "https://econdatatools.com/news/fed-vice-chair-jefferson-speech-october-1-2026-gdp-inflation-rates"
        retrieved_at: "2026-10-05T07:47:16+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder data; market-implied range 3.75-4.0% with a hard ceiling implied at 4.0% (24% probability)."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Econ Data Tools Editorial Team: Fed Vice Chair Jefferson: GDP grew 2.4% in first half, inflation 'too"
    url: "https://econdatatools.com/news/fed-vice-chair-jefferson-speech-october-1-2026-gdp-inflation-rates"
    published_at: "2026-10-02T00:00:00.000Z"
    retrieved_at: "2026-10-05T07:47:16+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
