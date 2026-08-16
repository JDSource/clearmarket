---
signal_id: "CMSIG20260816VS01"
signal_slug: "will-eric-barlow-be-the-republican-nomin-vol-13474"
headline: "Barlow WY GOP nominee: 81% on $13K Kalshi surge"
semantic_title: "Barlow holds at 81% as Wyoming GOP primary draws fresh bets"
telemetry: "81% · $13K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-16T08:23:38+00:00"
event_id: "CM-EVT-SBQ8NYFV24"
event_slug: "kxgovwynomr-26"
event_question: "Will a Wyoming Republican governor nominee be determined by the 2026 election cycle?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVWYNOMR-26-EBAR"
  question_raw: "Will Eric Barlow be the Republican nominee for Governor in Wyoming?"
  current_price: 0.81
  volume_24h_usd: 13474.55
  volume_cumulative_usd: 47847.91
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-31T14:00:00Z"
bullets:
  - "Kalshi prices Barlow at 81%, strong favorite, but roughly 1-in-5 odds of an upset remain."
  - "$13.5K in 24h represents 28% of all-time contract volume, indicating a meaningful conviction push."
  - "Surge likely reflects proximity to the Wyoming GOP primary and new public polling or endorsement news."
  - "Nomination resolution expected at primary; price above 75% suggests money is backing Barlow to clear the field."
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
      kalshi_vol_24h_usd: 13474.55
sources:
  - label: "ClearMarket market record: Will a Wyoming Republican governor nominee be determine"
    url: "https://clearmarket.fyi/events/kxgovwynomr-26"
    retrieved_at: "2026-08-16T08:23:38+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 28% all-time volume day at 81% odds signals desks that new information, polling, endorsements, or opponent withdrawals, is being priced into Barlow's path to the Wyoming GOP nomination.
