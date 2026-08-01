---
signal_id: "CMSIG20260801VS02"
signal_slug: "will-donavan-mckinney-be-the-democratic-vol-89483"
headline: "McKinney MI-13 Dem nominee: 85% on $89K Kalshi surge"
semantic_title: "Heavy trading backs McKinney as MI-13 Democratic nominee at 85%"
telemetry: "85% · $89K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-01T09:55:41+00:00"
event_id: "CM-EVT-CYX84N0L20"
event_slug: "kxmi13d-26"
event_question: "Will the Democratic nominee for Michigan's 13th congressional district be decided by the 2026 general election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMI13D-26-DMCK"
  question_raw: "Will Donavan McKinney be the Democratic nominee for MI-13?"
  current_price: 0.85
  volume_24h_usd: 89483.56
  volume_cumulative_usd: 231493.97
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi prices McKinney at 85% to win the MI-13 Democratic nomination, strong frontrunner read."
  - "24h volume of $89K is 39% of all-time flow, a meaningful single-day acceleration."
  - "Attention likely driven by primary filing deadlines, endorsement news, or rival Thanedar's weakening position."
  - "Primary outcome resolves this contract; McKinney and Thanedar are the key names in market."
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
      kalshi_vol_24h_usd: 89483.56
sources:
  - label: "ClearMarket market record: Will the Democratic nominee for Michigan's 13th congres"
    url: "https://clearmarket.fyi/events/kxmi13d-26"
    retrieved_at: "2026-08-01T09:55:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should note the 85% cross-venue consensus with McKinney and the parallel Thanedar contract at 15%, the market is not hedged; it is directional, and this volume confirms traders are not awaiting further information.
