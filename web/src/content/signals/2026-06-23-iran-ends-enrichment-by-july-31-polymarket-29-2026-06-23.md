---
signal_id: "CMSIG2026062303"
signal_slug: "iran-ends-enrichment-by-july-31-polymarket-29-2026-06-23"
headline: "Iran ends enrichment by July 31: Polymarket 29%"
semantic_title: "Iran uranium enrichment halt by July 31 stays well below even odds"
telemetry: "Polymarket 29%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-23T05:22:42.000Z"
event_id: "CM-EVT-8SWDJJDJM0"
event_slug: "iran-agrees-to-end-enrichment-of-uranium-by-july-31"
event_question: "Will Iran agree to end enrichment of uranium by July 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x151b13b0d75a282ea864a2835963c0164c03e8fa3064c4d44026e3af5f2ff8d4"
  question_raw: " Iran agrees to end enrichment of uranium by July 31?"
  current_price: 0.29
  volume_24h_usd: 6990.058033
  arbitration_model: "uma_oracle"
  resolves_at: "2026-07-31T00:00:00Z"
bullets:
  - "Polymarket prices Iran agreeing to end uranium enrichment by July 31 at only 29%."
  - "Iran's explicit denial of enrichment concessions is consistent with the market's skeptical pricing well below 50%."
  - "The June 30 enrichment-halt contract sits at 24%, nearly identical to July 31, suggesting the market sees little incremental probability of a deal in that extra month."
  - "Resolves via UMA oracle; what counts as 'agreeing to end enrichment' versus a pause or cap is a live definitional risk."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US waived Iran sanctions after Switzerland talks, but Iran publicly denied it had begun dismantling its nuclear program."
    publisher: "Mia Gonzalez"
    published_at: "2026-06-23T05:22:42.000Z"
    source_url: "https://www.rappler.com/world/us-iran-peace-deal-updates-june-23-2026/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Mia Gonzalez"
        source_url: "https://www.rappler.com/world/us-iran-peace-deal-updates-june-23-2026/"
        retrieved_at: "2026-06-23T10:59:18+00:00"
  - type: "pm_response"
    notes: "Polymarket's 29% on enrichment halt by July 31 reflects the market's reading that sanctions relief does not automatically translate to Iranian nuclear concessions."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Mia Gonzalez: US waives Iran sanctions, Trump says he will 'do what I have to' if Te"
    url: "https://www.rappler.com/world/us-iran-peace-deal-updates-june-23-2026/"
    published_at: "2026-06-23T05:22:42.000Z"
    retrieved_at: "2026-06-23T10:59:18+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
