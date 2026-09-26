---
signal_id: "CMSIG2026092601"
signal_slug: "hormuz-reopens-by-dec-31-polymarket-21-2026-09-26"
headline: "Hormuz reopens by Dec 31: Polymarket 21%"
semantic_title: "Hormuz traffic back to normal by year-end stays near long-shot odds"
telemetry: "Polymarket 21%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-26T02:44:28.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.21
  volume_24h_usd: 328933.149681
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts only 21% on Strait of Hormuz traffic returning to normal by December 31."
  - "Iran's seven-day reopening proposal and Trump's reported rejection are consistent with the market's skeptical pricing, no resolution in sight."
  - "Houthi drone strikes near Riyadh add a second risk vector, further clouding any near-term Hormuz normalization scenario."
  - "The Kalshi contract on US embassy reopening in Iran sits at just 4%, signaling the broader diplomatic gap the market sees between the two sides."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran proposed a seven-day plan to reopen the Strait of Hormuz but Trump reportedly rejected it, while Houthi drones struck near Riyadh."
    publisher: "Lekshmy Pavithran,Surabhi Vasundharadevi,Nathaniel Lacsina"
    published_at: "2026-09-26T02:44:28.000Z"
    source_url: "https://gulfnews.com/world/mena/iran-proposes-hormuz-plan-trump-reportedly-rejects-saudi-intercepts-houthi-drones-near-riyadh-1.500688383"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Lekshmy Pavithran,Surabhi Vasundharadevi,Nathaniel Lacsina"
        source_url: "https://gulfnews.com/world/mena/iran-proposes-hormuz-plan-trump-reportedly-rejects-saudi-intercepts-houthi-drones-near-riyadh-1.500688383"
        retrieved_at: "2026-09-26T07:47:13+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; Kalshi embassy contract resolves via The New York Times."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Lekshmy Pavithran,Surabhi Vasundharadevi,Nathaniel Lacsina: Iran’s Hormuz reopening plan rejected by Trump as Saudi air defences i"
    url: "https://gulfnews.com/world/mena/iran-proposes-hormuz-plan-trump-reportedly-rejects-saudi-intercepts-houthi-drones-near-riyadh-1.500688383"
    published_at: "2026-09-26T02:44:28.000Z"
    retrieved_at: "2026-09-26T07:47:13+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
