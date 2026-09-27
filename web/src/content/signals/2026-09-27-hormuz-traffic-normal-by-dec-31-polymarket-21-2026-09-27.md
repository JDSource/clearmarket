---
signal_id: "CMSIG2026092704"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-21-2026-09-27"
headline: "Hormuz traffic normal by Dec 31: Polymarket 21%"
semantic_title: "Strait of Hormuz back to normal by year-end stays below 25 percent"
telemetry: "Polymarket 21%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-27T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.21
  volume_24h_usd: 133025.89523300002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts 21% odds on Strait of Hormuz traffic returning to normal by December 31, 2026."
  - "Trump's public rejection of Iran's reopening proposal is consistent with this below-25% probability; the market is not pricing a near-term breakthrough."
  - "Iran's stated desire to wait for an official U.S. response keeps a slim path open, but the Polymarket contract reflects deep skepticism."
  - "A companion Kalshi contract on a U.S.-Iran nuclear deal by 2026 and related Hormuz transit-count questions carry no current prices, leaving Polymarket's 21% as the primary market signal on timeline."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "President Trump rejected Iran's proposal to reopen the Strait of Hormuz, with Iran saying it will wait for an official U.S. response."
    publisher: "AFP"
    published_at: "2026-09-27T00:00:00.000Z"
    source_url: "https://www.thehindu.com/news/international/trump-rejects-iran-proposal-for-deal-to-reopen-hormuz/article71514089.ece"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "AFP"
        source_url: "https://www.thehindu.com/news/international/trump-rejects-iran-proposal-for-deal-to-reopen-hormuz/article71514089.ece"
        retrieved_at: "2026-09-27T07:47:06+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via uma_oracle; Trump's explicit rejection of the Iranian proposal is the key near-term headwind for this contract."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "AFP: Trump rejects Iran proposal for deal to reopen Hormuz - The Hindu"
    url: "https://www.thehindu.com/news/international/trump-rejects-iran-proposal-for-deal-to-reopen-hormuz/article71514089.ece"
    published_at: "2026-09-27T00:00:00.000Z"
    retrieved_at: "2026-09-27T07:47:06+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
