---
signal_id: "CMSIG2026061805"
signal_slug: "us-iran-nuclear-deal-by-june-30-polymarket-51-2026-06-18"
headline: "US-Iran nuclear deal by June 30: Polymarket 51%"
semantic_title: "US-Iran nuclear deal by June 30 wavers at the midpoint"
telemetry: "Polymarket 51%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-18T09:17:18.000Z"
event_id: "CM-EVT-LG47Z78CF2"
event_slug: "us-iran-nuclear-deal-by-june-30"
event_question: "Will the US and Iran reach a nuclear deal by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa70fc3695a65833b91b45df6db6015096f3e1471b70352ca411b4209010e7633"
  question_raw: "US-Iran nuclear deal by June 30?"
  current_price: 0.51
  volume_24h_usd: 1088905.717404001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "The Polymarket prediction market prices exactly 51% on a US-Iran nuclear deal being reached by June 30, 2026."
  - "The MoU signing and uranium dilution terms move the process forward, but unresolved technical issues keep the market at a coin-flip rather than near-certainty."
  - "The near-50/50 pricing reflects genuine timeline ambiguity: a deal in principle exists but formal nuclear agreement by June 30 is uncertain."
  - "The Polymarket contract on Iran ending uranium enrichment by June 30 sits at 24% (CM-EVT-73D6P1DKY8), and by December 31 at 46% (CM-EVT-4CKJ2D3T77), showing the market assigns better odds to a longer runway than to the June deadline."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Turkey's foreign minister confirmed the US-Iran deal still awaits resolution of technical issues, even as the Islamabad MoU was signed and uranium dilution terms were announced."
    publisher: "aa.com.tr"
    published_at: "2026-06-18T09:17:18.000Z"
    source_url: "https://www.aa.com.tr/en/turkiye/us-iran-deal-awaits-resolution-of-technical-issues-turkish-foreign-minister/3970356"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "aa.com.tr"
        source_url: "https://www.aa.com.tr/en/turkiye/us-iran-deal-awaits-resolution-of-technical-issues-turkish-foreign-minister/3970356"
        retrieved_at: "2026-06-18T11:48:44+00:00"
  - type: "pm_response"
    notes: "The Polymarket contract resolves via uma_oracle; the distinction between an MoU and a full nuclear deal is likely a material resolution edge case."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "aa.com.tr: US-Iran deal awaits resolution of technical issues: Turkish foreign mi"
    url: "https://www.aa.com.tr/en/turkiye/us-iran-deal-awaits-resolution-of-technical-issues-turkish-foreign-minister/3970356"
    published_at: "2026-06-18T09:17:18.000Z"
    retrieved_at: "2026-06-18T11:48:44+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
