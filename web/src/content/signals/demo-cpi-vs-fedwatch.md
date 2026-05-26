---
signal_id: "CMSIGDEMO00003"
signal_slug: "demo-cpi-vs-fedwatch"
headline: "Prediction markets price softer May CPI than economists expect"
category_tag: "VS_BENCHMARK_DRIFT"
secondary_tags: []
detection_path: "benchmark_drift"
pre_news_classification: "concurrent"
published_at: "2026-05-23T08:30:00-04:00"
event_id: "CMCPI26MAYHI"
event_slug: "kalshi-may-cpi-yoy-35-plus"
event_question: "Will May 2026 CPI YoY come in at or above 3.5%?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26MAY-Y35"
  question_raw: "May 2026 CPI YoY at or above 3.5%"
  current_price: 0.18
  price_24h_ago: 0.19
  volume_24h_usd: 412000
  volume_7d_usd: 1380000
  volume_cumulative_usd: 2940000
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS CPI-U release, series CUUR0000SA0"
  resolves_at: "2026-06-12T12:30:00Z"
related_markets:
  - platform: "polymarket"
    platform_market_id: "0xmaycpi2026"
    question_raw: "May 2026 CPI YoY 3.5% or higher"
    current_price: 0.22
bullets:
  - "Prediction markets are pricing the May CPI report well below the economist consensus, and the gap is the widest since the contract listed in April."
  - "Kalshi traders put the odds of May inflation hitting 3.5% or higher at 18%. Polymarket prices it at 22%. The Bloomberg economist median forecast sits at 28%."
  - "Markets and economists started moving in opposite directions on April 23, the day April CPI printed at 3.4% versus a 3.5% consensus. Traders added downside immediately; economists revised more slowly."
  - "The hard data still favors the consensus. Sticky-services inflation rose 0.4% month-over-month in April, and the Atlanta Fed's nowcast points to 3.6% annualized — both suggest May could surprise to the upside."
  - "The release lands June 12. Earlier signals to watch: April PPI on May 14, Atlanta Fed sticky-CPI updates, and the Cleveland Fed CPI nowcast."
atomic_claims:
  - type: "benchmark_divergence"
    significance:
      threshold: 5.0
      threshold_unit: "pp"
      current: 8.4
      passed: true
      percentile_30d: 96
      reason: "PM consensus diverges -8.4pp from Bloomberg economist median; widest gap since contract listed Apr 14"
    poly_price: 0.22
    kalshi_price: 0.18
    pm_consensus_24h_vw: 0.196
    benchmark_source: "Bloomberg economist consensus median"
    benchmark_source_url: "https://www.bloomberg.com/markets/economics"
    benchmark_value: 0.28
    benchmark_retrieved_at: "2026-05-23T07:30:00-04:00"
    divergence_pp: -8.4
    liquidity_context:
      poly_vol_24h_usd: 280000
      kalshi_vol_24h_usd: 412000
      poly_vol_7d_usd: 920000
      kalshi_vol_7d_usd: 1380000
    field_provenance:
      poly_price:
        tier: "direct"
        method: "polymarket_clob_api"
        retrieved_at: "2026-05-23T07:30:00-04:00"
      kalshi_price:
        tier: "direct"
        method: "kalshi_api"
        retrieved_at: "2026-05-23T07:30:00-04:00"
      pm_consensus_24h_vw:
        tier: "derived"
        method: "vol_weighted_24h"
        inputs: ["poly_price", "kalshi_price"]
        note: "weighted by volume_24h_usd on each venue"
      benchmark_value:
        tier: "mediated"
        method: "perplexity_grounded"
        source: "Bloomberg economist consensus median"
        source_url: "https://www.bloomberg.com/markets/economics"
        retrieved_at: "2026-05-23T07:30:00-04:00"
      divergence_pp:
        tier: "derived"
        method: "arithmetic"
        inputs: ["pm_consensus_24h_vw", "benchmark_value"]
        note: "pm_consensus_24h_vw - benchmark_value"
  - type: "benchmark_context"
    corr_30d_poly: 0.74
    corr_30d_kalshi: 0.81
    corr_breakpoint_date: "2026-04-23"
    poly_offset_pp: -6.0
    kalshi_offset_pp: -10.0
    interp: "Correlation broke on April 23 (April CPI print day, 3.4% vs 3.5% consensus). PMs added downside; economist consensus revised slower. Hard-data lens (Atlanta Fed sticky-CPI nowcast 3.6% annualized) favors consensus."
    field_provenance:
      corr_30d_poly:
        tier: "derived"
        method: "correlation_30d"
        inputs: ["poly_price (cm_marks_history)", "benchmark_value (historical)"]
        note: "Pearson correlation, 30-day rolling window (n=30 daily closes)"
      corr_30d_kalshi:
        tier: "derived"
        method: "correlation_30d"
        inputs: ["kalshi_price (cm_marks_history)", "benchmark_value (historical)"]
        note: "Pearson correlation, 30-day rolling window (n=30 daily closes)"
      corr_breakpoint_date:
        tier: "derived"
        method: "breakpoint_detection"
        inputs: ["corr_30d_poly (historical)", "corr_30d_kalshi (historical)"]
        note: "first day where rolling 7d correlation dropped >2 stdev"
      poly_offset_pp:
        tier: "derived"
        method: "arithmetic"
        inputs: ["poly_price", "benchmark_value"]
        note: "poly_price - benchmark_value"
      kalshi_offset_pp:
        tier: "derived"
        method: "arithmetic"
        inputs: ["kalshi_price", "benchmark_value"]
        note: "kalshi_price - benchmark_value"
      interp:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Bloomberg economist consensus (May 2026 CPI)"
    url: "https://www.bloomberg.com/markets/economics"
    retrieved_at: "2026-05-23T07:30:00-04:00"
  - label: "CME FedWatch implied path"
    url: "https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html"
    retrieved_at: "2026-05-23T07:30:00-04:00"
  - label: "Atlanta Fed sticky-price CPI"
    url: "https://www.atlantafed.org/research/inflationproject/stickyprice"
    retrieved_at: "2026-05-23T07:30:00-04:00"
field_provenance:
  pm_data: "kalshi_api, polymarket_clob_api"
  news_context: "perplexity_grounded"
  editorial_judgment: "llm_judge_cm_signal_v1"
---

PM consensus on the May CPI YoY ≥3.5% question is 8.4pp below the Bloomberg economist median. Either PMs are correctly pricing a soft May print after the April miss, or they've over-extrapolated and arbitrage compresses on the June 12 release.
