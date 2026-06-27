---
signal_id: "CMSIG2026062406"
signal_slug: "iran-ends-uranium-enrichment-by-dec-31-polymarket-29-2026-06-24"
headline: "Iran ends uranium enrichment by Dec 31: Polymarket 29%"
semantic_title: "Iran enrichment end by year-end wavers near long odds"
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
  volume_24h_usd: 17958.469888
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 29% odds on Iran agreeing to end uranium enrichment by December 31, 2026."
  - "IAEA inspection visits proceeding under a preliminary deal are a positive step, but the market's sub-30% pricing reflects deep skepticism about a full enrichment halt."
  - "Companion Polymarket contract (CM-EVT-73D6P1DKY8) prices only 1% on an enrichment end by June 30, confirming the market sees any deal as a second-half-2026 possibility at best."
  - "Resolves via Polymarket uma_oracle; requires a formal Iranian agreement to cease enrichment activity, not merely inspection access."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The IAEA chief confirmed inspectors will visit Iranian nuclear sites as part of a preliminary peace agreement, but called for very strong verification mechanisms."
    publisher: "bbc.co.uk"
    published_at: "2026-06-24T12:32:00.000Z"
    source_url: "https://www.bbc.co.uk/news/articles/cpd395zv81vo"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "bbc.co.uk"
        source_url: "https://www.bbc.co.uk/news/articles/cpd395zv81vo"
        retrieved_at: "2026-06-27T01:35:43+00:00"
  - type: "pm_response"
    notes: "Polymarket's 29% year-end contract versus 1% June 30 contract implies the market sees a deal as plausible but dependent on extended negotiation, not imminent."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "bbc.co.uk: UN nuclear chief says inspectors will visit Iran sites as part of war"
    url: "https://www.bbc.co.uk/news/articles/cpd395zv81vo"
    published_at: "2026-06-24T12:32:00.000Z"
    retrieved_at: "2026-06-27T01:35:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
