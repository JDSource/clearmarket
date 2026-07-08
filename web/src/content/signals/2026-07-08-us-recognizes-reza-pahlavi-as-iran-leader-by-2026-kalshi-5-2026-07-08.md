---
signal_id: "CMSIG2026070808"
signal_slug: "us-recognizes-reza-pahlavi-as-iran-leader-by-2026-kalshi-5-2026-07-08"
headline: "US recognizes Reza Pahlavi as Iran leader by 2026: Kalshi 5%"
semantic_title: "Reza Pahlavi recognition as Iran leader holds at deep discount"
telemetry: "Kalshi 5%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-08T07:10:32.000Z"
event_id: "CM-EVT-SY50TZ6672"
event_slug: "kxrecogpersoniran-26"
event_question: "Will the United States recognize Reza Pahlavi as the leader of Iran by 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXRECOGPERSONIRAN-26"
  question_raw: "Will the United States recognize Reza Pahlavi as the leader of Iran in 2026?"
  current_price: 0.053
  volume_24h_usd: 13.72
  arbitration_model: "kalshi_staff"
  resolution_source: "ABC"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only a 5% probability the US formally recognizes Reza Pahlavi as leader of Iran by end-2026, resolving via ABC."
  - "Despite full-scale US military strikes on over 80 Iranian targets and Trump declaring the ceasefire over, the market assigns near-zero odds to regime replacement via formal US recognition."
  - "A companion Kalshi contract prices only a 5% chance the US reopens its embassy in Iran (CM-EVT-34SYT4T2T1), reinforcing that the market sees confrontation continuing without either diplomatic normalization or regime change."
  - "Resolves via ABC News reporting of a formal US government recognition statement; the current military escalation does not appear to move this market toward regime-change pricing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Iran struck US positions at Isa Air Base in Bahrain and attacked tankers in the Strait of Hormuz, prompting over 80 US retaliatory strikes and Trump declaring the ceasefire over."
    publisher: "Darryl Coote"
    published_at: "2026-07-08T07:10:32.000Z"
    source_url: "https://www.upi.com/Top_News/World-News/2026/07/08/iran-United-States-attack/9561783491084/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Darryl Coote"
        source_url: "https://www.upi.com/Top_News/World-News/2026/07/08/iran-United-States-attack/9561783491084/"
        retrieved_at: "2026-07-08T10:13:38+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 5% resolves via ABC; the price reflects market consensus that even intensified military strikes fall well short of the threshold for formal US recognition of an alternative Iranian government."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Darryl Coote: Iran attacks Bahrain, Kuwait after U.S. strikes - UPI.com"
    url: "https://www.upi.com/Top_News/World-News/2026/07/08/iran-United-States-attack/9561783491084/"
    published_at: "2026-07-08T07:10:32.000Z"
    retrieved_at: "2026-07-08T10:13:38+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
