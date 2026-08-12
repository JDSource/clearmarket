---
signal_id: "CMSIG20260812VS00"
signal_slug: "will-david-crowley-be-the-democratic-nom-vol-5657279"
headline: "Crowley WI-Gov Dem nominee: 100% on $5.7M"
semantic_title: "Crowley locks up Wisconsin Dem governor nod"
telemetry: "100% · $5.7M 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-12T09:08:32+00:00"
event_id: "CM-EVT-GTB8QZVGM8"
event_slug: "kxgovwinomd-26"
event_question: "Will a Wisconsin Democratic Governor be nominated by the 2026 election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVWINOMD-26-DCRO"
  question_raw: "Will David Crowley be the Democratic nominee for Governor in Wisconsin?"
  current_price: 0.999
  volume_24h_usd: 5657279.48
  volume_cumulative_usd: 6966298.7
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-31T14:00:00Z"
bullets:
  - "Kalshi prices Crowley at 100%, market treats the Democratic nomination as settled."
  - "24h volume of $5.7M is 81% of all-time handle, a near-total resolution flush."
  - "Surge likely driven by a definitive primary result or filing deadline passing today."
  - "Contract resolves on Democratic nominee certification; no remaining uncertainty priced."
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
      kalshi_vol_24h_usd: 5657279.48
sources:
  - label: "ClearMarket market record: Will a Wisconsin Democratic Governor be nominated by th"
    url: "https://clearmarket.fyi/events/kxgovwinomd-26"
    retrieved_at: "2026-08-12T09:08:32+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

The volume spike is a settlement event, not a positioning one, desks should treat this line as closed and shift attention to the general-election Wisconsin governor market.
