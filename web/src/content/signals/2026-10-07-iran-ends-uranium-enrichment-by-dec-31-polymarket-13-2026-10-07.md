---
signal_id: "CMSIG2026100707"
signal_slug: "iran-ends-uranium-enrichment-by-dec-31-polymarket-13-2026-10-07"
headline: "Iran ends uranium enrichment by Dec 31: Polymarket 13%"
semantic_title: "Iran uranium deal by year-end stays a long shot at 13 percent"
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
  volume_24h_usd: 4167.542309
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Iran agreeing to end uranium enrichment by December 31 at 13%, firmly in long-shot territory."
  - "Vance's public pivot to reduced rather than zero enrichment signals some diplomatic softening, but the 13% price shows the market is not treating this as a near-term breakthrough."
  - "Active US military strikes on Iran reported on October 8 (Story 29) are consistent with, not contradictory to, this low probability, diplomacy and military action are running in parallel."
  - "Polymarket resolves via UMA oracle; the precise definition of 'agree to end enrichment' will be critical, a reduced-enrichment deal may not satisfy the resolution standard."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US set new demands for an Iran nuclear deal, with Vice President JD Vance calling for reduced but not zero enrichment, suggesting room for compromise but major obstacles remain."
    publisher: "Caolán Magee"
    published_at: "2026-10-07T00:00:00.000Z"
    source_url: "https://www.aljazeera.com/news/2026/10/7/us-sets-new-demands-for-iran-deal-what-are-they"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Caolán Magee"
        source_url: "https://www.aljazeera.com/news/2026/10/7/us-sets-new-demands-for-iran-deal-what-are-they"
        retrieved_at: "2026-10-08T07:48:09+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 13%; the market is clearly not pricing in Vance's rhetorical softening as a near-term deal catalyst."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Caolán Magee: US sets new demands for Iran deal: What are they?"
    url: "https://www.aljazeera.com/news/2026/10/7/us-sets-new-demands-for-iran-deal-what-are-they"
    published_at: "2026-10-07T00:00:00.000Z"
    retrieved_at: "2026-10-08T07:48:09+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
