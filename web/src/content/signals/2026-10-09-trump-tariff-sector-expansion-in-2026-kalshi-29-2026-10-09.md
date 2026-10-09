---
signal_id: "CMSIG2026100905"
signal_slug: "trump-tariff-sector-expansion-in-2026-kalshi-29-2026-10-09"
headline: "Trump tariff sector expansion in 2026: Kalshi 29%"
semantic_title: "Tariff sector scope expansion holds near 30%"
telemetry: "Kalshi 29%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-09T00:00:00.000Z"
event_id: "CM-EVT-YH6B0KCSV8"
event_slug: "kxtariffsector-27jan01"
event_question: "Which sectors will Trump impose tariffs on in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTARIFFSECTOR-27JAN01-WIND"
  question_raw: "Will Trump issue any executive action on imposing tariffs specifically on wind turbines, where the executive action must explicitly reference wind turbines in its title, operative text, or fact sheet (not merely in an attached tariff schedule annex) during in 2026?"
  current_price: 0.29
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "the White House"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices 29% on Trump imposing tariffs on additional sectors in 2026, per the White House resolution source."
  - "The broad global tariff announcement covers 60 economies but the Kalshi contract on further sector expansion stays well below 50%, suggesting markets see current action as largely contained."
  - "The EU tech-fine warning adds an escalation risk not yet fully priced; 29% reflects uncertainty rather than conviction either way."
  - "Resolves via the White House; the contract likely tracks formal executive action designating new product categories, not the rate level on existing tariffs."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Trump administration unveiled new import tariffs of 10-12.5% on goods from 60 economies and threatened additional duties targeting the European Union over technology fines."
    publisher: "cnnbc.com"
    published_at: "2026-10-09T00:00:00.000Z"
    source_url: "https://cnnbc.com/united-states-unveils-broad-global-tariffs-and-warns-european-union-over-technology-fines"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cnnbc.com"
        source_url: "https://cnnbc.com/united-states-unveils-broad-global-tariffs-and-warns-european-union-over-technology-fines"
        retrieved_at: "2026-10-09T07:48:13+00:00"
  - type: "pm_response"
    notes: "Kalshi at 29% is below even odds despite a significant tariff announcement, implying markets are not pricing further sectoral expansion as the base case."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cnnbc.com: United States Unveils Broad Global Tariffs and Warns European Union Ov"
    url: "https://cnnbc.com/united-states-unveils-broad-global-tariffs-and-warns-european-union-over-technology-fines"
    published_at: "2026-10-09T00:00:00.000Z"
    retrieved_at: "2026-10-09T07:48:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
