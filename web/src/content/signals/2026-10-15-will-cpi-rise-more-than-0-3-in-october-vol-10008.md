---
signal_id: "CMSIG20261015VS07"
signal_slug: "will-cpi-rise-more-than-0-3-in-october-vol-10008"
headline: "CPI >0.3% Oct '26: 19% on $10K, 81% of all-time"
semantic_title: "Traders back CPI staying under 0.3% in October 2026"
telemetry: "19% · $10K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-15T07:48:38+00:00"
event_id: "CM-EVT-N58KJP0K82"
event_slug: "kxcpi-26oct"
event_question: "Will CPI be released in October?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26OCT-T0.3"
  question_raw: "Will CPI rise more than 0.3% in October 2026?"
  current_price: 0.19
  volume_24h_usd: 10008.12
  volume_cumulative_usd: 12376.62
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-02-09T14:56:00Z"
bullets:
  - "At 19%, Kalshi traders assign low but non-trivial odds that October 2026 CPI prints above 0.3% month-over-month."
  - "$10K in 24h is 81% of all-time volume, nearly the entirety of this contract's trading in one session."
  - "An 81% all-time share in one day almost certainly reflects a CPI-adjacent data release or Fed communication sharpening near-term inflation expectations."
  - "Contract resolves on the official October 2026 CPI monthly change reading."
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
      kalshi_vol_24h_usd: 10008.12
sources:
  - label: "ClearMarket market record: Will CPI be released in October?"
    url: "https://clearmarket.fyi/events/kxcpi-26oct"
    retrieved_at: "2026-10-15T07:48:38+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Four-fifths of lifetime volume arriving at 19% means the market has just formed a strong consensus that October inflation stays tame, a tradeable signal for rates and macro desks ahead of the print.
