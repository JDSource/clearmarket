---
signal_id: "CMSIG2026112205"
signal_slug: "iran-ends-enrichment-by-dec-31-polymarket-3-2026-11-22"
headline: "Iran ends enrichment by Dec 31: Polymarket 3%"
semantic_title: "Iran ending uranium enrichment by December stays a long shot"
telemetry: "Polymarket 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-22T03:23:49.000Z"
event_id: "CM-EVT-4CKJ2D3T77"
event_slug: "iran-agrees-to-end-enrichment-of-uranium-by-december-31"
event_question: "Will Iran agree to end enrichment of uranium by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xff68b32e6543ae8b44ccb520604b6ea224a1bac071a186fb65f6f40949a758df"
  question_raw: " Iran agrees to end enrichment of uranium by December 31?"
  current_price: 0.03
  volume_24h_usd: 70.696708
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only a 3% chance Iran agrees to end uranium enrichment by December 31."
  - "Active Iranian military operations against US assets in Bahrain run directly counter to the enrichment-surrender scenario, consistent with the market's near-zero pricing."
  - "Trump's 2027 timeline signal (Story 20) compounds the case that the market is correctly pricing out a 2026 resolution."
  - "Resolves via UMA oracle by December 31; the companion Polymarket contract on Congress approving an Iran deal (also 3%) confirms broad market skepticism of any near-term settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran released footage of a 'missile city,' claimed hits on US Patriot radar systems in Bahrain, and active fighting continued even as diplomatic efforts were reported."
    publisher: "thenationalnews.com"
    published_at: "2026-11-22T03:23:49.000Z"
    source_url: "https://www.thenationalnews.com/news/mena/2026/11/22/live-iran-underground-missile-city/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "thenationalnews.com"
        source_url: "https://www.thenationalnews.com/news/mena/2026/11/22/live-iran-underground-missile-city/"
        retrieved_at: "2026-11-22T07:47:40+00:00"
  - type: "pm_response"
    notes: "Polymarket contract via UMA oracle; pricing consistent across both enrichment and congressional approval contracts at 3%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "thenationalnews.com: Middle East latest: Iran releases video of 'missile city' as diplomati"
    url: "https://www.thenationalnews.com/news/mena/2026/11/22/live-iran-underground-missile-city/"
    published_at: "2026-11-22T03:23:49.000Z"
    retrieved_at: "2026-11-22T07:47:40+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
