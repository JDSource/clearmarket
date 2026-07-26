---
signal_id: "CMSIG2026072604"
signal_slug: "iran-ends-enrichment-by-dec-31-polymarket-22-2026-07-26"
headline: "Iran ends enrichment by Dec 31: Polymarket 22%"
semantic_title: "Iran uranium enrichment end by year-end stays a long shot"
telemetry: "Polymarket 22%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-26T00:00:00.000Z"
event_id: "CM-EVT-4CKJ2D3T77"
event_slug: "iran-agrees-to-end-enrichment-of-uranium-by-december-31"
event_question: "Will Iran agree to end enrichment of uranium by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xff68b32e6543ae8b44ccb520604b6ea224a1bac071a186fb65f6f40949a758df"
  question_raw: " Iran agrees to end enrichment of uranium by December 31?"
  current_price: 0.22
  volume_24h_usd: 19167.097273
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts 22% odds on Iran agreeing to end uranium enrichment by December 31, 2026."
  - "The airstrike pause and active diplomacy are positive signals, but the market prices the deal as unlikely, skepticism outweighs the ceasefire narrative."
  - "The Strait of Hormuz traffic returning to normal by December 31 sits at 58% on Polymarket, a notably higher probability, suggesting markets see shipping normalization as more achievable than a full nuclear deal."
  - "The Kalshi contract on Trump visiting Iran sits at only 3%, consistent with talks being conducted at lower diplomatic levels."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US airstrikes on Iran paused after nearly two weeks, with diplomatic talks pressing forward to avert a return to all-out war."
    publisher: "Reuters"
    published_at: "2026-07-26T00:00:00.000Z"
    source_url: "https://quews.news/iran-war-spreads-to/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Reuters"
        source_url: "https://quews.news/iran-war-spreads-to/"
        retrieved_at: "2026-07-26T09:55:47+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; the year-end deadline leaves roughly five months for a deal to materialize."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Reuters: Iran war spreads to Red Sea and Caspian, Gulf quiet as US forgoes stri"
    url: "https://quews.news/iran-war-spreads-to/"
    published_at: "2026-07-26T00:00:00.000Z"
    retrieved_at: "2026-07-26T09:55:47+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
