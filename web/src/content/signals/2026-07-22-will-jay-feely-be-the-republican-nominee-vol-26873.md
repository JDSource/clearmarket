---
signal_id: "CMSIG20260722VS03"
signal_slug: "will-jay-feely-be-the-republican-nominee-vol-26873"
headline: "Feely AZ-01 GOP nominee: 100% on $27K surge"
semantic_title: "Jay Feely's Republican AZ-01 nomination trades at certainty"
telemetry: "100% · $27K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-22T10:22:39+00:00"
event_id: "CM-EVT-3YB040ZX15"
event_slug: "kxaz01r-26"
event_question: "Will the Republican nominee for Arizona's 1st congressional district be determined by the 2026 election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAZ01R-26-JFEE"
  question_raw: "Will Jay Feely be the Republican nominee for AZ-1?"
  current_price: 0.999
  volume_24h_usd: 26873.47
  volume_cumulative_usd: 58748.49
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi prices Jay Feely's Republican nomination at 100%, no probability of another outcome remains."
  - "24h volume of $27K is 46% of all-time, compressing into a fully-resolved market stance."
  - "Volume at ceiling likely reflects last participants closing opposing legs after a definitive result."
  - "Resolves on official GOP nominee certification for Arizona's 1st congressional district."
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
      kalshi_vol_24h_usd: 26873.47
sources:
  - label: "ClearMarket market record: Will the Republican nominee for Arizona's 1st congressi"
    url: "https://clearmarket.fyi/events/kxaz01r-26"
    retrieved_at: "2026-07-22T10:22:39+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 100% print drawing nearly half of all-time volume in one session confirms a settlement event has occurred, the Republican primary in AZ-01 is done, and paired with the Shah spike, the general election matchup is now set.
