---
signal_id: "CMSIG2026072004"
signal_slug: "iran-ends-uranium-enrichment-by-dec-31-polymarket-16-2026-07-20"
headline: "Iran ends uranium enrichment by Dec 31: Polymarket 16%"
semantic_title: "Iran uranium enrichment deal by year-end wavers at 16 percent"
telemetry: "Polymarket 16%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-20T00:00:00.000Z"
event_id: "CM-EVT-4CKJ2D3T77"
event_slug: "iran-agrees-to-end-enrichment-of-uranium-by-december-31"
event_question: "Will Iran agree to end enrichment of uranium by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xff68b32e6543ae8b44ccb520604b6ea224a1bac071a186fb65f6f40949a758df"
  question_raw: " Iran agrees to end enrichment of uranium by December 31?"
  current_price: 0.16
  volume_24h_usd: 6105.728223000002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 16% on Iran agreeing to end uranium enrichment by December 31, 2026."
  - "Nine consecutive nights of US strikes and Khamenei's explicit rejection of a ceasefire are consistent with the low 16% pricing."
  - "Iran simultaneously signaling ongoing diplomatic exchanges with the US via Rubio creates a cross-current the market is not yet resolving upward."
  - "Resolves via Polymarket's UMA oracle; a formal enrichment-halt announcement by any recognized authority before December 31 would settle YES."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US carried out its ninth consecutive night of air strikes against Iran as Strait of Hormuz tensions escalated and Ayatollah Khamenei called a ceasefire worthless."
    publisher: "Al Jazeera Staff"
    published_at: "2026-07-20T00:00:00.000Z"
    source_url: "https://www.aljazeera.com/news/2026/7/20/us-bombs-iran-for-ninth-consecutive-night-as-hormuz-tensions-escalate"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Al Jazeera Staff"
        source_url: "https://www.aljazeera.com/news/2026/7/20/us-bombs-iran-for-ninth-consecutive-night-as-hormuz-tensions-escalate"
        retrieved_at: "2026-07-20T10:47:34+00:00"
  - type: "pm_response"
    notes: "Polymarket contract via UMA oracle; active kinetic conflict keeps probability anchored at low levels."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Al Jazeera Staff: US bombs Iran for ninth consecutive night as Hormuz tensions escalate"
    url: "https://www.aljazeera.com/news/2026/7/20/us-bombs-iran-for-ninth-consecutive-night-as-hormuz-tensions-escalate"
    published_at: "2026-07-20T00:00:00.000Z"
    retrieved_at: "2026-07-20T10:47:34+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
