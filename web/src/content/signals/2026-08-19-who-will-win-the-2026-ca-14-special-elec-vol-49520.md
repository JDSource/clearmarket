---
signal_id: "CMSIG20260819VS07"
signal_slug: "who-will-win-the-2026-ca-14-special-elec-vol-49520"
headline: "CA-14 special election winner: 97% on $50K spike"
semantic_title: "CA-14 special election winner trading near certainty"
telemetry: "97% · $50K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-19T08:32:13+00:00"
event_id: "CM-EVT-T3PBGQWXX8"
event_slug: "kxca14swinner-26"
event_question: "Will a special election be held for California's 14th congressional district before the 2026 general election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCA14SWINNER-26-AWAH"
  question_raw: "Who will win the 2026 CA-14 special election?"
  current_price: 0.97
  volume_24h_usd: 49520.26
  volume_cumulative_usd: 121585.29
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi prices the leading CA-14 special election candidate at 97%, high conviction, small residual risk."
  - "$50K in 24h accounts for 41% of all-time volume, a strong single-session concentration."
  - "California special elections can produce late mail-ballot shifts; the 3% discount reflects that tail risk."
  - "Resolves on California's certified results for the 2026 CA-14 congressional special election."
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
      kalshi_vol_24h_usd: 49520.26
sources:
  - label: "ClearMarket market record: Will a special election be held for California's 14th c"
    url: "https://clearmarket.fyi/events/kxca14swinner-26"
    retrieved_at: "2026-08-19T08:32:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

High single-day volume share at 97% signals a desk that a frontrunner's lead is decisive but uncertified, the 3% residual is the live canvass risk, not a competitive threat.
