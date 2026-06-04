---
signal_id: "CMSIG2026060403"
signal_slug: "iran-unrestricted-hormuz-shipping-by-june-30-polymarket-13-2026-06-04"
headline: "Iran unrestricted Hormuz shipping by June 30: Polymarket 13%"
semantic_title: "Iran agreeing to open Hormuz by June 30 priced a long shot"
telemetry: "Polymarket 13%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-04T01:40:01.000Z"
event_id: "CM-EVT-FP5Q8518G7"
event_slug: "iran-agrees-to-unrestricted-shipping-through-hormuz-by-june-30"
event_question: "Will Iran agree to unrestricted shipping through Hormuz by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x1723b7ee4118dee6ae6be8802cb7b6e239c37d199997b20a8191e32553a5bd68"
  question_raw: "Iran agrees to unrestricted shipping through Hormuz by June 30?"
  current_price: 0.13
  volume_24h_usd: 6616.107209
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket contract puts 13% on Iran agreeing to unrestricted Hormuz shipping by June 30."
  - "Fresh Iranian strikes on Kuwait and US counter-strikes on Qeshm Island are consistent with this low probability."
  - "Companion Polymarket contract on Hormuz returning to normal by end of June sits at 20%, showing minimal upside even on a longer window."
  - "Resolves via portwatch.imf.org traffic data; physical shipping normalisation, not just a ceasefire statement, is required."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran attacked Kuwait and traded strikes with the US, threatening the Persian Gulf ceasefire."
    publisher: "nbcnews.com"
    published_at: "2026-06-04T01:40:01.000Z"
    source_url: "https://www.nbcnews.com/world/iran/iran-attacks-kuwait-strikes-us-ceasefire-peace-talks-trump-rcna348213"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "nbcnews.com"
        source_url: "https://www.nbcnews.com/world/iran/iran-attacks-kuwait-strikes-us-ceasefire-peace-talks-trump-rcna348213"
        retrieved_at: "2026-06-04T03:24:20+00:00"
  - type: "pm_response"
    notes: "Polymarket at 13% reflects the escalating Gulf strikes making near-term shipping normalisation unlikely."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "nbcnews.com: Iran attacks Kuwait, trades strikes with U.S. in test to ceasefire"
    url: "https://www.nbcnews.com/world/iran/iran-attacks-kuwait-strikes-us-ceasefire-peace-talks-trump-rcna348213"
    published_at: "2026-06-04T01:40:01.000Z"
    retrieved_at: "2026-06-04T03:24:20+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
