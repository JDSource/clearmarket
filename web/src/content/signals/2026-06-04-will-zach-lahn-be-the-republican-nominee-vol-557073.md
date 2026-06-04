---
signal_id: "CMSIG20260604VS02"
signal_slug: "will-zach-lahn-be-the-republican-nominee-vol-557073"
headline: "Lahn IA GOP governor nominee: 100% on $557K"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-04T11:15:28+00:00"
event_id: "CM-EVT-N70PDTB9T9"
event_slug: "kxgovianomr-26"
event_question: "Will Kim Reynolds be the Iowa Republican Governor nominee by the 2026 election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVIANOMR-26-ZLAH"
  question_raw: "Will Zach Lahn be the Republican nominee for Governor in Iowa?"
  current_price: 0.997
  volume_24h_usd: 557073.25
  volume_cumulative_usd: 868681.77
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-06-02T14:00:00Z"
bullets:
  - "Kalshi prices 100%, market has fully resolved Lahn as Iowa GOP gubernatorial nominee."
  - "Kalshi: $557K 24h volume, 64% of $868K all-time; bulk of lifetime activity hit on resolution."
  - "Lahn's primary win confirmation triggered settlement flow, concentrating volume at finality."
  - "Contract resolves YES; volume is settlement and position close-out activity."
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
      kalshi_vol_24h_usd: 557073.25
sources:
  - label: "ClearMarket market record: Will Kim Reynolds be the Iowa Republican Governor nomin"
    url: "https://clearmarket.fyi/events/kxgovianomr-26"
    retrieved_at: "2026-06-04T11:15:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

100% price absorbing 64% of all-time volume in one day is a classic resolution signature; desks should note Lahn as the confirmed Iowa GOP gubernatorial candidate for 2026 cycle positioning.
