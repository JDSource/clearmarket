---
signal_id: "CMSIG2026081105"
signal_slug: "iran-ends-uranium-enrichment-by-dec-31-polymarket-14-2026-08-11"
headline: "Iran ends uranium enrichment by Dec 31: Polymarket 14%"
semantic_title: "Iran ends uranium enrichment by year-end stays a long shot"
telemetry: "Polymarket 14%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-11T00:00:00.000Z"
event_id: "CM-EVT-4CKJ2D3T77"
event_slug: "iran-agrees-to-end-enrichment-of-uranium-by-december-31"
event_question: "Will Iran agree to end enrichment of uranium by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xff68b32e6543ae8b44ccb520604b6ea224a1bac071a186fb65f6f40949a758df"
  question_raw: " Iran agrees to end enrichment of uranium by December 31?"
  current_price: 0.14
  volume_24h_usd: 1579.976664
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts only 14% on Iran agreeing to end uranium enrichment by December 31, a long-shot read consistent with talks collapsing."
  - "The return to sanctions rather than negotiation is fully consistent with this low probability, the market is not pricing a diplomatic breakthrough."
  - "Companion Polymarket contract CM-EVT-LCPV825X09 prices 46% on Strait of Hormuz traffic returning to normal by year-end, suggesting the market sees a slightly better chance of commercial normalization than nuclear resolution."
  - "Resolves via UMA oracle; the question is binary on Iran's formal agreement, not on partial or informal steps."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump pivoted back to sanctions after nuclear talks with Iran collapsed, making a near-term diplomatic resolution appear increasingly remote."
    publisher: "apnews.com"
    published_at: "2026-08-11T00:00:00.000Z"
    source_url: "https://apnews.com/article/trump-iran-sanctions-d96e3bf53eb4050097e6cab128db82cb"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/trump-iran-sanctions-d96e3bf53eb4050097e6cab128db82cb"
        retrieved_at: "2026-08-13T09:07:47+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 14%; the gap between 46% Hormuz normalization odds and 14% enrichment-deal odds implies the market sees a possible Hormuz resolution path that does not require a nuclear agreement."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: After talks with Iran fizzle, Trump turns back to sanctions | AP News"
    url: "https://apnews.com/article/trump-iran-sanctions-d96e3bf53eb4050097e6cab128db82cb"
    published_at: "2026-08-11T00:00:00.000Z"
    retrieved_at: "2026-08-13T09:07:47+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
