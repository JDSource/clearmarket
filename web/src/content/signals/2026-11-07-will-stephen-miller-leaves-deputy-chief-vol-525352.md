---
signal_id: "CMSIG20261107VS00"
signal_slug: "will-stephen-miller-leaves-deputy-chief-vol-525352"
headline: "Miller Deputy exit: 95% on $525K surge"
semantic_title: "Heavy trading backs Miller out as Deputy Chief by 2027"
telemetry: "95% · $525K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-07T14:39:51+00:00"
event_id: "CM-EVT-Z5Z4K6WBZ9"
event_slug: "kxtrumpadminleave-26dec31"
event_question: "Will someone leave their role in the Trump administration in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPADMINLEAVE-26DEC31-SMIL"
  question_raw: "Will Stephen Miller leaves Deputy Chief of Staff in before 2027?"
  current_price: 0.952
  volume_24h_usd: 525352.56
  volume_cumulative_usd: 678807.84
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-07T15:00:00Z"
bullets:
  - "Kalshi prices a 95% chance Miller leaves Deputy Chief of Staff before 2027, implying near-certainty."
  - "$525K traded in 24h, 77% of the contract's entire all-time volume in a single session."
  - "Surge suggests a catalyst is either known or imminent; attention at this scale typically precedes a formal announcement."
  - "Contract resolves end-2026; resolution window is weeks away, compressing any remaining uncertainty."
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
      kalshi_vol_24h_usd: 525352.56
sources:
  - label: "ClearMarket market record: Will someone leave their role in the Trump administrati"
    url: "https://clearmarket.fyi/events/kxtrumpadminleave-26dec31"
    retrieved_at: "2026-11-07T14:39:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A desk should treat this as a near-resolved contract, the volume and 95% price together signal the market has effectively priced in Miller's departure; track for a White House personnel announcement imminently.
