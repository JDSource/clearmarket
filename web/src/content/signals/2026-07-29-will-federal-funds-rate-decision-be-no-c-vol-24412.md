---
signal_id: "CMSIG20260729VS03"
signal_slug: "will-federal-funds-rate-decision-be-no-c-vol-24412"
headline: "Fed Jul pause with dissent: 60% on $24K"
semantic_title: "Traders back a Fed dissent alongside a July pause at 60%"
telemetry: "60% · $24K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-29T10:36:04+00:00"
event_id: "CM-EVT-P6QJP9BW02"
event_slug: "kxfedcombo-26jul"
event_question: "Will the Federal Reserve in July 2026 cut rates and have at least one dissent?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDCOMBO-26JUL-0-T0"
  question_raw: "Will Federal Funds Rate Decision be No change AND Dissents be >0 for Jul 2026?"
  current_price: 0.6
  volume_24h_usd: 24412.57
  volume_cumulative_usd: 38191.04
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-07-29T17:55:00Z"
bullets:
  - "Kalshi prices no-change decision plus at least one dissent at 60%, a lean toward internal Fed friction."
  - "64% of all-time volume hit in 24h, the contract's heaviest session ahead of the July meeting."
  - "Pre-meeting positioning intensifies as a hawkish dissent would signal policy divergence within the FOMC."
  - "Resolves on the July 2026 FOMC statement and meeting minutes release."
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
      kalshi_vol_24h_usd: 24412.57
sources:
  - label: "ClearMarket market record: Will the Federal Reserve in July 2026 cut rates and hav"
    url: "https://clearmarket.fyi/events/kxfedcombo-26jul"
    retrieved_at: "2026-07-29T10:36:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy late-cycle positioning at 60% tells macro desks the market considers a dissenting Fed voice nearly as likely as not, with meaningful implications for the rate path narrative.
