---
signal_id: "CMSIG2026082407"
signal_slug: "us-bitcoin-reserve-by-2026-polymarket-12-2026-08-24"
headline: "US Bitcoin reserve by 2026: Polymarket 12%"
semantic_title: "US national Bitcoin reserve before 2027 stays a long shot"
telemetry: "Polymarket 12%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-24T08:15:48.000Z"
event_id: "CM-EVT-0F2G0B8X49"
event_slug: "us-national-bitcoin-reserve-before-2027"
event_question: "Will the United States establish a national Bitcoin reserve before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x953b1439569eef0a0e639566acd35d32ebadee8ab70dbb2f8e00bb936a277aa2"
  question_raw: "US national Bitcoin reserve before 2027?"
  current_price: 0.12
  volume_24h_usd: 129.166665
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts 12% on the United States establishing a national Bitcoin reserve before 2027, resolves via UMA oracle."
  - "Trump keeping the door open aligns with elevated odds relative to the Kalshi contract (CM-EVT-JQRXSG4ZX9) at just 5%, creating a cross-venue gap of 7 percentage points."
  - "The Polymarket contract is nearly 2.5 times the Kalshi price; the gap likely reflects differing resolution criteria between the two venues."
  - "Bitcoin trading near $77,000-$80,000 this week after a 23% surge provides a market-implied backdrop of rising crypto sentiment, yet the reserve contract remains well below 25%."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "President Trump said he has not ruled out new U.S. government Bitcoin purchases as the administration's reserve strategy continues to take shape."
    publisher: "Yevheny Serhiienko"
    published_at: "2026-08-24T08:15:48.000Z"
    source_url: "https://bitcoinfoundation.org/news/regulation/trump-keeps-door-open-to-new-u-s-bitcoin-purchases-as-reserve-strategy-takes-shape/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Yevheny Serhiienko"
        source_url: "https://bitcoinfoundation.org/news/regulation/trump-keeps-door-open-to-new-u-s-bitcoin-purchases-as-reserve-strategy-takes-shape/"
        retrieved_at: "2026-08-24T08:42:17+00:00"
  - type: "pm_response"
    notes: "Polymarket resolves via UMA oracle; Kalshi resolves via the New York Times; differing resolution standards drive the cross-venue price gap."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Yevheny Serhiienko: Trump Keeps Door Open to New U.S. Bitcoin Purchases as Reserve Strateg"
    url: "https://bitcoinfoundation.org/news/regulation/trump-keeps-door-open-to-new-u-s-bitcoin-purchases-as-reserve-strategy-takes-shape/"
    published_at: "2026-08-24T08:15:48.000Z"
    retrieved_at: "2026-08-24T08:42:17+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
