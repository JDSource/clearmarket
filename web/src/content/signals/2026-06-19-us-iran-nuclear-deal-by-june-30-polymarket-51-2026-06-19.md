---
signal_id: "CMSIG2026061905"
signal_slug: "us-iran-nuclear-deal-by-june-30-polymarket-51-2026-06-19"
headline: "US-Iran nuclear deal by June 30: Polymarket 51%"
semantic_title: "US-Iran nuclear deal by June 30 holds at even odds after MOU signing"
telemetry: "Polymarket 51%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-19T11:53:17.000Z"
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
  - "The Polymarket contract on a US-Iran nuclear deal by June 30 sits at 51%, effectively coin-flip odds with 10 days remaining."
  - "The Lebanon ceasefire removes a key near-term obstacle to Switzerland talks, yet the market is not pricing a high-conviction outcome, reflecting the chaotic negotiating environment described in news coverage."
  - "The companion contract on Iran ending uranium enrichment by June 30 (CM-EVT-73D6P1DKY8) prices only 24%, indicating the market sharply discounts full denuclearization terms within this deadline even if a deal framework is signed."
  - "Resolves via uma_oracle; a formal nuclear deal announcement by June 30 is required for a yes resolution, not merely an MOU or ceasefire."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Israel and Hezbollah agreed to a ceasefire in Lebanon, easing tensions that had been straining the US-Iran interim memorandum of understanding signed June 18."
    publisher: "france24.com"
    published_at: "2026-06-19T11:53:17.000Z"
    source_url: "https://www.france24.com/en/middle-east/20260619-israel-hezbollah-agree-to-ceasefire-in-lebanon-as-attacks-strain-us-iran-interim-deal"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "france24.com"
        source_url: "https://www.france24.com/en/middle-east/20260619-israel-hezbollah-agree-to-ceasefire-in-lebanon-as-attacks-strain-us-iran-interim-deal"
        retrieved_at: "2026-06-20T10:30:38+00:00"
  - type: "pm_response"
    notes: "Polymarket at 51% reflects genuine uncertainty: a deal framework exists but full nuclear terms remain unresolved, and the Lebanon ceasefire is a necessary but not sufficient condition."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "france24.com: Israel, Hezbollah agree to ceasefire in Lebanon as attacks strain US-I"
    url: "https://www.france24.com/en/middle-east/20260619-israel-hezbollah-agree-to-ceasefire-in-lebanon-as-attacks-strain-us-iran-interim-deal"
    published_at: "2026-06-19T11:53:17.000Z"
    retrieved_at: "2026-06-20T10:30:38+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
