---
signal_id: "CMSIG2026062408"
signal_slug: "clarity-act-signed-into-law-by-end-of-2026-polymarket-41-2026-06-24"
headline: "Clarity Act signed into law by end of 2026: Polymarket 41%"
semantic_title: "Clarity Act signed into law by 2026 consensus wavers near even odds"
telemetry: "Polymarket 41%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-24T21:04:58.000Z"
event_id: "CM-EVT-ZXN47LV744"
event_slug: "clarity-act-signed-into-law-in-2026"
event_question: "Will the Clarity Act be signed into law by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9cb23d04b2ded06147482076688b69b487a8d982c63ebdda2ab3678cf27cf390"
  question_raw: "Clarity Act signed into law in 2026?"
  current_price: 0.41
  volume_24h_usd: 20998.637233
  arbitration_model: "uma_oracle"
  resolution_source: "congress.gov"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "Polymarket prices 41% on the Clarity Act being signed into law by end of 2026, resolving via congress.gov."
  - "Senator Daines's fall 2026 timeline is consistent with the near-even market price; the market is not treating the statement as a near-certain legislative commitment."
  - "FinCEN's concurrent proposal of new stablecoin CIP rules (Story 33) adds regulatory momentum context but does not directly move the Clarity Act contract."
  - "Resolves via congress.gov confirmation of enactment; a fall introduction window leaves limited floor time before year-end, which likely explains the sub-50% pricing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Senator Steve Daines said the Senate could release cryptocurrency tax legislation as early as fall 2026, as the CLARITY Act legislative push continues."
    publisher: "Shiraz Jagati"
    published_at: "2026-06-24T21:04:58.000Z"
    source_url: "https://news.bitcoin.com/senate-crypto-tax-bill-fall-2026-daines/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Shiraz Jagati"
        source_url: "https://news.bitcoin.com/senate-crypto-tax-bill-fall-2026-daines/"
        retrieved_at: "2026-06-27T10:02:20+00:00"
  - type: "pm_response"
    notes: "Polymarket contract on the Clarity Act signed into law by December 31, 2026 via congress.gov; at 41%, the market is treating Senator Daines's fall timeline as possible but uncertain given legislative calendar constraints."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Shiraz Jagati: Senate Could Unveil Crypto Tax Bill by Fall 2026 as CLARITY Act Push C"
    url: "https://news.bitcoin.com/senate-crypto-tax-bill-fall-2026-daines/"
    published_at: "2026-06-24T21:04:58.000Z"
    retrieved_at: "2026-06-27T10:02:20+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
