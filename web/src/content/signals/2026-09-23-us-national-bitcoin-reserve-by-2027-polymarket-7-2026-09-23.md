---
signal_id: "CMSIG2026092307"
signal_slug: "us-national-bitcoin-reserve-by-2027-polymarket-7-2026-09-23"
headline: "US national Bitcoin reserve by 2027: Polymarket 7%"
semantic_title: "US national Bitcoin reserve before 2027 stays a long shot"
telemetry: "Polymarket 7%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-23T00:00:00.000Z"
event_id: "CM-EVT-0F2G0B8X49"
event_slug: "us-national-bitcoin-reserve-before-2027"
event_question: "Will the United States establish a national Bitcoin reserve before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x953b1439569eef0a0e639566acd35d32ebadee8ab70dbb2f8e00bb936a277aa2"
  question_raw: "US national Bitcoin reserve before 2027?"
  current_price: 0.07
  volume_24h_usd: 168.861429
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on the United States establishing a national Bitcoin reserve before 2027 prices at 7%."
  - "The reported inter-agency turf war and legislative failure are consistent with Polymarket's low probability; the market is not pricing a near-term breakthrough."
  - "Companion Kalshi contract on Trump creating a National Bitcoin Reserve in 2026 sits at 10%, a small premium to Polymarket but both firmly in long-shot territory."
  - "Resolves via Polymarket's UMA oracle, which will assess whether a formal national reserve has been officially established before January 1, 2027."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "A Treasury-Commerce turf war is stalling the Trump administration's reported $20 billion Bitcoin reserve plan after a September 16 committee vote failed to advance legislation."
    publisher: "blockchainreporter.net"
    published_at: "2026-09-23T00:00:00.000Z"
    source_url: "https://blockchainreporter.net/united-states-crypto-reserve/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "blockchainreporter.net"
        source_url: "https://blockchainreporter.net/united-states-crypto-reserve/"
        retrieved_at: "2026-09-24T13:07:56+00:00"
  - type: "pm_response"
    notes: "Polymarket (7%) and Kalshi (10%) are aligned in pricing the Bitcoin reserve plan as unlikely this year; the spread between venues is narrow given the legislative obstacle now confirmed."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "blockchainreporter.net: United States Crypto Reserve: Treasury-Commerce Turf War Stalls Plan"
    url: "https://blockchainreporter.net/united-states-crypto-reserve/"
    published_at: "2026-09-23T00:00:00.000Z"
    retrieved_at: "2026-09-24T13:07:56+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
