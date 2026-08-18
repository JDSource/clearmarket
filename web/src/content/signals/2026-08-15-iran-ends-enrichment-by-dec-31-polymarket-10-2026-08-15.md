---
signal_id: "CMSIG2026081506"
signal_slug: "iran-ends-enrichment-by-dec-31-polymarket-10-2026-08-15"
headline: "Iran ends enrichment by Dec 31: Polymarket 10%"
semantic_title: "Iran uranium enrichment deal by year-end stays a long shot"
telemetry: "Polymarket 10%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-15T00:00:00.000Z"
event_id: "CM-EVT-4CKJ2D3T77"
event_slug: "iran-agrees-to-end-enrichment-of-uranium-by-december-31"
event_question: "Will Iran agree to end enrichment of uranium by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xff68b32e6543ae8b44ccb520604b6ea224a1bac071a186fb65f6f40949a758df"
  question_raw: " Iran agrees to end enrichment of uranium by December 31?"
  current_price: 0.1
  volume_24h_usd: 44227.121787
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket contract on Iran agreeing to end uranium enrichment by December 31 sits at just 10%, with trading volume up 10,953% day over day."
  - "The extraordinary volume surge, over 110 times normal, signals the expired 60-day deadline and ongoing military posture are driving intense fresh attention to this contract."
  - "Trump's threat to bomb US ally Oman and Iran's vow to escalate over Hormuz are directionally consistent with the low 10% probability."
  - "Companion Kalshi contract on the US reopening its embassy in Iran (CM-EVT-34SYT4T2T1) sits at only 2%, confirming prediction markets see near-zero normalization near-term."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US pulled its last aircraft carrier from Asia to focus on Iran and the Western Hemisphere as the 60-day Versailles ceasefire deadline expired without a broader deal."
    publisher: "apnews.com"
    published_at: "2026-08-15T00:00:00.000Z"
    source_url: "https://apnews.com/article/aircraft-carriers-trump-china-pacific-iran-war-87cfb838de8c13464fa3cab1840ad87d"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/aircraft-carriers-trump-china-pacific-iran-war-87cfb838de8c13464fa3cab1840ad87d"
        retrieved_at: "2026-08-18T08:30:34+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; the volume explosion on the deadline expiry date makes this the most actively repriced geopolitical contract in this batch."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: Trump shifts aircraft carrier and US focus away from Asia | AP News"
    url: "https://apnews.com/article/aircraft-carriers-trump-china-pacific-iran-war-87cfb838de8c13464fa3cab1840ad87d"
    published_at: "2026-08-15T00:00:00.000Z"
    retrieved_at: "2026-08-18T08:30:34+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
