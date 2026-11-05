---
signal_id: "CMSIG20261105VS06"
signal_slug: "will-mary-peltola-win-the-2026-alaska-se-vol-229611"
headline: "Peltola AK Senate win: 94% on $229K Election Day flow"
semantic_title: "Betting backs Mary Peltola in Alaska Senate at 94%"
telemetry: "94% · $230K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-11-05T07:49:08+00:00"
event_id: "CM-EVT-6KJ40RJZP3"
event_slug: "kxaksenate-26nov03"
event_question: "Who will win the Alaska Senate election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAKSENATE-26NOV03-MPEL"
  question_raw: "Will Mary Peltola win the 2026 Alaska Senate race?"
  current_price: 0.942
  volume_24h_usd: 229611.25
  volume_cumulative_usd: 739863.97
  arbitration_model: "kalshi_staff"
  resolves_at: "2026-11-10T15:00:00Z"
bullets:
  - "Kalshi prices Mary Peltola winning the Alaska Senate race at 94%, a strong individual-candidate conviction read."
  - "31% of all-time contract volume, $229K, arrived in 24 hours, the heaviest single-day session on this market."
  - "Peltola pricing aligns tightly with the broader Democratic Alaska Senate contract at 95%, implying she is the consensus nominee and winner."
  - "Resolves on certified Peltola vote share; the 6% tail covers third-party, ranked-choice, or recount scenarios."
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
      kalshi_vol_24h_usd: 229611.25
sources:
  - label: "ClearMarket market record: Who will win the Alaska Senate election?"
    url: "https://clearmarket.fyi/events/kxaksenate-26nov03"
    retrieved_at: "2026-11-05T07:49:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Peltola at 94% with nearly a third of all-time volume in one day tells the desk the market treats her personal victory as effectively coincident with the Democratic win, watch ranked-choice counts for the residual tail.
