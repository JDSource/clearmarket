---
signal_id: "CMSIG2026061108"
signal_slug: "democrats-win-senate-in-2026-polymarket-44-2026-06-11"
headline: "Democrats win Senate in 2026: Polymarket 44%"
semantic_title: "Senate Democratic control in 2026 wavers just below coin-flip"
telemetry: "Polymarket 44%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-11T14:35:39.000Z"
event_id: "CM-EVT-M9WJY06T90"
event_slug: "which-party-will-win-the-senate-in-2026"
event_question: "Will the Republican Party or Democratic Party win control of the U.S. Senate in the 2026 midterm elections?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x307a1ed89d60b61002dd5bbf00e1408c5ed2ab3fcdb056191ca7ef9bc34d38f3"
  question_raw: "Will the Democratic Party control the Senate after the 2026 Midterm elections?"
  current_price: 0.44
  volume_24h_usd: 6746.159307
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Democratic control of the Senate after 2026 midterms at 44%, just below even despite favorable forecaster moves."
  - "The three-race shift toward Democrats described by the forecaster is not yet fully reflected; the market still prices Republicans as slight favorites."
  - "A companion Kalshi contract prices Democratic control of the House at 79%, suggesting markets see an asymmetric Democratic advantage in the lower chamber."
  - "Resolution is via uma_oracle using certified election results; forecaster upgrades do not directly move the resolution trigger."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "A leading nonpartisan forecaster shifted three Senate races toward Democrats, calling the Democratic path to a majority clear."
    publisher: "AOL"
    published_at: "2026-06-11T14:35:39.000Z"
    source_url: "https://www.aol.com/news/senate-map-tightens-top-forecaster-143539392.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "AOL"
        source_url: "https://www.aol.com/news/senate-map-tightens-top-forecaster-143539392.html"
        retrieved_at: "2026-06-14T10:47:32+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via uma_oracle on final certified Senate race outcomes; the 44% price suggests markets discount the forecaster's optimism for Democrats."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "AOL: Senate map tightens as top forecaster moves 3 races toward Democrats -"
    url: "https://www.aol.com/news/senate-map-tightens-top-forecaster-143539392.html"
    published_at: "2026-06-11T14:35:39.000Z"
    retrieved_at: "2026-06-14T10:47:32+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
