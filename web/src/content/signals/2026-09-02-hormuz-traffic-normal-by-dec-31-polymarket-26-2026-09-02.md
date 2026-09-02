---
signal_id: "CMSIG2026090206"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-26-2026-09-02"
headline: "Hormuz traffic normal by Dec 31: Polymarket 26%"
semantic_title: "Strait of Hormuz normal traffic by year-end holds below 30%"
telemetry: "Polymarket 26%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-02T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.26
  volume_24h_usd: 69229.86162700003
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Hormuz traffic returning to normal by December 31 sits at 26%, pricing the outcome as unlikely through year-end."
  - "Fresh US-Iran military exchanges break a month-long lull and are directly hostile to any near-term normalization of the Strait, the 26% is consistent with renewed escalation."
  - "Iran attacks on Gulf neighbors (Story 20) and US bases in Jordan (Story 27) compound the disruption risk, reinforcing the below-30% positioning."
  - "Resolution via UMA oracle on whether Hormuz transit volumes return to pre-conflict norms by December 31; the contract does not define a specific vessel-count threshold publicly."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran launched retaliatory strikes on US bases across the Middle East after US strikes killed five people at a wedding, escalating the US-Iran military exchange."
    publisher: "rfi.fr"
    published_at: "2026-09-02T00:00:00.000Z"
    source_url: "https://www.rfi.fr/en/international-news/20260902-iran-attacks-us-sites-after-american-strikes-wedding-deaths"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "rfi.fr"
        source_url: "https://www.rfi.fr/en/international-news/20260902-iran-attacks-us-sites-after-american-strikes-wedding-deaths"
        retrieved_at: "2026-09-02T12:29:02+00:00"
  - type: "pm_response"
    notes: "Polymarket at 26% is the only priced Hormuz resolution signal available; all other Hormuz candidate contracts show no price, limiting cross-market comparison."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "rfi.fr: Iran attacks US sites after American strikes, wedding deaths"
    url: "https://www.rfi.fr/en/international-news/20260902-iran-attacks-us-sites-after-american-strikes-wedding-deaths"
    published_at: "2026-09-02T00:00:00.000Z"
    retrieved_at: "2026-09-02T12:29:02+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
