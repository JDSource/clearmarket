---
signal_id: "CMSIG20261010VS03"
signal_slug: "will-the-democratic-party-win-the-attorn-vol-18473"
headline: "NY AG (D): 91% on $18K Kalshi surge"
semantic_title: "NY AG Democratic hold trades near certainty at 91%"
telemetry: "91% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-10T14:12:44+00:00"
event_id: "CM-EVT-2WVDLYDTS5"
event_slug: "kxattygenny-26"
event_question: "Will the New York Attorney General race be decided by January 2027?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXATTYGENNY-26-D"
  question_raw: "Will the Democratic party win the Attorney General race in New York?"
  current_price: 0.91
  volume_24h_usd: 18473.66
  volume_cumulative_usd: 39343.08
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-02T15:00:00Z"
bullets:
  - "Kalshi prices Democratic retention at 91%, the market treats a Republican win as a remote scenario."
  - "$18K in 24h is 47% of all-time volume, a notable mid-cycle burst for a near-consensus contract."
  - "Fresh volume at the top of the range suggests traders are either confirming the price or hunting for value at the margins."
  - "Resolves on New York Attorney General election result."
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
      kalshi_vol_24h_usd: 18473.66
sources:
  - label: "ClearMarket market record: Will the New York Attorney General race be decided by J"
    url: "https://clearmarket.fyi/events/kxattygenny-26"
    retrieved_at: "2026-10-10T14:12:44+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Near-max pricing drawing nearly half its lifetime volume in one day signals a desk that something, a legal story, a candidate event, or cross-market attention, has prompted traders to double-check this consensus.
