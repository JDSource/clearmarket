---
signal_id: "CMSIG2026091101"
signal_slug: "fed-funds-upper-bound-seen-3-75-4-0-kalshi-ladder-2026-09-11"
headline: "Fed funds upper bound seen 3.75-4.0%: Kalshi ladder"
semantic_title: "Fed funds above 3.75% prices in as rate hike nears"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-11T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Fed funds upper bound, next FOMC meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.02
  volume_24h_usd: 98.4
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder pins the Fed funds upper bound in the 3.75-4.0% range: 81% above 3.75%, but only 2% above 4.0%."
  - "August CPI data released Sept. 11 matched forecasts on headline but core beat at 0.3% month-over-month; the Kalshi distribution is fully consistent with a 25bp hike, not a larger move."
  - "Volume on this ladder surged 61x day-over-day, signaling a sharp burst of fresh positioning around the FOMC meeting this week."
  - "The Polymarket contract on Bank of England rate hikes in 2026 sits at 81%, suggesting global central bank tightening pressure is broadly repricing in tandem."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Elevated August CPI data, with core CPI rising 0.3% month-over-month, is keeping pressure on the Federal Reserve to raise rates at its upcoming meeting."
    publisher: "nytimes.com"
    published_at: "2026-09-11T00:00:00.000Z"
    source_url: "https://www.nytimes.com/2026/09/11/business/economy/inflation-cpi-august.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "nytimes.com"
        source_url: "https://www.nytimes.com/2026/09/11/business/economy/inflation-cpi-august.html"
        retrieved_at: "2026-09-13T13:04:33+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via Federal Reserve announcement; the tight 3.75-4.0% clustering leaves virtually no probability on a hold or a 50bp move."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "nytimes.com: Elevated Inflation Keeps Pressure on Fed to Raise Rates - The New York"
    url: "https://www.nytimes.com/2026/09/11/business/economy/inflation-cpi-august.html"
    published_at: "2026-09-11T00:00:00.000Z"
    retrieved_at: "2026-09-13T13:04:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
