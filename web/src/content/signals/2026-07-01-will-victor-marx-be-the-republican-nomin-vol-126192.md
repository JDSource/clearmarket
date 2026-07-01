---
signal_id: "CMSIG20260701VS03"
signal_slug: "will-victor-marx-be-the-republican-nomin-vol-126192"
headline: "Marx CO GOP governor nominee: 57% on $126K"
semantic_title: "Capital defends Victor Marx as Colorado GOP frontrunner"
telemetry: "57% · $126K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-01T11:21:48+00:00"
event_id: "CM-EVT-3X1XZGV3C4"
event_slug: "kxgovconomr-26"
event_question: "Will Abe Suthers be elected Colorado Republican Governor nominee by 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVCONOMR-26-VMAR"
  question_raw: "Will Victor Marx be the Republican nominee for Governor in Colorado?"
  current_price: 0.57
  volume_24h_usd: 126192.34
  volume_cumulative_usd: 177453.71
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi prices Marx as a slight favorite at 57% for the Colorado Republican gubernatorial nomination."
  - "$126K in 24h equals 71% of all-time contract volume, near-total history in one session."
  - "Spike coincides with primary calendar pressure; Colorado GOP nomination race entering decisive phase."
  - "Thin all-time liquidity means price is highly sensitive to new entrants and polling shifts."
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
      kalshi_vol_24h_usd: 126192.34
sources:
  - label: "ClearMarket market record: Will Abe Suthers be elected Colorado Republican Governo"
    url: "https://clearmarket.fyi/events/kxgovconomr-26"
    retrieved_at: "2026-07-01T11:21:48+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Concentration of 71% of all-time volume in a single session on a low-liquidity state primary contract suggests informed regional political money is establishing a position ahead of a near-term nomination catalyst.
