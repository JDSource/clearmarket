---
signal_id: "CMSIG2026110304"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-12-2026-11-03"
headline: "Hormuz traffic normal by Dec 31: Polymarket 12%"
semantic_title: "Strait of Hormuz traffic normalization stays a long shot"
telemetry: "Polymarket 12%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-03T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.12
  volume_24h_usd: 244410.33954499997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Strait of Hormuz traffic returning to normal by December 31 at just 12%."
  - "Fresh US strikes on Iranian targets are consistent with the low probability: the market sees very little chance of full normalization within two months."
  - "Iran's parallel diplomatic signals from President Pezeshkian have not moved the needle toward a higher probability, per current pricing."
  - "A companion question on whether the US and Iran will sign a deal has no live price, leaving the Polymarket Hormuz contract as the clearest quantified read on conflict resolution odds."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US struck Iranian targets in the Strait of Hormuz on the eve of the midterm elections, with officials leaving unclear what comes next."
    publisher: "Michelle L. Price, Samy Magdy, Elena Becatoros"
    published_at: "2026-11-03T00:00:00.000Z"
    source_url: "https://apnews.com/article/iran-us-strikes-strait-hormuz-183b3d32d9bf5241f744abb917e6713e"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Michelle L. Price, Samy Magdy, Elena Becatoros"
        source_url: "https://apnews.com/article/iran-us-strikes-strait-hormuz-183b3d32d9bf5241f744abb917e6713e"
        retrieved_at: "2026-11-03T15:45:44+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle based on verified shipping traffic data through December 31."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Michelle L. Price, Samy Magdy, Elena Becatoros: US strikes Iran on the eve of midterm elections, official says | AP Ne"
    url: "https://apnews.com/article/iran-us-strikes-strait-hormuz-183b3d32d9bf5241f744abb917e6713e"
    published_at: "2026-11-03T00:00:00.000Z"
    retrieved_at: "2026-11-03T15:45:44+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
