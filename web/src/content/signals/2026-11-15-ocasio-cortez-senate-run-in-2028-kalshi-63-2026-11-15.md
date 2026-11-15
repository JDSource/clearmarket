---
signal_id: "CMSIG2026111506"
signal_slug: "ocasio-cortez-senate-run-in-2028-kalshi-63-2026-11-15"
headline: "Ocasio-Cortez Senate run in 2028: Kalshi 63%"
semantic_title: "AOC runs for Senate in 2028 stays favored above 50%"
telemetry: "Kalshi 63%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-15T02:24:25.000Z"
event_id: "CM-EVT-MKF0D4VPY1"
event_slug: "kxaocsenate-28"
event_question: "Will Alexandria Ocasio-Cortez run for Senate in 2028?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAOCSENATE-28"
  question_raw: "Will Alexandria Ocasio-Cortez run for Senate in 2028?"
  current_price: 0.63
  volume_24h_usd: 1.26
  arbitration_model: "kalshi_staff"
  resolution_source: "ABC"
  resolves_at: "2028-04-01T14:00:00Z"
bullets:
  - "The Kalshi contract on Alexandria Ocasio-Cortez running for Senate in 2028 sits at 63%, keeping it in favored territory."
  - "The DSA presidential push introduces a competing path, yet the market still prices Senate as the more likely route at nearly two-to-one."
  - "If Ocasio-Cortez pivots toward a presidential campaign, a Senate run becomes mutually exclusive, which would be a direct resolution-negative event."
  - "Resolves via ABC; the contract likely turns on whether she files for a Senate seat, not merely expresses interest in a presidential bid."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "New York Democratic Socialists of America formally urged Representative Alexandria Ocasio-Cortez to run for president, complicating her Senate path."
    publisher: "Gloria Pazmino"
    published_at: "2026-11-15T02:24:25.000Z"
    source_url: "https://www.cnn.com/2026/11/14/politics/ocasio-cortez-aoc-dsa-new-york-president"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Gloria Pazmino"
        source_url: "https://www.cnn.com/2026/11/14/politics/ocasio-cortez-aoc-dsa-new-york-president"
        retrieved_at: "2026-11-15T07:48:03+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 63%; resolves via ABC; no intraday move claimed."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Gloria Pazmino: Democratic socialists in New York formally urge Alexandria Ocasio-Cort"
    url: "https://www.cnn.com/2026/11/14/politics/ocasio-cortez-aoc-dsa-new-york-president"
    published_at: "2026-11-15T02:24:25.000Z"
    retrieved_at: "2026-11-15T07:48:03+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
