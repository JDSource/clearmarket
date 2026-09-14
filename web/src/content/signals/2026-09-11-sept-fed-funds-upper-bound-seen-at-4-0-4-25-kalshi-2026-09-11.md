---
signal_id: "CMSIG2026091101"
signal_slug: "sept-fed-funds-upper-bound-seen-at-4-0-4-25-kalshi-2026-09-11"
headline: "Sept Fed funds upper bound seen at 4.0-4.25%: Kalshi"
semantic_title: "Fed funds upper bound nears full pricing at 4.0 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-11T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Sept 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.17
  volume_24h_usd: 73.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the September 2026 Fed funds upper bound in the 4.0-4.25% range: 63% above 4.0%, only 17% above 4.25%."
  - "August CPI surprise citing gas price spike aligns with the market's near-certainty of a hike; ladder is consistent with 25bp move."
  - "The sharp drop from 63% to 17% between the 4.0% and 4.25% strikes signals one hike priced in, not two consecutive moves at this meeting."
  - "Companion Polymarket contract (CM-EVT-87QV1G78C4) puts 90% on the Fed raising rates at all in 2026, corroborating the Kalshi ladder read."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Economists say a September Fed rate hike is all but guaranteed following a hotter-than-expected August CPI report driven by spiking gas prices."
    publisher: "cbsnews.com"
    published_at: "2026-09-11T00:00:00.000Z"
    source_url: "https://www.cbsnews.com/news/fed-rate-hike-september-likelihood-cpi/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cbsnews.com"
        source_url: "https://www.cbsnews.com/news/fed-rate-hike-september-likelihood-cpi/"
        retrieved_at: "2026-09-14T14:41:02+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via Federal Reserve official rate announcement; the 4.0-4.25% mode implies a single 25bp hike from the prior bound."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cbsnews.com: Fed rate hike in September is all but guaranteed after CPI report, eco"
    url: "https://www.cbsnews.com/news/fed-rate-hike-september-likelihood-cpi/"
    published_at: "2026-09-11T00:00:00.000Z"
    retrieved_at: "2026-09-14T14:41:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
