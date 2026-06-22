---
signal_id: "CMSIG2026062203"
signal_slug: "iran-unrestricted-hormuz-by-june-30-polymarket-31-2026-06-22"
headline: "Iran unrestricted Hormuz by June 30: Polymarket 31%"
semantic_title: "Hormuz unrestricted shipping by June 30 pricing fractures"
telemetry: "Polymarket 31%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-22T00:20:37.000Z"
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
  - "Polymarket prices Iran formally agreeing to unrestricted Hormuz shipping by June 30 at 31%, well below even odds with 8 days left."
  - "Progress in Switzerland is real but the headline roadmap targets 60 days, not 8, making the June 30 bar difficult to clear."
  - "A companion Polymarket contract asking only whether any ships transit by June 30 sits at 28%, nearly identical, suggesting markets see partial reopening as nearly as unlikely as a full agreement."
  - "Resolves via uma_oracle; the requirement is a formal Iranian agreement on unrestricted passage, not merely resumed negotiations or transit of a single vessel."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "US-Iran talks continue in Switzerland with encouraging progress reported, but Trump reiterated threats to take over the Strait while Iran has not yet formally agreed to reopen it."
    publisher: "straitstimes.com"
    published_at: "2026-06-22T00:20:37.000Z"
    source_url: "https://www.straitstimes.com/world/middle-east/us-iran-talks-go-into-day-2-after-trump-threats-hormuz-closure"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "straitstimes.com"
        source_url: "https://www.straitstimes.com/world/middle-east/us-iran-talks-go-into-day-2-after-trump-threats-hormuz-closure"
        retrieved_at: "2026-06-22T13:32:28+00:00"
  - type: "pm_response"
    notes: "Polymarket at 31% is consistent with the parallel any-transit contract at 28%, indicating the market is pricing little daylight between a partial and a full agreement by month-end."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "straitstimes.com: US-Iran talks continue amid Hormuz closure and Trump threats | The Str"
    url: "https://www.straitstimes.com/world/middle-east/us-iran-talks-go-into-day-2-after-trump-threats-hormuz-closure"
    published_at: "2026-06-22T00:20:37.000Z"
    retrieved_at: "2026-06-22T13:32:28+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
