---
signal_id: "CMSIG2026062505"
signal_slug: "iran-hormuz-unrestricted-shipping-by-june-30-polymarket-31-2026-06-25"
headline: "Iran Hormuz unrestricted shipping by June 30: Polymarket 31%"
semantic_title: "Iran unrestricted Hormuz shipping by June 30 fractures"
telemetry: "Polymarket 31%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-25T20:16:00.000Z"
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
  - "Polymarket prices 31% on Iran agreeing to unrestricted Hormuz shipping by June 30, a below-even probability with four days remaining in the window."
  - "The drone strike on a commercial vessel is directly at odds with the near-term resolution scenario the 31% price implies."
  - "The companion Polymarket contract on Hormuz traffic returning to normal by December 31 prices at 78%, showing the market sees eventual normalization but not before month-end."
  - "Resolves via UMA oracle; the July 31 traffic-return contract at 47% and the December contract at 78% reveal a market pricing a multi-month delay, not a near-term fix."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran's Revolutionary Guards struck a Singapore-flagged commercial vessel in the Strait of Hormuz with a drone, pausing UN evacuation efforts."
    publisher: "cbsnews.com"
    published_at: "2026-06-25T20:16:00.000Z"
    source_url: "https://www.cbsnews.com/news/iran-strikes-commercial-ship-strait-of-hormuz-us-iran-deal-oil/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cbsnews.com"
        source_url: "https://www.cbsnews.com/news/iran-strikes-commercial-ship-strait-of-hormuz-us-iran-deal-oil/"
        retrieved_at: "2026-06-26T10:48:01+00:00"
  - type: "pm_response"
    notes: "Polymarket's three-horizon Hormuz term structure (18% June, 47% July, 78% December) shows the market treating the drone strike as a near-term resolution blocker."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cbsnews.com: Iran strikes commercial ship in Strait of Hormuz in challenge to U.S.-"
    url: "https://www.cbsnews.com/news/iran-strikes-commercial-ship-strait-of-hormuz-us-iran-deal-oil/"
    published_at: "2026-06-25T20:16:00.000Z"
    retrieved_at: "2026-06-26T10:48:01+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
