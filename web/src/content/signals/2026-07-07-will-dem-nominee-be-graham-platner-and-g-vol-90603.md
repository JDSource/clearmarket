---
signal_id: "CMSIG20260707VS06"
signal_slug: "will-dem-nominee-be-graham-platner-and-g-vol-90603"
headline: "Platner nom + Dem wins Maine Senate: 60% on $91K"
semantic_title: "Platner nominee plus Democratic general win priced as coin-flip"
telemetry: "60% · $91K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-07T10:52:51+00:00"
event_id: "CM-EVT-2KYR51YTD3"
event_slug: "kxmesenoutcome-27jan"
event_question: "Will Dem Nominee be Graham Platner AND General Election Winner be Democrat for Jan 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXMESENOUTCOME-27JAN-GPD"
  question_raw: "Will Dem Nominee be Graham Platner AND General Election Winner be Democrat for Jan 2027?"
  current_price: 0.6
  volume_24h_usd: 90603.85
  volume_cumulative_usd: 258197.02
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "60% on the compound outcome, Platner as Democratic nominee AND general election win, reflects strong but conditional conviction."
  - "$90.6K in 24h, 35% of all-time, flows directly from Platner dropout contract reshaping the race narrative."
  - "Apparent tension: 91% on Platner dropout (Spike 0) yet 60% here implies either the dropout resolves the other way or the contract structure differs."
  - "Contract resolves on Platner securing the Democratic nomination and Democrats winning the general in Maine's Senate race (likely January 2027 resolution)."
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
      kalshi_vol_24h_usd: 90603.85
sources:
  - label: "ClearMarket market record: Will Dem Nominee be Graham Platner AND General Election"
    url: "https://clearmarket.fyi/events/kxmesenoutcome-27jan"
    retrieved_at: "2026-07-07T10:52:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Desks should reconcile the 91% dropout probability with the 60% compound contract, the market structure likely defines 'drop out' differently from 'not the nominee,' making careful contract-term review essential before taking positions.
