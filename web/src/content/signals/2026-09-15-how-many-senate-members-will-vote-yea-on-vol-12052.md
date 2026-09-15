---
signal_id: "CMSIG20260915VS03"
signal_slug: "how-many-senate-members-will-vote-yea-on-vol-12052"
headline: "Crypto bill Yea count: 54% on $12K surge"
semantic_title: "Crypto structure bill Senate vote count sits near 50%"
telemetry: "54% · $12K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-15T13:06:46+00:00"
event_id: "CM-EVT-CSYS5KPXK6"
event_slug: "kxvoteclarity-26may16"
event_question: "Senate votes on crypto market structure bill, May 16, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXVOTECLARITY-26MAY16-T50"
  question_raw: "How many Senate members will vote Yea on a crypto market structure bill (as defined in KXCRYPTOSTRUCTURE)?"
  current_price: 0.54
  volume_24h_usd: 12052.99
  volume_cumulative_usd: 31326.47
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices a 54% chance the DeFi crypto market structure bill clears the relevant Senate Yea threshold."
  - "38% of all-time volume arrived in 24 hours, the market's heaviest single day of engagement."
  - "Floor scheduling news or a whip count update on the crypto bill likely drove traders to take fresh positions."
  - "Resolution tied to the Senate floor vote on the crypto market structure legislation."
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
      kalshi_vol_24h_usd: 12052.99
sources:
  - label: "ClearMarket market record: Senate votes on crypto market structure bill, May 16, 2"
    url: "https://clearmarket.fyi/events/kxvoteclarity-26may16"
    retrieved_at: "2026-09-15T13:06:46+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-even odds at 54% with a record-volume day tells a compliance or digital-assets desk that legislative passage is genuinely uncertain and that new vote-count intelligence is actively moving the market.
