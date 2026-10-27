---
signal_id: "CMSIG20261027VS03"
signal_slug: "will-yashar-win-the-most-seats-in-the-20-vol-460809"
headline: "Yashar most Knesset seats: 78% on $461K"
semantic_title: "Yashar leads Israeli seat race at 78% with heavy backing"
telemetry: "78% · $461K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-27T13:54:51+00:00"
event_id: "CM-EVT-SV1SCXFSY0"
event_slug: "israeli-legislative-election-winner"
event_question: "Will the Israeli legislative election result in a clear winner by the next scheduled election date?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd05da9807740aa0f5bc9e9232daabe87a21e5012c19e283abf414f1c1651118b"
  question_raw: "Will Yashar win the most seats in the 2026 Israeli legislative election?"
  current_price: 0.78
  volume_24h_usd: 460809.99127500004
  volume_cumulative_usd: 1476165.849736
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-27T00:00:00Z"
bullets:
  - "Polymarket prices Yashar at 78% to win the most seats, the clear market frontrunner in the 2026 Israeli election."
  - "24h volume of $461K is 31% of all-time, reinforcing the frontrunner read with meaningful fresh capital."
  - "Yashar's 78% sits against Likud's 21% and Together's 0%, suggesting the field has largely converged on this outcome."
  - "Resolves on certified 2026 Knesset seat totals."
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
      poly_vol_24h_usd: 460809.99127500004
sources:
  - label: "ClearMarket market record: Will the Israeli legislative election result in a clear"
    url: "https://clearmarket.fyi/events/israeli-legislative-election-winner"
    retrieved_at: "2026-10-27T13:54:51+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Yashar's commanding odds combined with sustained volume make this the anchor contract for Israeli election exposure, desks pricing political risk should treat 78% as the current consensus.
