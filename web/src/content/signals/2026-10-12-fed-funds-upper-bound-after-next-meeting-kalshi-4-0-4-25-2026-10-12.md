---
signal_id: "CMSIG2026101202"
signal_slug: "fed-funds-upper-bound-after-next-meeting-kalshi-4-0-4-25-2026-10-12"
headline: "Fed funds upper bound after next meeting: Kalshi 4.0-4.25%"
semantic_title: "Fed funds upper bound stays priced near 4.0 to 4.25 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-12T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound after next meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.19
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "The Kalshi ladder prices the Fed funds upper bound in the 4.0-4.25% range: 81% above 4.0% but only 19% above 4.25%, implying one more hike is consensus, two is a tail."
  - "Bank of America's two-hike call for October and December sits at the outer edge of what the Kalshi distribution reflects: 6% above 4.5% and 2% above 4.75%."
  - "The September payroll miss of 29,000 against a 90,000 estimate, reported separately, is the main counterweight to the BofA hawkish view."
  - "A companion Kalshi contract on the Fed making a cut greater than 25 basis points sits at 2%, consistent with the hike-bias framing in the ladder distribution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bank of America expects two more Fed rate hikes in 2026, in October and December, citing strong US growth."
    publisher: "Vikram G"
    published_at: "2026-10-12T00:00:00.000Z"
    source_url: "https://www.newkerala.com/news/a/strong-us-growth-sticky-inflation-may-prompt-two-278.htm"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Vikram G"
        source_url: "https://www.newkerala.com/news/a/strong-us-growth-sticky-inflation-may-prompt-two-278.htm"
        retrieved_at: "2026-10-12T07:49:04+00:00"
  - type: "pm_response"
    notes: "The Kalshi ladder on the Fed funds upper bound shows the market is pricing one hike as the base case, treating the BofA two-hike forecast as a meaningful but low-probability outcome."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Vikram G: BofA Sees Two More Fed Rate Hikes in 2026 on Strong US Growth"
    url: "https://www.newkerala.com/news/a/strong-us-growth-sticky-inflation-may-prompt-two-278.htm"
    published_at: "2026-10-12T00:00:00.000Z"
    retrieved_at: "2026-10-12T07:49:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
