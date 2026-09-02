---
signal_id: "CMSIG2026083101"
signal_slug: "fed-funds-upper-bound-post-sept-ladder-implies-3-75-4-0-2026-08-31"
headline: "Fed funds upper bound post-Sept: ladder implies 3.75-4.0%"
semantic_title: "Fed funds above 4 percent stays a long shot after Jackson Hole"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-31T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds rate upper bound after September 2026 meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.00"
  question_raw: "Will the upper bound of the federal funds rate be above 4.00% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.42
  volume_24h_usd: 104.46
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Ladder pins the implied upper bound in the 3.75-4.0% range: 91% above 3.50%, 75% above 3.75%, but only 42% above 4.0%."
  - "Warsh's Jackson Hole pivot pushed markets toward a hike, but the ladder shows the consensus stopping short of 4.0%, not fully embracing an aggressive move."
  - "A second ladder (CM-EVT-4ZQLQPNH91) is far more compressed: only 62% above 3.75% and 2% above 4.0%, suggesting significant disagreement across market participants on the September endpoint."
  - "Resolution turns on the actual FOMC statement following the September meeting; the spread between the two ladders signals meaningful uncertainty about whether a hike lands at all."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Chair Kevin Warsh's Jackson Hole speech flipped markets toward pricing a September rate hike, though analysts remain divided on whether data supports tighter policy."
    publisher: "Jeff Cox"
    published_at: "2026-08-31T00:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/08/31/markets-see-warsh-endorsing-a-rate-hike-in-september-not-everyone-is-convinced.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jeff Cox"
        source_url: "https://www.cnbc.com/2026/08/31/markets-see-warsh-endorsing-a-rate-hike-in-september-not-everyone-is-convinced.html"
        retrieved_at: "2026-09-02T12:29:02+00:00"
  - type: "pm_response"
    notes: "Two Polymarket ladders cover the same post-September funds rate; their divergence at the 3.75% strike is the sharpest cross-contract signal available."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jeff Cox: Markets see Warsh endorsing a rate hike in September. Not everyone is"
    url: "https://www.cnbc.com/2026/08/31/markets-see-warsh-endorsing-a-rate-hike-in-september-not-everyone-is-convinced.html"
    published_at: "2026-08-31T00:00:00.000Z"
    retrieved_at: "2026-09-02T12:29:02+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
