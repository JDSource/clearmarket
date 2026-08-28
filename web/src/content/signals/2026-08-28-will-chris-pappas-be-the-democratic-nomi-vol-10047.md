---
signal_id: "CMSIG20260828VS05"
signal_slug: "will-chris-pappas-be-the-democratic-nomi-vol-10047"
headline: "Pappas NH Dem Senate: 93% on $10K Polymarket"
semantic_title: "Pappas NH Democratic nomination steady at 93% on Polymarket"
telemetry: "93% · $10K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-28T19:52:39+00:00"
event_id: "CM-EVT-HY8R70V952"
event_slug: "new-hampshire-democratic-senate-primary-winner"
event_question: "Will the Democratic Party winner of the New Hampshire Senate primary be determined by the 2026 primary election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xf78be595172a9db8c6323e1927aa44b2fa2d52805d97bf4a9664593b42326534"
  question_raw: "Will Chris Pappas be the Democratic nominee for Senate in New Hampshire?"
  current_price: 0.932
  volume_24h_usd: 10047.440818000001
  volume_cumulative_usd: 32401.085523
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-08T00:00:00Z"
bullets:
  - "93% on Polymarket mirrors Kalshi's 94%, cross-venue convergence strengthens the Pappas nomination read."
  - "31% of all-time Polymarket handle today, suggesting renewed but smaller-scale confirmation trading."
  - "Spread between venues is within rounding, no exploitable arb, just parallel conviction."
  - "Resolves on New Hampshire primary certification, same trigger as the Kalshi contract."
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
      poly_vol_24h_usd: 10047.440818000001
sources:
  - label: "ClearMarket market record: Will the Democratic Party winner of the New Hampshire S"
    url: "https://clearmarket.fyi/events/new-hampshire-democratic-senate-primary-winner"
    retrieved_at: "2026-08-28T19:52:39+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-identical cross-venue pricing with simultaneous volume bursts signals market-wide settlement on Pappas, a desk can treat both contracts as redundant confirmation and shift focus to general-election exposure.
