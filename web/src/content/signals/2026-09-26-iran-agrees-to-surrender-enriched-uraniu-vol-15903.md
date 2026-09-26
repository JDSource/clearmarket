---
signal_id: "CMSIG20260926VS03"
signal_slug: "iran-agrees-to-surrender-enriched-uraniu-vol-15903"
headline: "Iran uranium deal by Oct 31: 3% on $16K"
semantic_title: "Iran uranium surrender by Oct 31 trades at 3% on fresh volume"
telemetry: "3% · $16K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-26T07:47:58+00:00"
event_id: "CM-EVT-Z3K4DFFZY1"
event_slug: "iran-agrees-to-surrender-enriched-uranium-stockpile-by"
event_question: "Will Iran agree to surrender its enriched uranium stockpile by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xaff5b702feef28fd0207583e17f8f2610d8191b5951441974e166dcdb61366e2"
  question_raw: "Iran agrees to surrender enriched uranium stockpile by October 31, 2026?"
  current_price: 0.03
  volume_24h_usd: 15903.792102
  volume_cumulative_usd: 51731.614438000004
  arbitration_model: "uma_oracle"
  resolves_at: "2026-10-31T00:00:00Z"
bullets:
  - "3% on Polymarket prices an Iran enriched-uranium surrender by October 31, 2026 as an extreme tail risk."
  - "24h volume of $16K is 31% of all-time, a material one-day share for a geopolitical resolution contract."
  - "Fresh attention to a near-zero geopolitics contract often follows a diplomatic statement, IAEA report, or back-channel leak."
  - "Resolves YES only if Iran formally agrees to surrender stockpile by October 31, 2026."
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
      poly_vol_24h_usd: 15903.792102
sources:
  - label: "ClearMarket market record: Will Iran agree to surrender its enriched uranium stock"
    url: "https://clearmarket.fyi/events/iran-agrees-to-surrender-enriched-uranium-stockpile-by"
    retrieved_at: "2026-09-26T07:47:58+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

New flow into a 3% geopolitical contract just five weeks from its deadline is a signal worth flagging, desks should check whether any IAEA communications or P5+1 talks catalyzed the session.
