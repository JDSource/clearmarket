---
signal_id: "CMSIG2026112104"
signal_slug: "congress-approves-iran-deal-by-2026-polymarket-3-2026-11-21"
headline: "Congress approves Iran deal by 2026: Polymarket 3%"
semantic_title: "Congress approving an Iran deal by year-end stays a long shot"
telemetry: "Polymarket 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-21T11:13:29.000Z"
event_id: "CM-EVT-PB2TWNBNL3"
event_slug: "congress-approves-iran-deal-in-2026-20260616005217959"
event_question: "Will Congress approve an Iran deal by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0665610d8a06655edb83376e45fd8d2dd78889d2b3a1b2668efe398514cf87ae"
  question_raw: "Congress approves Iran deal in 2026?"
  current_price: 0.03
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T04:59:00Z"
bullets:
  - "The Polymarket contract prices only a 3% chance Congress approves an Iran deal by end of 2026."
  - "Trump's own statement pushing the timeline to 2027 is consistent with the market's near-zero probability for a 2026 congressional approval."
  - "Active combat, Iran claiming an F-16 hit, IRGC striking Bahrain bases, further undermines the case for a rapid diplomatic resolution."
  - "Resolves via UMA oracle; congressional approval is a higher bar than a bilateral executive agreement, explaining the discount versus any executive-action pathway."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump said he wants a 'permanent' deal with Iran but warned the next move may not come until 2027, while Tehran denied chemical weapons claims."
    publisher: "Frank Andrews"
    published_at: "2026-11-21T11:13:29.000Z"
    source_url: "https://www.cbsnews.com/live-updates/iran-war-trump-tehran-denies-chemical-weapons/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Frank Andrews"
        source_url: "https://www.cbsnews.com/live-updates/iran-war-trump-tehran-denies-chemical-weapons/"
        retrieved_at: "2026-11-22T07:47:40+00:00"
  - type: "pm_response"
    notes: "Polymarket contract via UMA oracle; 3% pricing aligns with Trump's own 2027 timeline signal."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Frank Andrews: Live Updates: Trump says next move on Iran may not come until 2027 as"
    url: "https://www.cbsnews.com/live-updates/iran-war-trump-tehran-denies-chemical-weapons/"
    published_at: "2026-11-21T11:13:29.000Z"
    retrieved_at: "2026-11-22T07:47:40+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
