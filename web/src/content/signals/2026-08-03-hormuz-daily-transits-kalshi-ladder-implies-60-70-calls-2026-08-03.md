---
signal_id: "CMSIG2026080305"
signal_slug: "hormuz-daily-transits-kalshi-ladder-implies-60-70-calls-2026-08-03"
headline: "Hormuz daily transits: Kalshi ladder implies 60-70 calls"
semantic_title: "Hormuz transit volume seen staying low, stuck below 70 daily calls"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-03T00:00:00.000Z"
event_id: "CM-EVT-ZP6006CHN9"
event_slug: "kxhormuzweekly-26jul26"
event_question: "Strait of Hormuz daily transit calls"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHORMUZWEEKLY-26JUL26-T70"
  question_raw: "Will there be more than 70 transit calls through the Strait of Hormuz from Jul 20, 2026 to Jul 26, 2026?"
  current_price: 0.16
  volume_24h_usd: 172.69
  arbitration_model: "kalshi_staff"
  resolution_source: "IMF PortWatch"
  resolves_at: "2026-10-26T14:00:00Z"
bullets:
  - "Kalshi ladder implies roughly 60-70 daily transit calls through the Strait of Hormuz: 71% above 60 but only 16% above 70."
  - "Trump's optimism about imminent reopening is being faded by the market, which puts only 16% odds on transit volume recovering above 70 daily calls."
  - "A companion Polymarket contract (CM-EVT-LCPV825X09) prices Strait of Hormuz traffic returning to normal by December 31 at just 57%, a longer-horizon market also reflecting deep uncertainty."
  - "Resolution: Strait of Hormuz transit call data (the named resolution source) settles each strike on the Kalshi ladder."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump called off fresh Iran strikes and said new talks could reopen the Strait of Hormuz, expressing optimism the waterway could reopen imminently."
    publisher: "apnews.com"
    published_at: "2026-08-03T00:00:00.000Z"
    source_url: "https://apnews.com/article/mideast-iran-us-israel-palestinians-gaza-3b92568b6f2eec283eb51d0327ee682a"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/mideast-iran-us-israel-palestinians-gaza-3b92568b6f2eec283eb51d0327ee682a"
        retrieved_at: "2026-08-04T10:33:12+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder and Polymarket year-end contract both show the market discounting Trump's optimism on a rapid Hormuz reopening."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: Trump says new talks on Iran war will begin Monday | AP News"
    url: "https://apnews.com/article/mideast-iran-us-israel-palestinians-gaza-3b92568b6f2eec283eb51d0327ee682a"
    published_at: "2026-08-03T00:00:00.000Z"
    retrieved_at: "2026-08-04T10:33:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
