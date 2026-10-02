---
signal_id: "CMSIG20261002VS04"
signal_slug: "will-apvienotais-saraksts-as-win-the-m-vol-26523"
headline: "AS wins most Latvian seats: 99% on $27K surge"
semantic_title: "Apvienotais Saraksts leading the 2026 Latvian election priced as a lock"
telemetry: "99% · $27K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-02T07:48:52+00:00"
event_id: "CM-EVT-TPH1FR3YZ0"
event_slug: "latvian-parliamentary-election-winner"
event_question: "Will the Latvian parliamentary election result in a single party winning an outright majority by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0eac20f7ed673d0e99385158ea468f6540aa208abefb74613f8170c2f9909e53"
  question_raw: "Will Apvienotais Saraksts (AS) win the most seats in the 2026 Latvian parliamentary election?"
  current_price: 0.988
  volume_24h_usd: 26523.662347
  volume_cumulative_usd: 87498.446563
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-03T00:00:00Z"
bullets:
  - "99% pricing treats an AS plurality in the 2026 Saeima as virtually certain, leaving a 1% residual for all alternatives."
  - "30% of all-time volume arrived in the past 24 hours, a sharp late-campaign concentration as election day nears."
  - "Fresh volume at near-certainty odds implies traders are closing out short positions rather than initiating new long bets."
  - "Resolves on official 2026 Latvian parliamentary seat totals."
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
      poly_vol_24h_usd: 26523.662347
sources:
  - label: "ClearMarket market record: Will the Latvian parliamentary election result in a sin"
    url: "https://clearmarket.fyi/events/latvian-parliamentary-election-winner"
    retrieved_at: "2026-10-02T07:48:52+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

For a desk tracking Eastern European political risk, the volume surge at 99% signals the market has fully priced an AS victory, meaning residual risk lies in coalition composition and post-election policy, not the seat-count outcome itself.
