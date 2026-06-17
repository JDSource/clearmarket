---
signal_id: "CMSIG2026061704"
signal_slug: "iran-unrestricted-hormuz-shipping-by-june-30-polymarket-31-2026-06-17"
headline: "Iran unrestricted Hormuz shipping by June 30: Polymarket 31%"
semantic_title: "Iran unrestricted Hormuz shipping by June 30 fractures below one-third"
telemetry: "Polymarket 31%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-17T11:24:00.000Z"
event_id: "CM-EVT-FP5Q8518G7"
event_slug: "iran-agrees-to-unrestricted-shipping-through-hormuz-by-june-30"
event_question: "Will Iran agree to unrestricted shipping through Hormuz by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x1723b7ee4118dee6ae6be8802cb7b6e239c37d199997b20a8191e32553a5bd68"
  question_raw: "Iran agrees to unrestricted shipping through Hormuz by June 30?"
  current_price: 0.31
  volume_24h_usd: 49749.449696000025
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices unrestricted Iran shipping through Hormuz by June 30 at only 31%, despite deal-leak headlines pointing to Strait reopening."
  - "Markets are treating the leak as incomplete; deal signing, Iranian compliance, and physical vessel movement all remain separate hurdles within 13 days."
  - "The December 31 Hormuz normalization contract on Polymarket sits at 78%, indicating markets believe reopening is likely eventually but not imminent."
  - "Resolves via UMA oracle; 'unrestricted shipping' language likely requires verified transit data, not just a signed agreement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Leaked deal terms show Iran agreeing to reopen the Strait of Hormuz and retain oil export rights as part of a US-Iran ceasefire framework."
    publisher: "spectrumlocalnews.com"
    published_at: "2026-06-17T11:24:00.000Z"
    source_url: "https://spectrumlocalnews.com/tx/san-antonio/international/2026/06/17/iran-united-states-war-israel-lebanon-negotiations-strait-hormuz-oil-tentative-deal"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "spectrumlocalnews.com"
        source_url: "https://spectrumlocalnews.com/tx/san-antonio/international/2026/06/17/iran-united-states-war-israel-lebanon-negotiations-strait-hormuz-oil-tentative-deal"
        retrieved_at: "2026-06-17T12:13:58+00:00"
  - type: "pm_response"
    notes: "The 31% June 30 versus 78% December 31 spread on Polymarket is the key cross-contract signal on Hormuz reopening timeline risk."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "spectrumlocalnews.com: Iran to reopen Strait, can sell oil in deal, per leaks"
    url: "https://spectrumlocalnews.com/tx/san-antonio/international/2026/06/17/iran-united-states-war-israel-lebanon-negotiations-strait-hormuz-oil-tentative-deal"
    published_at: "2026-06-17T11:24:00.000Z"
    retrieved_at: "2026-06-17T12:13:58+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
