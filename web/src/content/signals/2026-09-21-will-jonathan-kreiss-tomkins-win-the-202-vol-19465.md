---
signal_id: "CMSIG20260921VS03"
signal_slug: "will-jonathan-kreiss-tomkins-win-the-202-vol-19465"
headline: "Kreiss-Tomkins AK governor: 82% on $19K"
semantic_title: "Kreiss-Tomkins leads Alaska governor race as buyers back 82% odds"
telemetry: "82% · $19K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-21T14:47:42+00:00"
event_id: "CM-EVT-552YG8W5J1"
event_slug: "alaska-governor-election-winner"
event_question: "Will Mark Begich win the 2026 Alaska Governor election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x43cedce4a6af0136d37d53408fc965388baee3145db6da72a5b5da8d2746ced3"
  question_raw: "Will Jonathan Kreiss-Tomkins win the 2026 Alaska governor election?"
  current_price: 0.824
  volume_24h_usd: 19465.047668
  volume_cumulative_usd: 76912.94068399999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Kreiss-Tomkins at 82%, reflecting strong conviction that he is the clear front-runner in Alaska's 2026 race."
  - "Today's $19K in volume equals 25% of all-time, a notable single-day concentration for an Alaska state-level contract."
  - "Fresh participation at elevated odds suggests the market is confirming rather than challenging his front-runner status following a likely news event."
  - "Resolves on the outcome of the 2026 Alaska gubernatorial election."
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
      poly_vol_24h_usd: 19465.047668
sources:
  - label: "ClearMarket market record: Will Mark Begich win the 2026 Alaska Governor election?"
    url: "https://clearmarket.fyi/events/alaska-governor-election-winner"
    retrieved_at: "2026-09-21T14:47:42+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy volume accumulating at 82% on a state-level race signals that desks treating Alaska's governor contest as a tail risk are now treating it as a resolved question, which itself can precede a catalyst or organizational shift.
