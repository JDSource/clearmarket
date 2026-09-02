---
signal_id: "CMSIG20260902VS04"
signal_slug: "will-richard-neal-be-the-democratic-nomi-vol-61942"
headline: "Neal MA-01 Dem nominee: 99% on $62K volume"
semantic_title: "Fresh volume backs Neal as MA-01 Democratic pick at 99%"
telemetry: "99% · $62K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-02T12:29:56+00:00"
event_id: "CM-EVT-FVM9ZNZPY7"
event_slug: "kxmaprimary-01d26"
event_question: "Will the Massachusetts 1st Congressional District Democratic nominee be decided by the 2026 general election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMAPRIMARY-01D26-RNEA"
  question_raw: "Will Richard Neal be the Democratic nominee for MA-01?"
  current_price: 0.99
  volume_24h_usd: 61942.08
  volume_cumulative_usd: 120452.46
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi prices Richard Neal at 99% for the MA-01 Democratic nomination, market sees no credible challenger."
  - "$62K in 24h accounts for 51% of all-time contract volume, a notable mid-cycle concentration."
  - "Paired with the Lynch MA-08 spike, the session suggests broad repositioning across Massachusetts congressional races."
  - "Resolves on certification of the MA-01 Democratic primary winner."
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
      kalshi_vol_24h_usd: 61942.08
sources:
  - label: "ClearMarket market record: Will the Massachusetts 1st Congressional District Democ"
    url: "https://clearmarket.fyi/events/kxmaprimary-01d26"
    retrieved_at: "2026-09-02T12:29:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Simultaneous spikes in both Massachusetts congressional nomination contracts suggest a single catalyst, possibly a primary date or filing deadline, is driving traders to close residual short positions.
