---
signal_id: "CMSIG2026091901"
signal_slug: "fed-funds-upper-bound-kalshi-ladder-4-0-4-25-2026-09-19"
headline: "Fed funds upper bound: Kalshi ladder 4.0-4.25%"
semantic_title: "Fed funds upper bound stays near 4.0-4.25 percent range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-19T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds rate upper bound (post-hike path)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.4
  volume_24h_usd: 412.35
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the federal funds upper bound squarely in the 4.0-4.25% range: 84% above 4.0%, collapsing to 40% above 4.25% and just 4% above 4.50%."
  - "Multiple outlets confirm the Fed hiked Wednesday; the ladder distribution is consistent with one hike having landed near or at 4.25%, with the market assigning very low odds to further tightening beyond that level."
  - "The sharp drop from 84% to 40% between the 4.0% and 4.25% strikes signals the market sees 4.25% as the likely terminal ceiling, not a waypoint."
  - "Cross-check: the Polymarket contract on an emergency Fed rate cut before 2027 sits at just 2%, reinforcing that markets expect the hiking cycle to pause, not reverse or accelerate."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Chair Kevin Warsh's rate hike signals a structural break with low-inflation era, as Wall Street reassesses the Fed's credibility on the 2% target."
    publisher: "Jeffry Bartash"
    published_at: "2026-09-19T00:00:00.000Z"
    source_url: "https://www.marketwatch.com/story/warshs-fed-shows-its-serious-about-taming-inflation-why-wall-street-now-believes-it-55dc5af5"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jeffry Bartash"
        source_url: "https://www.marketwatch.com/story/warshs-fed-shows-its-serious-about-taming-inflation-why-wall-street-now-believes-it-55dc5af5"
        retrieved_at: "2026-09-21T07:47:18+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via the actual Fed funds upper bound; the 4.0-4.25% consensus is the sharpest mass of probability in the distribution."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jeffry Bartash: Warsh’s Fed shows it’s serious about taming inflation. Why Wall Street"
    url: "https://www.marketwatch.com/story/warshs-fed-shows-its-serious-about-taming-inflation-why-wall-street-now-believes-it-55dc5af5"
    published_at: "2026-09-19T00:00:00.000Z"
    retrieved_at: "2026-09-21T07:47:18+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
