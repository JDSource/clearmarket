---
signal_id: "CMSIG2026092705"
signal_slug: "hormuz-back-to-normal-by-dec-31-polymarket-22-2026-09-27"
headline: "Hormuz back to normal by Dec 31: Polymarket 22%"
semantic_title: "Strait of Hormuz back to normal by year-end stays below 25%"
telemetry: "Polymarket 22%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-27T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.22
  volume_24h_usd: 47164.339777999994
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts 22% on Strait of Hormuz traffic returning to normal by December 31, keeping resolution a long shot."
  - "Trump's public rejection of the Iranian truce roadmap is consistent with the market's sub-25% pricing; a diplomatic breakthrough before year-end looks unlikely."
  - "Iran's insistence on diplomacy as the only path to reopening the strait, combined with Trump signaling resumed hostilities post-midterms, supports the market's skeptical stance."
  - "A companion Kalshi contract (CM-EVT-34SYT4T2T1) puts just 2% on the US reopening its embassy in Iran by 2026, confirming the broader diplomatic impasse is priced across venues."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump rejected Iran's seven-day truce plan at the UN but expects indirect talks to resume this week, while Iran insists the Strait of Hormuz can only be reopened through diplomacy."
    publisher: "france24.com"
    published_at: "2026-09-27T00:00:00.000Z"
    source_url: "https://www.france24.com/en/middle-east/20260927-trump-expects-iran-talks-next-week-after-rejecting-seven-day-truce-proposal"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "france24.com"
        source_url: "https://www.france24.com/en/middle-east/20260927-trump-expects-iran-talks-next-week-after-rejecting-seven-day-truce-proposal"
        retrieved_at: "2026-09-28T07:47:41+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; 'normal' traffic likely requires an official or widely reported return to pre-conflict transit volumes."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "france24.com: Trump expects Iran talks next week after rejecting seven-day truce pro"
    url: "https://www.france24.com/en/middle-east/20260927-trump-expects-iran-talks-next-week-after-rejecting-seven-day-truce-proposal"
    published_at: "2026-09-27T00:00:00.000Z"
    retrieved_at: "2026-09-28T07:47:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
