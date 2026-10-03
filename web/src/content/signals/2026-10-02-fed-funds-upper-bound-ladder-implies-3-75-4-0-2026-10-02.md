---
signal_id: "CMSIG2026100204"
signal_slug: "fed-funds-upper-bound-ladder-implies-3-75-4-0-2026-10-02"
headline: "Fed funds upper bound: ladder implies 3.75-4.0%"
semantic_title: "Fed funds rate seen staying in 3.75 to 4.0 percent range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-02T00:00:00.000Z"
event_id: "CM-EVT-6BS28TS762"
event_slug: "kxfed-26oct"
event_question: "Federal funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26OCT-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Oct 28, 2026 meeting?"
  current_price: 0.18
  volume_24h_usd: 1478.38
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-11-04T18:05:00Z"
bullets:
  - "The Kalshi ladder prices 99% above 3.75% but only 18% above 4.0%, placing the market-implied upper bound in the 3.75-4.0% range."
  - "Jefferson's no-rush language is consistent with the ladder: the market sees 4.0% as a ceiling with only 18% odds of breaching it."
  - "The 29,000-job September print reinforces the pause case; the ladder's sharp drop above 4.0% reflects that data flow."
  - "A separate Kalshi contract on a cut greater than 25 basis points this year prices at just 4%, confirming the market sees a narrow hold corridor, not easing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Vice Chair Philip Jefferson said the central bank is in no rush to raise rates again, suggesting an October hike is unlikely."
    publisher: "Thao Ta"
    published_at: "2026-10-02T00:00:00.000Z"
    source_url: "https://ph.investing.com/news/economy-news/fed-vice-chair-jefferson-no-rush-to-raise-rates-again-2611399"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Thao Ta"
        source_url: "https://ph.investing.com/news/economy-news/fed-vice-chair-jefferson-no-rush-to-raise-rates-again-2611399"
        retrieved_at: "2026-10-03T12:59:34+00:00"
  - type: "pm_response"
    notes: "The Kalshi ladder is the only live Fed-path instrument with pricing in this cluster; all other Fed rate contracts lack quoted prices."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Thao Ta: Fed Vice Chair Jefferson: No rush to raise rates again By Investing.co"
    url: "https://ph.investing.com/news/economy-news/fed-vice-chair-jefferson-no-rush-to-raise-rates-again-2611399"
    published_at: "2026-10-02T00:00:00.000Z"
    retrieved_at: "2026-10-03T12:59:34+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
