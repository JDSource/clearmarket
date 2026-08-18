---
signal_id: "CMSIG2026081807"
signal_slug: "wti-crude-by-dec-31-ladder-implies-80-85-2026-08-18"
headline: "WTI crude by Dec 31: ladder implies $80-$85"
semantic_title: "WTI oil by year-end priced in the $80-$85 range"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-18T07:58:59.000Z"
event_id: "CM-EVT-N12K7YZCV3"
event_slug: "kxwtidiry-26dec31h1430"
event_question: "WTI crude oil price, December 31 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXWTIDIRY-26DEC31H1430-T85"
  question_raw: "Will the price of WTI oil be above 85 on December 31, 2026 at 02:30 PM EST?"
  current_price: 0.32
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "ICE"
  resolves_at: "2027-01-07T22:30:00Z"
bullets:
  - "The prediction market ladder for WTI crude on December 31 implies a central range of $80-$85: 53% above $80 but only 32% above $85."
  - "Iran-Oman escalation and Hormuz uncertainty are consistent with elevated oil price distribution, with the tail showing 17% above $100 and 13% above $120."
  - "The fat upper tail at $100-$120 reflects genuine geopolitical risk premium in the distribution, not a base case."
  - "The 10-year Treasury yield at 4.744% noted in MarketScreener data confirms bond markets are also registering the inflation-risk feedback loop from oil."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Treasury yields rose as oil prices gained amid escalating US-Iran tensions and threats against Oman, fueling fresh inflation fears."
    publisher: "Joseph Wilkins"
    published_at: "2026-08-18T07:58:59.000Z"
    source_url: "https://www.cnbc.com/2026/08/18/treasury-yields-.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Joseph Wilkins"
        source_url: "https://www.cnbc.com/2026/08/18/treasury-yields-.html"
        retrieved_at: "2026-08-18T08:30:34+00:00"
  - type: "pm_response"
    notes: "Ladder carries no named resolution source in the provided data; the distribution's heavy right tail is the key signal for cross-market inflation risk reads."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Joseph Wilkins: Treasury yields rise as oil gains and U.S.-Iran tensions fuel inflatio"
    url: "https://www.cnbc.com/2026/08/18/treasury-yields-.html"
    published_at: "2026-08-18T07:58:59.000Z"
    retrieved_at: "2026-08-18T08:30:34+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
