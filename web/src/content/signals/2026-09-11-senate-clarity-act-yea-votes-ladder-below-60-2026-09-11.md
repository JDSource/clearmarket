---
signal_id: "CMSIG2026091107"
signal_slug: "senate-clarity-act-yea-votes-ladder-below-60-2026-09-11"
headline: "Senate CLARITY Act Yea votes: ladder below 60"
semantic_title: "Senate crypto bill vote count stays shy of 60"
telemetry: "Kalshi ladder"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-09-11T00:00:00.000Z"
event_id: "CM-EVT-CSYS5KPXK6"
event_slug: "kxvoteclarity-26may16"
event_question: "Senate Yea votes on crypto market structure bill"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXVOTECLARITY-26MAY16-T50"
  question_raw: "How many Senate members will vote Yea on a crypto market structure bill (as defined in KXCRYPTOSTRUCTURE)?"
  current_price: 0.31
  volume_24h_usd: 612.46
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Ladder prices only 31% above 50 votes and 22% above 60 votes, implying the market-implied Yea count is well below the 60-vote cloture threshold."
  - "The news headline itself cites 17% market odds of passage, which aligns with the ladder's distribution showing a sharp drop in probability above the 60-vote strike."
  - "Revised DeFi oversight provisions added days before the vote introduce fresh uncertainty that could cost votes from both crypto-friendly and skeptical senators."
  - "Resolution uses the Senate's official recorded vote count from the September 15 procedural roll call."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The CLARITY Act, a 630-page crypto market-structure bill with new DeFi rules, faces a September 15 procedural Senate vote needing 60 votes to advance, with market odds at just 17% of passage."
    publisher: "en.theblockbeats.news"
    published_at: "2026-09-11T00:00:00.000Z"
    source_url: "https://en.theblockbeats.news/news/63670"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "en.theblockbeats.news"
        source_url: "https://en.theblockbeats.news/news/63670"
        retrieved_at: "2026-09-11T12:32:20+00:00"
  - type: "pm_response"
    notes: "The ladder's sub-30% probability above 60 votes is the operative data point; the news narrative of '60 votes away' is consistent with that pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "en.theblockbeats.news: CLARITY Act: Only 60 Votes Away from Passage, Market Odds at Just 17%"
    url: "https://en.theblockbeats.news/news/63670"
    published_at: "2026-09-11T00:00:00.000Z"
    retrieved_at: "2026-09-11T12:32:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
