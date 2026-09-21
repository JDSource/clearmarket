---
signal_id: "CMSIG20260921VS06"
signal_slug: "will-jonathan-kreiss-tomkins-win-the-202-vol-20316"
headline: "Kreiss-Tomkins AK governor: 84% on $20K surge"
semantic_title: "Kreiss-Tomkins leads the Alaska governor race at 84%"
telemetry: "84% · $20K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-21T07:48:00+00:00"
event_id: "CM-EVT-552YG8W5J1"
event_slug: "alaska-governor-election-winner"
event_question: "Will Mark Begich win the 2026 Alaska Governor election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x43cedce4a6af0136d37d53408fc965388baee3145db6da72a5b5da8d2746ced3"
  question_raw: "Will Jonathan Kreiss-Tomkins win the 2026 Alaska governor election?"
  current_price: 0.835
  volume_24h_usd: 20316.669116
  volume_cumulative_usd: 76782.05272999997
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Jonathan Kreiss-Tomkins at 84% to win the 2026 Alaska governor election, a strong favorite read."
  - "26% of all-time volume traded in 24h, the second-largest single-session share for this contract."
  - "Fresh volume backing an 84% price suggests new information, polling, endorsements, or a rival's withdrawal, is reinforcing the frontrunner framing."
  - "Resolves on 2026 Alaska gubernatorial election outcome."
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
      poly_vol_24h_usd: 20316.669116
sources:
  - label: "ClearMarket market record: Will Mark Begich win the 2026 Alaska Governor election?"
    url: "https://clearmarket.fyi/events/alaska-governor-election-winner"
    retrieved_at: "2026-09-21T07:48:00+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Sustained buying into an already high-probability candidate signals the market is absorbing a positive catalyst for Kreiss-Tomkins, a desk should check for a major endorsement or opponent exit that prompted the fresh volume.
