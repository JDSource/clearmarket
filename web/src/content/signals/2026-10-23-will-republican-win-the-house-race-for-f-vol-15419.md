---
signal_id: "CMSIG20261023VS07"
signal_slug: "will-republican-win-the-house-race-for-f-vol-15419"
headline: "Rep FL-25 House: 17% on $15.4K, 38% all-time vol"
semantic_title: "Democrats ahead in FL-25 as Republican odds slip to 17%"
telemetry: "17% · $15K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-23T13:04:13+00:00"
event_id: "CM-EVT-Q8F4815M66"
event_slug: "kxhouserace-fl25-26"
event_question: "Will the Florida 25th House seat be won in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-FL25-26-R"
  question_raw: "Will Republican win the House race for FL-25?"
  current_price: 0.17
  volume_24h_usd: 15419.11
  volume_cumulative_usd: 40829.92
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices the Republican candidate at just 17% in FL-25, market firmly favors the Democrat in this seat."
  - "24h volume of $15.4K is 38% of all-time total, marking a significant one-day concentration of trading."
  - "Heavy volume into a 17% Republican contract suggests desks are either locking in the Democratic lean or probing for a shift."
  - "Resolves on Florida 25th District House race result."
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
      kalshi_vol_24h_usd: 15419.11
sources:
  - label: "ClearMarket market record: Will the Florida 25th House seat be won in the next ele"
    url: "https://clearmarket.fyi/events/kxhouserace-fl25-26"
    retrieved_at: "2026-10-23T13:04:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

More than a third of all-time volume hitting FL-25 at 17% Republican signals desks are treating this as a firm Democratic seat and incorporating it into House majority count scenarios.
