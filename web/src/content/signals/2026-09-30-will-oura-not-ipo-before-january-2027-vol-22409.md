---
signal_id: "CMSIG20260930VS04"
signal_slug: "will-oura-not-ipo-before-january-2027-vol-22409"
headline: "Oura IPO by Jan 2027: 12% on $22K, 66% of all-time"
semantic_title: "Oura IPO before January 2027 stays a long shot at 12%"
telemetry: "88% · $22K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-09-30T07:48:11+00:00"
event_id: "CM-EVT-TV6FPVN7B4"
event_slug: "oura-ipo-closing-market-cap"
event_question: "Will Oura's IPO closing market cap exceed $5 billion?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xbfc5804406e3254b98ff869862aebb77dedf35b54374b3c8ddfee73168cac219"
  question_raw: "Will Oura not IPO before January 2027?"
  current_price: 0.88
  volume_24h_usd: 22409.411543
  volume_cumulative_usd: 34101.778847999994
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T00:00:00Z"
bullets:
  - "Polymarket implies only a 12% chance Oura completes an IPO before January 2027, the 'no IPO' side prices at 88%."
  - "$22K in 24h represents 66% of all-time contract volume, the overwhelming majority of lifetime liquidity in one day."
  - "Surge likely triggered by an Oura funding announcement, filing rumor, or broader wearables-sector IPO news."
  - "Contract resolves if Oura lists publicly before January 1, 2027; the window is now roughly 90 days."
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
      poly_vol_24h_usd: 22409.411543
sources:
  - label: "ClearMarket market record: Will Oura's IPO closing market cap exceed $5 billion?"
    url: "https://clearmarket.fyi/events/oura-ipo-closing-market-cap"
    retrieved_at: "2026-09-30T07:48:11+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

Two-thirds of all-time volume arriving in a single day on a near-expired IPO window contract signals that a specific Oura corporate announcement is driving attention, desks should track any S-1 or funding news.
