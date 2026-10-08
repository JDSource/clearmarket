---
signal_id: "CMSIG2026100705"
signal_slug: "iran-ends-enrichment-by-dec-31-polymarket-13-2026-10-07"
headline: "Iran ends enrichment by Dec 31: Polymarket 13%"
semantic_title: "Iran ending uranium enrichment by year-end stays a long shot"
telemetry: "Polymarket 13%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-07T00:00:00.000Z"
event_id: "CM-EVT-4CKJ2D3T77"
event_slug: "iran-agrees-to-end-enrichment-of-uranium-by-december-31"
event_question: "Will Iran agree to end enrichment of uranium by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xff68b32e6543ae8b44ccb520604b6ea224a1bac071a186fb65f6f40949a758df"
  question_raw: " Iran agrees to end enrichment of uranium by December 31?"
  current_price: 0.13
  volume_24h_usd: 5146.522309
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only a 13% chance Iran agrees to end uranium enrichment by December 31, 2026."
  - "New US demands and Vance's compromise signals suggest diplomacy is alive, but Polymarket's pricing reflects deep skepticism a deal closes this year."
  - "The US military preparing Iran strike options (Story 10, 12) and deadlocked diplomacy (Story 24) are consistent with the low probability the market assigns to a nuclear agreement."
  - "Resolves via UMA oracle; the contract requires Iran to formally agree to end enrichment, not merely reduce it."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US set new demands on Iran including reduced nuclear enrichment, with Vice President JD Vance signaling room for compromise but major obstacles remaining."
    publisher: "Caolán Magee"
    published_at: "2026-10-07T00:00:00.000Z"
    source_url: "https://www.aljazeera.com/news/2026/10/7/us-sets-new-demands-for-iran-deal-what-are-they"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Caolán Magee"
        source_url: "https://www.aljazeera.com/news/2026/10/7/us-sets-new-demands-for-iran-deal-what-are-they"
        retrieved_at: "2026-10-08T15:10:10+00:00"
  - type: "pm_response"
    notes: "Polymarket at 13% on a year-end enrichment halt suggests participants see the US-Iran deadlock as more likely to persist than resolve within this calendar year."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Caolán Magee: US sets new demands for Iran deal: What are they?"
    url: "https://www.aljazeera.com/news/2026/10/7/us-sets-new-demands-for-iran-deal-what-are-they"
    published_at: "2026-10-07T00:00:00.000Z"
    retrieved_at: "2026-10-08T15:10:10+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
