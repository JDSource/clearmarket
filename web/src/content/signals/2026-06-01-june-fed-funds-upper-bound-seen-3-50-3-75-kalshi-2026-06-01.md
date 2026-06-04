---
signal_id: "CMSIG2026060101"
signal_slug: "june-fed-funds-upper-bound-seen-3-50-3-75-kalshi-2026-06-01"
headline: "June Fed funds upper bound seen 3.50-3.75%: Kalshi"
semantic_title: "Funds rate above 3.75 percent post-June FOMC a long shot"
telemetry: "Kalshi 34%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-01T16:15:00.000Z"
event_id: "CM-EVT-4ZQLQPNH91"
event_slug: "kxfed-26sep"
event_question: "Fed funds upper bound following June 2026 FOMC"
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
  - "Kalshi pins the Fed funds upper bound in the 3.50-3.75% range: 91% above 3.50% but only 34% above 3.75%."
  - "CME FedWatch hike odds are consistent with the Kalshi distribution, which shows near-zero probability above 4.25%."
  - "The sharp drop from 91% to 34% between 3.50% and 3.75% marks the market's credible ceiling for near-term policy."
  - "A companion Kalshi contract prices only 19% on any Fed cut before 2027, underscoring a prolonged hold as the base case."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "CME FedWatch now shows 28% of traders pricing a December Fed rate hike, the first non-zero hike odds since 2023."
    publisher: "Warren Cohen"
    published_at: "2026-06-01T16:15:00.000Z"
    source_url: "https://thefinancialwire.com/markets-priced-the-first-fed-rate-cut-no-earlier-than-september-and-28-of-cme-fedwatch-traders-now-bet-on-a-december-hike-the-first-non-zero-hike-odds-since-2023/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Warren Cohen"
        source_url: "https://thefinancialwire.com/markets-priced-the-first-fed-rate-cut-no-earlier-than-september-and-28-of-cme-fedwatch-traders-now-bet-on-a-december-hike-the-first-non-zero-hike-odds-since-2023/"
        retrieved_at: "2026-06-04T11:14:54+00:00"
  - type: "pm_response"
    notes: "Kalshi resolves via the Federal Reserve's official post-meeting rate announcement."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Warren Cohen: Markets priced the first Fed rate cut no earlier than September, and"
    url: "https://thefinancialwire.com/markets-priced-the-first-fed-rate-cut-no-earlier-than-september-and-28-of-cme-fedwatch-traders-now-bet-on-a-december-hike-the-first-non-zero-hike-odds-since-2023/"
    published_at: "2026-06-01T16:15:00.000Z"
    retrieved_at: "2026-06-04T11:14:54+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
