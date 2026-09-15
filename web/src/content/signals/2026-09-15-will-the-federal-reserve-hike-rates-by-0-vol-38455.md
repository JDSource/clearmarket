---
signal_id: "CMSIG20260915VS01"
signal_slug: "will-the-federal-reserve-hike-rates-by-0-vol-38455"
headline: "Fed Oct hold: 62% on $38K Kalshi surge"
semantic_title: "Fed October hold stays the consensus bet at 62%"
telemetry: "62% · $38K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-15T13:06:46+00:00"
event_id: "CM-EVT-FPF77GZ320"
event_slug: "kxfeddecision-26oct"
event_question: "Will the Federal Reserve make a decision in October 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDDECISION-26OCT-H0"
  question_raw: "Will the Federal Reserve Hike rates by 0bps at their October 2026 meeting?"
  current_price: 0.62
  volume_24h_usd: 38455.36
  volume_cumulative_usd: 98383.11
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-10-28T18:05:00Z"
bullets:
  - "Kalshi prices a 62% chance the Fed holds rates unchanged at 0bps in October 2026, a bare majority conviction."
  - "39% of all-time volume landed in 24 hours, making this the market's single heaviest session on record."
  - "A September macro print, CPI, payrolls, or Fed speaker, likely catalyzed fresh positioning ahead of the October decision."
  - "Resolution is the October 2026 FOMC meeting outcome."
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
      kalshi_vol_24h_usd: 38455.36
sources:
  - label: "ClearMarket market record: Will the Federal Reserve make a decision in October 202"
    url: "https://clearmarket.fyi/events/kxfeddecision-26oct"
    retrieved_at: "2026-09-15T13:06:46+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 39% all-time volume share in one session on a 62% hold price tells a rates desk that consensus is fragile, the market is re-pricing Fed path risk in real time and warrants close tracking into the next data release.
