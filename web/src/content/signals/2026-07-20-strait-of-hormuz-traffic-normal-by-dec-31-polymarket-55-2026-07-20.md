---
signal_id: "CMSIG2026072005"
signal_slug: "strait-of-hormuz-traffic-normal-by-dec-31-polymarket-55-2026-07-20"
headline: "Strait of Hormuz traffic normal by Dec 31: Polymarket 55%"
semantic_title: "Hormuz traffic normalization by year-end holds near 50%"
telemetry: "Polymarket 55%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-20T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.55
  volume_24h_usd: 107039.98679899999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices 55% on Strait of Hormuz traffic returning to normal by December 31, 2026."
  - "Active tanker attacks and ongoing US strikes present a concrete downside to normalization, yet the market is near coin-flip, consistent with Iran's reported diplomatic signaling."
  - "Secretary of State Marco Rubio's diplomatic overtures create a credible off-ramp that the market is partially pricing into the 55% figure."
  - "Resolves via Polymarket UMA oracle; normal traffic likely requires both a cessation of IRGC interdiction and US acknowledgment of restored shipping lanes."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Iran confirmed diplomatic exchanges with the US are ongoing even as US strikes continued and IRGC attacked oil tankers in the Strait of Hormuz."
    publisher: "Swati Gandhi"
    published_at: "2026-07-20T00:00:00.000Z"
    source_url: "https://www.livemint.com/news/world/us-iran-war-news-latest-live-updates-donald-trump-american-troops-ceasefire-deal-tehran-jordan-kuwait-bahrain-araghchi-11784508200833.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Swati Gandhi"
        source_url: "https://www.livemint.com/news/world/us-iran-war-news-latest-live-updates-donald-trump-american-troops-ceasefire-deal-tehran-jordan-kuwait-bahrain-araghchi-11784508200833.html"
        retrieved_at: "2026-07-20T10:47:34+00:00"
  - type: "pm_response"
    notes: "Polymarket contract via UMA oracle; near-even pricing reflects the tension between active conflict and parallel diplomacy."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Swati Gandhi: US-Iran war LIVE: Iran says diplomatic exchanges with the US are ongoi"
    url: "https://www.livemint.com/news/world/us-iran-war-news-latest-live-updates-donald-trump-american-troops-ceasefire-deal-tehran-jordan-kuwait-bahrain-araghchi-11784508200833.html"
    published_at: "2026-07-20T00:00:00.000Z"
    retrieved_at: "2026-07-20T10:47:34+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
