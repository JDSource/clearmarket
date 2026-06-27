---
signal_id: "CMSIG2026062405"
signal_slug: "iran-ends-enrichment-by-dec-31-polymarket-29-2026-06-24"
headline: "Iran ends enrichment by Dec 31: Polymarket 29%"
semantic_title: "Iran uranium enrichment end by December holds below one-in-three"
telemetry: "Polymarket 29%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-24T12:32:00.000Z"
event_id: "CM-EVT-4CKJ2D3T77"
event_slug: "iran-agrees-to-end-enrichment-of-uranium-by-december-31"
event_question: "Will Iran agree to end uranium enrichment by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xff68b32e6543ae8b44ccb520604b6ea224a1bac071a186fb65f6f40949a758df"
  question_raw: " Iran agrees to end enrichment of uranium by December 31?"
  current_price: 0.29
  volume_24h_usd: 2215.24
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 29% on Iran agreeing to end uranium enrichment by December 31, resolving via uma_oracle."
  - "IAEA inspection visits represent a procedural step, and the market is not treating this as a near-certain path to full enrichment cessation."
  - "The companion Polymarket contract on Iran ending enrichment by June 30 sits at only 2%, confirming the market sees any deal as a second-half-2026 possibility at best."
  - "Resolves via uma_oracle on public agreement announcement; the 27-percentage-point gap between June 30 (2%) and December 31 (29%) captures the market's view that talks will be slow."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The IAEA chief confirmed inspectors will visit Iranian nuclear sites under a preliminary peace agreement between Iran and the US."
    publisher: "bbc.co.uk"
    published_at: "2026-06-24T12:32:00.000Z"
    source_url: "https://www.bbc.co.uk/news/articles/cpd395zv81vo"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "bbc.co.uk"
        source_url: "https://www.bbc.co.uk/news/articles/cpd395zv81vo"
        retrieved_at: "2026-06-27T10:02:20+00:00"
  - type: "pm_response"
    notes: "Polymarket contracts on Iranian enrichment cessation at both June 30 (2%) and December 31 (29%); the spread reveals the market treats IAEA inspection news as a starting point, not a conclusion."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "bbc.co.uk: UN nuclear chief says inspectors will visit Iran sites as part of war"
    url: "https://www.bbc.co.uk/news/articles/cpd395zv81vo"
    published_at: "2026-06-24T12:32:00.000Z"
    retrieved_at: "2026-06-27T10:02:20+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
