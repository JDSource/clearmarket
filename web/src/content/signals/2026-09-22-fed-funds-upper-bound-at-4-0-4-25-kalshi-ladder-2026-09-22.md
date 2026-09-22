---
signal_id: "CMSIG2026092201"
signal_slug: "fed-funds-upper-bound-at-4-0-4-25-kalshi-ladder-2026-09-22"
headline: "Fed funds upper bound at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound seen settling at 4.0-4.25 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-22T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound following September 2026 FOMC"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.38
  volume_24h_usd: 185.53
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the September 2026 Fed funds upper bound in the 4.0-4.25% range: 84% above 4.0%, only 38% above 4.25%, and just 5% above 4.50%."
  - "Multiple officials including St. Louis Fed President Alberto Musalem flagged more hikes needed, yet the Kalshi distribution shows the market sees this cycle near its peak rather than pricing a sustained march higher."
  - "The 4.50% strike at only 5% probability signals the market is largely fading aggressive hike-continuation rhetoric from Fed officials."
  - "The Kalshi contract resolves via the Federal Reserve's official announced upper bound following the September 2026 FOMC meeting."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Reuters analysis questions whether Fed Chair Kevin Warsh is running a data-driven institution, as the September FOMC meeting delivered a rate hike amid persistent inflation."
    publisher: "Mike Dolan"
    published_at: "2026-09-22T00:00:00.000Z"
    source_url: "https://www.reuters.com/commentary/reuters-open-interest/losing-plot-warshs-fed-more-touchy-feely-than-data-driven-2026-09-22/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Mike Dolan"
        source_url: "https://www.reuters.com/commentary/reuters-open-interest/losing-plot-warshs-fed-more-touchy-feely-than-data-driven-2026-09-22/"
        retrieved_at: "2026-09-22T07:47:31+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder data provides the full distribution; only the 4.0-4.25% zone carries meaningful probability mass, suggesting markets treat current hiking as a near-terminal move."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Mike Dolan: Losing the plot? Warsh's Fed more 'touchy-feely' than data-driven | Re"
    url: "https://www.reuters.com/commentary/reuters-open-interest/losing-plot-warshs-fed-more-touchy-feely-than-data-driven-2026-09-22/"
    published_at: "2026-09-22T00:00:00.000Z"
    retrieved_at: "2026-09-22T07:47:31+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
