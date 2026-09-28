---
signal_id: "CMSIG2026092806"
signal_slug: "hormuz-traffic-normal-by-dec-31-polymarket-23-2026-09-28"
headline: "Hormuz traffic normal by Dec 31: Polymarket 23%"
semantic_title: "Strait of Hormuz traffic back to normal by year-end stays a long shot"
telemetry: "Polymarket 23%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-28T00:00:00.000Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.23
  volume_24h_usd: 80845.17216799999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Strait of Hormuz traffic returning to normal by December 31 at just 23%, a long-shot outcome despite active mediation."
  - "Trump's rejection of a seven-day truce proposal is consistent with the market's skepticism; talks resuming Monday or Tuesday have not shifted the odds."
  - "Dollar strength and hawkish Fed bets from separate stories are partially attributed to US-Iran tension, reinforcing the macro relevance of this contract."
  - "Resolves via uma_oracle; the definition of 'normal' traffic will be the key settlement dispute if a partial reopening occurs."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Mediators are still working with Iran and the US on brokering a deal after Trump rejected Tehran's seven-day truce proposal."
    publisher: "SAMY MAGDY"
    published_at: "2026-09-28T00:00:00.000Z"
    source_url: "https://www.seattletimes.com/nation-world/nation/officials-say-mediators-are-still-working-with-iran-and-the-us-on-a-possible-deal/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "SAMY MAGDY"
        source_url: "https://www.seattletimes.com/nation-world/nation/officials-say-mediators-are-still-working-with-iran-and-the-us-on-a-possible-deal/"
        retrieved_at: "2026-09-28T16:24:04+00:00"
  - type: "pm_response"
    notes: "Polymarket contract on Hormuz normalization by year-end resolves via uma_oracle; at 23%, the market puts long odds against a deal materializing in three months."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "SAMY MAGDY: Mediators working to broker US-Iran deal even after Trump rejected lat"
    url: "https://www.seattletimes.com/nation-world/nation/officials-say-mediators-are-still-working-with-iran-and-the-us-on-a-possible-deal/"
    published_at: "2026-09-28T00:00:00.000Z"
    retrieved_at: "2026-09-28T16:24:04+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
