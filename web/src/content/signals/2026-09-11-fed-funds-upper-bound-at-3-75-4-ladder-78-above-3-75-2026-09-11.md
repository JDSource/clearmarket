---
signal_id: "CMSIG2026091102"
signal_slug: "fed-funds-upper-bound-at-3-75-4-ladder-78-above-3-75-2026-09-11"
headline: "Fed funds upper bound at 3.75-4%: ladder 78% above 3.75%"
semantic_title: "Fed funds upper bound seen near 3.75 to 4 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-11T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Fed funds upper bound (post-Sept 2026 meeting)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.38
  volume_24h_usd: 513.76
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Ladder prices 78% above 3.75% but only 38% above 4.00%, pinning the market-implied upper bound in the 3.75-4.00% range."
  - "Oil above $100 and hot PPI data align with the market holding the 3.75% strike as the likely post-meeting rate floor."
  - "The companion event CM-EVT-4ZQLQPNH91 shows a sharper cliff at 4.00%, just 2% above that level, suggesting both ladders agree the upper bound stops near 4.00%."
  - "Resolution follows the Federal Reserve's announced target range after the September 16 decision."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US Treasury yields are climbing as crude tops $100 and inflation bets intensify ahead of the September 16 FOMC meeting."
    publisher: "asia.nikkei.com"
    published_at: "2026-09-11T00:00:00.000Z"
    source_url: "https://asia.nikkei.com/business/markets/us-yields-climb-as-oil-soars-inflation-amps-up-rate-hike-bets"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "asia.nikkei.com"
        source_url: "https://asia.nikkei.com/business/markets/us-yields-climb-as-oil-soars-inflation-amps-up-rate-hike-bets"
        retrieved_at: "2026-09-11T12:32:20+00:00"
  - type: "pm_response"
    notes: "Two correlated ladders on the same Fed meeting converge; CM-EVT-MR57HVWJT3 carries a wider distribution but the implied peak is identical."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "asia.nikkei.com: US yields climb as oil soars, inflation amps up rate-hike bets - Nikke"
    url: "https://asia.nikkei.com/business/markets/us-yields-climb-as-oil-soars-inflation-amps-up-rate-hike-bets"
    published_at: "2026-09-11T00:00:00.000Z"
    retrieved_at: "2026-09-11T12:32:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
