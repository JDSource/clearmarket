---
signal_id: "CMSIG2026072307"
signal_slug: "clarity-act-signed-in-2026-polymarket-39-2026-07-23"
headline: "Clarity Act signed in 2026: Polymarket 39%"
semantic_title: "CLARITY Act becoming law in 2026 priced below 40%"
telemetry: "Polymarket 39%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-23T00:00:00.000Z"
event_id: "CM-EVT-ZXN47LV744"
event_slug: "clarity-act-signed-into-law-in-2026"
event_question: "Will the Clarity Act be signed into law in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9cb23d04b2ded06147482076688b69b487a8d982c63ebdda2ab3678cf27cf390"
  question_raw: "Clarity Act signed into law in 2026?"
  current_price: 0.39
  volume_24h_usd: 119615.20660500001
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "Polymarket prices a 39% chance the Clarity Act is signed into law in 2026, a minority probability reflecting real legislative uncertainty."
  - "Stalled Senate talks are consistent with the sub-40% read; the market is not pricing the bill as likely to pass this year."
  - "Bitcoin's drop to below $64,700 (Story 34/35) correlates with the legislative setback, but the BTC price-level ladder (CM-EVT-R55TT711T7) already implies Bitcoin below $67,500 by July 31 at 61%, suggesting the market had priced in weakness before the stall."
  - "Polymarket contract resolves via UMA oracle; the bill requires Senate Republican votes plus Democratic crossover support, the resolution trigger is presidential signature."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Bitcoin slid below $64,700 partly as Senate CLARITY Act bipartisan talks stalled, with the new draft barring Trump and officials from issuing crypto."
    publisher: "Terence Zimwara"
    published_at: "2026-07-23T00:00:00.000Z"
    source_url: "https://news.bitcoin.com/bitcoin-slides-below-64700-as-senate-clarity-act-talks-stall-and-oil-tops-101/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Terence Zimwara"
        source_url: "https://news.bitcoin.com/bitcoin-slides-below-64700-as-senate-clarity-act-talks-stall-and-oil-tops-101/"
        retrieved_at: "2026-07-24T10:13:15+00:00"
  - type: "pm_response"
    notes: "Polymarket at 39% on the Clarity Act; the legislative stall news is directionally aligned with, not a surprise versus, the sub-50% market probability."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Terence Zimwara: Bitcoin Slides Below $64,700 as Senate CLARITY Act Talks Stall and Oil"
    url: "https://news.bitcoin.com/bitcoin-slides-below-64700-as-senate-clarity-act-talks-stall-and-oil-tops-101/"
    published_at: "2026-07-23T00:00:00.000Z"
    retrieved_at: "2026-07-24T10:13:15+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
