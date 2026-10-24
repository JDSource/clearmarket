---
signal_id: "CMSIG2026102208"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-12-2026-10-22"
headline: "Hormuz traffic normal by Dec 31: Polymarket 12%"
semantic_title: "Strait of Hormuz traffic returning to normal by year-end stays a long shot"
telemetry: "Polymarket 12%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-22T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.12
  volume_24h_usd: 14117.232248999999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on Strait of Hormuz traffic returning to normal by December 31 sits at 12%, a strong long-shot read."
  - "With a US naval blockade now in effect and Iran threatening wider strikes on economic targets, the market at 12% is consistent with an escalating, not de-escalating, scenario."
  - "Oil near $100-116 per barrel (Stories 33, 35) corroborates the market's pricing of prolonged disruption rather than imminent normalization."
  - "Resolution via Polymarket's uma_oracle; the contract likely requires a return to pre-blockade transit volumes, making partial resumption insufficient for settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump accused Iran of fabricating ship strikes to drive up oil prices, while a US naval blockade on Iranian port traffic in the Strait of Hormuz took effect."
    publisher: "Duarte Dias Digital Journalist"
    published_at: "2026-10-22T00:00:00.000Z"
    source_url: "https://www.cbsnews.com/live-updates/iran-war-trump-us-ceasefire-talks-ongoing/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Duarte Dias Digital Journalist"
        source_url: "https://www.cbsnews.com/live-updates/iran-war-trump-us-ceasefire-talks-ongoing/"
        retrieved_at: "2026-10-24T12:26:12+00:00"
  - type: "pm_response"
    notes: "Polymarket at 12% on Hormuz normalization by year-end reflects the active US blockade and Iranian escalation rhetoric, with the price level consistent with a market that sees the disruption persisting well into 2027."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Duarte Dias Digital Journalist: Trump accuses Iran of making up fake strikes on ships to drive up oil"
    url: "https://www.cbsnews.com/live-updates/iran-war-trump-us-ceasefire-talks-ongoing/"
    published_at: "2026-10-22T00:00:00.000Z"
    retrieved_at: "2026-10-24T12:26:12+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
