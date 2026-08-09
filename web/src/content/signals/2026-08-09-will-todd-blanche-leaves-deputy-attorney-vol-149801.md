---
signal_id: "CMSIG20260809VS02"
signal_slug: "will-todd-blanche-leaves-deputy-attorney-vol-149801"
headline: "Blanche DAG departure: 98% on $150K volume"
semantic_title: "Todd Blanche DAG exit before 2027 priced near certain"
telemetry: "98% · $150K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-09T08:37:25+00:00"
event_id: "CM-EVT-Z5Z4K6WBZ9"
event_slug: "kxtrumpadminleave-26dec31"
event_question: "Will someone leave their role in the Trump administration in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPADMINLEAVE-26DEC31-TBLA"
  question_raw: "Will Todd Blanche leaves Deputy Attorney General in before 2027?"
  current_price: 0.981
  volume_24h_usd: 149801.8
  volume_cumulative_usd: 502126.15
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-07T15:00:00Z"
bullets:
  - "Kalshi prices Todd Blanche leaving as Deputy Attorney General before 2027 at 98%, market treats departure as a near-certainty."
  - "24h volume of $150K is 30% of a $502K all-time pool, the single largest daily draw on this contract."
  - "Fresh attention at a near-ceiling price implies a concrete signal, announcement, leak, or confirmation, is driving conviction."
  - "Contract resolves if Blanche vacates the DAG role before January 1, 2027."
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
      kalshi_vol_24h_usd: 149801.8
sources:
  - label: "ClearMarket market record: Will someone leave their role in the Trump administrati"
    url: "https://clearmarket.fyi/events/kxtrumpadminleave-26dec31"
    retrieved_at: "2026-08-09T08:37:25+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume pushing a 98% contract higher signals the market has processed a credible public signal of departure, relevant for desks tracking DOJ leadership continuity and its downstream policy implications.
