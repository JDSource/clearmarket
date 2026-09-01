---
signal_id: "CMSIG20260901VS00"
signal_slug: "will-ed-markey-be-the-democratic-nominee-vol-239851"
headline: "Markey MA Dem nominee: 99% on $240K surge"
semantic_title: "Markey MA Senate nomination trades near certainty"
telemetry: "99% · $240K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-01T13:00:43+00:00"
event_id: "CM-EVT-J620PJQLH6"
event_slug: "kxsenatemad-26"
event_question: "Will the Massachusetts Democratic Senate nominee be determined by September 15, 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSENATEMAD-26-EMAR"
  question_raw: "Will Ed Markey be the Democratic nominee for the Senate in Massachusetts?"
  current_price: 0.993
  volume_24h_usd: 239851.18
  volume_cumulative_usd: 879153.39
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-09-15T14:00:00Z"
bullets:
  - "99% price leaves almost no room for a Democratic primary upset in Massachusetts."
  - "24h volume of $240K is 27% of all-time, a significant conviction flush into an already-settled line."
  - "Fresh capital at near-certainty odds suggests traders are locking in positions ahead of a formal filing deadline or ballot certification."
  - "Contract resolves on Democratic nominee status; no general-election outcome implied."
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
      kalshi_vol_24h_usd: 239851.18
sources:
  - label: "ClearMarket market record: Will the Massachusetts Democratic Senate nominee be det"
    url: "https://clearmarket.fyi/events/kxsenatemad-26"
    retrieved_at: "2026-09-01T13:00:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume into a 99% line signals desks are treating the Markey nomination as a closing hedge or position cleanup, not a directional bet, watch for a catalyst like a primary filing deadline.
