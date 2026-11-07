---
signal_id: "CMSIG2026110601"
signal_slug: "fed-funds-upper-bound-seen-at-4-0-4-25-kalshi-ladder-2026-11-06"
headline: "Fed funds upper bound seen at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds rate seen topping out near 4 to 4.25 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-06T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds upper bound post-December 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.01
  volume_24h_usd: 47.84
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder puts 78% odds on the federal funds upper bound clearing 4.0%, but collapses to just 1% above 4.25%, implying the market sees 4.0-4.25% as the likely ceiling."
  - "Fed officials and news commentary lean hawkish after the 165,000-job October print, but Kalshi pricing shows the market is not pricing a runaway hike cycle beyond one more move."
  - "The sharp cliff between the 4.0% and 4.25% strikes signals the market treats December as likely but views further hikes as a tail risk, not a base case."
  - "Resolution is determined by the actual federal funds rate upper bound set at the December 2026 FOMC meeting, as announced by the Federal Reserve."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A stronger-than-expected October jobs report bolstered Fed officials' case for a December rate hike, with San Francisco Fed President Mary Daly saying higher rates are likely needed."
    publisher: "streetinsider.com"
    published_at: "2026-11-06T00:00:00.000Z"
    source_url: "https://www.streetinsider.com/Reuters/Fed+seen+sticking+to+December+rate+hike+after+jobs+data/27304646.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "streetinsider.com"
        source_url: "https://www.streetinsider.com/Reuters/Fed+seen+sticking+to+December+rate+hike+after+jobs+data/27304646.html"
        retrieved_at: "2026-11-07T07:48:17+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder data is the only priced source available; no intraday price move can be attributed."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "streetinsider.com: Fed seen sticking to December rate hike after jobs data"
    url: "https://www.streetinsider.com/Reuters/Fed+seen+sticking+to+December+rate+hike+after+jobs+data/27304646.html"
    published_at: "2026-11-06T00:00:00.000Z"
    retrieved_at: "2026-11-07T07:48:17+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
