---
signal_id: "CMSIG2026072405"
signal_slug: "hormuz-normal-by-dec-31-polymarket-51-2026-07-24"
headline: "Hormuz normal by Dec 31: Polymarket 51%"
semantic_title: "Strait of Hormuz back to normal by year-end sits near 50%"
telemetry: "Polymarket 51%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-24T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.51
  volume_24h_usd: 168294.78269199998
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 51% chance the Strait of Hormuz returns to normal shipping traffic by December 31, 2026, essentially a coin flip."
  - "Escalating strikes on night 13, Houthi attacks on Saudi tankers, and Iran rejecting a ceasefire are all consistent with a market stuck near 50% rather than pricing swift resolution."
  - "A separate Polymarket contract (CM-EVT-4J73Y3RD96) prices only 1% on Hormuz returning to normal by July 31, the term structure shows the market sees recovery as a late-year possibility at best."
  - "The Kalshi ladder (CM-EVT-ZP3JDLXZQ0) implies peak single-day Hormuz transit calls in the 10-15 range, with 71% above 10 but only 16% above 15, consistent with severely reduced but not zero traffic."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US launched a 13th consecutive night of strikes on Iranian military targets as Iran-backed Houthis attacked Saudi oil tankers and the US vowed retaliation."
    publisher: "rte.ie"
    published_at: "2026-07-24T00:00:00.000Z"
    source_url: "https://www.rte.ie/news/2026/0724/1584878-us-strikes-iran/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "rte.ie"
        source_url: "https://www.rte.ie/news/2026/0724/1584878-us-strikes-iran/"
        retrieved_at: "2026-07-24T10:13:15+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; the near-50% price reflects maximum uncertainty given active combat and no ceasefire framework."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "rte.ie: Fresh strikes as US vows retaliation for Houthis attacks"
    url: "https://www.rte.ie/news/2026/0724/1584878-us-strikes-iran/"
    published_at: "2026-07-24T00:00:00.000Z"
    retrieved_at: "2026-07-24T10:13:15+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
