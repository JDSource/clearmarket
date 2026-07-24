---
signal_id: "CMSIG2026072304"
signal_slug: "iran-ends-enrichment-by-dec-31-polymarket-23-2026-07-23"
headline: "Iran ends enrichment by Dec 31: Polymarket 23%"
semantic_title: "Iran uranium enrichment end by December stays a long shot at 23%"
telemetry: "Polymarket 23%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-23T00:00:00.000Z"
event_id: "CM-EVT-4CKJ2D3T77"
event_slug: "iran-agrees-to-end-enrichment-of-uranium-by-december-31"
event_question: "Will Iran agree to end enrichment of uranium by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xff68b32e6543ae8b44ccb520604b6ea224a1bac071a186fb65f6f40949a758df"
  question_raw: " Iran agrees to end enrichment of uranium by December 31?"
  current_price: 0.23
  volume_24h_usd: 1759.9592830000001
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts only 23% probability on Iran agreeing to end uranium enrichment by December 31, 2026; trading volume is up 1,330% day over day, the largest volume surge in this batch."
  - "The House war-powers rebuke signals congressional fracture on Iran policy, and surging volume on the enrichment contract suggests fresh attention is being priced, though the market remains skeptical of a deal."
  - "Iran rejecting the Iraqi-brokered ceasefire proposal (Story 27) is consistent with the low 23% probability, the market is not pricing imminent diplomatic resolution."
  - "Kalshi (CM-EVT-34SYT4T2T1) prices only 5% on the US reopening its embassy in Iran, a harder diplomatic bar but directionally confirming that markets put long odds against near-term normalization."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US House narrowly passed a resolution to halt military action in Iran as the conflict with Iran escalates, with four Republicans joining Democrats."
    publisher: "apnews.com"
    published_at: "2026-07-23T00:00:00.000Z"
    source_url: "https://apnews.com/article/iran-congress-war-powers-resolution-vote-0ba2387a476fe08de0bfd6281adb9639"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/iran-congress-war-powers-resolution-vote-0ba2387a476fe08de0bfd6281adb9639"
        retrieved_at: "2026-07-24T10:13:15+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; the 1,330% volume spike day over day is a real measured signal of surging market attention on this claim."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: House again passes resolution seeking to halt military action in Iran"
    url: "https://apnews.com/article/iran-congress-war-powers-resolution-vote-0ba2387a476fe08de0bfd6281adb9639"
    published_at: "2026-07-23T00:00:00.000Z"
    retrieved_at: "2026-07-24T10:13:15+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
