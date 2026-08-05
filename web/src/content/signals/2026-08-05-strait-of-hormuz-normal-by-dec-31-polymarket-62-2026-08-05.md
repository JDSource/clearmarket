---
signal_id: "CMSIG2026080501"
signal_slug: "strait-of-hormuz-normal-by-dec-31-polymarket-62-2026-08-05"
headline: "Strait of Hormuz normal by Dec 31: Polymarket 62%"
semantic_title: "Hormuz traffic return to normal stays near 50-50 by year-end"
telemetry: "Polymarket 62%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-05T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.62
  volume_24h_usd: 176620.11254200005
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket contract puts 62% odds on Strait of Hormuz traffic returning to normal by December 31."
  - "Multiple reports of imminent deal and Trump optimism are consistent with the 62% pricing, market is not fully convinced a durable reopening follows a short-term framework."
  - "A 60-day temporary agreement would not automatically satisfy a 'return to normal' resolution; the gap between a deal and sustained normal traffic explains the below-75% pricing."
  - "News flow is dense across multiple stories today; the Polymarket contract resolves via uma_oracle, meaning resolution requires evidence of sustained normal traffic levels, not just a signed agreement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran and Oman reported positive progress on a phased Hormuz shipping framework while US-Tehran talks advance toward a potential 60-day agreement."
    publisher: "Jay Hilotin,Surabhi Vasundharadevi,Balaram Menon,Christian Borbon"
    published_at: "2026-08-05T00:00:00.000Z"
    source_url: "https://gulfnews.com/world/mena/iran-oman-report-positive-progress-on-strait-of-hormuz-shipping-framework-as-us-tehran-talks-advance-1.500630949"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jay Hilotin,Surabhi Vasundharadevi,Balaram Menon,Christian Borbon"
        source_url: "https://gulfnews.com/world/mena/iran-oman-report-positive-progress-on-strait-of-hormuz-shipping-framework-as-us-tehran-talks-advance-1.500630949"
        retrieved_at: "2026-08-05T10:30:51+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 62% is the only priced Hormuz event in this batch; all other Hormuz candidate events lack a current price."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jay Hilotin,Surabhi Vasundharadevi,Balaram Menon,Christian Borbon: Iran, Oman Report ‘Positive’ Progress on Strait of Hormuz Shipping Dea"
    url: "https://gulfnews.com/world/mena/iran-oman-report-positive-progress-on-strait-of-hormuz-shipping-framework-as-us-tehran-talks-advance-1.500630949"
    published_at: "2026-08-05T00:00:00.000Z"
    retrieved_at: "2026-08-05T10:30:51+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
