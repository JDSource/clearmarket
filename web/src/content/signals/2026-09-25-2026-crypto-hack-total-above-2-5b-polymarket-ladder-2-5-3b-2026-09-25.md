---
signal_id: "CMSIG2026092508"
signal_slug: "2026-crypto-hack-total-above-2-5b-polymarket-ladder-2-5-3b-2026-09-25"
headline: "2026 crypto hack total above $2.5B: Polymarket ladder ~$2.5-3B"
semantic_title: "Annual crypto hack losses seen settling between $2.5B and $3B"
telemetry: "Polymarket ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-25T00:00:00.000Z"
event_id: "CM-EVT-88PZ3D88F1"
event_slug: "total-crypto-hack-value-in-2026"
event_question: "Total 2026 crypto hack value"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x8084019b7fb72aadb8202bf727b3bb324b559f797caa94df04a08ea4e074c257"
  question_raw: "Over $3B crypto hack value in 2026?"
  current_price: 0.291
  volume_24h_usd: 485.49
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "The Polymarket ladder prices the 2026 total crypto hack value in the $2.5B-$3.0B range, with 79% above $2.5B but only 29% above $3.0B."
  - "The Bitget $352 million hack attributed to North Korea adds a large incremental data point and is consistent with the market's modal range, trading volume on this ladder rose 7,097% day over day."
  - "The 97% probability above $2.0B confirms 2026 is already tracking as a record-level hack year; the tail risk of exceeding $3.5B sits at 24%."
  - "Resolves via Polymarket's UMA oracle; the aggregation methodology for counting hacks, whether the Bitget loss is included at the full alleged amount or a recovered/adjusted figure, is the key settlement edge."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Bitget CEO Gracy Chen said investigators linked a $352 million hack to North Korean hacking group IP addresses, adding to a string of major 2026 crypto thefts."
    publisher: "Matthew Tan"
    published_at: "2026-09-25T00:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/09/25/crypto-platform-bitget-suspects-north-korea-in-352-million-hack.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Matthew Tan"
        source_url: "https://www.cnbc.com/2026/09/25/crypto-platform-bitget-suspects-north-korea-in-352-million-hack.html"
        retrieved_at: "2026-09-25T07:47:46+00:00"
  - type: "pm_response"
    notes: "Polymarket ladder with 72x day-over-day volume surge; market-implied range $2.5B-$3.0B for total 2026 crypto hack losses, resolving via UMA oracle."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Matthew Tan: Crypto platform Bitget suspects North Korea in $352 million hack"
    url: "https://www.cnbc.com/2026/09/25/crypto-platform-bitget-suspects-north-korea-in-352-million-hack.html"
    published_at: "2026-09-25T00:00:00.000Z"
    retrieved_at: "2026-09-25T07:47:46+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
