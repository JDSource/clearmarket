---
signal_id: "CMSIG20260910VS00"
signal_slug: "will-lucie-castets-win-the-2027-french-p-vol-164610"
headline: "Castets France 2027: 0% on $165K surge"
semantic_title: "Castets 2027 French presidency priced out at 0%"
telemetry: "0% · $165K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-10T12:40:48+00:00"
event_id: "CM-EVT-GD1GGR4710"
event_slug: "next-french-presidential-election"
event_question: "Will a new French president be elected in the next French Presidential Election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xac9719f855755f578e4979f8edb4e17e259e8e1cc79e46bdbde49e23dbd8b98f"
  question_raw: "Will Lucie Castets win the 2027 French presidential election?"
  current_price: 0.001
  volume_24h_usd: 164610.27
  volume_cumulative_usd: 418273.518
  arbitration_model: "uma_oracle"
  resolves_at: "2027-04-30T00:00:00Z"
bullets:
  - "Polymarket prices Castets at 0%, treating her presidential bid as effectively dead."
  - "39% of all-time volume, $165K, landed in 24 hours, making this a mass-attention event."
  - "Fresh French presidential market activity suggests news or political realignment driving re-examination."
  - "Resolves on 2027 French presidential election result."
atomic_claims:
  - type: "volume_anomaly"
    provenance: "24h + cumulative volume direct from polymarket API; intensity = 24h/cumulative (derived)"
    field_provenance:
      volume_24h_usd:
        tier: "direct"
        method: "polymarket_api"
      intensity:
        tier: "derived"
        method: "arithmetic"
        inputs: ["volume_24h_usd", "volume_cumulative_usd"]
    liquidity_context:
      poly_vol_24h_usd: 164610.27
sources:
  - label: "ClearMarket market record: Will a new French president be elected in the next Fren"
    url: "https://clearmarket.fyi/events/next-french-presidential-election"
    retrieved_at: "2026-09-10T12:40:48+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A near-total-volume wipeout at 0% signals desks should watch for a Castets withdrawal or formal party decision closing off her candidacy path.
