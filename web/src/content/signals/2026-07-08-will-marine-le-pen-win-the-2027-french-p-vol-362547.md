---
signal_id: "CMSIG20260708VS01"
signal_slug: "will-marine-le-pen-win-the-2027-french-p-vol-362547"
headline: "Le Pen 2027 win: 27% on $363K Polymarket flow"
semantic_title: "Traders stack Le Pen 2027 conviction at 27%"
telemetry: "27% · $363K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-08T10:14:29+00:00"
event_id: "CM-EVT-GD1GGR4710"
event_slug: "next-french-presidential-election"
event_question: "Will a new French president be elected in the next French Presidential Election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x8126317d621047fb13d508a2651eecc8d38305904671822a62309c5aabd353aa"
  question_raw: "Will Marine Le Pen win the 2027 French presidential election?"
  current_price: 0.271
  volume_24h_usd: 362547.04180299974
  volume_cumulative_usd: 1261757.954513998
  arbitration_model: "uma_oracle"
  resolves_at: "2027-04-30T00:00:00Z"
bullets:
  - "Polymarket prices Le Pen winning the presidency at 27%, meaningful tail risk, not consensus."
  - "24h volume $363K is 29% of all-time, reflecting a fresh wave of directional interest."
  - "Likely catalyzed by companion ballot-eligibility spike (Spike 5) resolving her candidacy near 89%."
  - "Resolves after the 2027 French presidential election final round."
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
      poly_vol_24h_usd: 362547.04180299974
sources:
  - label: "ClearMarket market record: Will a new French president be elected in the next Fren"
    url: "https://clearmarket.fyi/events/next-french-presidential-election"
    retrieved_at: "2026-07-08T10:14:29+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy concurrent flow across Le Pen ballot and win contracts suggests a coordinated reassessment of her electoral viability, desks should monitor for a legal or political development confirming her candidacy.
