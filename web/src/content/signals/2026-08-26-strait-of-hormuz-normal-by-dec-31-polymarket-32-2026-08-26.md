---
signal_id: "CMSIG2026082605"
signal_slug: "strait-of-hormuz-normal-by-dec-31-polymarket-32-2026-08-26"
headline: "Strait of Hormuz normal by Dec 31: Polymarket 32%"
semantic_title: "Hormuz traffic back to normal by year-end stays below 50%"
telemetry: "Polymarket 32%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-26T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.32
  volume_24h_usd: 83978.277517
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts 32% odds on Strait of Hormuz traffic returning to normal by December 31, resolves via uma_oracle."
  - "The Atlantic's reporting that Tehran is deliberately prolonging talks while U.S. munitions ran low is consistent with the market's below-50% pricing on a near-term resolution."
  - "Qatar PM heading to Tehran (Story 27) and Pakistan proposing a 60-day diplomatic timeline (Story 24) provide some upside optionality but have not shifted the Polymarket price above one-third."
  - "Resolves via uma_oracle determination that Strait of Hormuz shipping traffic has returned to pre-conflict normal levels by December 31, 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump is pursuing economic sanctions against Iran as a new lever after a prolonged bombing campaign and stalled diplomacy, with Tehran deliberately prolonging the conflict."
    publisher: "Jonathan Lemire, Nancy A. Youssef"
    published_at: "2026-08-26T00:00:00.000Z"
    source_url: "https://www.theatlantic.com/politics/2026/08/trump-iran-war-midterms-sanctions/688412/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jonathan Lemire, Nancy A. Youssef"
        source_url: "https://www.theatlantic.com/politics/2026/08/trump-iran-war-midterms-sanctions/688412/"
        retrieved_at: "2026-08-27T18:46:25+00:00"
  - type: "pm_response"
    notes: "Polymarket at 32% prices in meaningful skepticism that active diplomacy converts to a reopened strait within 2026."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jonathan Lemire, Nancy A. Youssef: The Real Reason Trump Wants Economic Sanctions in Iran - The Atlantic"
    url: "https://www.theatlantic.com/politics/2026/08/trump-iran-war-midterms-sanctions/688412/"
    published_at: "2026-08-26T00:00:00.000Z"
    retrieved_at: "2026-08-27T18:46:25+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
