---
signal_id: "CMSIG2026072202"
signal_slug: "hormuz-normal-by-dec-31-polymarket-54-2026-07-22"
headline: "Hormuz normal by Dec 31: Polymarket 54%"
semantic_title: "Hormuz year-end normalization stays near 50% amid war escalation"
telemetry: "Polymarket 54%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-22T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.54
  volume_24h_usd: 66032.991374
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 54% on Strait of Hormuz traffic returning to normal by December 31."
  - "Continued nightly US strikes and a collapsed ceasefire effort leave the market only marginally above 50%, reflecting deep uncertainty."
  - "The 1% July contract on the same outcome confirms markets see no near-term off-ramp, loading all probability mass into Q4."
  - "Resolves via UMA oracle against a definition of 'normal' Hormuz transit volumes."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Fresh US strikes on Iran for the 11th consecutive night overshadowed Pakistan's bid to revive a collapsed ceasefire, deepening the conflict."
    publisher: "economictimes.indiatimes.com"
    published_at: "2026-07-22T00:00:00.000Z"
    source_url: "https://economictimes.indiatimes.com/news/international/world-news/fresh-us-iran-strikes-overshadow-pakistans-bid-to-revive-collapsed-ceasefire/articleshow/132549154.cms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "economictimes.indiatimes.com"
        source_url: "https://economictimes.indiatimes.com/news/international/world-news/fresh-us-iran-strikes-overshadow-pakistans-bid-to-revive-collapsed-ceasefire/articleshow/132549154.cms"
        retrieved_at: "2026-07-22T10:22:09+00:00"
  - type: "pm_response"
    notes: "Polymarket holds 54% on year-end Hormuz normalization, effectively a coin-flip despite escalating military action."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "economictimes.indiatimes.com: iran: Fresh US-Iran strikes overshadow Pakistan's bid to revive collap"
    url: "https://economictimes.indiatimes.com/news/international/world-news/fresh-us-iran-strikes-overshadow-pakistans-bid-to-revive-collapsed-ceasefire/articleshow/132549154.cms"
    published_at: "2026-07-22T00:00:00.000Z"
    retrieved_at: "2026-07-22T10:22:09+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
