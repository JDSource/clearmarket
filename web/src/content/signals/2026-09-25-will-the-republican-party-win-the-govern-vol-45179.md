---
signal_id: "CMSIG20260925VS01"
signal_slug: "will-the-republican-party-win-the-govern-vol-45179"
headline: "Vermont GOP gov: 82% on $45K Kalshi surge"
semantic_title: "Vermont GOP governorship holds strong at 82%"
telemetry: "82% · $45K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-25T13:13:41+00:00"
event_id: "CM-EVT-ZSNM57MQS0"
event_slug: "govpartyvt-26"
event_question: "Vermont Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYVT-26-R"
  question_raw: "Will the Republican party win the governorship in Vermont"
  current_price: 0.82
  volume_24h_usd: 45179.43
  volume_cumulative_usd: 92174.76
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-05T15:00:00Z"
bullets:
  - "Kalshi prices Republican win at 82%, reflecting a near-consensus lean in a state where the incumbent GOP governor has cross-party appeal."
  - "24h volume of $45K is 49% of all-time contract volume, a remarkable single-day concentration of capital."
  - "Vermont's GOP governor has historically outperformed the party label; fresh volume confirms, rather than challenges, that read."
  - "Resolution tied to 2026 Vermont gubernatorial election result."
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
      kalshi_vol_24h_usd: 45179.43
sources:
  - label: "ClearMarket market record: Vermont Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyvt-26"
    retrieved_at: "2026-09-25T13:13:41+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Heavy one-day volume at a high price level suggests traders are locking in a near-consensus position ahead of an expected news event or early-vote data release.
