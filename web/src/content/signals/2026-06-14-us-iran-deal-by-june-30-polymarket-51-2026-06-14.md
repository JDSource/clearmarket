---
signal_id: "CMSIG2026061401"
signal_slug: "us-iran-deal-by-june-30-polymarket-51-2026-06-14"
headline: "US-Iran deal by June 30: Polymarket 51%"
semantic_title: "US-Iran nuclear deal by June 30 wavers near coin-flip"
telemetry: "Polymarket 51%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-14T03:01:33.000Z"
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
  - "Polymarket prices the US-Iran nuclear deal by June 30 at 51%, essentially a coin-flip despite Trump's signing claims."
  - "Trump announced a Sunday Geneva signing, but Tehran publicly stated no final decision had been made, keeping market conviction low."
  - "The near-even split reflects the gap between Trump's optimism and Iranian ambiguity on finalizing terms."
  - "A companion Kalshi contract on a Trump visit to Iran sits at just 8%, suggesting markets price diplomacy without personal engagement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump signaled a Sunday signing of a US-Iran peace deal in Geneva, with the Strait of Hormuz reopening expected to follow."
    publisher: "Balaram Menon"
    published_at: "2026-06-14T03:01:33.000Z"
    source_url: "https://gulfnews.com/world/mena/iran-us-deal-edges-closer-as-trump-signals-sunday-signing-and-hormuz-reopening-1.500573653"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Balaram Menon"
        source_url: "https://gulfnews.com/world/mena/iran-us-deal-edges-closer-as-trump-signals-sunday-signing-and-hormuz-reopening-1.500573653"
        retrieved_at: "2026-06-14T10:47:32+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via uma_oracle; Tehran's public hedging is the key factor holding the price from moving decisively above 50%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Balaram Menon: Trump Says US-Iran Peace Deal Imminent as Hormuz Strait Reopening Near"
    url: "https://gulfnews.com/world/mena/iran-us-deal-edges-closer-as-trump-signals-sunday-signing-and-hormuz-reopening-1.500573653"
    published_at: "2026-06-14T03:01:33.000Z"
    retrieved_at: "2026-06-14T10:47:32+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
