---
signal_id: "CMSIG2026110107"
signal_slug: "us-recognizes-reza-pahlavi-as-iran-leader-kalshi-6-2026-11-01"
headline: "US recognizes Reza Pahlavi as Iran leader: Kalshi 6%"
semantic_title: "US recognition of Reza Pahlavi stays a long shot"
telemetry: "Kalshi 6%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-01T00:00:00.000Z"
event_id: "CM-EVT-SY50TZ6672"
event_slug: "kxrecogpersoniran-26"
event_question: "Will the United States recognize Reza Pahlavi as the leader of Iran by 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXRECOGPERSONIRAN-26"
  question_raw: "Will the United States recognize Reza Pahlavi as the leader of Iran in 2026?"
  current_price: 0.062
  volume_24h_usd: 80.07
  arbitration_model: "kalshi_staff"
  resolution_source: "ABC"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi prediction market puts just 6% odds on the US recognizing Reza Pahlavi as leader of Iran by 2026."
  - "Diplomatic exploration between Tehran and Washington is ongoing, but the market sees near-zero probability of a regime-change-style outcome this year."
  - "The Polymarket contract on Hormuz traffic returning to normal by December 31 sits at 12%, consistent with the low probability of a comprehensive deal."
  - "The US embassy reopening in Iran contract on Kalshi (CM-EVT-34SYT4T2T1) is at 3%, reinforcing that markets see diplomacy as exploratory, not conclusive."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Iran and the US are exploring diplomacy amid rising threats of war, with Tehran saying it could reopen the Strait of Hormuz if conditions are met."
    publisher: "Maziar Motamedi"
    published_at: "2026-11-01T00:00:00.000Z"
    source_url: "https://www.aljazeera.com/news/2026/11/1/iran-and-us-explore-diplomacy-amid-rising-threats-of-war"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Maziar Motamedi"
        source_url: "https://www.aljazeera.com/news/2026/11/1/iran-and-us-explore-diplomacy-amid-rising-threats-of-war"
        retrieved_at: "2026-11-01T14:42:33+00:00"
  - type: "pm_response"
    notes: "The Kalshi contract resolves via ABC News reporting; the 6% reading is consistent across the Iran diplomatic event cluster, with no contract pricing a near-term breakthrough above low single digits."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Maziar Motamedi: Iran and US explore diplomacy amid rising threats of war | US-Israel w"
    url: "https://www.aljazeera.com/news/2026/11/1/iran-and-us-explore-diplomacy-amid-rising-threats-of-war"
    published_at: "2026-11-01T00:00:00.000Z"
    retrieved_at: "2026-11-01T14:42:33+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
