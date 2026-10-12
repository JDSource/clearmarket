---
signal_id: "CMSIG20261012VS02"
signal_slug: "will-republican-win-the-house-race-for-o-vol-17802"
headline: "GOP OH-10 House win: 86% on $17.8K"
semantic_title: "Republican hold of OH-10 draws heavy trading at 86%"
telemetry: "86% · $18K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-10-12T17:18:20+00:00"
event_id: "CM-EVT-TY2DWD9XJ0"
event_slug: "kxhouserace-oh10-26"
event_question: "OH-10 House winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-OH10-26-R"
  question_raw: "Will Republican win the House race for OH-10?"
  current_price: 0.86
  volume_24h_usd: 17802.13
  volume_cumulative_usd: 52970.69
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices Republican victory in OH-10 at 86%, strong favorite but not resolved."
  - "24h volume of $17.8K is 34% of all-time, a notable single-day concentration in a district race."
  - "The 14% residual suggests traders are pricing a non-trivial upset scenario worth active two-sided flow."
  - "Resolves on certified OH-10 House election result."
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
      kalshi_vol_24h_usd: 17802.13
sources:
  - label: "ClearMarket market record: OH-10 House winner?"
    url: "https://clearmarket.fyi/events/kxhouserace-oh10-26"
    retrieved_at: "2026-10-12T17:18:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

For a desk, the 34% all-time share in one session on an 86% contract points to active two-sided trading, worth monitoring for any candidate news or poll that could compress or widen that 14% tail.
