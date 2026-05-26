---
signal_id: "CMSIGDEMO00004"
signal_slug: "demo-argentina-volume-spike"
headline: "Argentina inflation contract sees 5x volume spike before INDEC release"
category_tag: "VOLUME_SPIKE"
secondary_tags: ["PRE_NEWS_PRICING"]
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-05-10T22:10:00-04:00"
event_id: "CMARGAPRINFL"
event_slug: "argentina-april-inflation-above-3"
event_question: "Will Argentina April 2026 monthly inflation print above 3.0%?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xargapr2026"
  question_raw: "Argentina April monthly inflation above 3.0%"
  current_price: 0.62
  price_24h_ago: 0.51
  volume_24h_usd: 980000
  volume_7d_usd: 1820000
  volume_cumulative_usd: 2240000
  arbitration_model: "uma_oracle"
  resolution_source: "INDEC monthly CPI bulletin"
  resolves_at: "2026-05-14T19:00:00Z"
related_markets: []
bullets:
  - "Polymarket's Argentina April inflation contract traded $980K in the last 24 hours — five times its trailing seven-day daily average of $187K, and the largest one-day surge since the contract listed."
  - "The contract's YES price moved with the volume, rising to 62% from 51% in the same window. Markets are pricing higher odds that April inflation will print above 3%."
  - "The spike comes four days before the INDEC release on May 14. Private-sector nowcasts from Orlando Ferreres put April at 3.1-3.3%, well above the 2.8% economist consensus."
  - "Kalshi does not list Argentine inflation contracts, leaving Polymarket as the only liquid prediction-market read on LatAm CPI."
atomic_claims:
  - type: "volume_anomaly"
    significance:
      threshold: 3.0
      threshold_unit: "x"
      current: 5.2
      passed: true
      percentile_30d: 99
      reason: "24h volume 5.2x trailing 7d baseline; largest spike since contract listed (prior max 2.4x on 2026-04-23)"
    current_vol_24h_usd: 980000
    baseline_vol_7d_avg_usd: 187000
    volume_ratio_vs_baseline: 5.2
    prior_max_ratio_30d: 2.4
    prior_max_ratio_date: "2026-04-23"
    field_provenance:
      current_vol_24h_usd:
        tier: "direct"
        method: "polymarket_clob_api"
        retrieved_at: "2026-05-10T22:00:00-04:00"
      baseline_vol_7d_avg_usd:
        tier: "derived"
        method: "rolling_7d_avg"
        inputs: ["cm_marks_history (7d daily volume snapshots)"]
        note: "mean of trailing 7 daily volume snapshots"
      volume_ratio_vs_baseline:
        tier: "derived"
        method: "arithmetic"
        inputs: ["current_vol_24h_usd", "baseline_vol_7d_avg_usd"]
        note: "current_vol_24h_usd / baseline_vol_7d_avg_usd"
  - type: "volume_context"
    venue: "polymarket"
    price_change_during_spike_pp: 11.0
    associated_catalyst: "INDEC April CPI release scheduled 2026-05-14T19:00:00Z (T-4d)"
    notes: "Private-sector nowcasts (Orlando Ferreres) running 3.1-3.3% vs 2.8% Bloomberg economist consensus. Spike consistent with informed flow ahead of scheduled release. Kalshi does not list — Polymarket is sole liquid venue for LatAm CPI."
    field_provenance:
      price_change_during_spike_pp:
        tier: "derived"
        method: "arithmetic"
        inputs: ["primary_market.current_price", "primary_market.price_24h_ago"]
        note: "current_price - price_at_spike_window_start (24h ago)"
      associated_catalyst:
        tier: "direct"
        method: "indec_release_calendar"
        source: "INDEC release calendar"
        source_url: "https://www.indec.gob.ar"
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Orlando Ferreres consultancy nowcast"
    url: "https://orlandoferreres.com"
    retrieved_at: "2026-05-10T22:00:00-04:00"
  - label: "INDEC release calendar"
    url: "https://www.indec.gob.ar"
    retrieved_at: "2026-05-10T22:00:00-04:00"
field_provenance:
  pm_data: "polymarket_clob_api"
  news_context: "perplexity_grounded"
  editorial_judgment: "llm_judge_cm_signal_v1"
---

Volume-spike pattern preceding a scheduled macro release. The 5.2× baseline anomaly suggests informed flow ahead of the May 14 INDEC print; Polymarket is the only liquid venue for LatAm CPI.
