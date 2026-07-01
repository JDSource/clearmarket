---
signal_id: "CMSIG20260701VS04"
signal_slug: "will-barbara-kirkmeyer-be-the-republican-vol-92428"
headline: "Kirkmeyer CO GOP nominee: 45% on $92K surge"
semantic_title: "Kirkmeyer flows challenge Marx's Colorado GOP lead"
telemetry: "45% · $92K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-01T11:21:48+00:00"
event_id: "CM-EVT-3X1XZGV3C4"
event_slug: "kxgovconomr-26"
event_question: "Will Abe Suthers be elected Colorado Republican Governor nominee by 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVCONOMR-26-BKIR"
  question_raw: "Will Barbara Kirkmeyer be the Republican nominee for Governor in Colorado?"
  current_price: 0.45
  volume_24h_usd: 92428.11
  volume_cumulative_usd: 125752.86
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi prices Kirkmeyer at 45%, a narrow underdog to Marx but within striking distance."
  - "$92K in 24h is 73% of all-time volume, mirroring the Marx contract's simultaneous surge."
  - "Paired volume spikes on both contracts signal a binary primary race crystallizing around two candidates."
  - "Marx 57% vs. Kirkmeyer 45% implies thin residual probability for any other entrant."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from kalshi API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "kalshi_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      kalshi_vol_24h_usd: 92428.11
sources:
  - label: "ClearMarket market record: Will Abe Suthers be elected Colorado Republican Governo"
    url: "https://clearmarket.fyi/events/kxgovconomr-26"
    retrieved_at: "2026-07-01T11:21:48+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous volume eruptions on the Marx and Kirkmeyer contracts, each consuming most of their all-time liquidity, confirm the Colorado GOP primary has resolved into a two-horse race demanding fresh desk coverage.
