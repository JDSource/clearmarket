---
signal_id: "CMSIG20260812VS06"
signal_slug: "will-the-democratic-party-win-the-govern-vol-66343"
headline: "Democrat wins NV governor: 34% on $66K"
semantic_title: "Nevada governor odds tilt Republican as fresh volume arrives"
telemetry: "34% · $66K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-12T09:08:32+00:00"
event_id: "CM-EVT-TNC2QWG2J9"
event_slug: "govpartynv-26"
event_question: "Nevada Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYNV-26-D"
  question_raw: "Will the Democratic party win the governorship in Nevada"
  current_price: 0.34
  volume_24h_usd: 66343.09
  volume_cumulative_usd: 102940.09
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-02T15:00:00Z"
bullets:
  - "Kalshi prices a Democratic Nevada governor win at just 34%, the market leans Republican in this race."
  - "$66K in 24h is 64% of all-time volume, suggesting this contract is early-stage and drawing initial positioning."
  - "Nevada's swing-state status and an open-seat dynamic are likely pulling cross-market attention here."
  - "Resolves on the certified winner of the 2026 Nevada gubernatorial election."
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
      kalshi_vol_24h_usd: 66343.09
sources:
  - label: "ClearMarket market record: Nevada Governor winner?"
    url: "https://clearmarket.fyi/events/govpartynv-26"
    retrieved_at: "2026-08-12T09:08:32+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 34% Democratic price in Nevada, historically competitive, is a notable signal for desks tracking 2026 gubernatorial landscape; the fresh-volume lean toward Republicans here is worth watching alongside polling.
