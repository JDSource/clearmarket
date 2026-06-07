---
signal_id: "CMSIG2026060705"
signal_slug: "hormuz-traffic-normal-by-june-30-polymarket-20-2026-06-07"
headline: "Hormuz traffic normal by June 30: Polymarket 20%"
semantic_title: "Hormuz full traffic by end of June priced as unlikely"
telemetry: "Polymarket ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-07T00:28:00.000Z"
event_id: "CM-EVT-YPW93GCTK6"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-end-of-june"
event_question: "Strait of Hormuz traffic normalization by June 30"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x348cd9adf4f6855f58bd9c6dbf9ff251c4142ef77233a5dc95c65b4b61cd2187"
  question_raw: "Strait of Hormuz traffic returns to normal by end of June?"
  current_price: 0.2
  volume_24h_usd: 274766.3442870001
  arbitration_model: "uma_oracle"
  resolution_source: "portwatch.imf.org"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices only 20% probability that Hormuz traffic fully normalizes by end of June."
  - "Iran attacking Bahrain and Kuwait is squarely at odds with any near-term normalization, consistent with markets pricing this as a low-probability outcome."
  - "The December 31 normalization contract at 76% shows the market still sees eventual reopening as likely, but not within weeks."
  - "Resolves via portwatch.imf.org; full traffic return to pre-conflict baseline required for yes."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran fired missiles at Bahrain and Kuwait after U.S. strikes on Iranian radar sites, escalating Gulf tensions and straining the ceasefire."
    publisher: "thevibes.com"
    published_at: "2026-06-07T00:28:00.000Z"
    source_url: "https://www.thevibes.com/articles/world/123717/gulf-tensions-escalate-as-iran-fires-missiles-at-bahrain-and-kuwait"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "thevibes.com"
        source_url: "https://www.thevibes.com/articles/world/123717/gulf-tensions-escalate-as-iran-fires-missiles-at-bahrain-and-kuwait"
        retrieved_at: "2026-06-07T10:26:16+00:00"
  - type: "pm_response"
    notes: "Polymarket's 20% near-term vs. 76% year-end spread captures the market's view that normalization is a months-long process, not a June event."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "thevibes.com: Gulf tensions escalate as Iran fires missiles at Bahrain and Kuwait |"
    url: "https://www.thevibes.com/articles/world/123717/gulf-tensions-escalate-as-iran-fires-missiles-at-bahrain-and-kuwait"
    published_at: "2026-06-07T00:28:00.000Z"
    retrieved_at: "2026-06-07T10:26:16+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
