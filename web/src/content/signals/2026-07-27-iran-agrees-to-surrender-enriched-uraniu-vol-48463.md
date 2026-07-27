---
signal_id: "CMSIG20260727VS02"
signal_slug: "iran-agrees-to-surrender-enriched-uraniu-vol-48463"
headline: "Iran uranium deal by Aug 31: 3% on $48K"
semantic_title: "Iran uranium surrender by August 31 trades at near-zero odds"
telemetry: "3% · $48K 24h"
category_tag: "VOLUME_SPIKE"
detection_path: "volume_spike"
pre_news_classification: "pre_news"
published_at: "2026-07-27T11:16:33+00:00"
event_id: "CM-EVT-Z3K4DFFZY1"
event_slug: "iran-agrees-to-surrender-enriched-uranium-stockpile-by"
event_question: "Will Iran agree to surrender its enriched uranium stockpile by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xaaa5a25b486566374edb205793371197c0f0195aff6a04341c1815bfef1a31f8"
  question_raw: "Iran agrees to surrender enriched uranium stockpile by August 31, 2026?"
  current_price: 0.028
  volume_24h_usd: 48463.801041
  volume_cumulative_usd: 61189.581657999996
  arbitration_model: "uma_oracle"
  resolves_at: "2026-08-31T00:00:00Z"
bullets:
  - "Polymarket prices Iran agreeing to surrender its enriched uranium stockpile by Aug 31 at 3%, effectively ruled out."
  - "24h volume $48K is 79% of all-time, the sharpest all-time concentration in this batch."
  - "Volume spike likely driven by nuclear talks news flow; market firmly rejecting the near-term scenario."
  - "Resolution deadline August 31, 2026 is five weeks away, leaving almost no runway."
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
      poly_vol_24h_usd: 48463.801041
sources:
  - label: "ClearMarket market record: Will Iran agree to surrender its enriched uranium stock"
    url: "https://clearmarket.fyi/events/iran-agrees-to-surrender-enriched-uranium-stockpile-by"
    retrieved_at: "2026-07-27T11:16:33+00:00"
field_provenance:
  pm_data: "polymarket_api"
  editorial_judgment: "cm_signal_llm_judge"
---

A 79% all-time volume share at 3% is a decisive crowd verdict against deal completion, desks monitoring Iran nuclear risk should treat the August 31 window as closed and focus on later resolution timelines.
