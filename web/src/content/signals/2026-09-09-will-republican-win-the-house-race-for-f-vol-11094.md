---
signal_id: "CMSIG20260909VS05"
signal_slug: "will-republican-win-the-house-race-for-f-vol-11094"
headline: "FL-25 Republican: 21% on $11K trading burst"
semantic_title: "Republicans slip to 21% odds in FL-25 House race"
telemetry: "21% · $11K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-09T12:40:54+00:00"
event_id: "CM-EVT-Q8F4815M66"
event_slug: "kxhouserace-fl25-26"
event_question: "Will the Florida 25th House seat be won in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-FL25-26-R"
  question_raw: "Will Republican win the House race for FL-25?"
  current_price: 0.21
  volume_24h_usd: 11094.16
  volume_cumulative_usd: 16057.28
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices a Republican win in FL-25 at just 21%, a notably weak reading in a Florida district."
  - "69% of all-time contract volume arrived in a single 24h window, signaling sudden market interest."
  - "FL-25 pricing implies Democrats are favored roughly 4-to-1; new candidate or polling data may have triggered attention."
  - "Resolves on certified 2026 midterm results for Florida's 25th Congressional District."
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
      kalshi_vol_24h_usd: 11094.16
sources:
  - label: "ClearMarket market record: Will the Florida 25th House seat be won in the next ele"
    url: "https://clearmarket.fyi/events/kxhouserace-fl25-26"
    retrieved_at: "2026-09-09T12:40:54+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 21% Republican read on a Florida seat, combined with a near-lifetime volume flush, warrants desk scrutiny of whether a candidate switch or major local development has repriced this race materially.
