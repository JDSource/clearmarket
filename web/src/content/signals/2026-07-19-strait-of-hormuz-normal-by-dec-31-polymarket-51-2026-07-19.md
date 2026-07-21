---
signal_id: "CMSIG2026071905"
signal_slug: "strait-of-hormuz-normal-by-dec-31-polymarket-51-2026-07-19"
headline: "Strait of Hormuz normal by Dec 31: Polymarket 51%"
semantic_title: "Hormuz normalization by year-end sits near 50% amid escalation"
telemetry: "Polymarket 51%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-19T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.51
  volume_24h_usd: 46759.78738899999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices the December 31 Hormuz normalization contract at 51%, just above coin-flip odds, reflecting deep uncertainty about resolution timing."
  - "Fresh US airstrikes on IRGC targets and Iran's suspension of its Islamabad MoU after reporting 50 killed are consistent with a market that has not priced in near-term de-escalation."
  - "A companion Polymarket contract (CM-EVT-4J73Y3RD96) puts only 1% on Hormuz returning to normal by July 31, confirming the market sees no near-term resolution."
  - "The 50-percentage-point gap between the July 31 (1%) and December 31 (51%) contracts implies the market concentrates resolution probability heavily in Q4 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US forces launched new airstrikes targeting IRGC units in Iran after two US troops were killed in an Iranian attack on a base in Jordan, escalating the Strait of Hormuz conflict."
    publisher: "aa.com.tr"
    published_at: "2026-07-19T00:00:00.000Z"
    source_url: "https://www.aa.com.tr/en/americas/us-forces-launch-new-strikes-on-iran-targeting-irgc-units-centcom/4002538"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "aa.com.tr"
        source_url: "https://www.aa.com.tr/en/americas/us-forces-launch-new-strikes-on-iran-targeting-irgc-units-centcom/4002538"
        retrieved_at: "2026-07-19T09:48:56+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolved via UMA oracle; the wide term-structure spread between July and December deadlines is the key signal."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "aa.com.tr: US forces launch new strikes on Iran, targeting IRGC units: CENTCOM"
    url: "https://www.aa.com.tr/en/americas/us-forces-launch-new-strikes-on-iran-targeting-irgc-units-centcom/4002538"
    published_at: "2026-07-19T00:00:00.000Z"
    retrieved_at: "2026-07-19T09:48:56+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
