---
signal_id: "CMSIG20260910VS04"
signal_slug: "will-republican-win-the-house-race-for-m-vol-18256"
headline: "MN-01 GOP House: 84% on $18K surge"
semantic_title: "Republican hold on MN-01 stays well-bid at 84%"
telemetry: "84% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-10T12:40:48+00:00"
event_id: "CM-EVT-0HH4XXLY85"
event_slug: "kxhouserace-mn01-26"
event_question: "Will MN-01 House winner be determined by January 4, 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-MN01-26-R"
  question_raw: "Will Republican win the House race for MN-01?"
  current_price: 0.84
  volume_24h_usd: 18256.07
  volume_cumulative_usd: 51007.76
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices the Republican at 84% to hold MN-01, a strong-lean probability in a historically red-leaning district."
  - "$18K traded in 24h equals 36% of all-time volume, a notable mid-cycle attention spike."
  - "Fresh volume at unchanged high odds suggests bettors are backing the incumbent lean rather than chasing a surprise."
  - "Resolves on the 2026 MN-01 House election."
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
      kalshi_vol_24h_usd: 18256.07
sources:
  - label: "ClearMarket market record: Will MN-01 House winner be determined by January 4, 202"
    url: "https://clearmarket.fyi/events/kxhouserace-mn01-26"
    retrieved_at: "2026-09-10T12:40:48+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Renewed buying at 84% on above-average volume signals the market is treating MN-01 as a safe Republican hold, relevant for desks tracking House majority seat counts.
