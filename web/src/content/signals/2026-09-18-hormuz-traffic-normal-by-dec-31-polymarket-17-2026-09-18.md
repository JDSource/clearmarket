---
signal_id: "CMSIG2026091806"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-17-2026-09-18"
headline: "Hormuz traffic normal by Dec 31: Polymarket 17%"
semantic_title: "Strait of Hormuz returning to normal by year-end stays unlikely"
telemetry: "Polymarket 17%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-18T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.17
  volume_24h_usd: 23478.750264000002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket prediction market puts only 17% odds on Strait of Hormuz traffic returning to normal by December 31, 2026."
  - "Houthi advances toward Bab el-Mandeb and continued regional escalation are consistent with Polymarket pricing a disrupted waterway through year-end."
  - "A separate US Treasury sanction on Iranian crypto exchange BitBank, tied to Hormuz maritime payments, adds further evidence of persistent chokepoint pressure."
  - "Resolution: Polymarket settles via its UMA oracle process, requiring verified shipping traffic data."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Houthi rebels have captured territory near the Bab el-Mandeb strait, threatening Saudi oil export routes and deepening regional instability."
    publisher: "indiatoday.in"
    published_at: "2026-09-18T00:00:00.000Z"
    source_url: "https://www.indiatoday.in/world/story/houthis-bab-el-mandeb-advance-saudi-oil-exports-red-sea-security-ptag-2997268-2026-09-18"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "indiatoday.in"
        source_url: "https://www.indiatoday.in/world/story/houthis-bab-el-mandeb-advance-saudi-oil-exports-red-sea-security-ptag-2997268-2026-09-18"
        retrieved_at: "2026-09-18T12:38:42+00:00"
  - type: "pm_response"
    notes: "Polymarket at 17% reflects deepening skepticism that the Hormuz disruption resolves within 2026, consistent with escalating Houthi and Iranian maritime activity this week."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "indiatoday.in: Houthis at Bab el-Mandeb raise fears for Saudi oil exports and Red Sea"
    url: "https://www.indiatoday.in/world/story/houthis-bab-el-mandeb-advance-saudi-oil-exports-red-sea-security-ptag-2997268-2026-09-18"
    published_at: "2026-09-18T00:00:00.000Z"
    retrieved_at: "2026-09-18T12:38:42+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
