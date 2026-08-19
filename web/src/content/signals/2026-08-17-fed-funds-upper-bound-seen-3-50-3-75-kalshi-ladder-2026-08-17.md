---
signal_id: "CMSIG2026081702"
signal_slug: "fed-funds-upper-bound-seen-3-50-3-75-kalshi-ladder-2026-08-17"
headline: "Fed funds upper bound seen 3.50-3.75%: Kalshi ladder"
semantic_title: "Near-term Fed funds rate stays below 3.75 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-17T00:00:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Near-term Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.29
  volume_24h_usd: 1718.02
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-23T18:05:00Z"
bullets:
  - "Kalshi ladder prices the near-term Fed funds upper bound in the 3.50-3.75% range: 98% above 3.50% but only 29% above 3.75%."
  - "Fading hike bets reported in the news are consistent with this distribution, the sharp drop from 98% to 29% at the 3.75% strike signals the market is treating a move above 3.75% as unlikely."
  - "A companion ladder (CM-EVT-MR57HVWJT3) for a later meeting implies ~3.75-4.00%, with 51% above 3.75%, showing a modest term-structure tilt toward a later hike surviving."
  - "Resolves via Federal Reserve official meeting outcome; upper-bound definition follows FOMC post-meeting statement language."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Rate hike bets are fading fast as cooler inflation may give Fed Chair Kevin Warsh political cover to hold rates steady."
    publisher: "Merin Rebecca Thomas"
    published_at: "2026-08-17T00:00:00.000Z"
    source_url: "https://www.ibtimes.com/fed-rate-hike-bets-are-fading-fast-cooler-inflation-could-leave-warsh-easier-choice-3806427"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Merin Rebecca Thomas"
        source_url: "https://www.ibtimes.com/fed-rate-hike-bets-are-fading-fast-cooler-inflation-could-leave-warsh-easier-choice-3806427"
        retrieved_at: "2026-08-19T08:31:28+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder shows a hard probability cliff at 3.75%, aligning with widespread Wall Street skepticism about a September move."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Merin Rebecca Thomas: Fed Rate Hike Bets Are Fading Fast. Cooler Inflation Could Leave Warsh"
    url: "https://www.ibtimes.com/fed-rate-hike-bets-are-fading-fast-cooler-inflation-could-leave-warsh-easier-choice-3806427"
    published_at: "2026-08-17T00:00:00.000Z"
    retrieved_at: "2026-08-19T08:31:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
