---
signal_id: "CMSIG20261121VS00"
signal_slug: "will-donald-trump-visit-north-korea-in-2-vol-19208"
headline: "Trump NK visit 2026: 0% on $19K surge"
semantic_title: "Trump North Korea visit in 2026 stays a long shot"
telemetry: "0% · $19K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-21T07:48:00+00:00"
event_id: "CM-EVT-V0BCKV3553"
event_slug: "which-countries-will-donald-trump-visit-in-2026"
event_question: "Which countries will Donald Trump visit in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x035b7cc0833f825c4476352a1d5edeb870fc8250776803352177d44d34b03c6e"
  question_raw: "Will Donald Trump visit North Korea in 2026?"
  current_price: 0.004
  volume_24h_usd: 19208.930692
  volume_cumulative_usd: 70479.848397
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Market prices zero probability, traders see no credible path to a Trump Pyongyang trip this year."
  - "24h volume of $19K represents 27% of all-time liquidity, a sharp concentration of fresh attention."
  - "Renewed diplomatic chatter or media speculation likely driving traffic; market is unmoved at the floor."
  - "Contract resolves end-2026; six weeks remain, leaving little runway for a surprise reversal."
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
      poly_vol_24h_usd: 19208.930692
sources:
  - label: "ClearMarket market record: Which countries will Donald Trump visit in 2026?"
    url: "https://clearmarket.fyi/events/which-countries-will-donald-trump-visit-in-2026"
    retrieved_at: "2026-11-21T07:48:00+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should read this as the market firmly ruling out a Trump, Kim summit in 2026 despite a notable fresh-capital test, the 0% price held through 27% of lifetime volume in a single session.
