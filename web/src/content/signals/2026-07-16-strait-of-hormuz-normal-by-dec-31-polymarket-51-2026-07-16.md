---
signal_id: "CMSIG2026071601"
signal_slug: "strait-of-hormuz-normal-by-dec-31-polymarket-51-2026-07-16"
headline: "Strait of Hormuz normal by Dec 31: Polymarket 51%"
semantic_title: "Hormuz reopening by year-end holds near coin-flip pricing"
telemetry: "Polymarket 51%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-16T03:41:44.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.51
  volume_24h_usd: 103893.667019
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts 51% on Strait of Hormuz traffic returning to normal by December 31, a near coin-flip despite active US-Iran military exchange."
  - "US strikes expanding into northern Iran and blockade enforcement are consistent with a market pricing deep uncertainty, not a near-term resolution."
  - "Polymarket separately prices only 1% on Hormuz normalization by July 31, showing the market sees virtually no short-term off-ramp from the conflict."
  - "Kalshi at 7% on the US reopening its embassy in Iran underscores how far markets place any diplomatic normalization."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US expanded airstrikes into northern Iran and fired on a ship attempting to break its naval blockade, while Iran retaliated against US allies."
    publisher: "apnews.com"
    published_at: "2026-07-16T03:41:44.000Z"
    source_url: "https://apnews.com/article/iran-us-hormuz-strait-war-july-16-2026-f98ff56554de2336f0e85bb5fdcae769"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/iran-us-hormuz-strait-war-july-16-2026-f98ff56554de2336f0e85bb5fdcae769"
        retrieved_at: "2026-07-17T09:53:11+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; the 51% level reflects genuine two-sided uncertainty as kinetic conflict continues."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: US expands its airstrike campaign against Iran | AP News"
    url: "https://apnews.com/article/iran-us-hormuz-strait-war-july-16-2026-f98ff56554de2336f0e85bb5fdcae769"
    published_at: "2026-07-16T03:41:44.000Z"
    retrieved_at: "2026-07-17T09:53:11+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
