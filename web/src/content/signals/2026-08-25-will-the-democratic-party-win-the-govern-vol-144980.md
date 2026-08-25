---
signal_id: "CMSIG20260825VS01"
signal_slug: "will-the-democratic-party-win-the-govern-vol-144980"
headline: "Ohio Dem governor: 57% on $145K inflow"
semantic_title: "Traders pile into Ohio governor as Democrats lead at 57%"
telemetry: "57% · $145K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-08-25T08:37:37+00:00"
event_id: "CM-EVT-ZJYN286LR2"
event_slug: "govpartyoh-26"
event_question: "Ohio Governor winner?"
primary_market:
  platform: "kalshi"
  platform_market_id: "GOVPARTYOH-26-D"
  question_raw: "Will the Democratic party win the governorship in Ohio"
  current_price: 0.57
  volume_24h_usd: 144980.59
  volume_cumulative_usd: 382007.88
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-14T15:00:00Z"
bullets:
  - "Kalshi prices Democrats to win Ohio's governorship at 57%, a modest but clear edge over Republicans."
  - "24h volume of $145K represents 38% of all-time, the race is drawing outsized fresh attention."
  - "Ohio is a bellwether swing-state governor's race; a pricing shift here carries downstream implications for 2026 cycle reads."
  - "No set resolution date yet; volume surge suggests traders expect a near-term catalyst, filing deadline, poll, or candidate news."
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
      kalshi_vol_24h_usd: 144980.59
sources:
  - label: "ClearMarket market record: Ohio Governor winner?"
    url: "https://clearmarket.fyi/events/govpartyoh-26"
    retrieved_at: "2026-08-25T08:37:37+00:00"
field_provenance:
  pm_data: "kalshi_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 38% all-time share in one session on a governor's race signals desks are positioning ahead of an expected data release, polling, filing, or endorsement, that could sharply reprice this contract.
