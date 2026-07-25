---
signal_id: "CMSIG2026072304"
signal_slug: "iran-ends-enrichment-by-dec-31-polymarket-23-2026-07-23"
headline: "Iran ends enrichment by Dec 31: Polymarket 23%"
semantic_title: "Iran enrichment deal by year-end stays a long shot at 23 percent"
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
  volume_24h_usd: 1631.006954
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 23% chance Iran agrees to end uranium enrichment by December 31, 2026."
  - "The House resolution signals congressional pressure to de-escalate, but the Polymarket contract at 23% reflects the market treating a full enrichment halt as still an unlikely outcome this year."
  - "A companion Polymarket contract (CM-EVT-QNQ4VPVP80) puts the Iranian regime's collapse before 2027 at just 9%, suggesting markets see the conflict as sustained but not regime-ending."
  - "Resolution depends on an official Iranian commitment to halt enrichment, as adjudicated by the Polymarket UMA oracle."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The House narrowly passed a resolution seeking to halt U.S. military action in Iran as the conflict continues to escalate."
    publisher: "apnews.com"
    published_at: "2026-07-23T00:00:00.000Z"
    source_url: "https://apnews.com/article/iran-congress-war-powers-resolution-vote-0ba2387a476fe08de0bfd6281adb9639"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/iran-congress-war-powers-resolution-vote-0ba2387a476fe08de0bfd6281adb9639"
        retrieved_at: "2026-07-25T09:42:27+00:00"
  - type: "pm_response"
    notes: "Polymarket at 23% shows the market is skeptical a diplomatic resolution materializes by year-end despite congressional de-escalation efforts."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: House again passes resolution seeking to halt military action in Iran"
    url: "https://apnews.com/article/iran-congress-war-powers-resolution-vote-0ba2387a476fe08de0bfd6281adb9639"
    published_at: "2026-07-23T00:00:00.000Z"
    retrieved_at: "2026-07-25T09:42:27+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
