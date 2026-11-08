---
signal_id: "CMSIG2026110706"
signal_slug: "s-p-500-annual-return-beats-btc-in-2026-kalshi-94-2026-11-07"
headline: "S&P 500 annual return beats BTC in 2026: Kalshi 94%"
semantic_title: "S&P 500 total return over Bitcoin stays heavily favored"
telemetry: "Kalshi 94%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-07T09:05:00.000Z"
event_id: "CM-EVT-BJPG2Z0CP5"
event_slug: "kxinxvsbtc-26dec31"
event_question: "Annual Return: S&P 500 Total Return Vs. BTC?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXINXVSBTC-26DEC31-INXTR"
  question_raw: "Will S&P 500 Total Return Index outperform BTC?"
  current_price: 0.94
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "For example, Google Finance"
  resolves_at: "2027-01-01T04:59:00Z"
bullets:
  - "Kalshi prices 94% odds that the S&P 500 total return outperforms Bitcoin's annual return in 2026."
  - "JPMorgan's 10% long-run Bitcoin return forecast, while bullish for crypto, is well below the implied equity return the market is pricing; the Kalshi contract is squarely against the Bitcoin-outperformance thesis."
  - "Companion Polymarket contract on Bitcoin outperforming Gold sits at 40%, showing crypto optimists see a narrower relative-performance gap against gold than against equities."
  - "Resolves via Google Finance or equivalent public price sources; Bitcoin's current price near $76K versus S&P year-to-date performance sets the current baseline."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "JPMorgan Asset Management assigned Bitcoin a compound annual return of approximately 10% in its 2027 projections, framing it as an emerging alternative asset."
    publisher: "Ghiles Ait Abdallah"
    published_at: "2026-11-07T09:05:00.000Z"
    source_url: "https://www.cointribune.com/en/jpmorgan-forecasts-an-annual-return-of-10-for-bitcoin-in-the-long-term/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Ghiles Ait Abdallah"
        source_url: "https://www.cointribune.com/en/jpmorgan-forecasts-an-annual-return-of-10-for-bitcoin-in-the-long-term/"
        retrieved_at: "2026-11-08T07:47:56+00:00"
  - type: "pm_response"
    notes: "Kalshi at 94% puts long odds against Bitcoin beating the S&P 500 total return in 2026, consistent with Bitcoin's post-election pullback and the equity market's resilience."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Ghiles Ait Abdallah: 10% per year for bitcoin? JPMorgan's forecast challenges Wall Street"
    url: "https://www.cointribune.com/en/jpmorgan-forecasts-an-annual-return-of-10-for-bitcoin-in-the-long-term/"
    published_at: "2026-11-07T09:05:00.000Z"
    retrieved_at: "2026-11-08T07:47:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
