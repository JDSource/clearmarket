---
signal_id: "CMSIG2026111706"
signal_slug: "ukraine-cedes-territory-to-russia-by-2026-polymarket-2-2026-11-17"
headline: "Ukraine cedes territory to Russia by 2026: Polymarket 2%"
semantic_title: "Ukraine agreeing to cede territory by year-end stays near zero"
telemetry: "Polymarket 2%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-17T00:45:11.000Z"
event_id: "CM-EVT-XP7FFT2MC9"
event_slug: "will-ukraine-agree-to-cede-territory-to-russia-before-2027"
event_question: "Will Ukraine agree to cede territory to Russia by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x21bf9a7dae81b6bd51acae73185686ab8997b81b1401e4be10e114d472599c26"
  question_raw: "Will Ukraine agree to cede territory to Russia before 2027?"
  current_price: 0.025
  volume_24h_usd: 618.26
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract prices only 2% odds on Ukraine formally agreeing to cede territory to Russia by end of 2026, resolving via UMA oracle."
  - "Active infrastructure strikes and Russia's unchanged negotiating position are consistent with the market's near-certain read that no territorial concession deal closes this year."
  - "The Trump-Putin-Xi meeting in Shenzhen this week is a live catalyst; even so, the market assigns near-zero probability to a formal Ukrainian territorial concession by year-end."
  - "A companion Kalshi contract on Russia-Ukraine peace talks by 2026 shows no price, leaving Polymarket as the only live read on the near-term resolution pathway."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Ukraine held peace talks with the US and Europe as Russia and Ukraine continued striking major infrastructure, with Irish Foreign Minister Helen McEntee noting no change in Russia's position."
    publisher: "Al Jazeera Staff"
    published_at: "2026-11-17T00:45:11.000Z"
    source_url: "https://www.aljazeera.com/news/2026/11/17/ukraine-holds-peace-talks-with-us-europe-as-conflict-escalates"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Al Jazeera Staff"
        source_url: "https://www.aljazeera.com/news/2026/11/17/ukraine-holds-peace-talks-with-us-europe-as-conflict-escalates"
        retrieved_at: "2026-11-17T07:48:04+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle by December 31, 2026; no territorial concession framework has been publicly proposed, consistent with the near-zero pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Al Jazeera Staff: Ukraine holds peace talks with US, Europe as conflict escalates | Russ"
    url: "https://www.aljazeera.com/news/2026/11/17/ukraine-holds-peace-talks-with-us-europe-as-conflict-escalates"
    published_at: "2026-11-17T00:45:11.000Z"
    retrieved_at: "2026-11-17T07:48:04+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
