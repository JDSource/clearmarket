---
signal_id: "CMSIG2026080308"
signal_slug: "btc-above-100k-by-sep-1-kalshi-ladder-3-11-2026-08-03"
headline: "BTC above $100K by Sep 1: Kalshi ladder 3-11%"
semantic_title: "Bitcoin death-cross signal keeps sub-$100K consensus intact"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-03T00:00:00.000Z"
event_id: "CM-EVT-ZPMYBGJP99"
event_slug: "kxbtcmax100-26"
event_question: "Bitcoin price above $100,000 by September 1, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAX100-26-AUG"
  question_raw: "Will Bitcoin be above $100000.00 by Sep 1, 2026 at 12:00AMET?"
  current_price: 0.03
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2026-10-01T04:00:00Z"
bullets:
  - "Kalshi ladder prices Bitcoin above $100K by September 1 at 3-11% across top strikes, embedding a deep bearish tilt."
  - "The death-cross signal, 20-week EMA approaching the 200-week EMA, echoes 2022 conditions and is directionally consistent with low ladder probabilities."
  - "Coldcard hardware wallet losses exceeding $90 million (Stories 28, 31, 32) add a separate sentiment headwind compounding the technical breakdown signal."
  - "The December 31 ladder (CM-EVT-0MWN62PNG9) at 13% for $100K shows the consensus bearish view extends well beyond the September horizon."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin's 20-week EMA is nearing a crossover below its 200-week EMA, a death-cross pattern that preceded a 29% decline in 2022."
    publisher: "Yashu Gola"
    published_at: "2026-08-03T00:00:00.000Z"
    source_url: "https://www.fxempire.com/forecasts/article/bitcoin-flashes-death-cross-that-preceded-30-price-decline-1614323"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Yashu Gola"
        source_url: "https://www.fxempire.com/forecasts/article/bitcoin-flashes-death-cross-that-preceded-30-price-decline-1614323"
        retrieved_at: "2026-08-03T11:18:40+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via spot BTC price against the $100K strike on September 1; same contract as Story 30, technical and macro catalysts now reinforcing the same pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Yashu Gola: Bitcoin Flashes ‘Death Cross’ That Preceded 30% Price Decline | FXEmpi"
    url: "https://www.fxempire.com/forecasts/article/bitcoin-flashes-death-cross-that-preceded-30-price-decline-1614323"
    published_at: "2026-08-03T00:00:00.000Z"
    retrieved_at: "2026-08-03T11:18:40+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
