---
signal_id: "CMSIG20260806VS03"
signal_slug: "will-marsha-blackburn-be-the-republican-vol-53958"
headline: "Blackburn TN GOP nominee: 97% on $54K"
semantic_title: "Blackburn as TN GOP governor nominee holds at 97% through a volume surge"
telemetry: "97% · $54K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-06T10:36:04+00:00"
event_id: "CM-EVT-5MV6W6X5T7"
event_slug: "kxgovtnnomr-2-26"
event_question: "Will Bill Lee be the Tennessee Republican Governor nominee by 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVTNNOMR-2-26-MBLA"
  question_raw: "Will Marsha Blackburn be the Republican nominee for Governor in Tennessee?"
  current_price: 0.969
  volume_24h_usd: 53958.41
  volume_cumulative_usd: 213517.64
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-08-31T14:00:00Z"
bullets:
  - "97% pricing leaves only a 3% tail that Blackburn fails to capture the Republican nomination."
  - "24h volume of $54K is 25% of a large $214K all-time base, a meaningful, sustained inflow."
  - "Fresh activity may reflect a filing deadline, poll release, or a rival candidate's exit."
  - "Resolves on Tennessee GOP primary result; near-certainty pricing offers little upside for new longs."
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
      kalshi_vol_24h_usd: 53958.41
sources:
  - label: "ClearMarket market record: Will Bill Lee be the Tennessee Republican Governor nomi"
    url: "https://clearmarket.fyi/events/kxgovtnnomr-2-26"
    retrieved_at: "2026-08-06T10:36:04+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

High price plus a fresh 25%-of-all-time volume tranche signals the market is stress-testing an incumbent favorite, a desk should watch for any credible primary challenger news that could move the 3% tail.
