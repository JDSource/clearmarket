---
signal_id: "CMSIG2026102904"
signal_slug: "hegseth-out-as-secdef-by-dec-31-polymarket-31-2026-10-29"
headline: "Hegseth out as SecDef by Dec 31: Polymarket 31%"
semantic_title: "Hegseth out as Defense Secretary by year-end holds near 30%"
telemetry: "Polymarket 31%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-29T20:00:00.000Z"
event_id: "CM-EVT-JWSH7Q94S8"
event_slug: "pete-hegseth-out-as-secretary-of-defense-by-december-31"
event_question: "Will Pete Hegseth be out as Secretary of Defense by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0fcfcfc35d71424c0693c717d2e3bc9b8992910835d124d80cd2f01498f1d3dc"
  question_raw: "Pete Hegseth out as Secretary of Defense by December 31?"
  current_price: 0.31
  volume_24h_usd: 29120.540398
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Hegseth departing as Secretary of Defense by December 31 stands at 31%."
  - "Hegseth firing the Pentagon's top military planner is a significant escalation of his authority, but the market puts only about one-in-three odds on his own departure this year."
  - "The market is not pricing in the dismissal as a precursor to Hegseth's own removal, the probability stays well below 50%."
  - "With the December 31 deadline weeks away, the Kalshi contract on his June 30 departure (CM-EVT-L20R2VDVG3) has no price available; the Polymarket year-end read is the primary signal."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Defense Secretary Pete Hegseth fired the Pentagon's top military planner as President Trump considers new strikes on Iran."
    publisher: "Konstantin Toropin, Associated Press"
    published_at: "2026-10-29T20:00:00.000Z"
    source_url: "https://www.pbs.org/newshour/politics/hegseth-fires-the-pentagons-top-military-planner-even-as-trump-considers-new-iran-strikes"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Konstantin Toropin, Associated Press"
        source_url: "https://www.pbs.org/newshour/politics/hegseth-fires-the-pentagons-top-military-planner-even-as-trump-considers-new-iran-strikes"
        retrieved_at: "2026-10-30T07:48:00+00:00"
  - type: "pm_response"
    notes: "Polymarket at 31% reflects meaningful but minority odds of Hegseth's departure by year-end, even as his aggressive personnel moves intensify scrutiny."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Konstantin Toropin, Associated Press: Hegseth fires the Pentagon's top military planner even as Trump consid"
    url: "https://www.pbs.org/newshour/politics/hegseth-fires-the-pentagons-top-military-planner-even-as-trump-considers-new-iran-strikes"
    published_at: "2026-10-29T20:00:00.000Z"
    retrieved_at: "2026-10-30T07:48:00+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
