---
signal_id: "CMSIG2026092504"
signal_slug: "2026-crypto-hack-total-ladder-implies-2-5b-3b-range-2026-09-25"
headline: "2026 crypto hack total: ladder implies $2.5B-$3B range"
semantic_title: "Crypto hack total for 2026 priced between $2.5B and $3B"
telemetry: "Polymarket ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-25T00:00:00.000Z"
event_id: "CM-EVT-88PZ3D88F1"
event_slug: "total-crypto-hack-value-in-2026"
event_question: "Total 2026 crypto hack value (USD)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x8084019b7fb72aadb8202bf727b3bb324b559f797caa94df04a08ea4e074c257"
  question_raw: "Over $3B crypto hack value in 2026?"
  current_price: 0.376
  volume_24h_usd: 710.6664310000001
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "The ladder prices 79% odds that 2026 crypto hack value exceeds $2.5B, but only 38% above $3B, implying a market-consensus range of $2.5B-$3B."
  - "The Bitget hack adds roughly $352M to the 2026 running total; trading volume on this ladder surged 72x day over day, reflecting direct market reaction to the news."
  - "The 97% probability above $2B confirms the $2B threshold is already treated as resolved, with the debate now centering on whether the year crosses $3B."
  - "Resolves on total verified 2026 crypto hack value; North Korean attribution, if confirmed, would not change resolution but underscores systemic risk driving the elevated range."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Bitget CEO Gracy Chen said investigators linked a 352 million dollar hack to North Korean IP addresses previously associated with state-sponsored hacking groups."
    publisher: "Matthew Tan"
    published_at: "2026-09-25T00:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/09/25/crypto-platform-bitget-suspects-north-korea-in-352-million-hack.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Matthew Tan"
        source_url: "https://www.cnbc.com/2026/09/25/crypto-platform-bitget-suspects-north-korea-in-352-million-hack.html"
        retrieved_at: "2026-09-25T13:12:47+00:00"
  - type: "pm_response"
    notes: "Ladder saw volume up 72x day over day following the Bitget hack disclosure; market is actively repricing the full-year cumulative figure upward."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Matthew Tan: Crypto platform Bitget suspects North Korea in $352 million hack"
    url: "https://www.cnbc.com/2026/09/25/crypto-platform-bitget-suspects-north-korea-in-352-million-hack.html"
    published_at: "2026-09-25T00:00:00.000Z"
    retrieved_at: "2026-09-25T13:12:47+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
