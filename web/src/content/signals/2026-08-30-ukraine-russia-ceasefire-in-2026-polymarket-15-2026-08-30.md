---
signal_id: "CMSIG2026083007"
signal_slug: "ukraine-russia-ceasefire-in-2026-polymarket-15-2026-08-30"
headline: "Ukraine-Russia ceasefire in 2026: Polymarket 15%"
semantic_title: "Ukraine-Russia ceasefire in 2026 puts odds at 15 percent"
telemetry: "Polymarket 15%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-30T00:00:00.000Z"
event_id: "CM-EVT-2089XJ01Y3"
event_slug: "russia-x-ukraine-ceasefire-by"
event_question: "Will Russia and Ukraine reach a ceasefire in 2026? (multi-deadline series)"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x84c625fdccf5c5246a15e476361e4563033906ee225800e1136c0d737596a72f"
  question_raw: "Russia x Ukraine ceasefire by December 31, 2026?"
  current_price: 0.15
  volume_24h_usd: 696.3
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract on a Ukraine-Russia ceasefire in 2026 prices at 15%, keeping the outcome a long shot."
  - "Overnight Russian strikes involving 130 drones and ballistic missiles are consistent with the market's low ceasefire probability; intensive bombardment runs directly counter to de-escalation."
  - "The companion Polymarket contract on a full peace deal before 2027 (CM-EVT-DCQYWYX424) prices at only 11%, with territory cession by Ukraine (CM-EVT-XP7FFT2MC9) at 7%, showing a consistent low-probability cluster across peace outcomes."
  - "Resolution on the ceasefire contract uses Polymarket's UMA oracle; a formal, verified cessation of hostilities is required, not an informal pause or local truce."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Russia struck Ukraine overnight with ballistic missiles and 130 drones, continuing intensive bombardment amid ongoing war."
    publisher: "newsukraine.rbc.ua"
    published_at: "2026-08-30T00:00:00.000Z"
    source_url: "https://newsukraine.rbc.ua/news/russia-strikes-ukraine-with-2-ballistic-missiles-1788070865.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "newsukraine.rbc.ua"
        source_url: "https://newsukraine.rbc.ua/news/russia-strikes-ukraine-with-2-ballistic-missiles-1788070865.html"
        retrieved_at: "2026-08-30T13:30:27+00:00"
  - type: "pm_response"
    notes: "Polymarket prices a tight cluster of low probabilities across ceasefire, peace deal, and territory cession contracts, broadly consistent with the ongoing Russian offensive posture."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "newsukraine.rbc.ua: Russia strikes Ukraine with 2 ballistic missiles and 130 drones overni"
    url: "https://newsukraine.rbc.ua/news/russia-strikes-ukraine-with-2-ballistic-missiles-1788070865.html"
    published_at: "2026-08-30T00:00:00.000Z"
    retrieved_at: "2026-08-30T13:30:27+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
