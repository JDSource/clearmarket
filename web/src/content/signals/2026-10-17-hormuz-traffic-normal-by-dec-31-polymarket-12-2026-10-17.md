---
signal_id: "CMSIG2026101708"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-12-2026-10-17"
headline: "Hormuz traffic normal by Dec 31: Polymarket 12%"
semantic_title: "Strait of Hormuz traffic back to normal by year-end stays unlikely"
telemetry: "Polymarket 12%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-17T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.12
  volume_24h_usd: 29749.808606000002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 12% odds on Strait of Hormuz shipping traffic returning to normal by December 31, 2026."
  - "Record-high attack reports are consistent with this low probability; the market is not pricing a near-term resolution despite Iran's stated openness to talks."
  - "AP's reporting on uneven but accumulating retail price impacts from the Iran war (Story 10) provides a real-economy backdrop: the market's 12% implies continued disruption through year-end."
  - "Resolution is via Polymarket's UMA oracle; 'normal' traffic is the key definitional edge case that the oracle will need to adjudicate."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Reported attacks on ships in or near the Strait of Hormuz have reached a record high, with Iran's president denying nuclear ambitions and signaling readiness for talks."
    publisher: "Frank Andrews"
    published_at: "2026-10-17T00:00:00.000Z"
    source_url: "https://www.cbsnews.com/live-updates/iran-war-us-trump-strait-of-hormuz-yemen-houthis-saudi-arabia/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Frank Andrews"
        source_url: "https://www.cbsnews.com/live-updates/iran-war-us-trump-strait-of-hormuz-yemen-houthis-saudi-arabia/"
        retrieved_at: "2026-10-17T11:57:10+00:00"
  - type: "pm_response"
    notes: "Polymarket resolves via UMA oracle; at 12%, the contract prices a roughly one-in-eight chance of full normalization by year-end despite record attack activity."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Frank Andrews: Live Updates: Iran's president denies nuclear ambitions, says he's rea"
    url: "https://www.cbsnews.com/live-updates/iran-war-us-trump-strait-of-hormuz-yemen-houthis-saudi-arabia/"
    published_at: "2026-10-17T00:00:00.000Z"
    retrieved_at: "2026-10-17T11:57:10+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
