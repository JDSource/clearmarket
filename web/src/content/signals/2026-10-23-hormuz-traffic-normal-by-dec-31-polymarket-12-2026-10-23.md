---
signal_id: "CMSIG2026102306"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-12-2026-10-23"
headline: "Hormuz traffic normal by Dec 31: Polymarket 12%"
semantic_title: "Strait of Hormuz back to normal by year-end stays unlikely"
telemetry: "Polymarket 12%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-23T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.12
  volume_24h_usd: 35629.341316
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 12% odds on Strait of Hormuz ship traffic returning to normal by December 31, 2026."
  - "Active tanker attacks and a new U.S. Navy blockade of Iranian-port traffic are consistent with Polymarket's strongly bearish odds on near-term normalization."
  - "Oil prices near $100 per barrel (Story 31) provide a concurrent cross-market signal that capital is pricing prolonged disruption, not a quick resolution."
  - "Resolves via UMA oracle; the definition of 'normal' traffic levels will be key to settlement, with partial recovery scenarios unlikely to qualify."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran reported seven oil tankers attacked in the Strait of Hormuz, with the U.S. Navy blockade on Iranian-port-bound traffic taking effect October 23."
    publisher: "ETV Bharat English Team"
    published_at: "2026-10-23T00:00:00.000Z"
    source_url: "https://www.etvbharat.com/en/international/live-blog--us-israel-iran-war-houthi-saudi-arabia-strait-of-hormuz-latest-updates-enn26102300426"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ETV Bharat English Team"
        source_url: "https://www.etvbharat.com/en/international/live-blog--us-israel-iran-war-houthi-saudi-arabia-strait-of-hormuz-latest-updates-enn26102300426"
        retrieved_at: "2026-10-23T07:48:07+00:00"
  - type: "pm_response"
    notes: "Polymarket at 12% reflects the market's skepticism that the blockade, active hostilities, and diplomatic deadlock can all resolve within ten weeks."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ETV Bharat English Team: West Asia Crisis LIVE | 7 Oil Tankers Attacked In Hormuz, Says Iran; U"
    url: "https://www.etvbharat.com/en/international/live-blog--us-israel-iran-war-houthi-saudi-arabia-strait-of-hormuz-latest-updates-enn26102300426"
    published_at: "2026-10-23T00:00:00.000Z"
    retrieved_at: "2026-10-23T07:48:07+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
