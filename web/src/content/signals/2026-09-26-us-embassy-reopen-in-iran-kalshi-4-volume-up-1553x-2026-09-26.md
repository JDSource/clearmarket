---
signal_id: "CMSIG2026092605"
signal_slug: "us-embassy-reopen-in-iran-kalshi-4-volume-up-1553x-2026-09-26"
headline: "US embassy reopen in Iran: Kalshi 4%, volume up 1553x"
semantic_title: "US embassy reopening in Iran stays a remote possibility"
telemetry: "Kalshi 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-26T00:00:00.000Z"
event_id: "CM-EVT-34SYT4T2T1"
event_slug: "kxiranembassy-27"
event_question: "Will the United States reopen its embassy in Iran?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXIRANEMBASSY-27"
  question_raw: "Will the US reopen its embassy in Iran before Jan 1, 2027?"
  current_price: 0.037
  volume_24h_usd: 13.13
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only 4% on the US reopening its embassy in Iran, with trading volume up 1553x day-over-day, a massive surge in attention on this contract."
  - "Iran's call for diplomacy is not moving the needle on this contract; 4% reflects deep market skepticism that any breakthrough reaches the level of embassy normalization."
  - "The volume spike confirms fresh money is engaging with Iran-resolution risk across the board, even as the headline probability stays near the floor."
  - "Resolves via The New York Times confirmation; embassy reopening requires formal diplomatic recognition steps well beyond a Hormuz traffic agreement, setting a high bar."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Iran insisted on a diplomatic solution after Trump rejected its Hormuz peace plan, with both sides still divided over who must move first."
    publisher: "al-monitor.com"
    published_at: "2026-09-26T00:00:00.000Z"
    source_url: "https://www.al-monitor.com/originals/2026/09/iran-insists-diplomatic-solution-after-trump-rejects-peace-plan"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "al-monitor.com"
        source_url: "https://www.al-monitor.com/originals/2026/09/iran-insists-diplomatic-solution-after-trump-rejects-peace-plan"
        retrieved_at: "2026-09-27T13:30:43+00:00"
  - type: "pm_response"
    notes: "Kalshi's 4% price with 1553x volume surge is the clearest signal in the Iran cluster: traders are watching closely but betting heavily against normalization."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "al-monitor.com: Iran insists on diplomatic solution after Trump rejects peace plan - A"
    url: "https://www.al-monitor.com/originals/2026/09/iran-insists-diplomatic-solution-after-trump-rejects-peace-plan"
    published_at: "2026-09-26T00:00:00.000Z"
    retrieved_at: "2026-09-27T13:30:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
