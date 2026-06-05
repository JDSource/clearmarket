---
signal_id: "CMSIG2026060306"
signal_slug: "us-iran-nuclear-deal-by-june-30-polymarket-28-2026-06-03"
headline: "US-Iran nuclear deal by June 30: Polymarket 28%"
semantic_title: "US-Iran nuclear deal by June 30 holds minority positioning"
telemetry: "Polymarket 28%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-03T18:02:52.000Z"
event_id: "CM-EVT-LG47Z78CF2"
event_slug: "us-iran-nuclear-deal-by-june-30"
event_question: "Will the US and Iran reach a nuclear deal by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa70fc3695a65833b91b45df6db6015096f3e1471b70352ca411b4209010e7633"
  question_raw: "US-Iran nuclear deal by June 30?"
  current_price: 0.28
  volume_24h_usd: 207316.77510300005
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices a 28% chance the U.S. and Iran reach a nuclear deal by June 30."
  - "The Lebanon ceasefire is framed as a precondition for broader Iran talks, but Hezbollah's subsequent rejection undermines that path before month-end."
  - "Companion Polymarket contracts on Israeli forces entering Nabatieh (19%) and Tyre (4%) suggest the military situation remains fluid, complicating diplomacy."
  - "Resolves via Polymarket's UMA oracle; a formal signed nuclear agreement between the U.S. and Iran must be reached before June 30."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Israel and Lebanon agreed to renew their ceasefire, contingent on Hezbollah halting attacks, in a U.S.-brokered arrangement tied to broader Iran negotiations."
    publisher: "bbc.co.uk"
    published_at: "2026-06-03T18:02:52.000Z"
    source_url: "https://www.bbc.co.uk/news/articles/c5y01pdqvkgo"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "bbc.co.uk"
        source_url: "https://www.bbc.co.uk/news/articles/c5y01pdqvkgo"
        retrieved_at: "2026-06-05T12:03:19+00:00"
  - type: "pm_response"
    notes: "Polymarket holds 28% on a June 30 deal despite Hezbollah's rejection of the ceasefire, implying the market sees a residual diplomatic path but assigns it low probability."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "bbc.co.uk: Israel and Lebanon agree to implement ceasefire if Hezbollah stops att"
    url: "https://www.bbc.co.uk/news/articles/c5y01pdqvkgo"
    published_at: "2026-06-03T18:02:52.000Z"
    retrieved_at: "2026-06-05T12:03:19+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
