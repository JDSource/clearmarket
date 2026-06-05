---
signal_id: "CMSIG20260605VS02"
signal_slug: "will-zach-lahn-be-the-republican-nominee-vol-557073"
headline: "Lahn Iowa GOP nominee: 100% on $557K surge"
semantic_title: "Zach Lahn locked in as Iowa GOP governor nominee at certainty"
telemetry: "100% · $557K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-06-05T12:03:57+00:00"
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
  - "Kalshi contract prints 100%, market treats Lahn's Republican nomination as fully resolved."
  - "$557K in 24h volume is 64% of all-time handle, suggesting a decisive confirming event occurred."
  - "Primary results or official certification likely just released, triggering settlement-driven flow."
  - "Contract nearing or at resolution; volume reflects position closeout rather than speculative entry."
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
    retrieved_at: "2026-06-05T12:03:57+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 100% price with 64% of lifetime volume in one session is a classic post-event settlement flush, desks tracking Iowa's 2026 gubernatorial race can mark Lahn as the confirmed Republican standard-bearer.
