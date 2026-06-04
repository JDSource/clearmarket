---
signal_id: "CMSIG2026060101"
signal_slug: "fed-funds-upper-bound-seen-3-50-3-75-kalshi-78-2026-06-01"
headline: "Fed funds upper bound seen 3.50-3.75%: Kalshi 78%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-01T16:15:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Fed funds upper bound after next meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26SEP-T3.75"
  question_raw: "Will the upper bound of the federal funds rate be above 3.75% following the Fed's Sep 16, 2026 meeting?"
  current_price: 0.34
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-09-16T18:05:00Z"
bullets:
  - "Kalshi pins the Fed funds upper bound in the 3.50-3.75% range: 94% above 3.25%, 78% above 3.50%, only 34% above 3.75%."
  - "CME FedWatch hike odds signal hawkish drift, but Kalshi pricing stays below 4.00%, consistent with hold rather than hike near-term."
  - "Companion ladder CM-EVT-RJ6SMJGK50 prices 96% above 3.50% but collapses to 2% above 3.75%, confirming both markets see 3.50% as the ceiling floor."
  - "Resolves via Federal Reserve official rate announcement; any emergency inter-meeting move would settle at actual upper bound."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "CME FedWatch shows 28% of traders pricing a December Fed rate hike, the first non-zero hike odds since 2023, as markets push first cut to September."
    publisher: "Warren Cohen"
    published_at: "2026-06-01T16:15:00.000Z"
    source_url: "https://thefinancialwire.com/markets-priced-the-first-fed-rate-cut-no-earlier-than-september-and-28-of-cme-fedwatch-traders-now-bet-on-a-december-hike-the-first-non-zero-hike-odds-since-2023/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Warren Cohen"
        source_url: "https://thefinancialwire.com/markets-priced-the-first-fed-rate-cut-no-earlier-than-september-and-28-of-cme-fedwatch-traders-now-bet-on-a-december-hike-the-first-non-zero-hike-odds-since-2023/"
        retrieved_at: "2026-06-03T01:50:17+00:00"
  - type: "pm_response"
    notes: "Two Kalshi ladders converge on a 3.50% ceiling with near-zero probability above 3.75%, sharply at odds with the 28% December hike odds cited by CME FedWatch."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Warren Cohen: Markets priced the first Fed rate cut no earlier than September, and"
    url: "https://thefinancialwire.com/markets-priced-the-first-fed-rate-cut-no-earlier-than-september-and-28-of-cme-fedwatch-traders-now-bet-on-a-december-hike-the-first-non-zero-hike-odds-since-2023/"
    published_at: "2026-06-01T16:15:00.000Z"
    retrieved_at: "2026-06-03T01:50:17+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
