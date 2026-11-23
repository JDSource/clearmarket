---
signal_id: "CMSIG2026112306"
signal_slug: "strait-of-hormuz-normal-by-dec-31-polymarket-3-2026-11-23"
headline: "Strait of Hormuz normal by Dec 31: Polymarket 3%"
semantic_title: "Strait of Hormuz returning to normal traffic by year-end stays a long shot"
telemetry: "Polymarket 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-23T03:22:56.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.028
  volume_24h_usd: 52570.852754
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only a 3% chance Strait of Hormuz traffic returns to normal by December 31, resolved via UMA oracle."
  - "Tanker mine strikes, drone shootdowns, and Israeli strike threats are consistent with the market's near-zero odds of a rapid normalization."
  - "Trading volume on the Israel-Turkey military clash contract surged 2,153x day over day, signaling broad fresh attention on regional escalation risk."
  - "Trump's signal that the next Iran move may not come until 2027 offers a theoretical pause, but the Polymarket contract on a US Iran deal by 2026 sits at just 2%, keeping the pressure on."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran shot down US drones and two oil tankers caught fire after hitting mines near the Strait of Hormuz, while Netanyahu was reported to be weighing a solo strike on Iran."
    publisher: "news.cgtn.com"
    published_at: "2026-11-23T03:22:56.000Z"
    source_url: "https://news.cgtn.com/news/2026-11-23/Iran-reports-downing-US-drones-Netanyahu-weighs-solo-strike-1SiCeMiYYeI/p.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "news.cgtn.com"
        source_url: "https://news.cgtn.com/news/2026-11-23/Iran-reports-downing-US-drones-Netanyahu-weighs-solo-strike-1SiCeMiYYeI/p.html"
        retrieved_at: "2026-11-23T07:47:39+00:00"
  - type: "pm_response"
    notes: "Polymarket at 3% on Hormuz normalization by year-end resolves via UMA oracle; the volume surge in adjacent contracts reflects acute market attention on escalation."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "news.cgtn.com: Iran reports downing US drones, Netanyahu weighs solo strike - CGTN"
    url: "https://news.cgtn.com/news/2026-11-23/Iran-reports-downing-US-drones-Netanyahu-weighs-solo-strike-1SiCeMiYYeI/p.html"
    published_at: "2026-11-23T03:22:56.000Z"
    retrieved_at: "2026-11-23T07:47:39+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
