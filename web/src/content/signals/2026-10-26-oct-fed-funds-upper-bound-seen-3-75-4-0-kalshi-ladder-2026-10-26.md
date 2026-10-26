---
signal_id: "CMSIG2026102602"
signal_slug: "oct-fed-funds-upper-bound-seen-3-75-4-0-kalshi-ladder-2026-10-26"
headline: "Oct Fed funds upper bound seen 3.75-4.0%: Kalshi ladder"
semantic_title: "Markets price a firm hold near 3.75-4 percent for Oct Fed"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-26T07:00:00.000Z"
event_id: "CM-EVT-6BS28TS762"
event_slug: "kxfed-26oct"
event_question: "Fed funds upper bound after Oct 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26OCT-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Oct 28, 2026 meeting?"
  current_price: 0.07
  volume_24h_usd: 103.7
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-11-04T18:05:00Z"
bullets:
  - "This Kalshi ladder shows 99% probability above 3.75% but only 7% above 4.0%, implying the implied mode sits at 3.75-4.0%."
  - "News framing of Fed as facing a 'crossroads' between inflation and growth is not reflected in pricing, which is overwhelmingly priced for a hold with no hike signal."
  - "Cross-ladder check: CM-EVT-MR57HVWJT3 implies a mode at 4.0-4.25%, suggesting a small inter-contract discrepancy; the 4.0% strike read differs between the two ladders."
  - "Resolves via the Federal Reserve's official Oct 28 announcement; a greater-than-25bp surprise move would be needed to shift the distribution materially."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Oil prices are rising, inflation is re-accelerating, and the labor market is cooling, placing the Fed at a critical crossroads ahead of its October 28 decision."
    publisher: "Investing.com"
    published_at: "2026-10-26T07:00:00.000Z"
    source_url: "https://www.investing.com/analysis/fed-rate-decision-looms-as-inflation-fears-rise-whats-next-for-markets-200690221"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Investing.com"
        source_url: "https://www.investing.com/analysis/fed-rate-decision-looms-as-inflation-fears-rise-whats-next-for-markets-200690221"
        retrieved_at: "2026-10-26T14:48:08+00:00"
  - type: "pm_response"
    notes: "This Kalshi ladder and CM-EVT-MR57HVWJT3 cover the same decision but show slightly different modal ranges; readers should treat 3.75-4.25% as the consensus band."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Investing.com: Fed Rate Decision Looms as Inflation Fears Rise: What’s Next for Marke"
    url: "https://www.investing.com/analysis/fed-rate-decision-looms-as-inflation-fears-rise-whats-next-for-markets-200690221"
    published_at: "2026-10-26T07:00:00.000Z"
    retrieved_at: "2026-10-26T14:48:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
