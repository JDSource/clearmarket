---
signal_id: "CMSIG20260730VS07"
signal_slug: "will-russia-capture-havrylivka-by-septem-vol-47775"
headline: "Russia takes Havrylivka Sep 30: 6% odds"
semantic_title: "Russia capturing Havrylivka by Sep 30 stays a long shot"
telemetry: "6% · $48K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-30T10:21:41+00:00"
event_id: "CM-EVT-RYR4XV6NT4"
event_slug: "will-russia-capture-havrylivka-by-february-28"
event_question: "Will Russia capture Havrylivka in 2026? (multi-deadline series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x99a94710860ba0285f53275e563e13c36865d9d717c7b4b5e5e520dacad4ae0d"
  question_raw: "Will Russia capture Havrylivka by September 30, 2026?"
  current_price: 0.057
  volume_24h_usd: 47775.98
  volume_cumulative_usd: 81696.020322
  arbitration_model: "uma_oracle"
  resolves_at: "2026-09-30T00:00:00Z"
bullets:
  - "6% pricing keeps a Russian capture of Havrylivka firmly in tail-risk territory through September 30."
  - "$47.8K in 24h volume is 58% of all-time, the contract's largest relative session, pointing to a fresh battlefield development."
  - "A spike of this scale into a low-priced geopolitical contract often precedes or responds to on-the-ground tactical news."
  - "Resolves on verified Russian control of Havrylivka by September 30, 2026."
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
      poly_vol_24h_usd: 47775.98
sources:
  - label: "ClearMarket market record: Will Russia capture Havrylivka in 2026? (multi-deadline"
    url: "https://clearmarket.fyi/events/will-russia-capture-havrylivka-by-february-28"
    retrieved_at: "2026-07-30T10:21:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-majority-of-lifetime volume into a 6%-priced territorial contract is a strong signal that new battlefield information is circulating, desks with Ukraine exposure should cross-reference OSINT and front-line reporting immediately.
