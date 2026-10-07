---
signal_id: "CMSIG2026100706"
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
  volume_24h_usd: 6.84
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts 13% odds on Iran agreeing to end uranium enrichment by December 31, 2026, resolving via UMA oracle."
  - "Vance's demand for enrichment cuts is a public negotiating position; at 13%, Polymarket is firmly fading any near-term deal, consistent with Iran's simultaneous pre-emptive strike threats."
  - "The companion Kalshi contract (CM-EVT-34SYT4T2T1) prices only 2% on the US reopening its embassy in Iran, reinforcing that markets see normalization as remote."
  - "Resolves via UMA oracle assessment of whether Iran formally agrees to cease enrichment before December 31, 2026."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US Vice President JD Vance called for reduced Iranian nuclear enrichment as a condition to end the conflict, while Iran threatened pre-emptive strikes."
    publisher: "Caolán Magee"
    published_at: "2026-10-07T00:00:00.000Z"
    source_url: "https://www.aljazeera.com/news/2026/10/7/us-sets-new-demands-for-iran-deal-what-are-they"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Caolán Magee"
        source_url: "https://www.aljazeera.com/news/2026/10/7/us-sets-new-demands-for-iran-deal-what-are-they"
        retrieved_at: "2026-10-07T15:02:04+00:00"
  - type: "pm_response"
    notes: "Polymarket at 13% reflects a market that treats US-Iran nuclear deal talks as a long shot despite public diplomatic signaling from both sides."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Caolán Magee: US sets new demands for Iran deal: What are they? | US-Israel war on I"
    url: "https://www.aljazeera.com/news/2026/10/7/us-sets-new-demands-for-iran-deal-what-are-they"
    published_at: "2026-10-07T00:00:00.000Z"
    retrieved_at: "2026-10-07T15:02:04+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
