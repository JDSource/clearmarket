---
signal_id: "CMSIG20260726VS01"
signal_slug: "will-donald-trump-announce-a-presidentia-vol-26676"
headline: "Trump 2028 announcement: 9% on $26K volume"
semantic_title: "Odds hold low on a Trump 2028 run announcement"
telemetry: "9% · $27K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-26T09:56:30+00:00"
event_id: "CM-EVT-4WMQ7GM282"
event_slug: "who-will-announce-presidential-run-before-2027"
event_question: "Will anyone announce a Presidential run before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xf4e255c0ffa52f8d5efa5c9068a6236ad3cb1b768802759798683fa961003d0f"
  question_raw: "Will Donald Trump announce a presidential run before 2027?"
  current_price: 0.088
  volume_24h_usd: 26676.665732999994
  volume_cumulative_usd: 48559.896305000024
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a Trump presidential-run announcement before 2027 at 9%, market treats it as unlikely near-term."
  - "55% of all-time volume arrived in 24h, a concentrated spike on a question with thin prior liquidity."
  - "Political speculation around Trump's post-midterm positioning likely catalyzed fresh bets."
  - "Resolves before Jan 1, 2027; any formal campaign filing would resolve YES immediately."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 26676.665732999994
sources:
  - label: "ClearMarket market record: Will anyone announce a Presidential run before 2027?"
    url: "https://clearmarket.fyi/events/who-will-announce-presidential-run-before-2027"
    retrieved_at: "2026-07-26T09:56:30+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

More than half the contract's lifetime volume landing in one session suggests a discrete political development prompted desks to stress-test early-announcement risk, the 9% print says the market isn't buying it.
