---
signal_id: "CMSIG2026071907"
signal_slug: "clarity-act-signed-in-2026-polymarket-43-2026-07-19"
headline: "CLARITY Act signed in 2026: Polymarket 43%"
semantic_title: "CLARITY Act passage in 2026 holds below 50%"
telemetry: "Polymarket 43%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-19T00:00:00.000Z"
event_id: "CM-EVT-ZXN47LV744"
event_slug: "clarity-act-signed-into-law-in-2026"
event_question: "Will the Clarity Act be signed into law in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9cb23d04b2ded06147482076688b69b487a8d982c63ebdda2ab3678cf27cf390"
  question_raw: "Clarity Act signed into law in 2026?"
  current_price: 0.43
  volume_24h_usd: 110541.63730700004
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "Polymarket prices a 43% probability that the CLARITY Act is signed into law in 2026."
  - "Warren's ethics pushback and Trump's crypto income scrutiny are consistent with the below-50% pricing; the market does not yet see passage as a base case."
  - "Story 35 reports Trump has agreed to ethics amendments as the final hurdle; if confirmed, that could shift the distribution materially, but no official White House confirmation exists yet."
  - "Resolves via Polymarket UMA oracle on signing by the President; Senate passage and House reconciliation both remain prerequisites."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Senator Elizabeth Warren is pressing Trump for crypto earnings disclosures as the Senate weighs the CLARITY Act, with Trump's $1.4 billion in crypto income drawing scrutiny."
    publisher: "Kevin Helms"
    published_at: "2026-07-19T00:00:00.000Z"
    source_url: "https://news.bitcoin.com/trumps-1-4b-crypto-income-draws-scrutiny-as-senate-weighs-clarity-act/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Kevin Helms"
        source_url: "https://news.bitcoin.com/trumps-1-4b-crypto-income-draws-scrutiny-as-senate-weighs-clarity-act/"
        retrieved_at: "2026-07-21T10:22:25+00:00"
  - type: "pm_response"
    notes: "Polymarket at 43% on CLARITY Act passage; Story 35's unconfirmed ethics amendment agreement represents a potential upside catalyst not yet reflected in the current contract price."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Kevin Helms: Trump’s $1.4B Crypto Income Draws Scrutiny as Senate Weighs CLARITY Ac"
    url: "https://news.bitcoin.com/trumps-1-4b-crypto-income-draws-scrutiny-as-senate-weighs-clarity-act/"
    published_at: "2026-07-19T00:00:00.000Z"
    retrieved_at: "2026-07-21T10:22:25+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
