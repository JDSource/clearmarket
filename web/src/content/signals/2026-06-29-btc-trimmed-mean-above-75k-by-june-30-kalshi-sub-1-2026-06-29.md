---
signal_id: "CMSIG2026062908"
signal_slug: "btc-trimmed-mean-above-75k-by-june-30-kalshi-sub-1-2026-06-29"
headline: "BTC trimmed mean above $75K by June 30: Kalshi sub-1%"
semantic_title: "Bitcoin above $75K by June 30 priced nearly fully out"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-29T00:37:55.000Z"
event_id: "CM-EVT-3MXSH7KHK5"
event_slug: "kxbtcmaxmon-btc-26jun30"
event_question: "BTC trimmed mean price June 30 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXMON-BTC-26JUN30-7500000"
  question_raw: "Will BTC trimmed mean be above $75000.00 by 11:59 PM ET on Jun 30, 2026?"
  current_price: 0.01
  volume_24h_usd: 234.93
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2026-07-01T03:59:59Z"
bullets:
  - "Kalshi ladder prices BTC trimmed mean above $75,000 by June 30 at just 1% across all strikes from $75K to $92.5K."
  - "Reports of 50,000 BTC moving to exchanges and deepening short-term holder losses are consistent with the market's near-zero probability of a sharp June recovery."
  - "A companion Kalshi binary contract prices Bitcoin outperforming gold in 2026 at 20%, reflecting broader multi-month skepticism beyond the immediate June expiry."
  - "Ladder resolves via CF Benchmarks trimmed mean; with one day to expiry on June 30, the sub-1% pricing across all strikes above $75K reflects near-certain resolution below that level."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin short-term holders are deepening losses as 50,000 BTC moved to exchanges, adding selling pressure to a market already struggling below $60,000."
    publisher: "Yoonseo Lee"
    published_at: "2026-06-29T00:37:55.000Z"
    source_url: "https://www.digitaltoday.co.kr/en/view/75742/bitcoin-short-term-holders-losses-deepen-50000-btc-move-to-exchanges"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Yoonseo Lee"
        source_url: "https://www.digitaltoday.co.kr/en/view/75742/bitcoin-short-term-holders-losses-deepen-50000-btc-move-to-exchanges"
        retrieved_at: "2026-06-29T01:46:24+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via CF Benchmarks on June 30; uniform 1% pricing across all above-$75K strikes confirms deep out-of-the-money status with one day remaining."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Yoonseo Lee: Bitcoin short-term holders' losses deepen as 50,000 BTC move to exchan"
    url: "https://www.digitaltoday.co.kr/en/view/75742/bitcoin-short-term-holders-losses-deepen-50000-btc-move-to-exchanges"
    published_at: "2026-06-29T00:37:55.000Z"
    retrieved_at: "2026-06-29T01:46:24+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
